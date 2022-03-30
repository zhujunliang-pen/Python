import os, shutil, sys
print(dir(os))
dir(shutil)
#help(os)
print(os.getcwd())      # 返回当前的工作目录'C:\\Python34'
#os.chdir('/server/accesslogs')   # 修改当前的工作目录
#os.system('mkdir today')   # 执行系统命令 mkdir 

#shutil.copyfile('data.db', 'archive.db')
#shutil.move('/build/executables', 'installdir')
sys.stderr.write('Warning, log file not found starting a new one\n')
sys.stdout.write("stdout")
print(sys.platform)
assert ('linux' in sys.platform), "该代码只能在 Linux 下执行"