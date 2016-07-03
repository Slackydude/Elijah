import urllib2, sys, getopt



def main(argv):
    start = '0'
    final = '0'
    url = "http://www.senado.cl/wspublico/tramitacion.php?boletin="
    try:
        opts, args = getopt.getopt(argv,"hs:f")
    except getopt.GetoptError:
        print 'BoletinGrabber.py -s [start] -f [final]'
        sys.exit(2)
    for opt, arg in opts:
        if opt == 'h':
            print 'BoletinGrabber.py -s [start] -f [final]'
            sys.exit()
        elif opt in ("-s"):
            for i in range(900):
                NumeroBoletin = int(arg) + i
                url = url + str(NumeroBoletin)
                print url
                response = urllib2.urlopen(url)
                XMLcontent = response.read()
                Nombre="Boletin-"+str(NumeroBoletin)+".xml"
                f = open(Nombre,'w')
                f.write(XMLcontent)
                f.close
                print 'ok'
                url = "http://www.senado.cl/wspublico/tramitacion.php?boletin="

        
if __name__ == '__main__':
    main(sys.argv[1:])