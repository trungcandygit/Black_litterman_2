"""Put pandoc/python-docx output into OOXML schema order (child-element sequences the XSD
requires) and add required attributes pandoc omits. Structure only; text is untouched."""
import re
import zipfile
from pathlib import Path

from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
M = "http://schemas.openxmlformats.org/officeDocument/2006/math"
SEQ = {
    f"{{{W}}}pPr": "pStyle keepNext keepLines pageBreakBefore framePr widowControl numPr suppressLineNumbers pBdr shd tabs suppressAutoHyphens kinsoku wordWrap overflowPunct topLinePunct autoSpaceDE autoSpaceDN bidi adjustRightInd snapToGrid spacing ind contextualSpacing mirrorIndents suppressOverlap jc textDirection textAlignment textboxTightWrap outlineLvl divId cnfStyle rPr sectPr pPrChange",
    f"{{{W}}}rPr": "rStyle rFonts b bCs i iCs caps smallCaps strike dstrike outline shadow emboss imprint noProof snapToGrid vanish webHidden color spacing w kern position sz szCs highlight u effect bdr shd fitText vertAlign rtl cs em lang eastAsianLayout specVanish oMath",
    f"{{{W}}}tcPr": "cnfStyle tcW gridSpan hMerge vMerge tcBorders shd noWrap tcMar textDirection tcFitText vAlign hideMark headers cellIns cellDel cellMerge tcPrChange",
    f"{{{W}}}tblPr": "tblStyle tblpPr tblOverlap bidiVisual tblStyleRowBandSize tblStyleColBandSize tblW jc tblCellSpacing tblInd tblBorders shd tblLayout tblCellMar tblLook tblCaption tblDescription tblPrChange",
    f"{{{W}}}style": "name aliases basedOn next link autoRedefine hidden uiPriority semiHidden unhideWhenUsed qFormat locked personal personalCompose personalReply rsid pPr rPr tblPr trPr tcPr tblStylePr",
    f"{{{W}}}sectPr": "headerReference footerReference footnotePr endnotePr type pgSz pgMar paperSrc pgBorders lnNumType pgNumType cols formProt vAlign noEndnote titlePg textDirection bidi rtlGutter docGrid printerSettings sectPrChange",
    f"{{{M}}}dPr": "begChr sepChr endChr grow shp ctrlPr",
    f"{{{W}}}settings": "writeProtection view zoom removePersonalInformation removeDateAndTime doNotDisplayPageBoundaries displayBackgroundShape printPostScriptOverText printFractionalCharacterWidth printFormsData embedTrueTypeFonts embedSystemFonts saveSubsetFonts saveFormsData mirrorMargins alignBordersAndEdges bordersDoNotSurroundHeader bordersDoNotSurroundFooter gutterAtTop hideSpellingErrors hideGrammaticalErrors activeWritingStyle proofState formsDesign attachedTemplate linkStyles stylePaneFormatFilter stylePaneSortMethod documentType mailMerge revisionView trackRevisions doNotTrackMoves doNotTrackFormatting documentProtection autoFormatOverride styleLockTheme styleLockQFSet defaultTabStop autoHyphenation consecutiveHyphenLimit hyphenationZone doNotHyphenateCaps showEnvelope summaryLength clickAndTypeStyle defaultTableStyle evenAndOddHeaders bookFoldRevPrinting bookFoldPrinting bookFoldPrintingSheets drawingGridHorizontalSpacing drawingGridVerticalSpacing displayHorizontalDrawingGridEvery displayVerticalDrawingGridEvery doNotUseMarginsForDrawingGridOrigin drawingGridHorizontalOrigin drawingGridVerticalOrigin doNotShadeFormData noPunctuationKerning characterSpacingControl printTwoOnOne strictFirstAndLastChars noLineBreaksAfter noLineBreaksBefore savePreviewPicture doNotValidateAgainstSchema saveInvalidXml ignoreMixedContent alwaysShowPlaceholderText doNotDemarcateInvalidXml saveXmlDataOnly useXSLTWhenSaving saveThroughXslt showXMLTags alwaysMergeEmptyNamespace updateFields hdrShapeDefaults footnotePr endnotePr compat docVars rsids mathPr attachedSchema themeFontLang clrSchemeMapping doNotIncludeSubdocsInStats doNotAutoCompressPictures forceUpgrade captions readModeInkLockDown smartTagType schemaLibrary shapeDefaults doNotEmbedSmartTags decimalSymbol listSeparator",
}
SEQ = {k: {n: i for i, n in enumerate(v.split())} for k, v in SEQ.items()}
DROP_SETTINGS = set()


def _order(el):
    seq = SEQ.get(el.tag)
    if seq:
        kids = list(el)
        known = [k for k in kids if isinstance(k.tag, str) and etree.QName(k).localname in seq]
        if known:
            rank = {id(k): seq[etree.QName(k).localname] for k in known}
            ordered = sorted(known, key=lambda k: rank[id(k)])
            it = iter(ordered)
            for i, k in enumerate(kids):
                if id(k) in rank:
                    el.remove(k)
            for k in ordered:
                el.append(k)
            # unknown children (extensions) go after the ordered ones; keep their relative order
            for k in kids:
                if id(k) not in rank:
                    el.remove(k); el.append(k)
    for c in el:
        if isinstance(c.tag, str):
            _order(c)


def fix(path):
    path = Path(path)
    zin = zipfile.ZipFile(path)
    items = [(i, zin.read(i.filename)) for i in zin.infolist()]
    zin.close()
    out = []
    for info, data in items:
        name = info.filename
        if name.startswith("word/") and name.endswith(".xml"):
            root = etree.fromstring(data)
            if name == "word/settings.xml":
                for c in list(root):
                    if c.tag in DROP_SETTINGS:
                        root.remove(c)
            for pm in root.iter(f"{{{W}}}pgMar"):
                for a, v in (("header", "708"), ("footer", "708"), ("gutter", "0")):
                    pm.set(f"{{{W}}}{a}", pm.get(f"{{{W}}}{a}", v))
            for ns in root.iter(f"{{{W}}}nsid"):
                v = ns.get(f"{{{W}}}val", "")
                if len(v) != 8:
                    ns.set(f"{{{W}}}val", v.rjust(8, "0")[-8:].upper())
            for rpr in root.iter(f"{{{M}}}rPr"):  # m:nor and m:sty are alternatives in the schema
                if rpr.find(f"{{{M}}}nor") is not None:
                    for st in rpr.findall(f"{{{M}}}sty"):
                        rpr.remove(st)
            _order(root)
            data = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)
        out.append((info, data))
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for info, data in out:
            z.writestr(info, data)
