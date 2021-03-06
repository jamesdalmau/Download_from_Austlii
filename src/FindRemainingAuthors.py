file_to_write = open('finalmissingauthorsfound.txt', 'w', encoding="utf8", errors="replace")
import os
list_of_possible_tags = ['JUDGMENT OF JUDGE','JUDGMENT OF THE HONOURABLE','REASONS FOR RULING OF THE HONOURABLE','JUDGMENT SUPRESSED','REASONS OF JUDGE','JUDGMENT OF JUDGE']
list_of_excluded_tags = ['(APPEALS TO A SINGLE JUDGE: APPLICATION)', '(APPEALS TO A SINGLE JUDGE: CIVIL)', 'APPEAL TO A SINGLE JUDGE: CIVIL', '(APPEALS TO A SINGLE JUDGE: CRIMINAL)', '(APPEALS TO A SINGLE JUDGE: PERMISSION TO APPEAL)', '(COURT OF CRIMINAL APPEAL: CRIMINAL)', '<LCCORAM>', 'APPEAL FROM A MASTER: CIVIL', 'APPEAL FROM A MASTER: APPLICATION']

with open('missingauthorsNewMethodRequired.txt', 'r', encoding="utf8", errors="replace") as list_of_files_to_read:
    lines_in_files_to_read = list_of_files_to_read.readlines()
    for file_in_list in lines_in_files_to_read:
        with open('d:\\txtutf\\' + file_in_list.strip(), encoding="utf8", errors='ignore') as f:
            lines_found = ''
            #print(file)
            lines = f.readlines()
            for line in lines:
                uppercase_line = line.upper()
                for possible_tag in list_of_possible_tags:
                    found_something = 0
                    #print(possible_tag + 'in' + uppercase_line)
                    if possible_tag in uppercase_line:
                        found_something = 1
                        for exclusion in list_of_excluded_tags:
                            if exclusion in uppercase_line:
                                found_something = 0
                        if found_something == 1:
                            lines_found = lines_found + '|' + uppercase_line.strip()
                        #print(file + ' - ' + uppercase_line)
            file_to_write.write(file_in_list.strip() + lines_found + "\n")