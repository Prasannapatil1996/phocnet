import os
from PIL import Image

yourpath = os.getcwd()
for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        print(os.path.join(root, name))
        if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
            if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".png"):
                print "A png file already exists for %s" % name
            # If a png is *NOT* present, create one from the tiff.
            else:
                outfile = os.path.splitext(os.path.join(root, name))[0] + ".png"
                try:
                    im = Image.open(os.path.join(root, name))
                    print "Generating png for %s" % name
                    im.thumbnail(im.size)
                    im.save(outfile, "png", quality=100)
                except Exception, e:
                    print e