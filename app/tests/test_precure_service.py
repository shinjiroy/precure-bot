import unittest
import bot.precure.service as precure

class PrecureServiceTest(unittest.TestCase):
    def setUp(self):
        # 初期化処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_call_message(self):
        name = 'モフルン'
        print(precure.call_message(name))
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()
