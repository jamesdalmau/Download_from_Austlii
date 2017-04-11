file_to_write = open('authors_no_tag_text_results.txt', 'w', encoding="utf8", errors="replace")
import os

with open('authors_no_tag_text.txt', 'r', encoding="utf8", errors="replace") as list_of_files_to_read:
    lines_in_files_to_read = list_of_files_to_read.readlines()
    for file_in_list in lines_in_files_to_read:
        with open('d:\\txtutf\\' + file_in_list.strip(), encoding="utf8", errors='ignore') as f:
            lines_found = ''
            lines = f.readlines()
            line_number = 0
            for line in lines:
                line_number = line_number + 1
                if line_number < 100:
                    uppercase_line = line.upper()
                    uppercase_line_stripped = uppercase_line.strip()
                    if len(uppercase_line_stripped) > 2:
                        if uppercase_line_stripped[-1]=='J' or uppercase_line_stripped[-2]=='J.':
                            lines_found = lines_found + '|' + uppercase_line.strip()
            file_to_write.write(file_in_list.strip() + lines_found + "\n")