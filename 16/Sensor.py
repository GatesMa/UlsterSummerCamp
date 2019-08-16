import pexpect
import sys
import time


def floatfromhex(h):
    t = float.fromhex(h)
    if t > float.fromhex('7FFF'):
        t = -(float.fromhex('FFFF') - t)
        pass
    return t

def clacTmpTarget(objT, ambT):
    m_tmpAmb = ambT/128.0
    Vobj2 = objT * 0.00000015625
    Tdie2 = m_tmpAmb + 273.15
    S0 = 6.4E-14
    a1 = 1.75E-3
    a2 = -1.678E-5
    b0 = -2.94E-5
    b1 = -5.7E-7
    b2 = 4.63E-9
    c2 = 13.4
    Tref = 298.15
    S = S0*(1+a1*(Tdie2 - Tref)+a2*pow((Tdie2 - Tref), 2))
    Vos = b0 + b1*(Tdie2 - Tref) + b2*pow((Tdie2 - Tref), 2)
    fObj = (Vobj2 - Vos) + c2*pow((Vobj2 - Vos), 2)
    tObj = pow(pow(Tdie2, 4) + (fObj/S),.25)
    tObj = (tObj - 273.15)

    return "%.2f" % tObj



bluetooth_adr = "54:6C:0E:53:1E:3D"


tool = pexpect.spawn('gatttool -b ' + bluetooth_adr + ' --interactive')
tool.expect('.*\[LE\]>', timeout = 600)
print('Preparing to connect. You might need to press the the side button...')
tool.sendline('connect')
tool.expect('Connection successful.*\[LE\]>')

tool.sendline('char-write-cmd 0x27 01')
tool.expect('\[LE\]>')

n = input('Intut the number of the loop:')

for i in range(1, int(n)):
    tool.sendline('char-read-hnd 0x24')
    tool.expect('descriptor: .*')
    rval = tool.after.split()
    #print(rval)
    objT = floatfromhex(str(rval[2] + rval[1])[2:6])
    ambT = floatfromhex(str(rval[4] + rval[3])[2:6])
    IRtemp = clacTmpTarget(objT, ambT)
    #print(rval[2] + rval[1])
    #print(rval[4] + rval[3])
    #print()
    print('-----------------------------')
    print(bluetooth_adr, ': ', IRtemp)
    print('Fahrenheit: \t' + IRtemp)
    celsius = (float(IRtemp) - 32) * 5.0/9.0
    print('Celsius:\t%.2f' % celsius)
    
    if celsius > 28.0 :
        print('Temperature is too high!!!')
        
    time.sleep(5)


