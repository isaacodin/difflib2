import difflib2
import argparse
from pathlib import Path

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fn1")
parser.add_argument("fn2")

args = parser.parse_args()

lines1 = Path(args.fn1).read_text().splitlines()
lines2 = Path(args.fn2).read_text().splitlines()

html_diff = difflib2.HtmlDiff().make_file(lines1, lines2)
Path('diff.html').write_text(html_diff)