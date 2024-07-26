# Usage

To use convert2ppt in a project:

```
import convert2ppt
from convert2ppt.generate_json import generate_json
from convert2ppt.load_pdfs import load_pdfs
from convert2ppt.generate_ppt import create_presentations
import sys


def main():

    print("Welcome to convert2ppt!")
    # Generate text content from PDFs
    data_dir = r".\data"
    load_pdfs(data_dir)

    # Generate JSON content from text content
    generate_json(data_dir)

    # Generate PowerPoint presentations from JSON content
    create_presentations(data_dir)
```
