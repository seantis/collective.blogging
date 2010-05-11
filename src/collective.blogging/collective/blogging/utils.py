import os

def scaleImage(data, w, h):
    import pdb; pdb.set_trace( )
    stdin, stdout = os.popen2("convert - -resize %sx%s - " % (int(w),int(h)),"b")
    stdin.write(data)
    stdin.close()

    scaled = stdout.read()
    stdout.close()
    
    return scaled