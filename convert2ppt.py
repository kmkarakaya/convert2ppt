from convert2ppt.generate_json import generate_json
from convert2ppt.load_pdfs import load_pdfs
from convert2ppt.generate_ppt import create_presentations
import sys


def main():

    print("Welcome to convert2ppt!")

    if getattr(sys, 'frozen', False):
        # running in a bundled app
        print('Running in a bundled app...')
        data_dir = input("Enter the path to the directory containing the documents (DEFAULT: .\data): ")
        if data_dir == "":
            data_dir = ".\data"
        print(f'data_dir: {data_dir}')
    else:
        # running normally
        print('Running normally...')
        data_dir = "convert2ppt\data"
        print(f'data_dir: {data_dir}')
    
        
    # Load PDFs and generate prompts
    load_pdfs(data_dir)

    # Generate JSON for PowerPoint presentations
    generate_json(data_dir)

    # Create PowerPoint presentations
    create_presentations(data_dir)

    input("Press Enter to exit...")

if __name__ == '__main__':
        
    main()