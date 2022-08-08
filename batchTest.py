import os
import argparse
import json


# usage python ./batchTest.py -b 10

def getargsinput():
    parser = argparse.ArgumentParser('Set script parameter', add_help=False)
    parser.add_argument("-b", "--batch", type=int, default="10", help="Input Batch Numbers")
    # (optional) if trtexec cmd not found, fill in the path like ./batchTest.py -e '~/TensorRT-8.4.1.5/bin/'
    parser.add_argument("-e", "--path", type=str, default='', help="Trtexec cmd Path")
    parser.add_argument("-j", "--jsonfile", type=str, default="", help="Import plan Path from json")
    parser.add_argument("-o", "--outputpath", type=str, default="", help="Output Path for json")
    return parser


def export_path():
    if args.jsonfile is None:
        return False
    else:
        try:
            with open(args.jsonfile, "r") as jsonfile:
                s = json.load(jsonfile)
        except FileNotFoundError:
            print("No indicate json found")
            return False
    return s


class BatchTest:
    def __init__(self):
        self.tested_num = 0
        # print("\033[1;33;44mIf trtexec is not found, please run with -e xxx/TensorRT/bin/\033[0m")

    def test_output(self, filename, filepath):
        print("\033[1;39;42mOutputting Profile and times for {name} \033[0m".format(name=filename))
        # Execute the Command here
        os.system("{exe}trtexec --loadEngine={path} --batch={batchnum} --exportProfile={outputpath}{name}_Profile.json\
                         --exportTimes={name}_Time.json ".format(path=filepath, batchnum=args.batch,
                                                                 name=filename, exe=args.path,
                                                                 outputpath=args.outputpath))
        self.tested_num += 1
        if self.tested_num == 0:
            print("No .plan or .PLAN File found in this directory, please Check")
            return 0
        return self.tested_num

    def test_all_engine_infolder(self):
        for filesname in os.listdir():
            if filesname.endswith(".plan") or filesname.endswith(".PLAN"):  # Acquire specifics .plan file.
                engine_path = os.path.join(os.getcwd(), filesname)
                self.test_output(filesname, engine_path)

    def automated_test(self):
        if export_path() is False:
            print("No .json input, looking for plans in local folder")
            self.test_all_engine_infolder()
        else:
            paths = export_path()
            for item in paths:
                engine_path = paths[item]["plan_path"]
                self.test_output(item, engine_path)
        return 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Batch Engine test Script', parents=[getargsinput()])
    args = parser.parse_args()
    test = BatchTest()
    test.automated_test()
