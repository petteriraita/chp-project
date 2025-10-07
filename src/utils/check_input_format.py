import logging

# Sigma letters(lowercase)
sigma_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
# Gamma letters(uppercase)
gamma_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
# number characters
number_characters = [chr(i) for i in range(ord('0'), ord('9') + 1)]
# special characters(comma, colon,linefeed)
special_characters = [',', ':', '\n']

def check_valid_characters(file_content: str) -> bool:
    """
    Return boolean indicating whether all characters in the file content are valid.
    """
    valid_characters = set(sigma_letters + gamma_letters + number_characters + special_characters)
    for char in file_content:
        if char not in valid_characters:
            return False
    return True


def check_input_format(file_content: str, logger: logging.Logger = None) -> bool:
    """
    Return boolean indicating whether the input format is valid.
    """
    
    if not check_valid_characters(file_content):
        if logger:
            logger.error("Invalid characters found in input")
        return False
    
    # Check that the first line contains a number
    lines = file_content.splitlines()
    first_line = lines[0].strip()
    second_line = lines[1].strip()

    # Check that there are at least 4 lines (1 for n, 1 for s, 1 for string t, 1 for subset R)
    if not lines or len(lines) < 4:
        if logger:
            logger.error("Input must contain at least 4 lines")
        return False
    
    # Check that the first line is a valid integer
    if not first_line.isdigit():
        if logger:
            logger.error("First line must be a valid integer")
        return False
    k = int(first_line)

    # Check that there are at least n + 2 lines: 1 for n, 1 for s, k for k strings
    if len(lines) < 1 + 1 + k:
        if logger:
            logger.error(f"Input must contain at least {1 + 1 + k} lines given n={k}")
        return False 
    
    # Check that the second line contains only sigma letters
    second_line = lines[1].strip()
    if any(char not in sigma_letters for char in second_line):
        if logger:
            logger.error("Second line must contain only sigma letters (lowercase a-z)")
        return False
    
    # Check that the following k lines contain only gamma and sigma letters
    for i in range(2, 2 + k):
        line = lines[i].strip()
        if any(char not in sigma_letters + gamma_letters for char in line):
            if logger:
                logger.error(f"Line {i+1} must contain only sigma (a-z) and gamma (A-Z) letters")
            return False
        
    # Check that the remaining lines (at most 26) are in the correct format
    remaining_lines = lines[2 + k:]
    if len(remaining_lines) > 26:
        if logger:
            logger.error("There can be at most 26 lines defining the subset R")
        return False

    for line in remaining_lines:
        if not line:
            if logger:
                logger.error("Empty line found in subset R definition")
            return False
        # Must start with a single uppercase letter from gamma_letters
        if line[0] not in gamma_letters:
            if logger:
                logger.error(f"Line in subset R must start with a single uppercase letter (A-Z), found: {line[0]}")
            return False
        # Must be followed by a colon
        if len(line) < 2 or line[1] != ':':
            if logger:
                logger.error("Line in subset R must have a colon (:) after the initial uppercase letter")
            return False
        # The rest (after colon) is either empty or a comma-separated list of sigma/gamma/number chars
        elements = line[2:].split(',') if line[2:] else []
        for elem in elements:
            if elem and any(c not in sigma_letters for c in elem):
                if logger:
                    logger.error(f"Invalid character found in subset R definition: {elem}")
                return False
            
    return True