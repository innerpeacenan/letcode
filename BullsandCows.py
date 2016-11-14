class Solution(object):
    def getHint(self, secret, guess):
        n=0
        m=0
        l=len(secret)
        for i in range(l):#计算bull位置数字都对的数量
            if secret[i]==guess[i]:
                n+=1
        for i in "0123456789":#数字对位置不对的数量
            p=secret.count(i)
            q=guess.count(i)
            if p>=q:
                m+=q
            else:
                m+=p
        m=m-n#计算bows
        return str(n)+'A'+str(m)+'B'
            
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        