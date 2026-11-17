#!/usr/bin/env python3
"""Turn a BibTeX export from SciX/ADS into the publications file of this site.

Usage (from the repository folder):
    python3 bin/clean_scix_bib.py ~/Downloads/export-bibtex.bib _bibliography/papers.bib

Papers listed in bin/selected_keys.txt (one SciX bibcode per line) are shown on the home page.
"""
import re
import sys
from pathlib import Path

JOURNALS = {
    r"\aj": "The Astronomical Journal",
    r"\apj": "The Astrophysical Journal",
    r"\apjl": "The Astrophysical Journal Letters",
    r"\apjs": "The Astrophysical Journal Supplement Series",
    r"\mnras": "Monthly Notices of the Royal Astronomical Society",
    r"\aap": "Astronomy \\& Astrophysics",
    r"\nat": "Nature",
    r"\natas": "Nature Astronomy",
    r"\pasp": "Publications of the Astronomical Society of the Pacific",
    r"\araa": "Annual Review of Astronomy and Astrophysics",
}
DROP = {"adsnote", "keywords", "primaryclass", "archiveprefix", "eprint", "eid"}


def main(src, dst):
    here = Path(__file__).resolve().parent
    sel_file = here / "selected_keys.txt"
    selected = set()
    if sel_file.exists():
        selected = {l.strip() for l in sel_file.read_text().splitlines() if l.strip() and not l.startswith("#")}

    text = Path(src).read_text(encoding="utf-8")
    out = ["---", "---", ""]
    n = 0
    for entry in re.split(r"(?m)^(?=@)", text):
        entry = entry.strip()
        if not entry.startswith("@"):
            continue
        head = re.match(r"@(\w+)\{([^,]+),", entry)
        etype, key = head.group(1).lower(), head.group(2)
        fields = {}
        for line in entry.splitlines()[1:]:
            m = re.match(r"\s*(\w+)\s*=\s*(.*?),?\s*$", line)
            if m:
                fields[m.group(1).lower()] = m.group(2)
        eprint = fields.get("eprint", "").strip("{}")
        jm = re.match(r"\{(\\\w+)\}", fields.get("journal", ""))
        if jm and jm.group(1) in JOURNALS:
            fields["journal"] = "{" + JOURNALS[jm.group(1)] + "}"
        if "author" in fields:
            fields["author"] = fields["author"].replace("and et al.", "and others")
        if eprint:
            fields["arxiv"] = "{" + eprint + "}"
        if key in selected:
            fields["selected"] = "{true}"
        lines = ["@%s{%s," % (etype, key.replace("&", "").replace(".", "_"))]
        lines += ["  %s = %s," % (k, v) for k, v in fields.items() if k not in DROP]
        lines[-1] = lines[-1].rstrip(",")
        lines.append("}")
        out += ["\n".join(lines), ""]
        n += 1
    Path(dst).write_text("\n".join(out), encoding="utf-8")
    print("wrote %d entries to %s" % (n, dst))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
