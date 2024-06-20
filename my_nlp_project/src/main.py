import os
import sys
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(project_root_path)

sys.path.append(os.path.join(project_root_path, 'src'))
import my_library.load_input_data as input_loader
import my_library.load_dictionary as dictionary_loader
import my_library.count_statistics as counter
import my_library.predict_polarity as predictor
import my_library.manage_output as output_manager

# データファイルと辞書ファイルのパスを設定
dict1_path = os.path.join(project_root_path, 'ext-lib', 'dictionary1.txt')
dict2_path = os.path.join(project_root_path, 'ext-lib', 'dictionary2.txt')

sentence_arrays = input_loader.load("../data/processed_data_v1.txt")

