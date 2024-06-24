import os
import sys
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(project_root_path)

sys.path.append(project_root_path)
import my_library.load_input_data as input_loader
import my_library.load_dictionary1 as dictionary_loader
import my_library.count_statistics as counter
import my_library.predict_polarity as predictor
import my_library.manage_output as output_manager

sentence_arrays = ["雨が降ってるから気分が落ち込む。早く晴れてほしいな。",
"友達と映画を見に行ったけど、感動して泣いちゃった。",
"新しい仕事が始まって緊張するけど、頑張りたい。",
"美味しいケーキを食べて、幸せな気持ちになった。",
"ペットが病気になって心配でたまらない。早く元気になって。",
"家族と一緒に過ごす時間がとても楽しかった。",
"仕事でミスをして上司に叱られてしまった。反省しないと。",
"旅行の計画を立てているときが一番ワクワクする。",
"久しぶりに会った友達と話して、元気が出た。",
"電車が遅れてイライラするけど、仕方がない。"]

#sentence = "コロナのせいで病院送りになって絶望していたが、治療後人並ならぬ賢さを手に入れた。"
d1 = dictionary_loader.load_dictionary1("../ext-lib/dictionary1.txt")
d2 = dictionary_loader.load_dictionary2("../ext-lib/dictionary2.txt")

#print(sentence_arrays)
#print(counter.regroup(d2).get("ほめ"))
#print(d2.get(sentence[0:4]))
#print(counter.count(d1, d2, sentence))
#print(predictor.predict_2(counter.count(d1, d2, sentence)))

result = []
for i in range(len(sentence_arrays)):
    sentence = sentence_arrays[i]
    count_statistics = counter.count(d1, d2, sentence)
    result.append(predictor.predict_2(count_statistics))

print(result)
#output_manager.output(sentence_arrays, result)