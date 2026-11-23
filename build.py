"""Собирает index.html из src/: шаблон + теория + тесты + разборы."""
from pathlib import Path
s = Path("src")
html = (s / "shell.html").read_text(encoding="utf-8")
for mark, f in [("/*CONTENT*/", "content.js"), ("/*QUIZ*/", "quiz.js"), ("/*EXPL*/", "explain.js")]:
    html = html.replace(mark, (s / f).read_text(encoding="utf-8"))
Path("index.html").write_text(html, encoding="utf-8")
print("index.html собран")
