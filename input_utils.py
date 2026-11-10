
def get_int(prompt: str) -> int:
    """정수를 입력할 때까지 다시 묻는다."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("정수로 입력해주세요.")

def get_int_range(prompt: str, low: int, high: int) -> int:
    """low 이상 high 이하의 정수를 입력받는다."""
    while True :
        n = get_int(prompt)
        if low <= n <= high:
            return n
        print(f"{low} ~ {high} 사이로 입력해 주세요")

def get_int_range_with_condition(prompt: str, low: int, high: int, condition: int) -> int:
    """low 이상 high 이하의 정수를 입력받는다."""
    while True :
        n = get_int(prompt)
        if n == condition:
            return condition
        if low <= n <= high:
            return n
        print(f"{low} ~ {high} 사이로 입력해 주세요")

if __name__ == "__main__":
    age = get_int("나이: ")
    score = get_int_range("점수(0~100): ", 0, 100)
    print(f"나이 {age}, 점수 {score}")


if __name__ == "__main__":
    age = get_int("나이: ")
    score = get_int_range("점수(0~100): ", 0, 100)
    print(f"나이 {age}, 점수 {score}")

