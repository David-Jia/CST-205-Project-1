#David Jia
#Takes 9 images and then applies a median filter to the image
list = [] # creates an empty list
for i in range(0,9): # allows the user to choose 9 images to fill the list
  file = pickAFile()
  list.append(makePicture(file))

# gets the height and width to make a new image of those dimensions
height = getHeight(list[0])
width = getWidth(list[0])
image = makeEmptyPicture(width, height)

# creates a list to append pixel color values
redValueList = []
greenValueList = []
blueValueList = []

for x in range(0,width):
  for y in range(0,height):
    for ix in range(0,9):
      pixel = getPixel(list[ix], x, y)
      
      # get red, green, blue value of pixel(RGB)
      red = getRed(pixel)
      green = getGreen(pixel)
      blue = getBlue(pixel)
      
      # appends the color value into the color lists
      redValueList.append(red)
      greenValueList.append(green)
      blueValueList.append(blue)
    
    # sorts the color lists by ascending value
    redValueList.sort()
    greenValueList.sort()
    blueValueList.sort()
    
    # gets the median color value
    newRed = redValueList[4]
    newGreen = greenValueList[4]
    newBlue = blueValueList[4]
    
    # places new pixel colors into new image
    newPixel = getPixel(image, x, y)
    setRed(newPixel, newRed)
    setGreen(newPixel, newGreen)
    setBlue(newPixel, newBlue)
    
    # removes colors from color lists to add colors from next pixel in
    for color in range(0,9):
      del redValueList[0]
      del greenValueList[0]
      del blueValueList[0]
      
show(image)