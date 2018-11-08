import copy
import random
import itertools

guess = []
shudu1 = [[''] * 9] * 9
shudu2 = [['' for i in range(9)] for i in range(9)]
shudu3 = [
        ['8',  '', '5',  '', '4',  '',  '',  '', '3'],
        [ '', '4',  '',  '',  '',  '',  '',  '', '5'],
        [ '',  '', '2',  '',  '',  '', '9', '4',  ''],
        ['1', '5', '8', '6',  '', '3',  '', '2', '7'],
        [ '', '9', '6',  '', '7', '8',  '',  '', '1'],
        ['7', '3', '4', '5', '2',  '', '8',  '', '9'],
        [ '',  '', '9',  '', '6', '7',  '', '3', '2'],
        [ '', '2', '1', '8', '3',  '', '6',  '', '4'],
        ['6', '7',  '',  '', '5', '4', '1', '9',  '']
        ]
shudu4 = [
        ['6',  '',  '', '4',  '',  '', '5',  '',  ''],
        [ '',  '', '1',  '', '8', '5', '6',  '',  ''],
        ['8',  '',  '',  '', '3',  '',  '',  '',  ''],
        [ '',  '',  '',  '', '9',  '', '4', '5', '2'],
        ['3',  '',  '', '2',  '', '8',  '',  '', '7'],
        [ '',  '',  '',  '',  '',  '',  '',  '',  ''],
        [ '',  '', '9', '8', '6', '4',  '',  '',  ''],
        [ '',  '',  '',  '',  '',  '',  '',  '', '9'],
        [ '', '7', '5',  '',  '',  '',  '',  '',  '']
        ]
shudu5 = [
        ['8',  '', '5',  '', '4',  '',  '',  '', '3'],
        [ '', '4',  '',  '',  '',  '',  '',  '', '5'],
        [ '',  '', '2',  '',  '',  '', '9', '4',  ''],
        ['1', '5',  '', '6',  '', '3',  '', '2', '7'],
        [ '',  '', '6',  '', '7', '8',  '',  '', '1'],
        ['7', '3', '4',  '', '2',  '', '8',  '', '9'],
        [ '',  '',  '',  '',  '', '7',  '', '3', '2'],
        [ '', '2', '1', '8', '3',  '', '6',  '', '4'],
        ['6', '7',  '',  '', '5', '4', '1', '9',  '']
        ]
shudu6 = [
        ['8',  '', '5',  '', '4',  '',  '',  '', '3'],
        [ '', '4',  '',  '',  '',  '',  '',  '',  ''],
        [ '',  '', '2',  '',  '',  '', '9', '4',  ''],
        ['1',  '',  '', '6',  '', '3',  '', '2',  ''],
        [ '',  '', '6',  '',  '', '8',  '',  '',  ''],
        ['7',  '', '4',  '', '2',  '', '8',  '', '9'],
        [ '',  '',  '',  '',  '',  '',  '', '3',  ''],
        [ '', '2', '1', '8',  '',  '', '6',  '', '4'],
        [ '', '7',  '',  '', '5',  '',  '', '9',  '']
        ]
shudu7 = [
        ['8',  '', '5',  '', '4',  '',  '',  '', '3'],
        [ '', '4',  '',  '',  '',  '',  '',  '',  ''],
        [ '',  '', '2',  '',  '',  '', '9', '4',  ''],
        ['1',  '',  '', '6',  '', '3',  '', '2',  ''],
        [ '',  '', '6',  '',  '', '8',  '',  '',  ''],
        ['7',  '', '4',  '', '2',  '', '8',  '',  ''],
        [ '',  '',  '',  '',  '',  '',  '', '3',  ''],
        [ '', '2', '1', '8',  '',  '', '6',  '', '4'],
        [ '', '7',  '',  '', '5',  '',  '', '9',  '']
        ]
shudu8 = [
        [ '',  '',  '', '7', '5', '2', '1',  '', '9'],
        [ '',  '',  '',  '',  '', '3',  '', '6',  ''],
        [ '',  '', '5',  '', '9', '1',  '', '4',  ''],
        ['5',  '', '2',  '',  '',  '', '3',  '',  ''],
        [ '', '3', '7',  '',  '', '6',  '',  '',  ''],
        ['6', '4',  '',  '', '8',  '', '5', '1',  ''],
        [ '', '5', '8',  '',  '',  '',  '',  '',  ''],
        ['9',  '',  '',  '',  '',  '', '7',  '',  ''],
        ['2',  '',  '', '4', '6', '8',  '',  '',  '']
        ]
