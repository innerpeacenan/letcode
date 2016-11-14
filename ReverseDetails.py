#本题首先将n转换为二进制，补高位0，高低位替换转换为二进制
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        a=[]
        m=0#Reverse的数
        if n==0:
            return 0
        while(n!=0):#将n转换为二进制，存入数组a中
            n,m=divmod(n,2)
            a.append(m)
        l=len(a)
        while(l<32):#在高位补0，补齐32位
            a.append(0)
            l+=1
        for i in range(0,32):#以a高位为地位，转换为十进制数
            if a[i]==1:
                m+=pow(2,31-i)
                
        return m-1