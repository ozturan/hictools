###########################################
# Juicebox to sparse triangular matrices  #
# for each chr-chr interactions			  #
# Use various ozturan/hictools            #
# for different Hi-C data formats.        #
#										  #
# Dogancan Ozturan               		  #
# 2018									  #
###########################################
# usage: python Juicebox2STM.py <juicertools jar file> <input .hic file> <bin size>


from subprocess import call
import sys

# specify the juicertool name
jarfile=sys.argv[1]
# specify the .hic file name
filename=sys.argv[2]
# select the bin size
bin=int(sys.argv[3])

chromosomes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, "X", "Y"]

def convert():
	for i in chromosomes:
	        call(["mkdir", "chr{0}".format(i)])
	        for j in chromosomes:
	                print "Dumping -> " "chr{0}".format(i), "chr{0}".format(j)
	                call(["java", "-jar", "{0}".format(jarfile),
	                        "dump", "observed", "NONE", "{0}".format(filename), "chr{0}".format(i), "chr{0}".format(j), "BP", "%d" %bin, "{0}_chr{1}_chr{2}.matrix".format(filename, i, j)])
	                call(["mv", "{0}_chr{1}_chr{2}.matrix".format(filename, i, j), "chr{0}".format(i)])
	                print "Done -> chr{0}_chr{1}.matrix".format(i, j)


convert()
print "\x1b[3;34;40m", "DUMPED! (Bin size:{0})".format(bin), "\x1b[0m"