shudu9 = [
        ['8', '1', '2', '9', '5',  '', '4', '3',  ''],
        [ '', '5',  '', '1',  '',  '',  '',  '', '6'],
        [ '',  '', '6',  '',  '',  '', '2',  '',  ''],
        [ '', '8',  '', '7',  '', '3', '1', '2',  ''],
        ['1',  '', '9', '5',  '', '4', '6', '7', '3'],
        [ '', '4',  '', '6',  '', '2',  '', '8',  ''],
        [ '',  '',  '', '2',  '',  '',  '', '4', '5'],
        [ '', '7',  '', '8',  '', '9', '3',  '',  ''],
        [ '',  '',  '',  '', '7',  '', '9', '1',  '']
        ]


def chk_row(shudu, x):
    row = []
    for y in range(9):
        if shudu[x][y] != '':
            if shudu[x][y] not in row:
                row.append(shudu[x][y])
            else:
                #print " CHK:\tROW check failed(%d, %s)" % (x, shudu[x][y])
                return 'NNN'
        else:
            pass
    return 'YYY'


def chk_col(shudu, y):
    col = []
    for x in range(9):
        if shudu[x][y] != '':
            if shudu[x][y] not in col:
                col.append(shudu[x][y])
            else:
                #print " CHK:\tCOL check failed(%d, %s)" % (y, shudu[x][y])
                return 'NNN'
        else:
            pass
    return 'YYY'


def chk_rec(shudu, x, y):
    rec = []
    xr = x / 3 * 3
    yr = y / 3 * 3
    for x1 in range(xr, xr + 3):
        for y1 in range(yr, yr + 3):
            if shudu[x1][y1] != '':
                if shudu[x1][y1] not in rec:
                    rec.append(shudu[x1][y1])
                else:
                    #print " CHK:\tREC check failed((%d,%d), %s)" % (x1, y1, shudu[x1][y1])
                    return 'NNN'
            else:
                pass
    return 'YYY'


def chk_1x1(shudu, x, y):
    if (chk_row(shudu, x) == 'NNN' or chk_col(shudu, y) == 'NNN' or chk_rec(shudu, x, y) == 'NNN'):
        return 'NNN'
    else:
        return 'YYY'


def chk_9x9(shudu):
    for x in range(9):
        chk_row(shudu, x)
    for y in range(9):
        chk_col(shudu, y)
    for x in range(3):
        for y in range(3):
            chk_rec(shudu, x * 3, y * 3)


def prt_9x9(shudu):
    print ''
    print "RC| 0 1 2 3 4 5 6 7 8"
    print "--|------------------"
    for x in range(9):
        print "%d |" % (x),
        for y in range(9):
            if shudu[x][y] is not '':
                print shudu[x][y],
            else:
                print ' ',
        print 


def rnd_9x9(shudu):
    for x in range(9):
        for y in range(9):
            shudu[x][y] = random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9', ''], 1)[0]


def scan_row(shudu, x):
    num = 0
    loc = []
    val = set()
    for y in range(9):
        if shudu[x][y] != '':
            val.add(shudu[x][y])
        else:
            loc.append((x, y))
            num += 1
    val = {'1', '2', '3', '4', '5', '6', '7', '8', '9'} - val
    return 'ROW%d'%(x), num, loc, val


def scan_col(shudu, y):
    num = 0
    loc = []
    val = set()
    for x in range(9):
        if shudu[x][y] != '':
            val.add(shudu[x][y])
        else:
            loc.append((x, y))
            num += 1
    val = {'1', '2', '3', '4', '5', '6', '7', '8', '9'} - val
    return 'COL%d'%(y), num, loc, val


