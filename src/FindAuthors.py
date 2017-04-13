file_to_write = open('authors.txt', 'w', encoding="utf8", errors="replace")
import os
list_of_possible_tags = ['CWDS','JUDGMENT SUPPRESSED','JUDICIAL REGISTRAR:','THIS JUDGMENT HAS BEEN TEMPORARILY REMOVED','RULING OF THE HONOURABLE','REASONS FOR THE VERDICT OF THE HONOURABLE','JUDGMENT WITHDRAWN','JUDGMENT NOT AVAILABLE IN ELECTRONIC FORM','REASONS FOR RULINGS OF THE HONOURABLE','REASONS FOR THE ORDERS OF THE HONOURABLE', 'JUDGMENT CREATED IN ERROR', 'JUDGMENT - ', '(SUPREME COURT MASTER)','DECISION NUMBER NOT IN USE']
list_of_excluded_tags = ['(APPEALS TO A SINGLE JUDGE: APPLICATION)', '(APPEALS TO A SINGLE JUDGE: CIVIL)', 'APPEAL TO A SINGLE JUDGE: CIVIL', '(APPEALS TO A SINGLE JUDGE: CRIMINAL)', '(APPEALS TO A SINGLE JUDGE: PERMISSION TO APPEAL)', '(COURT OF CRIMINAL APPEAL: CRIMINAL)', '<LCCORAM>', 'APPEAL FROM A MASTER: CIVIL', 'APPEAL FROM A MASTER: APPLICATION']
for file in os.listdir('d:\\txtutf\\'):
    if file.endswith(".txt"):
        with open('d:\\txtutf\\' + file, encoding="utf8", errors='ignore') as f:
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
            file_to_write.write(file + lines_found + "\n")