#0. isbn 검증(10자리용 13자리용)
    #   1) 10자리면 13자리로 변환후 검증
    #  
    #0. 책의 isbn으로 book table 에서 검색
    #
    #0. DB결과가 없다면 nvr에서 끌어오기
    #   1) isbn 으로 https://book.naver.com/search/search.nhn?sm=sta_hty.book&sug=&where=nexearch&query=9788954650700 으로 검색
    #   2) 결과가 없다면 
    #           정보가 없음 ( 테이블에도, yes에도 없음  그러면 중립 중앙도서관에서 검색(?)해봐야 하나?)
    #   3) 결과가 있다면 
    #           리스트의 첫번째 책 상세정보로 들어감(isbn 코드는 유일하므로 리스트에1개만 날올것으로 예상) 
    #       - 책 제목에서 링크를 끌어온다.(https://book.naver.com/bookdb/book_detail.nhn?bid=13561694)
    #       - 13561694 코드가 nvr의 코드
    #   4) 

from isbn import clsISBN

def CreateBookData(isbnNo):
    
    a=clsISBN("9788954650700")
    print(a.checkISBN("9788954650700"))

    return True
        

print(CreateBookData(""))
    
