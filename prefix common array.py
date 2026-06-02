class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        h={}
        c=[]
        count=0
        for i in range(len(A)):
            if A[i] in h and B[i] in h:
                count=count+2

            elif A[i]==B[i] :
                h[A[i]]=1
                count+=1

            elif A[i] in h and B[i] not in h:
                count+=1
                h[B[i]]=1

            elif A[i]not in h and B[i] in h:
                count+=1
                h[A[i]]=1

            else:
                h[A[i]]=1
                h[B[i]]=1

            c.append(count)
        return c
