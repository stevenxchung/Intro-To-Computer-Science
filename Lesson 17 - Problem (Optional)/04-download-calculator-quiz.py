# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

# print 2 ** 10      # one kilobit, kb
# print 2 ** 10 * 8  # one kilobyte, kB

# print 2 ** 20      # one megabit, Mb
# print 2 ** 20 * 8  # one megabyte, MB

# print 2 ** 30      # one gigabit, Gb
# print 2 ** 30 * 8  # one gigabyte, GB

# print 2 ** 40      # one terabit, Tb
# print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).


def convert_seconds(seconds):
    # Initialize parameters in the following order
    hours = int(seconds / 3600)
    seconds = seconds % 3600
    minutes = int(seconds / 60)
    seconds = seconds % 60
    string = str(hours)
    # Check hours
    if hours == 1:
        string += " hour, "
    else:
        string += " hours, "
    string += str(minutes)
    # Check minutes
    if minutes == 1:
        string += " minute, "
    else:
        string += " minutes, "
    string += str(seconds)
    # Check seconds
    if seconds == 1:
        string += " second"
    else:
        string += " seconds"

    return string


def download_time(size, up_file, speed, up_speed):
    # Check for Gb/GB
    if up_file[0] == 'G':
        if up_file[1] == 'B':
            time = size * 2 ** 30 * 8
        else:
            time = size * 2 ** 30
    # Check for Tb/TB
    elif up_file[0] == 'T':
        if up_file[1] == 'B':
            time = size * 2 ** 40 * 8
        else:
            time = size * 2 ** 40
    # Check for Mb/MB
    elif up_file[0] == 'M':
        if up_file[1] == 'B':
            time = size * 2 ** 20 * 8
        else:
            time = size * 2 ** 20
    # Check for other cases (kb/kB)
    else:
        if up_file[1] == 'B':
            time = size * 2 ** 10 * 8
        else:
            time = size * 2 ** 10

    # Format to decimal
    time *= 1.0

    # Similar process to above
    if up_speed[0] == 'G':
        if up_speed[1] == 'B':
            time = time / (speed * 2 ** 30 * 8)
        else:
            time = time / (speed * 2 ** 30)
    elif up_speed[0] == 'T':
        if up_speed[1] == 'B':
            time = time / (speed * 2 ** 40 * 8)
        else:
            time = time / (speed * 2 ** 40)
    elif up_speed[0] == 'M':
        if up_speed[1] == 'B':
            time = time / (speed * 2 ** 20 * 8)
        else:
            time = time / (speed * 2 ** 20)
    else:
        if up_speed[1] == 'B':
            time = time / (speed * 2 ** 10 * 8)
        else:
            time = time / (speed * 2 ** 10)

    return convert_seconds(time)


print(download_time(1024, 'kB', 1, 'MB'))
# >>> 0 hours, 0 minutes, 1 second

print(download_time(1024, 'kB', 1, 'Mb'))
# >>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print(download_time(13, 'GB', 5.6, 'MB'))
# >>> 0 hours, 39 minutes, 37.1428571429 seconds

print(download_time(13, 'GB', 5.6, 'Mb'))
# >>> 5 hours, 16 minutes, 57.1428571429 seconds

print(download_time(10, 'MB', 2, 'kB'))
# >>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print(download_time(10, 'MB', 2, 'kb'))
# >>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable
