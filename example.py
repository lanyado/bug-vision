from main import BugVision

def main(num1: int, num2: int) -> int:
    with BugVision():
        return num1 / num2
    
def run_main():
    main(1, 0)

if __name__ == '__main__':
    run_main()