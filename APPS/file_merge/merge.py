# function for merging files given as parameter
import os

print('test line 1')
# defining the function with list of arguments for input files and keyword
# argument for output file.
def merge_files(*args, output=None):
    print('test line 2')
    answer2 = ""
    #if output is not given, print error, usage and exit
    if output is None:
        print("Error! You did not specify 'output' parameter")
        print("Usage: merge_files(file1, file2,...,output=output_file)")
        return 1
    # if output file is found, ask if user wants to rewrite it
    if os.path.isfile(output):
        while True:
            question1 = 'Output file %s already exists! Do you want to overwrite it? y/n ' % output
            answer1 = input(question1)
            answer1 = answer1.lower()
            if answer1 == 'y' or answer1 == 'n':
                break
    # if he wants to rewrite it, then go forward
    if answer1 == 'y':
        # read the file, to check if it has some content
        # and ask user if he wants to keep the content (append to the file)
        with open(output, 'r') as tmp:
            tmp_out = tmp.read()
        if tmp_out != '':
            while True:
                question2 = 'File %s has some content! Do you want to append to it? y/n ' % output
                answer2 = input(question2)
                answer2 = answer2.lower()
                if answer2 == 'y' or answer2 == 'n':
                    break
    else:
        # if he doesn't, then exit
        print('Exiting. Bye...')
        return 0

    # open the output file for writing
    with open(output, 'w') as out:
        # write back the content of the output file, if user agreed in previous step
        if answer2 == 'y':
            out.write(tmp_out)
        # then, for each file in input list, check if it is present on the system
        # if yes, then open and read it, and write its content to output file
        for file in args:
            if os.path.isfile(file):
                with open(file, 'r') as inp:
                    out.write(inp.read())
                    print('File %s written to %s.' % (file, output))
            # if it's not present, write skip message to console
            else:
                print('File %s does not exist. Skipping...' % file)

if "__name__" == "__main__":
    print('test line 3')
