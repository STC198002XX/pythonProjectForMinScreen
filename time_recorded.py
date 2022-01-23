import time


def time_message():
    localtime = time.localtime()
    result = time.strftime("%Y-%m-%d %H:%M:%S ", localtime)
    return result


if __name__ == '__main__':
    print(time_message())