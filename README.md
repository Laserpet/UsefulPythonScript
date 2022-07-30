# UsefulPythonScript
To collect some useful python script that I use in my past work

Usually just drag it into the folder that you'd like to run it, and open the terminal and run:

$ python3 xxx.py -a 123 -b 321


And it will work just fine. Also check the environment requirement yourself, which I don't really know what will went wrong on other computers~


# RenamePictures.py
    Its a command line script for now.
    Rename all jpg jpeg png webp files in folders
    Notice that all except png will be converted into jpg.
    Once done, it could not be undone, use with care.
    By default it will use the date as one of the seeds of the serial name. 
    You can set another seed to make the serial number change (multiplier), and use -id to set the file name prefix.
        
    -p specifies the path eg: D:\pictures\test\
    -l specifies the filename length of the renamed file
    -s specifies the seed for the date multiplier
    -r specifies randomization
    -v print conversion process log
    
    目前是控制台命令执行。
    重命名文件夹下所有的图片文件，将名字改为随机数字或按id+日期+序列号的形式。当然可以选择参数。
    默认即使用日期作为序列名称的种子之一，可以再设定一个种子使得序列号发生变化（乘数），使用-id 设定文件名前缀。
    -p 指定路径 eg: D:\pictures\test\
    -l 指定重命名文件的文件名长度
    -s 指定日期乘数的种子
    -r 指定随机化
    -v 打印转化过程日志


# BatchTest.py
    Specificly used in my TensorRT project, to test the engine file that was converted in batch and output the info into json file.
