import re
import datetime
import os


def Convert(string):
    li = list(string.split(" "))
    return li

def Wooble(time, fileName):

    old_file_name = fileName

    file = open(old_file_name , "r", encoding='iso-8859-1')
    lines = file.readlines()
    file.close()

    text = ''
    regex = '^[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}'
    toAdd = ".000000"
    oldTime = []
    newTime = []
    newFirst = []

    timeWooble = time

    for line in lines:

        if re.search(regex, line, re.DOTALL) is not None:
            text += line.rstrip('\n')
            text += '\n'

            both = re.findall('^[0-9]{2}:[0-9]{2}:[0-9]{2}.*', line)

            first = re.search('[0-9]{2}:[0-9]{2}:[0-9]{2}(\,)[0-9]{3}', line)
            second = re.search('[0-9]{2}:[0-9]{2}:[0-9]{2}(\,)[0-9]{3}$', line)

            first = first.group()
            first = str(first)

            second = second.group()
            second = str(second)

            date_time_first = datetime.datetime.strptime(first, '%H:%M:%S,%f')
            date_time_secnd = datetime.datetime.strptime(second, '%H:%M:%S,%f')

            finalFirstTime = date_time_first + datetime.timedelta(0, timeWooble)
            finalFirstTime = str(finalFirstTime)

            if len(finalFirstTime) != 26:
                finalFirstTime = finalFirstTime + toAdd

            finalFirstTime = finalFirstTime[12:-3]
            finalFirstTime = f"{'0'}{finalFirstTime}"


            finalSecndTime = date_time_secnd + datetime.timedelta(0, timeWooble)

            finalSecndTime = str(finalSecndTime)

            if len(finalSecndTime) != 26:
                finalSecndTime = finalSecndTime + toAdd

            finalSecndTime = finalSecndTime[12:-3]
            finalSecndTime = f"{'0'}{finalSecndTime}"

            newFirst.append(first)

            both = str(both)

            oldTime.append(both)

            both = both.replace(first, finalFirstTime)
            both = both.replace(second, finalSecndTime)

            # print(both)
            newTime.append(both)

            #print(both)


    i = -1
    final_file = ''

    for line in lines:
        if re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}', line) is not None:
            i += 1

        oldRep = str(oldTime[i])[2:-2]
        newRep = str(newTime[i])[2:-2]

        final_file += line.replace(oldRep, newRep)

    username = os.getlogin()  # Fetch username
    new_file_name = old_file_name + "_timed" + '.srt'

    with open(f'C:\\Users\\{username}\\Desktop\\' + new_file_name, 'w', encoding='iso-8859-1') as f:
        f.write(final_file)
        print("DONE!")


if __name__ == '__main__':
    Wooble(4, "sub")
