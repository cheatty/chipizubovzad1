#1
"""
def read_files(file_paths):
    combined_text = ""
    for path in file_paths:
        with open(path, 'r') as file:
            combined_text += file.read().strip()
    return combined_text

def longest_sequence_of_x(text):
    max_count = 0
    current_count = 0
    for char in text:
        if char == 'X':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count

file_paths = ['36037.txt']
combined_text = read_files(file_paths)

result = longest_sequence_of_x(combined_text)
print(result)
"""

#2
"""
def read_files(file_paths):
    combined_text = ""
    for path in file_paths:
        with open(path, 'r') as file:
            combined_text += file.read().strip()
    return combined_text

def max_length_without_xzzy(text):
    max_length = 0
    current_length = 0
    i = 0
    while i < len(text):
        if text[i:i+4] == "XZZY":
            max_length = max(max_length, current_length)
            current_length = 0
            i += 4
        else:
            current_length += 1
            i += 1
    max_length = max(max_length, current_length)
    return max_length

file_paths = ['36037.txt']
combined_text = read_files(file_paths)

result = max_length_without_xzzy(combined_text)
print(result)
"""

#3

def read_files(file_paths):
    combined_text = ""
    for path in file_paths:
        with open(path, 'r') as file:
            combined_text += file.read().strip()
    return combined_text

def count_groups_of_e(text):
    count = 0
    i = 0
    while i < len(text):
        if text[i] == 'E':
            start = i
            i += 1
            while i < len(text) and text[i] != 'E':
                if text[i] == 'F':
                    break
                i += 1
            if i < len(text) and text[i] == 'E' and (i - start + 1) >= 12:
                count += 1
        i += 1
    return count

file_paths = ['46982.txt']
combined_text = read_files(file_paths)

result = count_groups_of_e(combined_text)
print(result)