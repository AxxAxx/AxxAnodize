import argparse
import sys

def main():

    '''Console script'''
    parser = argparse.ArgumentParser()

    # An argument without - is required
    parser.add_argument('surfacearea', type=float, help='Surface area in mm^2')
    parser.add_argument('-thickness', type=float, default=1, help='The anodizing thickness in "mils"')
    parser.add_argument('-currentdensity', type=float, default=12, help='The current density, default is 12 Amp/ft^2')

    # Show help if no arguments are given
    if len(sys.argv) <=1:
        sys.argv.append('--help')

    args = parser.parse_args()

############################################################
    
    feet_per_mm = 0.00328083989

    square_feet = args.surfacearea*feet_per_mm**2
    
    setcurrent = square_feet * args.currentdensity
    time =  720 * args.thickness / args.currentdensity
    #time = 2 # TEMP
    peakvoltage = 2.5 * args.currentdensity
    print ('\033[91m')
    print('='*40) 
    print('          Anodizing recipie')
    print('          Axel Johansson V1.4')
    print('='*40)
    print ('\033[0m')    
    print(' Part Surface Area:\033[4m\t%.1f\033[0m mm^2' % (args.surfacearea))
    print(' Set Current:\033[4m\t\t%.2f\033[0m Ampere' % (setcurrent))
    print(' Time:\t\t\t%.1f Minutes' % (time))
    print(' Peak voltage:\t\t%.1f Vdc' % (peakvoltage))
    print(' Oxide thickness:\t%.1f micrometer' % (args.thickness*25.4))
    print('-'*40)
    print(' REMEMBER:\n (+) Goes to the Part\n (-) Goes to the Cathode')
    print('-'*40)
    print('')
    #print ('\033[0m')
###########################################################    
if __name__ == "__main__":
    main()
