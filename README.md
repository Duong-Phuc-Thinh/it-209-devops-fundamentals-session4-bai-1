# Bài 1: Khởi tạo Local Repository và Cấu hình danh tính

## Giới thiệu
Bài tập này hướng dẫn cách khởi tạo một Git repository cục bộ, cấu hình danh tính tác giả ở cấp độ local, tạo tệp tin, đưa vào Staging Area và thực hiện commit đầu tiên.

## Các lệnh đã thực hiện
1. Khởi tạo Git repository:
   git init
2. Cấu hình danh tính cục bộ:
   git config --local user.name "Nguyen Van A"
   git config --local user.email "nguyenvana@example.com"
3. Tạo tệp tin và commit:
   echo "Hello Git" > README.md
   git add README.md
   git commit -m "Initial commit"
4. Kiểm tra lịch sử:
   git log --oneline

## Hướng dẫn chạy chương trình Python
Chạy tệp script tự động hóa bằng lệnh:
python main.py