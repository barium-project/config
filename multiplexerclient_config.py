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
    info = {'493nm' :(1, '607.426050', (0,1), stretched, displayPID, 1,[-5,5]),
            '650nm' :(11, '461.311710', (0,2), stretched, displayPID, 2,[-5,5])
            }
    '''
    IP address of the wavemeter computer
    '''
    ip = '10.97.111.8'

    #ip = '10.97.112.2'
