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
    """
    This function loads all PDF files from a specified directory, extracts the text content from each PDF file, 
    and offers the user the option to save the extracted text to a .txt file.

    Parameters:
    data_dir (str): The directory from which to load the PDF files.

    The function performs the following steps:
    1. Deletes any non-PDF files in the specified directory.
    2. Lists all PDF files in the directory.
    3. If no PDF files are found, the function prints a message and exits.
    4. If PDF files are found, the function prints a message indicating the number of PDF files found.
    5. The function then extracts the text content from each PDF file and appends it to a list of prompts.
    6. The function prints a message warning the user that the extracted text may sometimes be garbage and should be reviewed before saving.
    7. For each prompt, the function prints the first 100 characters of the extracted text and asks the user if they want to save the content to a .txt file.
    8. If the user responds with 'y', the function saves the content to a .txt file in the same directory as the original PDF file. The .txt file has the same name as the PDF file, but with a .txt extension instead of .pdf.
    9. If the user responds with anything other than 'y', the function skips the current document and moves on to the next one.
    """

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
        #show the first 100 characters of the extracted text without extra white spaces
        print(f"Extracted text from '{docs[i]}' starts with:\n\n '{' '.join(prompts[i][:100].split())}...'")
        #ask the user if they want to save the extracted text to a .txt file
        response = input(f"\nCan we continue with the extracted content? (y/n): ")
        if response.lower() != 'y':
            print('Skipping this document.')
            continue
        filename = docs[i].replace('.pdf','.txt')
        full_path = os.path.join(data_dir, filename)
        with open(full_path, 'w', encoding='utf-8') as file:
            file.write(prompts[i])
        print(f"Saved content to '{full_path}'")