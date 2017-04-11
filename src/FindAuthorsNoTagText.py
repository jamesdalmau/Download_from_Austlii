file_to_write = open('authors_no_tag_text_results.txt', 'w', encoding="utf8", errors="replace")
import os

with open('missingauthorsNewMethodRequired.txt', 'r', encoding="utf8", errors="replace") as list_of_files_to_read:
    lines_in_files_to_read = list_of_files_to_read.readlines()
    for file_in_list in lines_in_files_to_read:
        with open('d:\\txtutf\\' + file_in_list.strip(), encoding="utf8", errors='ignore') as f:
            lines_found = ''
            #print(file)
            lines = f.readlines()
            for line in lines: