def output(sentence_arrays, result):
    resultsentence = []
    for i in range(len(sentence_arrays)):
        resultsentence.append([sentence_arrays[i], result[i]])
    print(resultsentence)
