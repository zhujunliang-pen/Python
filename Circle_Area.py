import sys
import getopt

from Const import PI

def Circle_Area(r):
	return PI * r * r
	
	
def main(args):
	r = 0
	try:
		opts, args = getopt.getopt(args, "r:", ["--radius"])
	except getopt.GetoptError:
		print("params error, -r [radius]")
		exit
	for opt,arg in opts:
		if opt in ("-r", "--radius"):
			try:
				r = float(arg)
			except Exception:
				print("半径数字输入错误")
				
	print("r=", r)
	print("Circle R=", r, " Area=", Circle_Area(r))

if __name__ == "__main__":
	main(sys.argv[1:])