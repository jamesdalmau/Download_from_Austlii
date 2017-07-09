file_to_write = open('MetadataWithGender.txt', 'w', encoding="utf8", errors="replace")
import os
list_of_author_lists = []

with open('UniqueAuthorsForPython.txt', 'r', encoding="utf8", errors="replace") as author_file:
    author_lines = author_file.readlines()
    for author_line in author_lines:
        exec("author_line_array=['" + author_line[:-1].replace(',',"','")+ "']")
        list_of_author_lists.append(author_line_array)

with open('MetadataForPython.txt', 'r', encoding="utf8", errors="replace") as source_file:
    source_file_lines = source_file.readlines()
    for source_file_line in source_file_lines:
        exec("source_line_array=['" + source_file_line[:-1].replace(',',"','")+ "']")
        gender_to_write = "N/A"
        for author_entry in list_of_author_lists:
            if (author_entry[0] == source_line_array[2]) and (author_entry[1] == source_line_array[4]):
                gender_to_write = author_entry[2]
        file_to_write.write(str(source_line_array[0])+','+str(source_line_array[1])+','+str(source_line_array[2])+','+str(source_line_array[3])+','+str(source_line_array[4])+','+gender_to_write+'\n')