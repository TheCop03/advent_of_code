
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

print(layers)
layerNum = 0
decodedImage = [None for _ in range(widePixel * tallPixel)]

for layer in layers:
    for pixelIndex, pixel in enumerate(layer):
        if decodedImage[pixelIndex] == None or decodedImage[pixelIndex] == '2':
            decodedImage[pixelIndex] = pixel

print(decodedImage)
for index, i in enumerate(decodedImage):
    if (i == '1'):
        print(i, end=' '),
    else:
        print(' ', end=' ')

    if index != 0 and (index % widePixel) == widePixel - 1:
        print('\n')

print('\n')
print(''.join(decodedImage))
