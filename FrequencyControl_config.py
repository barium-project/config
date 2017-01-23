class FrequencyControl_config(object):

    '''
    IP address of the computer running the server
    '''
    ip = 'bender'

    ''' List the GPIB addresses for the client HP8672A and HP8672B to connect to
    '''

    gpibA = ['GPIB0::19','GPIB0::21']
    gpibB = ['GPIB0::6','GPIB0::7','GPIB0::8']


    '''
    Set the default frequencies and powers for the oscillators
    '''
    default = {'GPIB0::19':[5000,-90,-10], 'GPIB0::21':[5000,-90,-10], 'GPIB0::6':[200,-140], 'GPIB0::7':[200,-140],'GPIB0::8':[200,-140]}

    cool_133 =  {'GPIB0::19':[3817,0,-2], 'GPIB0::21':[5882,0,2], 'GPIB0::6':[100,-140], \
                  'GPIB0::7':[100,-140],'GPIB0::8':[100,-140], '493nm':.004233, '650nm':.000988}

    cool_135 =  {'GPIB0::19':[3592,0,-2], 'GPIB0::21':[5882,-100,-10], 'GPIB0::6':[538,-11], \
                  'GPIB0::7':[482,-11],'GPIB0::8':[341,-16], '493nm':.000416, '650nm':.000193}

    cool_138 = {'GPIB0::19':[3000,-100,-10], 'GPIB0::21':[3000,-100,-10], 'GPIB0::6':[100,-140], 'GPIB0::7':[100,-140],'GPIB0::8':[100,-140]}



    heat_135 = {'GPIB0::19':[2000,-100,-10], 'GPIB0::21':[2000,-100,-10], 'GPIB0::6':[100,-140], 'GPIB0::7':[100,-140],'GPIB0::8':[100,-140]}