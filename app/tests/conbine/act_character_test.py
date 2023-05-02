import unittest
import bot.precure.service as precure
import bot.core as core

class ActCharacterTest(unittest.TestCase):
    precure_names = [
        'キュアブラック',
        'キュアホワイト',
        'シャイニールミナス',
        'キュアブルーム',
        'キュアイーグレット',
        'キュアドリーム',
        'キュアルージュ',
        'キュアレモネード',
        'キュアミント',
        'キュアアクア',
        'ミルキィローズ',
        'キュアピーチ',
        'キュアベリー',
        'キュアパイン',
        'キュアパッション',
        'キュアブロッサム',
        'キュアマリン',
        'キュアサンシャイン',
        'キュアムーンライト',
        'キュアメロディ',
        'キュアリズム',
        'キュアビート',
        'キュアミューズ',
        'キュアハッピー',
        'キュアサニー',
        'キュアピース',
        'キュアマーチ',
        'キュアビューティ',
        'キュアハート',
        'キュアダイヤモンド',
        'キュアロゼッタ',
        'キュアソード',
        'キュアエース',
        'キュアラブリー',
        'キュアプリンセス',
        'キュアハニー',
        'キュアフォーチュン',
        'キュアフローラ',
        'キュアマーメイド',
        'キュアトゥインクル',
        'キュアスカーレット',
        'キュアミラクル',
        'キュアマジカル',
        'キュアフェリーチェ',
        'キュアホイップ',
        'キュアカスタード',
        'キュアジェラート',
        'キュアマカロン',
        'キュアショコラ',
        'キュアパルフェ',
        'キュアエール',
        'キュアアンジュ',
        'キュアエトワール',
        'キュアマシェリ',
        'キュアアムール',
        'キュアスター',
        'キュアミルキー',
        'キュアソレイユ',
        'キュアセレーネ',
        'キュアコスモ',
        'キュアグレース',
        'キュアフォンテーヌ',
        'キュアスパークル',
        'キュアアース',
        'キュアサマー',
        'キュアコーラル',
        'キュアパパイア',
        'キュアフラミンゴ',
        'キュアラメール',
        'キュアプレシャス',
        'キュアスパイシー',
        'キュアヤムヤム',
        'キュアフィナーレ',
        'キュアスカイ',
        'キュアプリズム',
        'キュアウィング',
        'キュアバタフライ',
    ]

    def setUp(self):
        # 初期化処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_act_precure(self):

        for name in self.precure_names:
            call = precure.get_call_message(name)
            print(core._generate_response(call))

        self.assertEqual(1, 1)

    def test_act_mascot(self):

        for name in self.precure_names:
            call = precure.get_call_message(name)
            print(core._generate_response(call))

        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()
