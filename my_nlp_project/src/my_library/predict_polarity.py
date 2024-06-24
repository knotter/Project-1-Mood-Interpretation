def predict(count_statistics):
    Mood_result = count_statistics
    #cue = count_statistics[1:len(count_statistics)-1]
    #sentence = count_statistics[len(count_statistics)-1]

    if Mood_result[0] > Mood_result[1]:
        return "Positive"
    elif Mood_result[0] < Mood_result[1]:
        return "negative"
    else:
        return "neutral"

def predict_2(count_statistics):
    Mood_result = count_statistics[0]
    cue = count_statistics[1:len(count_statistics)-1]
    #print(cue)
    sentence = count_statistics[len(count_statistics)-1]
    regroup = []
    while sentence.find("。") != -1:
        while sentence.find("、") != -1:
            regroup.append(sentence.split("、")[0])
            sentence = sentence[sentence.index("、") + 1:]
            pass
        regroup.append(sentence.split("。")[0])
        sentence = sentence[:sentence.index("。")] + sentence[sentence.index("。") + 1:]

    result = []
    for m in range(len(regroup)):
        p, n, e = 0, 0, 0
        for index in cue[0]:
            #print(type(regroup[m]))
            #print(index[0])
            if regroup[m].find(index[0]) != -1:
                #print("HELLO")
                if index[1] == "p":
                    p += 1
                if index[1] == "n":
                    n += 1
                if index[1] == "e":
                    e += 1

        result.append([p, n, e])
    print("finished")
    return sentence, predict(result[-1])
