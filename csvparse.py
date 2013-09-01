import csv

class Webpage:
    def __init__(self, index, name, isjunction, pagetype, image):
        self.index = index
        self.name = name
        self.links = None
        self.isjunction = isjunction
        self.pagetype = pagetype
        self.image = image
        self.buttonclass = None
        self.description = None
        
    def addlink(self):
        #TODO
        pass

    def __str__(self):
        return self.index + " " + self.name + " " + self.isjunction + " " + self.pagetype + " " + self.image

def LoadCSV():
    pages = {}
    count = 0
    with open('/home/jam/richardtest.csv', 'rU') as csvfile:
        csvreader = csv.reader(csvfile, dialect='excel')
        for row in csvreader:
            index, name, isjunction, pagetype, image, links = row
            pages[count]=Webpage(index,name,isjunction,pagetype,image)
            count += 1
    return pages
