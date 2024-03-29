from blog.square import Square
 
class Number():
    """数字を扱うクラス"""

    # square を外から入れられるようにしてやる
    def __init__(self, x, square = Square()):
        self.x = x
        self.square = square

    def get_square(self):
        """2乗の値を返す"""
        return self.square.square(self.x)
