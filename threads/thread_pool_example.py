from concurrent import futures

def workers():
    print("Worker thread is running")

pool=futures.ThreadPoolExecutor(max_workers=2)

for i in range(5):
    pool.submit(workers)
    print(f"Task {i} submitted")

pool.shutdown(wait=True)

print("Main thread continuing to run")