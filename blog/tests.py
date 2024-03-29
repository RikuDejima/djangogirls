from django.test import TestCase
from blog.number import Number
from unittest.mock import MagicMock
 
class NumberTest(TestCase):
    """Number クラスのテスト"""

    def test_get_square(self):
        # モック作成
        square_mock = MagicMock()

        # square メソッドが呼ばれたら 4 を返す
        square_mock.square.return_value = 4

        # モックを注入した number オブジェクトを作成
        number = Number(2, square=square_mock)

        # get_square メソッドは、 square_mock の結果をそのまま返す
        self.assertEqual(number.get_square(), 4)

        # square オブジェクトの square メソッドが
        # 1回、正しく呼ばれていることを確認
        self.assertEqual(square_mock.square.call_count, 1)

        # 1回目（call_args_list[0]）に関数が呼ばれる時の
        #  x 引数（1番目の引数 args[0]）の値は 2
        args, kwargs = square_mock.square.call_args_list[0]
        self.assertEqual(args[0], 2)