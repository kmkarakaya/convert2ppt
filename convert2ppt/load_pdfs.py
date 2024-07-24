import os
import fitz  # PyMuPDF

def delete_non_pdf_files(data_dir):
    # delete all non-pdf files in the local directory
    # but first request user confirmation
    response=input(f"Are you sure you want to delete all non-pdf files in the {data_dir} directory? (y/n): ")
    if response.lower() != 'y':
        print('Operation cancelled.')
        exit()  # Exit the function if the user doesn't confirm the deletion    
    
    files = os.listdir(data_dir)
    for file in files:
        if not file.endswith('.pdf'):
            os.remove(os.path.join(data_dir, file))
            print(f"Deleted '{file}'")


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        page_text = page.get_text("text")
        if page_text:
            text += page_text
    return text

def load_pdfs(data_dir):

    delete_non_pdf_files(data_dir)
    # open and convert all pdf files in the local directory into a list variable called docs 
    docs = [doc for doc in os.listdir( data_dir) if doc.endswith('.pdf')]    

    #check if there is any pdf in the local folder
    #if there is no pdf file in the local folder, print 'No PDF files found in the local directory' and exit the function
    if len(docs) == 0:
        print('No PDF files found in the {data_dir} directory!')
        exit()
    else:
        print(f"Found {len(docs)} PDF files in the {data_dir} directory.")


    # generate a list of prompts from the pdf content

    prompts = []
    for doc in docs:
        pdf_path = os.path.join(data_dir, doc)
        text = extract_text_from_pdf(pdf_path)
        prompts.append(text)
     
    print("\nIMPORTANT:")
    print(f"Extracted text from PDF files, sometimes, could be garbage.")
    print(f"Please review the extracted text before saving it to a .txt file.")
    print("Note that we can not create a PowerPoint presentation from garbage text.\n")
    for i in range(len(prompts)):
        #show the first 100 characters of the extracted text
        print(f"Extracted text from '{docs[i]}' starts with:\n '{prompts[i][:100]}...'")
        #ask the user if they want to save the extracted text to a .txt file
        response = input(f"\nDo you want to save the content to a .txt file? (y/n): ")
        if response.lower() != 'y':
            print('Skipping this document.')
            continue
        filename = docs[i].replace('.pdf','.txt')
        full_path = os.path.join(data_dir, filename)
        with open(full_path, 'w', encoding='utf-8') as file:
            file.write(prompts[i])
        print(f"Saved content to '{full_path}'")