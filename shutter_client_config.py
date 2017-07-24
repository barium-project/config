class shutter_config(object):
    '''
    configuration file for arduino switch client
    info is the configuration dictionary in the form
    {channel_name: (port, display_location, inverted, enable)), }
    '''
    info = {'Channel 9': (9, (0,1), False, 5),
            'Channel 10': (10, (0,2), False, 6),
	    'Channel 11': (12, (0,3), False, 3),
	    'Channel 12': (11, (0,4), False, 7),
            }
