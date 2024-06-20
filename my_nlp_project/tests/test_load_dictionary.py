import unittest
import os
import sys

# プロジェクトのルートディレクトリを取得
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(project_root_path, 'src'))

from my_library.load_dictionary import load_dictionary1, load_dictionary2

class TestLoadDictionary(unittest.TestCase):
    def test_load_dictionary1(self):
        # 辞書ファイル1のパスを設定
        dict1_path = os.path.join(project_root_path, 'ext-lib', 'dictionary1.txt')

        # 辞書ファイル1を読み込む
        dictionary1 = load_dictionary1(dict1_path)
        # サンプルデータが正しく読み込まれているか確認
        self.assertIn('２，３日', dictionary1)
        self.assertEqual(dictionary1['２，３日'], 'e')

        # 辞書の内容を出力
        print("Dictionary 1 (first 10 entries):", list(dictionary1.items())[:10])

    def test_load_dictionary2(self):
        # 辞書ファイル2のパスを設定
        dict2_path = os.path.join(project_root_path, 'ext-lib', 'dictionary2.txt')

        # 辞書ファイル2を読み込む
        dictionary2 = load_dictionary2(dict2_path)
        # サンプルデータが正しく読み込まれているか確認
        self.assertIn('あがく', dictionary2)
        self.assertEqual(dictionary2['あがく'], 'ネガ（経験）')

        # 辞書の内容を出力
        print("Dictionary 2 (first 10 entries):", list(dictionary2.items())[:10])

if __name__ == '__main__':
    unittest.main()



