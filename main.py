import subprocess
import os

def run_command(command):
    print(f"Dang chay: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode

def main():
    print("=== Bat dau thuc hien bai tap Git Local Repository ===")
    
    # Khoi tao git
    run_command("git init")
    
    # Cau hinh local
    run_command('git config --local user.name "Hoc Vien Git"')
    run_command('git config --local user.email "hocvien@example.com"')
    
    # Tao file
    with open("sample.txt", "w") as f:
        f.write("Day la file du lieu dau tien cua du an.")
        
    # Add va commit
    run_command("git add sample.txt")
    run_command('git commit -m "Commit dau tien: Them file sample.txt"')
    
    # Kiem tra ket qua
    print("=== Kiem tra cau hinh va lich su commit ===")
    run_command("git config --local user.name")
    run_command("git config --local user.email")
    run_command("git log --oneline")

if __name__ == "__main__":
    main()