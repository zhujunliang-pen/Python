import sys, getopt
print(__name__)

def main(argv):
	inputfile = "";
	outputfile = "";
	try:								#ho: = -h-o:	
		opts, args = getopt.getopt(argv, "h:i:o:", ["ifile=", "ofile="])
	except getopt.GetoptError:
		print("E: Getopt.py -i <inputfile> -o <outputfile>")
		sys.exit(2)
	for opt, arg in opts:
		if opt == "-h":
			print("H: Getopt.py -i <inputfile> -o <outputfile>")
			exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	print("输入的文件为：", inputfile)
	print("输出的文件为：", outputfile)
	for arg in args:
		print(arg)
if __name__ == "__main__":
	main(sys.argv[1:])