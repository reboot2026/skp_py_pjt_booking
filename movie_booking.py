import json
from movie import Movie, load_movies
from input_utils import get_int, get_int_range, get_int_range_with_condition
from datetime import date 


class BookingManager:
    def __init__(self, name: str, movies:list[Movie]) -> None:
        self.name = name        # 로그인 사용자명 
        self.bookings = []      # 전체 예매 정보
        self.movies = movies    # 예매 가능한 영화 목록
        self.FILESNAME = "bookings.json"
        try:
            with open(self.FILESNAME, encoding="utf-8") as f:
                self.bookings = json.load(f)
        except json.decoder.JSONDecodeError:
            self.bookings = []
        
       
    def display_movies(self)-> None:
        """ 상영중인 영화 목록을 화면에 display """
        print("============= SKP영화관 상영 영화 ===============")
        for m in self.movies:
            print(m)
        print("===============================================")
        
    def booked_seats(self, movie:Movie) -> list[int] : 
        """ 전체 예매 정보에서 해당 영화의 예매된 좌석 번호만 list에 담아 반환한다. """
        if len(self.bookings) == 0 :
            return []
        return [booking["좌석번호"] for booking in self.bookings if booking["영화ID"] == movie.id]
       
    def book(self) -> None:
        """ 영화 및 좌석 예매 처리한다. """
        self.display_movies()

        # 예매할 영화 선택
        movie_id = get_int_range("예매할 영화 번호를 입력하세요 : ", 1, len(self.movies))
        movie = self.movies[movie_id -1]

        # 선택한 영화의 상영관 좌석 display
        booked = self.booked_seats(movie)
        movie.show_screen(booked) 

        # 좌석 선택 / 예매 처리
        seat_no = get_int_range("예매할 좌석 번호를 입력하세요 : ", 1, movie.rows * movie.cols)
        if seat_no in booked:
            print("이미 예매된 좌석입니다.")
        else:
            self.bookings.append({"이름":self.name, "영화ID":movie.id, "제목":movie.title, "상영관":movie.screen, "좌석번호":seat_no, "예매일자":str(date.today())})
            print("예매 완료되었습니다.")
            
    def get_user_bookings(self) -> list[dict] :
        """ 로그인 사용자의 예매 정보만 필터링하여 반환한다. """
        return [booking for booking in self.bookings if booking["이름"] == self.name]
        
    def show_bookings(self, user_bookings:list[dict]) -> None:
        """ 로그인 사용자의 예매 현황을 화면에 보여준다. """
        if len(user_bookings) == 0 :
            print("예매 내역이 없습니다.")
        else:
            print(f"======== {self.name} 님의 예매 현황 =========")
            for i, booking in enumerate(user_bookings, 1):
                print(f"{i} {booking['제목']} {booking['상영관']}({booking['좌석번호']}번)")
    
    def cancel(self, user_bookings:list[dict]) -> None:
        """ 로그인 사용자의 예매 내역을 보여주고 선택한 예매 건에 대해 취소처리한다."""
        if len(user_bookings) == 0 :
            print("예매 내역이 없습니다.")
            return 
        self.show_bookings(user_bookings)
        loop_quit_condition = 0 
        no = get_int_range_with_condition("취소할 예매 건 번호를 입력하세요 (0:취소):", 1, len(user_bookings), condition=loop_quit_condition)
        if no != loop_quit_condition:
            booking = user_bookings[no-1]
            self.bookings.remove(booking)
            print(f"취소처리 되었습니다.{booking}")
            self.show_bookings(self.get_user_bookings())
    
    def save(self) -> None:
        with open(self.FILESNAME, "w", encoding="utf-8") as f:
            json.dump(self.bookings, f, ensure_ascii=False, indent=2)
                
def show_menu() -> None:
    print("\n========= 영화 예매 ===========")
    print("1. 영화 예매  2. 예매 현황  3. 예매 취소  q. 종료")
                    
def main() -> None:
    movies = load_movies()
    name = input("로그인 사용자 이름을 입력하세요 : ").strip()
    
    manager = BookingManager(name, movies)
    while True:
        show_menu()
        choice = input("선택: ").strip()
        user_bookings = manager.get_user_bookings()
        if choice == 'q':
            manager.save()
            print("프로그램을 종료합니다.")
            break
        elif choice == '1':
            manager.book()
        elif choice == '2':
            manager.show_bookings(user_bookings)
        elif choice == '3':
            manager.cancel(user_bookings)
        else:
            print("잘못된 선택입니다.") 


if __name__ == "__main__":  
    main()
         
