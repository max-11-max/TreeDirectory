import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volume of a Cylinder')
parser.add_argument('-r', '--radius', type=int, metavar='', required=True,
                    help='Radius of Cylinder')
# -- makes argument optional, -r is its short notation, metavar='' removes
# the description which would apply to both notations
parser.add_argument('-H', '--height', type=int, metavar='', required=True,
                    help='Height of Cylinder')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
# basically adds optional arguments that will have different functions, if
# if called, or not called at all, required=True : argument must be passed
args = parser.parse_args()
# make arguments passed through the parser


def cylinder_volume(radius: int, height: int) -> float:
    vol = math.pi * (radius ** 2) * height
    return vol


if __name__ == '__main__':
    volume = cylinder_volume(args.radius, args.height)  # refers to the args
    # long notation
    if args.quiet:
        print(volume)
    elif args.verbose:
        print('Volume of a Cylinder with radius %s and height %s is %s' %
              (args.radius, args.height, volume))
    else:
        print('Volume of Cylinder = %s' % volume)
