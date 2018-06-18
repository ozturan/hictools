#!/usr/bin/env Rscript
###########################################
# Sparse triangular matrices to           #
# Fit-Hi-C-ready interactions matrices		# 
# Use various ozturan/hictools            #
# for different Hi-C data formats.        #
#										                      #
# Dogancan Ozturan               		      #
# 2018									                  #
###########################################
# usage: Rscript STM2FitHiC.R <filename> <chr1> <chr2> 
library(readr)
library(data.table)

args = commandArgs(trailingOnly=TRUE)

# data name
dataname2=args[1]
dataname=args[1]
#select the chromosome
chromosome1 = args[2]
chromosome2 = args[3]

dataname <- as.data.table(read_delim(sprintf("%s", dataname), 
                                     "\t", escape_double = FALSE, col_names = FALSE, 
                                     trim_ws = TRUE))


dataname[, ':='  (chr1 = chromosome1, chr2 = chromosome2)]
dataname <- dataname[,c(4, 1, 5, 2, 3)]

# Save!
write.table(dataname, file=sprintf('input_fithic_%s', dataname2), 
            quote=FALSE, sep='\t', col.names = FALSE, row.names = FALSE)

sprintf("Done!")