def scan_rec(shudu, x, y):
    num = 0
    loc = []
    val = set()
    xr = x / 3 * 3
    yr = y / 3 * 3
    for x1 in range(xr, xr + 3):
        for y1 in range(yr, yr + 3):
            if shudu[x1][y1] != '':
                val.add(shudu[x1][y1])
            else:
                loc.append((x1, y1))
                num += 1
    val = {'1', '2', '3', '4', '5', '6', '7', '8', '9'} - val
    return 'R%dC%d'%(xr, yr), num, loc, val


def scan_9x9(shudu):
    scan = []
    for x in range(9):
        scan.append(scan_row(shudu, x))
    for y in range(9):
        scan.append(scan_col(shudu, y))
    for x in range(3):
        for y in range(3):
            scan.append(scan_rec(shudu, x * 3, y * 3))
    return scan


def fill_1blank(shudu, s):
    x, y = s[2][0]
    shudu[x][y] = list(s[3])[0]
    rtn = chk_1x1(shudu, x, y)
    if rtn == 'YYY':
        print 'FILL:\t("YYY") * 1'
        return 'YY1'
    else:
        print 'FILL:\t("YYY") * 0'
        return 'YY0'


def fill_2blank(shudu, s):
    p = dict()
    x1, y1 = s[2][0]
    x2, y2 = s[2][1]
    for v1, v2 in itertools.permutations(list(s[3]), 2):
        shudu[x1][y1] = v1
        shudu[x2][y2] = v2
        print ' CHK:\t(%s, %s)' % (v1, v2)
        r1 = chk_1x1(shudu, x1, y1)
        r2 = chk_1x1(shudu, x2, y2)
        p[(v1, v2)] = (r1, r2)
    shudu[x1][y1] = shudu[x2][y2] = ''
    cnt = p.values().count(('YYY', 'YYY'))
    if cnt == 2:
        print 'FILL:\t("YYY", "YYY") * 2'
        return 'YY2'
    elif cnt == 1:
        print 'FILL:\t("YYY", "YYY") * 1'
        for k, v in p.items():
            if v == ('YYY', 'YYY'):
                shudu[x1][y1], shudu[x2][y2] = k
                break
        return 'YY1'
    else: 
        print 'FILL:\t("YYY", "YYY") * 0'
        return 'YY0'


def fill_3blank(shudu, s):
    p = dict()
    x1, y1 = s[2][0]
    x2, y2 = s[2][1]
    x3, y3 = s[2][2]
    for v1, v2, v3 in itertools.permutations(list(s[3]), 3):
        shudu[x1][y1] = v1
        shudu[x2][y2] = v2
        shudu[x3][y3] = v3
        print ' CHK:\t(%s, %s, %s)' % (v1, v2, v3)
        r1 = chk_1x1(shudu, x1, y1)
        r2 = chk_1x1(shudu, x2, y2)
        r3 = chk_1x1(shudu, x3, y3)
        p[(v1, v2, v3)] = (r1, r2, r3)
    shudu[x1][y1] = shudu[x2][y2] = shudu[x3][y3] = ''
    cnt = p.values().count(('YYY', 'YYY', 'YYY'))
    if cnt >= 2:
        print 'FILL:\t("YYY", "YYY", "YYY") * %d' % (cnt)
        return 'YY2'
    elif cnt == 1:
        print 'FILL:\t("YYY", "YYY", "YYY") * 1'
        for k, v in p.items():
            if v == ('YYY', 'YYY', 'YYY'):
                shudu[x1][y1], shudu[x2][y2], shudu[x3][y3] = k
                break
        return 'YY1'
    else: 
        print 'FILL:\t("YYY", "YYY", "YYY") * 0'
        return 'YY0'


