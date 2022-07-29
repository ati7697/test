from wordfreq import *
listOfN = []
for v, k in l:
    result = (v * 100) // 11
    output = ''
    times = 2 * v
    while (times > 0):
        output += "*"
        times = times - 1

    print(k, [output], result,"%")


# def histogram(items):
#     for n in items:
#         output = ''
#         times = n
#         while (times > 0):
#             output += '*'
#             times = times - 1
#         print(output)
# histogram([2, 3, 6, 5])