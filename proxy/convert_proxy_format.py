# Đọc file proxies.txt và chuyển đổi định dạng proxy

input_file = 'proxies.txt'           # File đầu vào dạng ip:port:user:pass
output_file = 'converted_proxies.txt'  # File đầu ra dạng http://user:pass@ip:port

with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', encoding='utf-8') as outfile:

    for line in infile:
        line = line.strip()
        if not line or line.startswith('#'):
            continue  # Bỏ qua dòng rỗng hoặc comment

        try:
            ip, port, user, password = line.split(':')
            proxy = f"http://{user}:{password}@{ip}:{port}"
            outfile.write(proxy + '\n')
        except ValueError:
            print(f"Lỗi định dạng ở dòng: {line}")