def fill_4blank(shudu, s):
    p = dict()
    x1, y1 = s[2][0]
    x2, y2 = s[2][1]
    x3, y3 = s[2][2]
    x4, y4 = s[2][3]
    for v1, v2, v3, v4 in itertools.permutations(list(s[3]), 4):
        shudu[x1][y1] = v1
        shudu[x2][y2] = v2
        shudu[x3][y3] = v3
        shudu[x4][y4] = v4
        print ' CHK:\t(%s, %s, %s, %s)' % (v1, v2, v3, v4)
        r1 = chk_1x1(shudu, x1, y1)
        r2 = chk_1x1(shudu, x2, y2)
        r3 = chk_1x1(shudu, x3, y3)
        r4 = chk_1x1(shudu, x4, y4)
        p[(v1, v2, v3, v4)] = (r1, r2, r3, r4)
    shudu[x1][y1] = shudu[x2][y2] = shudu[x3][y3] = shudu[x4][y4] = ''
    cnt = p.values().count(('YYY', 'YYY', 'YYY', 'YYY'))
    if cnt >= 2:
        print 'FILL:\t("YYY", "YYY", "YYY", "YYY") * %d' % (cnt)
        return 'YY2'
    elif cnt == 1:
        print 'FILL:\t("YYY", "YYY", "YYY", "YYY") * 1'
        for k, v in p.items():
            if v == ('YYY', 'YYY', 'YYY', 'YYY'):
                shudu[x1][y1], shudu[x2][y2], shudu[x3][y3], shudu[x4][y4] = k
                break
        return 'YY1'
    else: 
        print 'FILL:\t("YYY", "YYY", "YYY") * 0'
        return 'YY0'


def tryfill_2blank(shudu, s):
    p = dict()
    x1, y1 = s[2][0]
    x2, y2 = s[2][1]
    for v1, v2 in itertools.permutations(list(s[3]), 2):
        shudu[x1][y1] = v1
        shudu[x2][y2] = v2
        print ' CHK:\t(%s, %s)' % (v1, v2)
        r1 = chk_1x1(shudu, x1, y1)
        r2 = chk_1x1(shudu, x2, y2)
        p[(v1, v2)] = (r1, r2)
    shudu[x1][y1] = shudu[x2][y2] = ''
    cnt = p.values().count(('YYY', 'YYY'))
    if cnt == 2:
        print 'TRY2:\t("YYY", "YYY") * 2'
        # 1. append the snapshot of shudu.
        for k, v in p.items():
            if v == ('YYY', 'YYY'):
                shudu[x1][y1], shudu[x2][y2] = k
                guess.append(copy.deepcopy(shudu))
        pop = guess.pop()
        for i in range(9):
            for j in range(9):
                shudu[i][j] = pop[i][j]
        print 'PUSH:\tGuess level = %d, Try' % (len(guess)), s[0], s[2], k
        return 'YY1'
    elif cnt == 1:
        print 'TRY2:\t("YYY", "YYY") * 1'
        return 'YY1'
    else: 
        print 'TRY2:\t("YYY", "YYY") * 0'
        return 'YY0'


def tryfill_3blank(shudu, s):
    p = dict()
    x1, y1 = s[2][0]
    x2, y2 = s[2][1]
    x3, y3 = s[2][2]
    for v1, v2, v3 in itertools.permutations(list(s[3]), 3):
        shudu[x1][y1] = v1
        shudu[x2][y2] = v2
        shudu[x3][y3] = v3
        print ' CHK:\t(%s, %s, %s)' % (v1, v2, v3)
        r1 = chk_1x1(shudu, x1, y1)
        r2 = chk_1x1(shudu, x2, y2)
        r3 = chk_1x1(shudu, x3, y3)
        p[(v1, v2, v3)] = (r1, r2, r3)
    shudu[x1][y1] = shudu[x2][y2] = shudu[x3][y3] = ''
    cnt = p.values().count(('YYY', 'YYY', 'YYY'))
    if cnt >= 2:
        print 'TRY3:\t("YYY", "YYY", "YYY") * %d' % (cnt)
        # 1. append the snapshot of shudu.
        for k, v in p.items():
            if v == ('YYY', 'YYY', 'YYY'):
                shudu[x1][y1], shudu[x2][y2], shudu[x3][y3] = k
                guess.append(copy.deepcopy(shudu))
        pop = guess.pop()
        for i in range(9):
            for j in range(9):
                shudu[i][j] = pop[i][j]
        print 'PUSH:\tGuess level = %d, Try' % (len(guess)), s[0], s[2], k
        return 'YY1'
    elif cnt == 1:
        print 'TRY3:\t("YYY", "YYY", "YYY") * 1'
        return 'YY1'
    else: 
        print 'TRY3:\t("YYY", "YYY", "YYY") * 0'
        return 'YY0'


