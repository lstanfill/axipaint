# this is almost finished - just need a way to break up paths that are only slightly over 20 in a more manageable way
# ie. if the length is less than 30 just divide the path in two
# so if we started at 22, instead of chopping at 20 and having 2 left over we have two groups of 11

import sys
from svgpathtools import svg2paths2, wsvg, disvg, Path, CubicBezier, Line, parse_path
paths, attributes, svg_attributes = svg2paths2(sys.argv[1])

# show us what length we're starting with
print("PATHS", len(paths))

for i in paths:
    n = 0
    # lets break the longer paths into chunks of 20 or less
    if len(i) > 30:

        # take the index of our offending paths and tell us how long the paths are
        indy = paths.index(i)
        print("orig", "index=", indy, "length=", len(i))

        # do the actual breaking into chunks of 20 -- this part is a little cloudy to me
        newpaths = [i[x:x + 30] for x in range(0, len(i), 30)]
        print("NEWPATHS", len(newpaths))

        # use the index of our too-long path and replace that path with our first shorter chunk
        paths[indy] = newpaths[0]
        print("indy1:", indy)

        # for the rest of the chunked up paths, insert sequentially behind the first chunk
        for x in range(len(newpaths)-1):
            indy += 1
            n += 1
            paths.insert(indy, newpaths[n])

            # if we want to check how long each new path is
            # print("indy:", indy)

# for n in paths:
#     print("new", len(n))

# print the length of our new svg compared to the old length
print("PATHS", len(paths))
print("ORIGINALLY", len(attributes))
print("Okay! Ready to paint!")


# format properly
paths = [Path(*x) for x in paths]

# open in inkscape
disvg(paths)

# optional save if we don't want to save from inkscape, this will have no attributes.
#wsvg(paths, filename='output1.svg')





