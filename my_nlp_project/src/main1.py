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

sentence_arrays = input_loader.load("../data/processed_data_v1.txt")
sentence = "友達と喧嘩してしまって、悲しい気持ちになった。"
d1 = dictionary_loader.load_dictionary1("../ext-lib/dictionary1.txt")
d2 = dictionary_loader.load_dictionary2("../ext-lib/dictionary2.txt")

#print(counter.regroup(d2).get("ほめ"))
#print(d2.get(sentence[0:4]))
#print(counter.count(d1, d2, sentence))
print(predictor.predict_2(counter.count(d1, d2, sentence)))

result = []
for i in range(len(sentence_arrays)):
    sentence = sentence_arrays[i]
    count_statistics = counter.count(d1, d2, sentence)
    result.append(predictor.predict(count_statistics))

output_manager.output(sentence_arrays, result)