def tryfill_4blank(shudu, s):
    p = dict()
    x1, y1 = s[2][0]
    x2, y2 = s[2][1]
    x3, y3 = s[2][2]
    x4, y4 = s[2][3]
    for v1, v2, v3, v4 in itertools.permutations(list(s[3]), 4):
        shudu[x1][y1] = v1
        shudu[x2][y2] = v2
        shudu[x3][y3] = v3
        shudu[x4][y4] = v4
        print ' CHK:\t(%s, %s, %s, %s)' % (v1, v2, v3, v4)
        r1 = chk_1x1(shudu, x1, y1)
        r2 = chk_1x1(shudu, x2, y2)
        r3 = chk_1x1(shudu, x3, y3)
        r4 = chk_1x1(shudu, x4, y4)
        p[(v1, v2, v3, v4)] = (r1, r2, r3, r4)
    shudu[x1][y1] = shudu[x2][y2] = shudu[x3][y3] = shudu[x4][y4] = ''
    cnt = p.values().count(('YYY', 'YYY', 'YYY', 'YYY'))
    if cnt >= 2:
        print 'TRY4:\t("YYY", "YYY", "YYY", "YYY") * %d' % (cnt)
        # 1. append the snapshot of shudu.
        for k, v in p.items():
            if v == ('YYY', 'YYY', 'YYY', 'YYY'):
                shudu[x1][y1], shudu[x2][y2], shudu[x3][y3], shudu[x4][y4] = k
                guess.append(copy.deepcopy(shudu))
        pop = guess.pop()
        for i in range(9):
            for j in range(9):
                shudu[i][j] = pop[i][j]
        print 'PUSH:\tGuess level = %d, Try' % (len(guess)), s[0], s[2], k
        return 'YY1'
    elif cnt == 1:
        print 'TRY4:\t("YYY", "YYY", "YYY", "YYY") * 1'
        return 'YY1'
    else: 
        print 'TRY4:\t("YYY", "YYY", "YYY", "YYY") * 0'
        return 'YY0'


