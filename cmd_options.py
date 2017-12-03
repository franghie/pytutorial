from optparse import OptionParser

parser = OptionParser()
parser.add_option("-n", "--samuel", dest="xiaobing", default=100000,  help="samuel salary")
parser.add_option("-s", "--sunnie", dest="lingdao",  default=50000, help="sunnie salary")
parser.add_option("-e", "--expense", dest="huafei", default=40000, help="living expense")
(options, args) = parser.parse_args()


total = float(options.xiaobing) + float(options.lingdao) - float(options.huafei)
print("{}".format(total))



