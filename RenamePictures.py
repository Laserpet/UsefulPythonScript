import os
import random
import sys
import time
import argparse


# usage python ./xxx.py -id someone


def getargsinput():
    parser = argparse.ArgumentParser('Set script parameter', add_help=False)
    parser.add_argument("-id", "--identify", type=str, default="", help="Identify the renamed file with extra ids")
    parser.add_argument("-p", "--path", type=str, required=True,
                        help="target folder, if not set then it's the current folder.")
    parser.add_argument("-l", "--length", type=int, default=7, help="How long the name will be")
    parser.add_argument("-s", "--seed", type=int, default=10000, help="time multiple seed")
    parser.add_argument("-r", "--random", default=False, action='store_true', help="Random rename the file")
    parser.add_argument("-v", "--verbose", default=False, action='store_true', help="If you want Verbose")

    return parser


class BatchRename:
    '''
    Rename all jpg jpeg png webp files in folders
    Notice that all except png will be converted into jpg.
    Once done, it could not be undone, use with care.
    '''

    def __init__(self):
        self.path = None
        self.converted = 0

    def rename(self, input_args):
        self.path = input_args.path
        filelist = os.listdir(input_args.path)  # store the path args
        total_num = len(filelist) - 1  # Acquire all file in folders
        print("Get {} files in folder, processing.".format(total_num))
        startnum = 0  # starts with 0
        nowtime = int(time.strftime("%m%d", time.localtime()))  # Acquire the time now

        if input_args.random:
            upperlimit = 10 ** input_args.length
            print("Random file name with length set to {}.".format(input_args.length))
        else:
            print("Using today's date {} to rename  and seed is set to {}, ".format(nowtime, input_args.seed), end='')
            print('by default the nums will be in serial, but you can also random the numbers with -r')
            i = nowtime * args.seed + startnum  # Multiply the date with seed, if not set then it will be 10000.
            print('File name length is set to {}.'.format(input_args.length))

        # if input_args.verbose:
        #     print(filelist)

        for item in filelist:

            if input_args.random:
                i = random.randint(0, upperlimit)
            ids = input_args.identify

            if item.endswith('.jpg') or item.endswith('.JPG') or item.endswith('.JPEG') or item.endswith('.jpeg') \
                    or item.endswith('.jfif') or item.endswith('.JFIF') or item.endswith('.webp') or item.endswith(
                '.WEBP'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path),
                                   ids + format(str(i), '0>{}s'.format(input_args.length)) + '.jpg')
                try:
                    os.rename(src, dst)
                    if input_args.verbose:
                        print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                    self.converted += 1
                except:
                    continue
            if item.endswith('.bmp') or item.endswith('.BMP'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path),
                                   ids + format(str(i), '0>{}s'.format(input_args.length)) + '.bmp')
                try:
                    os.rename(src, dst)
                    if input_args.verbose:
                        print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                    self.converted += 1
                except:
                    continue
            if item.endswith('.png') or item.endswith('.PNG'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path),
                                   ids + format(str(i), '0>{}s'.format(input_args.length)) + '.png')
                try:
                    os.rename(src, dst)
                    if input_args.verbose:
                        print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                    self.converted += 1
                except:
                    print("none of the pictures found, please check the folder or alter the code")
                    continue
            print("\r", end="")
            print("Processing:{}% ({}/{})".format(round(100 * self.converted / total_num), self.converted, total_num),
                  end='', flush=True)
        print("")
        print("Process done, converted {} pictures".format(self.converted))
        return 1


if __name__ == '__main__':
    R = BatchRename()
    parser = argparse.ArgumentParser('Batch Engine test Script', parents=[getargsinput()])
    args = parser.parse_args()
    R.rename(args)