def calculate(shudu):
    print '##################################################################'
    tryfill = False
    for i in range(200):
        print '=================================================== [ %03d ] ======' % (i)
        # 1. scan 9x9, the return values contain the number of blanks, location of blanks, unfilled values.
        gohead = False
        prt_9x9(shudu)
        scan = scan_9x9(shudu)
        # 2. find the fewest blanks("") in 9 rows, 9 columns, 9 rectanger.
        # 3. fill the only one blank in shudu, then rescan.
        print '--( 1 )-----------------------------------------------------------'
        for s in scan:
            if s[1] == 1:
                print 'SCAN:\t', s
                rtn = fill_1blank(shudu, s) 
                if rtn == 'YY0':
                    # encouter a error, recall.
                    pop = guess.pop()
                    for i in range(9):
                        for j in range(9):
                            shudu[i][j] = pop[i][j]
                print ' POP:\tGuess level = %d' % (len(guess))
                gohead = True
                break
        if gohead:
            continue
        # 4. if having no only one blank left in shudu, try to fill the two blanks in shudu.
        #    for two blanks and two values, that is P22, two possibility.
        #        (B1V1, B2V2), (B1V2, B2V1)
        #    after checking, the result of pemutation(B1V1, B2V2) list below.
        #        B1V1: YYY, B2V2 YYY
        #        B1V1: NNN, B2V2 YYY
        #        B1V1: YYY, B2V2 NNN
        #        B1V2: NNN, B2V1 NNN
        #    after checking, the result of pemutation(B1V2, B2V1) list below.
        #        B1V2: YYY, B2V1 YYY
        #        B1V2: NNN, B2V1 YYY
        #        B1V2: YYY, B2V1 NNN
        #        B1V1: NNN, B2V2 NNN
        #    so, the conclusion:
        #        1) we get two  (YYY, YYY), the result is uncomfirmed, need guess.
        #        2) we get one  (YYY, YYY) and one of ((NNN, NNN), (NNN, YYY), (YYY, NNN)), the result is confirmed.
        #        3) we get zero (YYY, YYY), the last try is failed, then recall.
        print '--( 2 )-----------------------------------------------------------'
        for s in scan:
            if s[1] == 2:
                print 'SCAN:\t', s
                if tryfill:
                    rtn = tryfill_2blank(shudu, s)
                    tryfill = False
                else:
                    rtn = fill_2blank(shudu, s)
                if rtn == 'YY2':
                    gohead = False
                    # No break here
                elif rtn == 'YY1': 
                    gohead = True
                    break
                else:
                    # encouter a error, recall.
                    pop = guess.pop()
                    for i in range(9):
                        for j in range(9):
                            shudu[i][j] = pop[i][j]
                    print ' POP:\tGuess level = %d' % (len(guess))
                    gohead = True
                    break
        if gohead:
            continue
        # 5. if having no two blank left in shudu, try to fill the three blanks in shudu.
        #    for three blanks and three values, that is P33, six possibility.
        #        V1V2V3, V1V3V2, V2V1V3, V2V3V1, V3V1V2, V3V2V1
        #    after checking, the result of pemutation(V1V2V3) list below.
        #        B1V1: YYY, B2V2 YYY, B3V3 YYY
        #        B1V1: YYY, B2V2 YYY, B3V3 NNN
        #        B1V1: YYY, B2V2 NNN, B3V3 YYY
        #        B1V1: YYY, B2V2 NNN, B3V3 NNN
        #        B1V1: NNN, B2V2 YYY, B3V3 YYY
        #        B1V1: NNN, B2V2 YYY, B3V3 NNN
        #        B1V1: NNN, B2V2 NNN, B3V3 YYY
        #        B1V1: NNN, B2V2 NNN, B3V3 NNN
        #    after checking, the result of pemutation(V1V3V2, V2V1V3, V2V3V1, V3V1V2, V3V2V1) list below.
        #        ......
        #    so, the conclusion:
        #        1) we get two+ (YYY, YYY, YYY), the result is uncomfirmed, need guess.
        #        2) we get one  (YYY, YYY, YYY) and one of ((YYY, YYY, NNN) ...... (NNN, NNN, NNN)), the result is confirmed.
        #        3) we get zero (YYY, YYY, YYY), the last try is failed, then recall.
        print '--( 3 )-----------------------------------------------------------'
        for s in scan:
            if s[1] == 3:
                print 'SCAN:\t', s
                if tryfill:
                    rtn = tryfill_3blank(shudu, s)
                    tryfill = False
                else:
                    rtn = fill_3blank(shudu, s)
                if rtn == 'YY2':
                    gohead = False
                    # No break here
                elif rtn == 'YY1': 
                    gohead = True
                    break
                else:
                    # encouter a error, recall.
                    pop = guess.pop()
                    for i in range(9):
                        for j in range(9):
                            shudu[i][j] = pop[i][j]
                    print ' POP:\tGuess level = %d' % (len(guess))
                    gohead = True
                    break
        if gohead:
            continue
        # 6. if having no three blank left in shudu, try to fill the more blanks in shudu.
        print '--( 4 )-----------------------------------------------------------'
        for s in scan:
            if s[1] == 4:
                print 'SCAN:\t', s
                if tryfill:
                    rtn = tryfill_4blank(shudu, s)
                    tryfill = False
                else:
                    rtn = fill_4blank(shudu, s)
                if rtn == 'YY2':
                    gohead = False
                    # No break here
                elif rtn == 'YY1': 
                    gohead = True
                    break
                else:
                    # encouter a error, recall.
                    pop = guess.pop()
                    for i in range(9):
                        for j in range(9):
                            shudu[i][j] = pop[i][j]
                    print ' POP:\tGuess level = %d' % (len(guess))
                    gohead = True
                    break
        if gohead:
            continue
        #    if the max number of blanks is 0, which means we have no more job to do.
        num = set()
        for s in scan:
            num.add(s[1])
        maxnum = max(num)
        # 7. uncertainly, need guess.
        if num & {2, 3, 4}:
            print ' TRY:\tLet`s guess...'
            tryfill = True
            continue
        # 8. unable to crack it now.
        if num & {5, 6, 7, 8, 9}:
            print ' CHK:\tMaxNum(%d) beyond current capability.' % (min(num & {4, 5, 6, 7, 8, 9}))
            break
        # 9. job done.
        if maxnum == 0:
            print ' CHK:\tFinal check.'
            chk_9x9(shudu)
            print ' CHK:\tDone!'
            break
    guess[:] = []
        

if __name__ == "__main__":
    calculate(shudu9)


