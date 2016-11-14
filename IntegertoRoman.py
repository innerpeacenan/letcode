#本题主要利用了python的字典
class Solution(object):
    def intToRoman(self, num):
        m=num
        roman=''
        a=[{0:'',1:'M',2:'MM',3:'MMM'},#千位对应的罗马数字
        {0:'',1:'C',2:'CC',3:'CCC',4:'CD', 5:'D',6:'DC',7:'DCC', 8:'DCCC', 9:'CM'},#百位对应的罗马数字
        {0:'',1:'X',2:'XX',3:'XXX',4:'XL', 5:'L',6:'LX',7:'LXX', 8:'LXXX', 9:'XC'},#十位对应的罗马数字
        {0:'',1:'I',2:'II',3:'III',4:'IV', 5:'V',6:'VI',7:'VII', 8:'VIII', 9:'IX'}]#个位对应的罗马数字
        n,m=divmod(m,1000)#获取千位上的数字
        roman=roman+a[0][n]
        n,m=divmod(m,100)#百位上的数字
        roman=roman+a[1][n]
        n,m=divmod(m,10)#十位上的数字n，和个位上的数字m
        roman=roman+a[2][n]+a[3][m]
        # roman=roman.replace('')
        return roman
        """
        :type num: int
        :rtype: str
        """
        