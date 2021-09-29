import time

time_object = time.localtime()
time_object_formatted = time.strftime("%B %d %Y %H:%M:%S", time_object)

print(time_object_formatted)

time_string = "20 April, 2020"

time_object = time.strptime(time_string, "%d %B, %Y")

print(time_object)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)