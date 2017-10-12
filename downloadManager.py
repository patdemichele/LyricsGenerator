# Download Manager

# Handles downloading of Lyrics corpus.

def contains(artist):
    try:
        o = open("Data/ContainFile", "r")
    except IOError:
        o = open("Data/ContainFile", "w+")
        o.close()
        return False
    for line in open("Data/ContainFile"):
        if line == artist:
            o.close()
            return True
    o.close()
    return False
