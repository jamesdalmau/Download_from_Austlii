file_to_write = open('authors.txt', 'w', encoding="utf8", errors="replace")
import os
list_of_possible_tags = ['JUDGES:', 'JUDGMENT BY:', 'JUDGMENT OF:', 'COURT IN THE SUPREME COURT OF THE NORTHERN TERRITORY OF AUSTRALIA', 'CORAM:', 'JUDGE:', '- REASONS FOR JUDGMENT', 'COURT OF CRIMINAL APPEAL:', 'CORAM	:','BEFORE:', 'FULL COURT:', 'COURT IN THE FULL COURT OF THE SUPREME COURT OF SOUTH AUSTRALIA', 'COURT IN THE SUPREME COURT OF SOUTH AUSTRALIA', 'JUDGE(S):', 'BEFORE THE HON', 'REASONS FOR JUDGMENT :', 'BEFORE JUSTICE', 'JUDGMENT  -', 'COURT IN THE IN THE FULL COURT OF THE SUPREME COURT OF SOUTH AUSTRALIA', 'COURT IN THE SUPREME COURT OF THE NORTHERN TERRITORY', 'REASONS FOR JUDGMENT -', 'DECISION OF:', ': REASONS FOR DECISION', 'MASTER:','REASONS FOR DECISION OF THE HONOURABLE','JUDGMENT OF THE HONOURABLE','JUDGMENT OF :', 'COURT:	','COURT IN THE FULL COURT OF THE COURT OF APPEAL OF THE NORTHERN TERRITORY OF AUSTRALIA','COURT IN THE COURT OF APPEAL OF THE NORTHERN TERRITORY OF AUSTRALIA','JUDGMENT OF JUDGE','JUDGMENT OF THE HONOURABLE','REASONS FOR RULING OF THE HONOURABLE','JUDGMENT SUPRESSED','REASONS OF JUDGE','JUDGMENT OF JUDGE']
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