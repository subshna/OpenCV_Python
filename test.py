# def make_file(csvfile):
#     with open(csvfile) as f:
#         content = f.readlines()
#
#     content = [x.strip() for x in content]
#
#     sum = 0
#     for employee in content:
#         sum += len(employee.split(','))
#         #print (sum)
#
#     return sum
#
# print (make_file('E:\\Subash\\Python\\AI\\testfile.csv'))
import string, random

def random_string(size=5):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(size))

print (random_string(10))