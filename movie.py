import json 

class Movie:
    def __init__(self, id:int, title:str, show_date:str, screen:str, rows:int, cols:int) -> None:
        self.id = id
        self.title = title
        self.show_date = show_date
        self.screen = screen
        self.rows = rows
        self.cols = cols
       
    def show_screen(self, booked:int) -> None:
        """ 영화 상영관의 좌석번호 목록을 출력한다. (이미 예약된 좌석은 'X'로 출력) """
        print(f"=============== {self.screen} ===============")
        seat_count = self.cols * self.rows
        for i in range(seat_count) :
            seat_no = str(i + 1)
            if (i+1) in booked :
                seat_no = "X"
            if (i + 1) % self.cols == 0:
                print(f"{seat_no}\t")
            else :
                print(f"{seat_no}\t", end = " ")        
    
    def __str__(self) -> str:
        return f"{self.id}. {self.show_date} {self.title} ({self.screen})"
    

def load_movies() -> list[Movie]:
    """ 파일에 저장된 영화 목록을 불러와 list[Movie]로 반환한다. """
    movies = []
    with open("movies.json", encoding="utf-8") as f:
        for i, m in enumerate(json.load(f), 1):
            movies.append(Movie(i, m["제목"], m["상영일자"], m["상영관"], m["행수"], m["열수"]))
        #for m in json.load(f):
        #    movies.append(Movie(m["영화ID"], m["제목"], m["상영일자"], m["상영관"], m["행수"], m["열수"]))
    return movies
                    