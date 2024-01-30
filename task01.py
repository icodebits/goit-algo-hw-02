import queue
import threading
import time

# Черга заявок
request_queue = queue.Queue()

# Генерація нових заявок
def generate_request():
    while True:
        # Створимо нову заявку
        request = f"Request-{time.time()}"
        
        # Додамо заявку до черги
        request_queue.put(request)
        
        # Зачекаємо перед генерацією наступної заявки
        time.sleep(2)

# Обробка заявок
def process_request():
    while True:
        # Якщо черга не пуста
        if not request_queue.empty():
            # Видалимо заявку з черги
            request = request_queue.get()
            
            # Обробка заявки
            print(f"Processing request: {request}")
        else:
            # Виводимо повідомлення, що черга пуста
            print("Queue is empty. Waiting for requests.")
        
        # Зачекати перед обробкою наступної заявки
        time.sleep(1)

try:
    # Створити та запустити два окремі потоки для генерації та обробки заявок
    generate_thread = threading.Thread(target=generate_request)
    process_thread = threading.Thread(target=process_request)
    generate_thread.daemon = True
    process_thread.daemon  = True

    generate_thread.start()
    process_thread.start()

    while True:
        time.sleep(100)

    # Чекаемо, поки користувач не зупинить програму за допомогою Ctrl+C
except (KeyboardInterrupt, SystemExit):
    print("Main thread interrupted. Exiting.")
