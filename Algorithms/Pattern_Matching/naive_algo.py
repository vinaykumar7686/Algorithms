def match(txt, pat):
    '''
    function to return list containing indices where the matched patern is found.
    Inputs:
    txt = string in which pattern is to be found
    pat = pattern that is to be searched
    Output:
    list containing indices

    Time Complexity: O((n-m+1)*m)
    '''
    n = len(txt)
    m = len(pat)
    ans = []
    for i in range(0, n-m+1):
        j=0

        while j!=m:
            if txt[i+j]!=pat[j]:
                break
            j+=1
        
        if j==m:
            print(f'Pattern found at index : {i}')
            ans.append(i)
    return ans

if __name__ == "__main__":
    print(f'Pattern found at indices: {match("AABAACAADAABAAABAA","AABA")}')