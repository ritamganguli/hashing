class Solution:

    def longestKSubstr(self, s, k):
        i=-1
        j=-1
        ans=0
        hashmap={}
        while(True):
            f1=False
            f2=False
            while(i<len(s)-1):
                f1=True
                i+=1
                ch=s[i]
                #Fisrtly putting it into hashmap 
                if hashmap.get(ch)!=None:
                    hashmap[ch]+=1
                if hashmap.get(ch)==None:
                    hashmap[ch]=1
                #If there is lesser than k unique charecters we still consider taking
                if len(hashmap)<k:
                    continue
                #If we get k unique charecters
                elif len(hashmap)==k:
                    length=i-j
                    #if length so obtained of substring is greater than previous
                    if length>ans:
                        ans=length
                #If length exceeds than k we break
                else:
                    break
            while(j<i):
                f2=True
                j+=1
                ch=s[j]
                #If there is only one frequency of an element we remove it from the hashmap
                if hashmap.get(ch)==1:
                    del hashmap[ch]
                #If there is grater one frequency of an element we decrease it from the hashmap
                else:
                    hashmap[ch]-=1
                #If there are still greater than k elements we continue to remove
                if len(hashmap)>k:
                    continue
                #Exactly k we try to consider
                elif len(hashmap)==k:
                    length=i-j
                    if length>ans:
                        ans=length
                    else:
                        break
            if f1==False and f2==False:
                break
        if ans==0:
            return -1
        return(ans)
