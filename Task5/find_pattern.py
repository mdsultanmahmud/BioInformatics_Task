def validate_sequence(test_seq):
    neocleotieds = ["A", "T", "G", "C"]
    tem_seq = test_seq.upper()
    for nuc in tem_seq:
        if nuc not in neocleotieds:
            return False 
    return tem_seq 

def findPatternAndIndex(seq, pattern):
    seq = seq.upper()
    pattern = pattern.upper() 
    patternLen = len(pattern)
    count = 0 
    patternIndex = []
    seq_val = validate_sequence(seq)
    pattern_val = validate_sequence(pattern)
    if seq_val and pattern_val:
        for i in range(len(seq) - patternLen +1):
            if(seq[i:i+patternLen] == pattern):
                count += 1
                patternIndex.append(i)
    else: 
        if(seq_val  == False):
            return "Your Sequence is not valid!!"
        elif(pattern_val == False):
            return "Please Enter a Valid Pattern!!"
    return {"Pattern": pattern, "Repeated Times": count, "Index": patternIndex }


sequence = "CTAGCAGCCGCGGTAAAACGTAGGTCACAAGCGTTGTCCGGAATTACTGGGTGTAAAGGGAGCGCAGGCGGGAAGACAAGTTTGTAGTGAAATCCATGGGCTCAACCCATGAACTGCTTTCAAAACTGTTTTTCTTGAGTAGTGCAGAGGTAGGCGGAATTCCCGGTGTAGCGGTGGAATGTGTAGATATCGGGAGGAACACCAGTGGCGAAGGCGGCCTCCTGGGCACCAACTGACGCTGAGGCTCGAAAGTGTGGGTAGCAAACAGGATTAGATACCCTTGTAGTCCCCACCGTAATCC"
pattern = input("Enter a pattern: ")
print(findPatternAndIndex(sequence, pattern))