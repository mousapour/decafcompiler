import sys, getopt
from .parser import parse
def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('main.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    success = True


    with open("tests/" + inputfile, "r") as input_file:


        success = parse(input_file.read())

    with open("out/" + outputfile, "w") as output_file:
        # write result to output file. 
        # for the sake of testing :
        output_file.write("OK" if success else "Syntax Error")
#         output_file.write("""class
# T_ID Program
# {
# void
# T_ID main
# (
# )
# {
# }
# }""")


if __name__ == "__main__":
    main(sys.argv[1:])
