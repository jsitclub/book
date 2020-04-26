class isbn():
    def getCheckCode(self,isbn):
        sum=0
        #12자리계산후 13번째와 확인
        for i in range(12):         
            if i%2==0:
                sum+=int(isbn[i])
            else:
                sum+=int(isbn[i])*3
        
        if sum%10==0:
            return '0'
        else:
            return str(10-sum%10)
        

    def checkISBN13(self,isbn):
        if len(isbn)!=13:
            return False
        code=self.getCheckCode(isbn)
        if code==isbn[12]:
            return True
        else:
            return False

    def convertToISBN13(self,isbn):
        if len(isbn)!=10:
            return ""

        temp='978'+isbn
        return temp[:12]+self.getCheckCode(temp)
        


x=isbn()

num="8908070125"


num=x.convertToISBN13(num)
print(num)
print(x.checkISBN13(num))
