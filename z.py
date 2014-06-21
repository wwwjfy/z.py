import os
import random
import re
import sys
import time


def z():
    if len(sys.argv) < 2:
        sys.exit(0)
    datafile = os.getenv('_Z_DATA', os.getenv('HOME')) + '/.z'

    if os.path.isfile(datafile) and os.stat(datafile).st_uid != os.getuid():
        return

    if sys.argv[1] == '--add':
        path = os.path.expandvars(os.path.expanduser(sys.argv[2]))
        if path == os.getenv('HOME'):
            return

    lines = filter(lambda l:os.path.isdir(l.split('|', 1)[0]),
                   open(datafile).readlines())

    if sys.argv[1] == '--add':
        now = int(time.time())
        rank = {path: 1}
        ptime = {path: now}
        count = .0
        for l in lines:
            l = l.strip().split('|')
            if l[0] == path:
                rank[l[0]] = float(l[1]) + 1
                ptime[l[0]] = str(now)
            else:
                rank[l[0]] = float(l[1])
                ptime[l[0]] = l[2]
            count += float(l[1])
        if count > 6000:
            factor = 0.99
        else:
            factor = 1.0
        tempfile = datafile + '.' + str(random.randint(10000, 99999))
        with open(tempfile, 'w') as f:
            for x in rank.keys():
                f.write('%s|%s|%s\n' % (x, round(factor * rank[x], 5), ptime[x]))

        try:
            os.rename(tempfile, datafile)
        except:
            os.remove(tempfile)
            raise
    else:
        cd = None
        now = int(time.time())
        matches = {}
        imatches = {}
        hi_rank = -1
        ihi_rank = -1
        best_match = None
        ibest_match = None
        for l in lines:
            l = l.split('|')
            dx = now - int(l[2])
            if dx < 3600:
                rank = float(l[1]) * 4
            elif dx < 86400:
                rank = float(l[1]) * 2
            elif dx < 604800:
                rank = float(l[1]) / 2
            else:
                rank = float(l[1]) / 4
            matches[l[0]] = rank
            imatches[l[0]] = rank
            for x in sys.argv[1:]:
                if not re.search(x, l[0]):
                    matches.pop(l[0], None)
                if not re.search(x, l[0], re.I):
                    imatches.pop(l[0], None)
            if matches.get(l[0], None) and matches[l[0]] > hi_rank:
                best_match = l[0]
                hi_rank = matches[l[0]]
            elif imatches.get(l[0], None) and imatches[l[0]] > ihi_rank:
                ibest_match = l[0]
                ihi_rank = imatches[l[0]]
        if best_match:
            cd = best_match
        elif ibest_match:
            cd = ibest_match
        if cd:
            print(cd)

z()
