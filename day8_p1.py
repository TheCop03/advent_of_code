
widePixel = 25
tallPixel = 6

with open("day8_data.txt") as file:
    data = file.read()[:-1]

numLayers = int(len(data) / (widePixel * tallPixel))

layers = [[None for _ in range(widePixel * tallPixel)] for _ in range(numLayers)]
layerNum = 0
i = 0

for pixel in data:
    if (i == (widePixel * tallPixel)):
        i = 0
        layerNum += 1

    layers[layerNum][i] = pixel
    i += 1

fewestZero = widePixel * tallPixel
layerWithFewestZero = 0
num1 = widePixel * tallPixel
num2 = widePixel * tallPixel

for layerNum, layer in enumerate(layers):

    numZero = 0
    numOne = 0
    numTwo = 0

    for pixel in layer:
        if (pixel == '0'):
            numZero += 1
        elif (pixel == '1'):
            numOne += 1
        elif (pixel == '2'):
            numTwo += 1

    if numZero <= fewestZero:
        fewestZero = numZero
        layerWithFewestZero = layerNum
        num1 = numOne
        num2 = numTwo

    numZero = 0
    numOne = 0
    numTwo = 0

print(num1 * num2)
