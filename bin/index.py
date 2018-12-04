import argparse

parser = argparse.ArgumentParser(description = 'page.chatshier is used to page https://service.chatshier.com')

parser.add_argument('-dev', '--develop', dest = 'develop', action = 'store_const', const = True, help = 'enable to page develop')
parser.add_argument('-rel', '--release', dest = 'release', action = 'store_const', const = True, help = 'enable to page release')
parser.add_argument('-mas', '--master', dest = 'master', action = 'store_const', const = True, help = 'enable to page master')

args = parser.parse_args()

if args.develop:
    print('start to page develop')

if args.release:
    print('start to page release')

if args.master:
    print('start to page master')
