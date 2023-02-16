import os
import sys

def determine_word_count(target_program_path: str, buffer_size: int) -> int:
    for words in range(1, buffer_size + 64):
        if os.system(target_program_path + ' ' + 'AAAA' * words):
            return words - 1
    return -1
    
if __name__ == '__main__':
    word_count = determine_word_count(sys.argv[1], int(sys.argv[2]))
    print('Required words: ' + str(word_count))
    print('String: ' + 'AAAA' * word_count)
