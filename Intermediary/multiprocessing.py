import multiprocessing
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    # print(cpu_count())

    # a = Process(target=counter, args=(10000000000,))
    # a.start()
    # a.join()
    print("Finised in: ", time.perf_counter(), " seconds")

if __name__ == "__main__":
    main()