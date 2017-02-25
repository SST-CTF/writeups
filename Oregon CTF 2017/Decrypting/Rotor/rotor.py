#
# example keys:
#
#          AcidBurn 206177029435882881079
#          ZeroCool 118733477640976187249
#      CerealKiller 057228030928664253628
#     CrashOverride 175851556071936006109
#     PhantomPhreak 375157722934813517761

import sys;

def rol_string(s, amount):
    width = len(s)
    # rotating len(s) is identity op, so reduce the work
    amount = amount % width
    for i in range(amount):
        s = s[1:width] + s[0]
    return(s)

if len(sys.argv) != 3:
    print "usage: ", sys.argv[0], " <name> <serial>";
    quit()

# truncate/pad input name to 10 characters
name = sys.argv[1]
if len(name) > 10:
    name = name[0:10]
else:
    while len(name) < 10:
        name = name + 'S'

# convert serial to number eg: "1234" -> 1234
serial = int(sys.argv[2], 10);

# process serial
rotor0 = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ`abcdefghijklmnopqrstuvwxyz{|}~1akuEOY"
rotor1 = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ`abcdefghijklmnopqrstuvwxyz{|}~2blvFPZ9hqz"
rotor2 = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ`abcdefghijklmnopqrstuvwxyz{|}~3cmwGQ10irAIQ"
rotor3 = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ`abcdefghijklmnopqrstuvwxyz{|}~4dnxHR2ajsBJRY6cj"
rotor4 = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ`abcdefghijklmnopqrstuvwxyz{|}~5eoyIS3bktCKSZ7dkqw"
rotor5 = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ`abcdefghijklmnopqrstuvwxyz{|}~6fpzJT4cluDLT18elrxCHMR"
rotor6 = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ`abcdefghijklmnopqrstuvwxyz{|}~7gqAKU5dmvEMU29fmsyDINSW159cgkoswAEIM"
rotor7 = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ`abcdefghijklmnopqrstuvwxyz{|}~8hrBLV6enwFNV30gntzEJOTX260dhlptxBFJNQTWZ"
rotor8 = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ`abcdefghijklmnopqrstuvwxyz{|}~9isCMW7foxGOW4ahouAFKPUY37aeimquyCGKORUX13579ac"
rotor9 = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ`abcdefghijklmnopqrstuvwxyz{|}~0jtDNX8gpyHPX5bipvBGLQVZ48bfjnrvzDHLPSVY24680bdef"

rotor0 = rol_string(rotor0, serial);
rotor1 = rol_string(rotor1, serial);
rotor2 = rol_string(rotor2, serial);
rotor3 = rol_string(rotor3, serial);
rotor4 = rol_string(rotor4, serial);
rotor5 = rol_string(rotor5, serial);
rotor6 = rol_string(rotor6, serial);
rotor7 = rol_string(rotor7, serial);
rotor8 = rol_string(rotor8, serial);
rotor9 = rol_string(rotor9, serial);

# together, front characters of each rotor must spell your name
check = rotor0[0] + rotor1[0] + rotor2[0] + rotor3[0] + rotor4[0] + rotor5[0] + rotor6[0] + rotor7[0] + rotor8[0] + rotor9[0];

if name==check and serial>139 and serial<421336842070675358939:
    print "good"
else:
    print "bad"
