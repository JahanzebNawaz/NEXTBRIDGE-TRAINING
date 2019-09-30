
import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volumne of Cylinder')
parser.add_argument('-r', '--radius', type=int, required=True, help='Radius of Cylinder')
parser.add_argument('-hh', '--height', type=int, required=True, help='Height of Cylinder')
args = parser.parse_args()
def calculate(r, h):
    radius = (math.pi) * (r**2) * h
    return radius

if __name__ == '__main__':
    print(calculate(args.radius, args.height))


