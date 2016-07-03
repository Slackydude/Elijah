import urllib2, sys, getopt

class BoletinGrabber:
    def __init__(self, start, end, debug):
        self.start = start
        self.end = end
        self.debug = debug
        self.url = "http://www.senado.cl/wspublico/tramitacion.php?boletin="
        
    def ObtieneBoletin(self):
        if self.debug == 1:
            for i in range(self.end+1):
                NumeroBoletin = self.start + i
                self.url = self.url + str(NumeroBoletin)
                print self.url
                try:
                    response = urllib2.urlopen(self.url)
                    XMLcontent = response.read()
                    Nombre="Boletin-"+str(NumeroBoletin)+".xml"
                    f = open(Nombre,'w')
                    f.write(XMLcontent)
                    f.close
                    print 'ok'
                    self.url = "http://www.senado.cl/wspublico/tramitacion.php?boletin="
                except:
                    print "Unexpected error1:", sys.exc_info()[0]
        else:
            for i in range(self.end):
                NumeroBoletin = self.start + i
                self.url = self.url + str(NumeroBoletin)
                try:
                    response = urllib2.urlopen(self.url)
                    XMLcontent = response.read()
                    Nombre="Boletin-"+str(NumeroBoletin)+".xml"
                    f = open(Nombre,'w')
                    f.write(XMLcontent)
                    f.close
                    self.url = "http://www.senado.cl/wspublico/tramitacion.php?boletin="
                except:
                    print "Unexpected error:2", sys.exc_info()[0]
            
        
                
def usage():
    print "Boletin Grabber v1.0"
    print "-s [first document to fetch]"
    print "-f [final document to fetch]"
    print "-d {debug flag}"
    print "-h {help}"
    print "-i {interactive flag}"
    print "example: BoletinGrabber.py -s 1 -f 500 -d"

def main(argv):
    start = 0
    end = 0
    debug = 0
    
    try:
        opts, args = getopt.getopt(argv,"ihs:e:d", ["help", "start=", "end="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-s", "--start"):
            try:
                start = int(arg)
            except:
                print "Unexpected error:3", sys.exc_info()[0]
        elif opt in ("-e","--end"):
            try:
                end = int(arg)
            except:
                print "Unexpected error:4", sys.exc_info()[0]
        elif opt in ("-d"):
                debug = 1
        elif opt in("-i"):
            try:
                start = int(raw_input("Please enter the start number (aka Boletin number): "))
                end = int(raw_input("Please enter the final number: "))
            except ValueError:
                print ("Ooops, not a valid number")
    if end == 0 or end < start:
        usage()
        sys.exit()
    else:
        BoletinGrabber(start, end, debug).ObtieneBoletin()
      
if __name__ == '__main__':
    main(sys.argv[1:])
