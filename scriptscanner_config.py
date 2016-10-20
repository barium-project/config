class config(object):

    """
    scriptscanner config object for the molecules experiment.
    """
    # Folder names within the experiments folder that holder experiments
    exps = 'barium.lib.scripts.experiments.'

    # list in the format (import_path, class_name)
    scripts = [(exps + 'linescan_camera.linescan_camera', 'linescan_camera')]

    #allowed_concurrent = {}
    #allowed_concurrent['lasermonitor'] = ['lasermonitor']

launch_history = 1000