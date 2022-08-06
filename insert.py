import sys
from svgpathtools import svg2paths2, wsvg, disvg, Path, CubicBezier, Line, parse_path
paths, attributes, svg_attributes = svg2paths2(sys.argv[1])


refill = parse_path("M 868.94783,-82.376923 C 854.56897,-87.328441 842.69587,-87.915164 827.41103,-87.915164 820.4931,-87.915164 804.1214,-89.547618 799.71983,-85.146044 799.06713,-84.493356 800.13263,-83.202514 799.71983,-82.376923 793.95761,-70.852506 799.911,-85.337211 794.18158,-79.607803 794.00807,-79.434288 786.53141,-67.076567 785.87421,-65.762197 784.40377,-62.821322 785.57355,-57.154164 783.1051,-54.685715 782.4524,-54.033027 780.98866,-55.338403 780.33599,-54.685715 777.96936,-52.319092 780.33599,-33.244071 780.33599,-29.76363 780.33599,-28.623403 779.60297,-22.189271 780.33599,-21.456268 780.98866,-20.80358 782.4524,-22.108956 783.1051,-21.456268 784.41047,-20.150893 781.79973,-17.223403 783.1051,-15.918027 784.21351,-14.809624 786.62407,-14.418331 788.64335,-10.379786 789.48248,-8.7015296 790.25207,-3.2328038 791.41246,-2.0724242 792.06516,-1.4197364 793.52891,-2.725112 794.18158,-2.0724242 794.83427,-1.4197364 793.52891,0.04400857 794.18158,0.69669636 794.83427,1.3493841 796.29802,0.04400857 796.95071,0.69669636 797.60339,1.3493841 796.53791,2.6402265 796.95071,3.4658169 798.59616,6.7567124 806.94267,9.8463605 810.79631,11.773179 813.75004,13.250045 818.91907,10.296315 821.87278,11.773179 823.04037,12.356961 823.47434,13.958517 824.64192,14.542299 826.96113,15.701914 850.74622,16.129208 852.33313,14.542299 852.9858,13.889611 851.68043,12.425866 852.33313,11.773179 853.71767,10.38862 856.48681,10.38862 857.87135,9.0040581 860.60489,6.2705334 865.61458,-12.584768 868.94783,-15.918027 869.60052,-16.570715 871.06427,-15.265339 871.71697,-15.918027 872.77634,-16.977415 871.71697,-28.792403 871.71697,-29.76363 871.71697,-37.620961 871.54106,-47.850866 863.4096,-51.916594 861.75842,-52.742187 859.17674,-50.611219 857.87135,-51.916594 857.21868,-52.569282 858.52405,-54.033027 857.87135,-54.685715 856.18669,-56.37038 832.24975,-57.454836 827.41103,-57.454836 825.24277,-57.454836 814.94715,-58.836563 813.56542,-57.454836 811.42559,-55.315006 812.47899,-46.974616 810.79631,-43.609233 807.1839,-36.384415 807.1839,-31.450207 810.79631,-24.225389 811.20911,-23.399796 810.14361,-22.108956 810.79631,-21.456268 812.10169,-20.150893 815.02917,-22.761644 816.33456,-21.456268 816.98723,-20.80358 815.68186,-19.339835 816.33456,-18.687148 817.01771,-18.003979 832.26611,-18.003979 832.94928,-18.687148 833.60196,-19.339835 832.29659,-20.80358 832.94928,-21.456268 833.60196,-22.108956 835.0657,-20.80358 835.7184,-21.456268 838.41424,-24.152104 834.72029,-33.530846 832.94928,-35.301871")


def insert(listy, ele, n):
    result = []
    for st_idx in range(0, len(listy), n):
        result.extend(listy[st_idx:st_idx+n])
        result.append(ele)
    result.pop()
    return result


paths = insert(paths, refill, 1)


disvg(paths)