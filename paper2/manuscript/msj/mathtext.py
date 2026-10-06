import re
# ---------- inline math -> Unicode text (PLOS: no equation objects for symbols in running text) ----------
SYM = {"alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "tau": "τ", "varepsilon": "ε", "Phi": "Φ",
       "geq": "≥", "leq": "≤", "approx": "≈", "cdot": "·", "dots": "…", "lfloor": "⌊", "rfloor": "⌋",
       "lceil": "⌈", "rceil": "⌉", "sum": "Σ", "times": "×", "min": "min"}
COMB = {"hat": "\u0302", "widehat": "\u0302", "overline": "\u0304", "tilde": "\u0303"}

def readgroup(x, i):
    if i < len(x) and x[i] == "{":
        d = 0
        for j in range(i, len(x)):
            if x[j] == "{": d += 1
            elif x[j] == "}":
                d -= 1
                if d == 0: return x[i + 1:j], j + 1
        raise ValueError(x)
    if i < len(x) and x[i] == "\\":
        m = re.match(r"\\([A-Za-z]+|.)", x[i:]); return m.group(0), i + len(m.group(0))
    return x[i], i + 1

def plain(x):
    # plain characters of a group (for accents)
    x = re.sub(r"\\(text|mathrm|operatorname)\{([^}]*)\}", r"\2", x)
    for k, v in SYM.items(): x = x.replace("\\" + k, v)
    return x

def conv(x, script=False):
    out = []; i = 0
    def last_sig():
        t = "".join(out).rstrip()
        return t[-1] if t else ""
    while i < len(x):
        c = x[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+|.)", x[i:]); cmd = m.group(1); i += len(m.group(0))
            if cmd in ("text", "mathrm", "operatorname"):
                g, i = readgroup(x, i); out.append(g)
            elif cmd in COMB:
                g, i = readgroup(x, i); p = plain(g)
                acc = p[0] + COMB[cmd] + p[1:]
                out.append(f"*{acc}*" if len(p) == 1 and p.isalpha() and p.isascii() else acc)
            elif cmd in SYM:
                out.append(SYM[cmd])
            elif cmd in (",", ";"):
                out.append("" if script else " ")
            elif cmd in ("!", "left", "right"):
                pass
            else:
                raise ValueError("unknown command " + cmd)
        elif c in "_^":
            g, i = readgroup(x, i + 1)
            inner = conv(g, True).replace(" ", "")
            d = "~" if c == "_" else "^"
            out.append(f"{d}{inner}{d}")
        elif c.isalpha() and c.isascii():
            out.append(f"*{c}*"); i += 1
        elif c == "-":
            prev = last_sig()
            unary = prev in ("", "(", "=", "≤", "≥", "<", ">", "/", "^", "~") or script
            out.append("−" if (unary or script) else " − "); i += 1
        elif c in "+=<>" and not script:
            out.append(f" {c} "); i += 1
        elif c in "{}":
            i += 1
        else:
            out.append(c); i += 1
    r = "".join(out)
    r = re.sub(r" {2,}", " ", r)
    r = r.replace("( ", "(").replace(" )", ")")
    return r.strip()

def inline_math(text):
    # skip code chunks and inline code; convert $...$ (not $$)
    parts = re.split(r"(```.*?```|`[^`]*`|\$\$.*?\$\$)", text, flags=re.S)
    for k, p in enumerate(parts):
        if k % 2 == 0:
            parts[k] = re.sub(r"(?<!\$)\$([^$\n]+?)\$(?!\$)", lambda m: conv(m.group(1)), p)
    return "".join(parts)

