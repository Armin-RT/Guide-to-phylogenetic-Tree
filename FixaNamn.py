def do_subs(infile, outfile):
    intxt = open(infile).read()
    for sub in open('all_sequences.fna'):
        if sub.startswith('>'):
            sub = sub.strip().split(' ', 1)
            seq_id = sub[0][1:]
            full_name = sub[1]
            intxt = intxt.replace(seq_id, full_name)
    open(outfile, 'w').write(intxt)

do_subs('Combinedhaplotypes.txt', 'CombinedhaplotypesNames.txt')
