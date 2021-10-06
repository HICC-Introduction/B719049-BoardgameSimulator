class Point2:
    x: int
    y: int

    def __init__(self, x: int = 0, y: int = 0):
        """
        Struct for 2-dimension coordinate, integer values only.
        :param x: x coordinate
        :param y: y coordinate
        """
        self.x: int = x
        self.y: int = y
