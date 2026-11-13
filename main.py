import sys

def evaluate_board():
    # Hàm đánh giá đơn giản trả về nước đi mặc định
    return "e2e4"

def main():
    # Đọc dữ liệu từ hệ thống make.fun gửi tới qua stdin
    input_data = sys.stdin.read()
    
    # In ra nước đi tốt nhất (định dạng UCI)
    best_move = evaluate_board()
    print(best_move)

if __name__ == "__main__":
    main()