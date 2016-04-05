import json
import math

def init_empty(canvas):
    for j in range(784):
        canvas['pixel' + str(j)] = '0'

def avg_set(number_set):
    avg_canvas = {}
    init_empty(avg_canvas)

    def sum_canvas(canvasA,canvasB):
        sumed_canvas = {}
        for i in range(784) :
            key = 'pixel' + str(i)
            sumed_canvas[key] = int(canvasA[key]) + int(canvasB[key])
        return sumed_canvas

    avg_canvas = reduce(lambda c1,c2 : sum_canvas(c1,c2), number_set)
    avg_canvas = dict(map(lambda (k,v): (k, v / len(number_set)), avg_canvas.iteritems()))
    return avg_canvas

def eucledian_distance(numberA,numberB):
    distance = 0

    for i in range(len(numberB)):
        distance += (int(numberB['pixel' + str(i)]) - int(numberA['pixel' + str(i)])) ** 2
    distance = math.sqrt(distance)
    return distance

def print_set(number):
    start = 0
    end = 28
    for i in range(28):
        row = ""
        for j in range(start,end):
            pixel = number['pixel' + str(j)]
            if pixel != 0:
                if int(math.log10(pixel))+1 > 1 :
                    row += "|" + str(pixel) + "|"
                else:
                    row += "| " + str(pixel) + " | "
            else:
                row += "|" + str(pixel) + "| "
        row += "\n"
        print row,
        start = start + 28
        end = end + 28

#-------------- Code ---------------

numbers_train = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}

print 'Loading train file in memory...'
with open('train.json','r') as f:
        data = json.loads(f.read())
        f.closed
        for i in range(len(data)):
            numbers_train[int(data[i]["label"])].append(data[i])
            print "\r data train -> " + str(i + 1),

# print ''
# print "# of zeros  -> " + str(len(number[0]))
# print "# of ones   -> " + str(len(number[1]))
# print "# of twos   -> " + str(len(number[2]))
# print "# of threes -> " + str(len(number[3]))
# print "# of fours  -> " + str(len(number[4]))
# print "# of fives  -> " + str(len(number[5]))
# print "# of sixs   -> " + str(len(number[6]))
# print "# of sevens -> " + str(len(number[7]))
# print "# of eights -> " + str(len(number[8]))
# print "# of nines  -> " + str(len(number[9]))
# print ''
print ''

print 'Calculating train average...'
avg_train = []
for i in range(10):
    #print_set(avg_set(numbers_train[i]))
    avg_train.append(avg_set(numbers_train[i]))

print 'Loading test file in memory...'
numbers_test = []
with open('test.json','r') as f:
        data = json.loads(f.read())
        for i in range(len(data)):
            numbers_test.append(data[i])
            print "\r data test -> " + str(i + 1),
print ''

print 'Predicting numbers...'
prediction = []
for test in numbers_test:
    distances = []
    distance = 0

    for i in range(len(avg_train)):
        distance = eucledian_distance(avg_train[i],test)
        distances.append((i,distance))

    #print(type(distances))
    minimum = reduce(lambda t1,t2: t1 if t1[1] < t2[1] else t2 , distances)
    prediction.append(minimum[0])

print 'Writing prediction file in memory...'
with open('prediction2.csv','w') as f:
    f.write("imageId,Label\n")
    for i in range(len(prediction)):
        f.write(str(i+1) + "," + str(prediction[i]) + "\n")
        print "\r predictions writen -> " + str(i + 1),
