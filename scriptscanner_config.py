class config(object):

    """
    scriptscanner config object for the barium experiment.
    """
    # Folder names within the experiments folder that holder experiments
    exps = 'barium.lib.scripts.experiments.'

    # list in the format (import_path, class_name)
    scripts = [(exps + 'linescan_camera.linescan_camera', 'linescan_camera'), (exps + 'filament_loading.filament_loading', 'filament_loading'),(exps + 'frequency_scan.frequency_scan', 'frequency_scan'), \
               (exps + 'loading_curve.loading_curve', 'loading_curve'),(exps + 'loading_curve_cam.loading_curve_cam','loading_curve_cam')]

    #allowed_concurrent = {}
    #allowed_concurrent['lasermonitor'] = ['lasermonitor']

launch_history = 1000
