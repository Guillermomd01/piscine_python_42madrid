import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print(
            f"No scores provided. Usage python3 {sys.argv[0]} "
            f"<score1> <score2> ...")
    else:
        numbers_list = []
        error = False
        try:
            for arg in sys.argv[1:]:
                numbers_list.append(int(arg))
        except ValueError:
            print(f"{arg} is not a number")
            error = True
        if not error:
            total = sum(numbers_list)
            average = total / len(numbers_list)
            print(f"Scores processed: {numbers_list}")
            print(f"Total players: {len(numbers_list)}")
            print(f"Total score: {total}")
            print(f"Average score: {average:.1f}")
            print(f"High score: {max(numbers_list)}")
            print(f"Low score: {min(numbers_list)}")
