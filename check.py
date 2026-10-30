"""CI: every HTML page has a title, and every local link and stylesheet it references exists."""
import pathlib, re, sys

problems = []
for page in pathlib.Path(".").glob("*.html"):
    text = page.read_text()
    if not re.search(r"<title>[^<]+</title>", text):
        problems.append(f"{page}: no <title>")
    for ref in re.findall(r'(?:href|src)="([^"#:]+)"', text):
        if not pathlib.Path(ref).exists():
            problems.append(f"{page}: {ref} doesn't exist")
print("\n".join(problems) or "ok")
sys.exit(1 if problems else 0)
