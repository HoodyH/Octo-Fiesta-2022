
# find horizontal words from a matrix from a word list
def find_horizontal(matrix, words):
    # find horizontal words
    for word in words:
        for row_idx in range(len(matrix)):
            for col_idx in range(len(matrix[0])):
                possible_world = ''
                for i in range(len(word)):
                    try:
                        possible_world += matrix[row_idx][col_idx + i]
                    except IndexError:
                        break

                if possible_world == word:
                    print('found horizontal word: {}'.format(word))
                    return True

    return False

if __name__ == '__main__':
    # print hello word
    print('Hello World')
