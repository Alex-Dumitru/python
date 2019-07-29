import requests
from bs4 import BeautifulSoup as BS
import json
import os
import sys

# TODO - document all functions

REDBOOKS_ABSTRACTS = "https://www.redbooks.ibm.com/abstracts/"
setup = {}

def main():
    """[summary]
    """
    global setup
    # TODO - if book found in Downloads, move it to REDBOOKS folder
    
    # upload settings from setup.json that needs to be next to script
    setup_file_location = os.path.dirname(os.path.realpath(__file__))
    with open("{}\\setup.json".format(setup_file_location)) as setup_file:
        setup = json.load(setup_file)

    book_codes = get_book_codes()
    # check if tuple is empty, and exit if so
    if not book_codes:
        print("ERROR: No book codes found/received!")
        exit(1)

    names_of_redbooks = search_for_redbooks(book_codes)
    if not names_of_redbooks:
        print("No books found on Redbooks website based on the codes provided")
    else:
        print_summary(names_of_redbooks)

    if setup["RENAME"]:
        rename_redbooks(names_of_redbooks)


def search_for_redbooks(book_codes: tuple):
    """Searches for specific string on redbooks.ibm.com
    
    Arguments:
        book_codes {tuple} -- tuple with book codes to search for
    Returns:
        [dictionary] -- book_code: book_name
    """

    book_dict = {}

    global setup

    for book_code in book_codes:
        URI_string = build_URI_string(book_code)
        search_web_page = requests.get(URI_string)
        if search_web_page.status_code != 200:
            print("Book with code {} not found! Continuing...".format(book_code))
            continue
        web_page_content = search_web_page.content
        soup = BS(web_page_content, 'html.parser')
        book_name = soup.find('h1',{'class':'ibm-h1','id':'ibm-pagetitle-h1'}).text
        book_dict[book_code] = book_name

    return book_dict


def build_URI_string(book_code: str):
    """[summary]
    
    Arguments:
        book_code {str} -- [description]
    """
    URI_string = "{abstract}{code}.html?Open".format(abstract=REDBOOKS_ABSTRACTS,code=book_code)

    return URI_string


def get_book_codes():
    """[summary]
    """
    book_codes = []
    # Check CLI arguments
    if len(sys.argv) > 1:
        temp_book_code = sys.argv[1]
        # looking for this pdf 
        temp_book_code = os.path.abspath(temp_book_code) if "pdf" in temp_book_code else os.path.abspath(temp_book_code+".pdf")
        book_codes.append(temp_book_code)
    else:
        print("No book code passed!\nLooking into default folders:\n{}\n{}".format(setup["REDBOOKS_FOLDER"], setup["DOWNLOADS_FOLDER"]))
        # possible candidates: all pdf files.
        # extracting only the file name (dropping .pdf extension) because we will use it in the URI definition
        with os.scandir(setup["REDBOOKS_FOLDER"]) as redbooks_folder:
            for entry in redbooks_folder:
                if entry.is_file() and " " not in entry.name and entry.name.endswith(".pdf"):
                    book_codes.append(os.path.splitext(entry.name)[0])
        # with os.scandir(setup["DOWNLOADS_FOLDER"]) as redbooks_folder:
        #     for entry in redbooks_folder:
        #         if entry.is_file() and " " not in entry.name and entry.name.endswith(".pdf"):
        #             book_codes.append(os.path.splitext(entry.name)[0])

    return tuple(book_codes)


def print_summary(names_of_redbooks: dict):
    """[summary]
    
    Arguments:
        names_of_redbooks {dict} -- [description]
    """
    for key,val in names_of_redbooks.items():
        print("{} - {}".format(key,val))


def rename_redbooks(names_of_redbooks: dict):
    """[summary]
    
    Arguments:
        names_of_redbooks {dict} -- [description]
    """

    cur_dir = os.getcwd()
    os.chdir(setup["REDBOOKS_FOLDER"])
    for old,new in names_of_redbooks.items():
        new = new.replace(" ","_").replace(":","")
        os.rename(old+".pdf",new+".pdf")
    os.chdir(cur_dir)



if __name__ == "__main__":
    main()
