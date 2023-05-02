import unittest
import bot.core as core

class CoreTest(unittest.TestCase):
    def setUp(self):
        # 初期化処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_generate_response_start(self):
        messages = [
            {
                'role': 'system',
                'content': 'あなたは魔法つかいプリキュアのモフルンです。モフルンの口調で回答してください。第一人称は「モフルン」です。語尾に必ず「モフ」が付きます。ですますはつけません。',
            }
        ]
        print(core._generate_response(messages))
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()
