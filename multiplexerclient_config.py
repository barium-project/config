class multiplexer_config(object):
    '''
    multiplexer client configuration file

    Attributes
    ----------
    info: dict
    {channel_name: (Multiplexer Channel, hint, display_location (column,row), stretched, display PID,
    DAC Channel (0 unassigned)), Rail Volatages)}

    '''
    stretched = False
    displayPID = True
    info = {'493nm' :(1, '607.426140', (0,1), stretched, displayPID, 1,[-3,3]),
            '650nm' :(3, '461.311705', (0,2), stretched, displayPID, 2,[-5,5]),
            '455nm' :(2, '658.116220', (0,3), stretched, displayPID, 0,[-5,5]),
            '1171nm' :(11,'256.000000', (0,4), stretched, displayPID, 0,[-5,5]),
            }

    '''
    info: dict
    {channel_name: (Multiplexer Channel, hint, display_location (column,row), gain,
    DAC Channel (0 unassigned)), Rail Volatages, locked, output voltage)}
    '''
    single_lock = {
            '455nm' :(2, '658.116220', (0,3), .001,  7,[0,30], 0, 0),
            '585nm' :(16, '512.141000', (0,3), .001,  6,[0,30], 0, 0),
                   }
    '''
    name of cert for the wavemeter computer
    '''
    ip = 'wavemeter'

    #ip = '10.97.112.2'
