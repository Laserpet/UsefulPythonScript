import os
import random
import time
import argparse


# usage python ./xxx.py -id someone


def getargsinput():
    parser = argparse.ArgumentParser('Set script parameter', add_help=False)
    parser.add_argument("-id", "--identify", type=str, default="", help="Identify the renamed file with extra ids")
    parser.add_argument("-p", "--path", type=str, default='D:\\test\\', required=True,
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

    def rename(self, input_args):
        self.path = input_args.path
        filelist = os.listdir(input_args.path)  # store the path args
        total_num = len(filelist)  # Acquire all file in folders
        print("Get {} pics in folder, continuing process.".format(total_num))
        startnum = 1  # starts with 1
        nowtime = int(time.strftime("%m%d", time.localtime()))  # Acquire the time now


        if input_args.random:
            upperlimit = 10**input_args.length
            print("The whole thing is random now, but the multiplier is set to {}.".format(input_args.seed))
            i = random.randint(0, 1000) * input_args.seed
        else:
            print("Using today's date {} to rename  and seed is set to {}, ".format(nowtime, input_args.seed), end='')
            print('by default the nums will be in serial, but you can also random the numbers with -r')
            i = nowtime * args.seed + startnum  # Multiply the date with seed, if not set then it will be 10000.
        print('File name length is set to {}.'.format(input_args.length))
        for item in filelist:
            if input_args.random:
                i = random.randint(0, upperlimit)
            ids = input_args.identify
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path),
                                   ids + format(str(i), '0>{}s'.format(input_args.length)) + '.jpg')
                try:
                    os.rename(src, dst)
                    if input_args.verbose:
                        print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
            if item.endswith('.png'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path),
                                   ids + format(str(i), '0>{}s'.format(input_args.length)) + '.png')
                try:
                    os.rename(src, dst)
                    if input_args.verbose:
                        print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
            if item.endswith('.jpeg'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path),
                                   ids + format(str(i), '0>{}s'.format(input_args.length)) + '.jpg')
                try:
                    os.rename(src, dst)
                    if input_args.verbose:
                        print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
            if item.endswith('.webp'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path),
                                   ids + format(str(i), '0>{}s'.format(input_args.length)) + '.jpg')
                try:
                    os.rename(src, dst)
                    if input_args.verbose:
                        print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    print("none of jpg,png or webp found, please check the folder or alter the code")
                    continue
        print("Process done.")
        return 1


if __name__ == '__main__':
    R = BatchRename()
    parser = argparse.ArgumentParser('Batch Engine test Script', parents=[getargsinput()])
    args = parser.parse_args()
    R.rename(args)
