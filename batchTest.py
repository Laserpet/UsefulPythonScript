import os
import argparse


# usage python ./batchTest.py -b 10

def getargsinput():
    parser = argparse.ArgumentParser('Set script parameter', add_help=False)
    parser.add_argument("-b", "--batch", type=int, default="10", help="Input Batch Numbers")
    # (optional) if trtexec cmd not found, fill in the path like ./batchTest.py -e '~/TensorRT-8.4.1.5/bin/'
    parser.add_argument("-e", "--path", type=str, default="", help="Trtexec cmd Path")
    return parser


class BatchTest:
    def __init__(self):
        self.tested_num = 0
        print("\033[1;33;44mIf txtexec is not found, please run with -e xxx/TensorRT/bin/\033[0m")

    def test_all_engine(self, args):
        self.trtexec_path = '{}'.format(args.path)
        for files in os.listdir():
            if files.endswith(".plan") or files.endswith(".PLAN"):  # Acquire specifics .plan file.
                print("Outputing Profile and times for {name}".format(name=files))
                engine_path = os.path.join(os.getcwd(), files)
                os.system("{exe}trtexec --loadEngine={path} --batch={batchnum} --exportProfile={name}_Profile.json\
                 --exportTimes={name}_Time.json ".format(path=engine_path, batchnum=args.batch, \
                                                         name=files, exe=self.trtexec_path))
                self.tested_num += 1
        if self.tested_num == 0:
            print("No .plan or .PLAN File found in this directory, please Check")
            return 0
        return self.tested_num


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Batch Engine test Script', parents=[getargsinput()])
    args = parser.parse_args()
    test = BatchTest()
    test.test_all_engine(args)
