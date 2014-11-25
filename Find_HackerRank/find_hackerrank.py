def find_word_position_in_sentence(sentence):
    WORD = 'hackerrank'
    output_value = -1
    
    if sentence.endswith(WORD) and sentence.startswith(WORD):
        output_value = 0  
    elif sentence.endswith(WORD):
        output_value = 2
    elif sentence.startswith(WORD):
        output_value = 1
  
    return output_value

if __name__ == '__main__':  
    nb_sentences = int(input())
    for i in range(0, nb_sentences):
        print(find_word_position_in_sentence(input()))