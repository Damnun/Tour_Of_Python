"""이제 파이썬 프로그래밍 능력을 높여 줄 더 큰 날개를 달아 보자.
전 세계의 파이썬 사용자들이 만든 유용한 프로그램을 모아 놓은 것이 바로 파이썬 라이브러리이다. 
"라이브러리"는 "도서관"이라는 뜻 그대로 원하는 정보를 찾아보는 곳이다.
모든 라이브러리를 다 알 필요는 없고 어떤 일을 할 때 어떤 라이브러리를 사용해야 한다는 정도만 알면 된다. 
그러기 위해 어떤 라이브러리가 존재하고 어떻게 사용하는지 알아야 한다. 
자주 사용되고 꼭 알아 두면 좋은 라이브러리를 중심으로 하나씩 살펴보자.
"""


import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()  # join으로 스레드가 종료될때까지 기다린다.

print("End")