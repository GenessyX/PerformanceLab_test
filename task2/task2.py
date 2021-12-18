import argparse
import os

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return "<Point:{},{}>".format(str(self.x), str(self.y))

    def __repr__(self):
        return "<Point:{},{}>".format(str(self.x), str(self.y))

class Circle:
    def __init__(self, center: Point, radius: int):
        self.center = center
        self.radius = radius

    def point_position(self, point: Point) -> int:
        # Circle equation (x - c.x)**2 + (y - c.y)**2 < radius**2
        eq = (point.x - self.center.x)**2 + (point.y - self.center.y)**2 - self.radius**2
        if eq == 0:
            res = 0
        elif eq < 0:
            res = 1
        elif eq > 0:
            res = 2

        return res

    def __str__(self):
        return "<Circle: center: {}, radius: {}>".format(self.center, str(self.radius))

    def __repr__(self):
        return "<Circle: center: {}, radius: {}>".format(self.center, str(self.radius))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('circle_file', type=str)
    parser.add_argument('points_file', type=str)
    args = parser.parse_args()
    circle_file, points_file = args.circle_file, args.points_file
    if (not os.path.exists(circle_file) or not os.path.exists(points_file)):
        raise Exception("File not found")

    with open(circle_file, 'r') as c:
        file_content = [x.strip() for x in c.readlines()]
        center = Point(*[int(x) for x in file_content[0].split(" ")])
        radius = int(file_content[1])
        circle = Circle(center, radius)

    with open(points_file, 'r') as p:
        points = p.readlines()
        for point in points:
            p = Point(*[int(x) for x in point.split(" ")])
            print(circle.point_position(p))

    pass

if __name__ == "__main__":
    main()