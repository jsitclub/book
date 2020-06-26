class clsISBN():
    def __init__(self,isbnNo):
        self.isbnNo = isbnNo
        #if isbnNo.isnumeric

    def checkISBN(self):
        if len(self.isbnNo)!=13:
            return False
        code=self.__getCheckCode(self.isbnNo)
        if code==self.isbnNo[12]:
            return True
        else:
            return False
    
    def convertToISBN13(self):
        if len(self.isbnNo)!=10:
            return False
        code=self.__getCheckCode(self.isbnNo)
        if code==self.isbnNo[12]:
            return True
        else:
            return False

    def __getCheckCode(self,isbnNo):
        sum=0
        #12자리계산후 13번째와 확인
        for i in range(12):         
            if i%2==0:
                sum+=int(isbnNo[i])
            else:
                sum+=int(isbnNo[i])*3
        
        if sum%10==0:
            return '0'
        else:
            return str(10-sum%10)

    def __convertToISBN13(self):
        if len(self.isbnNo)!=10:
            return ""

        temp='978'+self.isbnNo
        return temp[:12]+self.__getCheckCode(temp)
        


# x13=clsISBN("9788908070127")
# print(x13.checkISBN())

# x10=clsISBN("8946410450")
