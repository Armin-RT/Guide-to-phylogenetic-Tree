# Guide-to-phylogenetic-Tree
Code for all steps
All code was done in Ubuntu Software
Get sequences
- Download genomes and put them in a folder
- Make a file with all sequences
-Make a Database

Tblast
-Run Tblast (use script from blast file directly in the terminal)

-Stitch up Tblasted results 

-Retrive haplotype

obs: These 2 scripts dont require changes in the file, for adding input file in, but you can just write the name of it when you run script
ex: python3 BLASTstitcher.py results.txt   


Reverse complement
-Get sequences that are in wrong direction from stitched tblast
-Retrieve the haplotype for those
-Complement them
-Switch out the complemented sequences with the original haplotype file
-Retrieve full name of the sequences


Remove pseudogenes
-Translate to protein 
transeq -sequence Example.txt -outseq outputp.txt 
-Remove them with premature proteins
-Create file with the asequences with matching names as the proteins that are left

Alignment
-use MACSE to align sequences
-Remove any more unnecessary sequences
-Code
java -jar macse_v2.07.jar -prog alignSequences -seq file.fasta

Iqtree
-Run Iqtree with 1000 boostrap replicates
-Generate the Tree
Code
-Iqtree2 -s - BB 1000

Analyze Data
-  first grab all the names of all the sequences before counting
-Count amount of fusspoks in each strain  (some strains have to be manually added,)
-Count how many fusspoks in genomic locations in some strains (some have to be added manually) – one also has to categorize the parts of the names of the data in excel
