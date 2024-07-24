from convert2ppt.generate_json import generate_json
from convert2ppt.load_pdfs import load_pdfs
from convert2ppt.generate_ppt import create_presentations



def main():
    data_dir = "convert2ppt\data"
    # Load PDFs and generate prompts
    load_pdfs(data_dir)

    # Generate JSON for PowerPoint presentations
    generate_json(data_dir)

    # Create PowerPoint presentations
    create_presentations(data_dir)

if __name__ == '__main__':
    main()