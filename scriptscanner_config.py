class config(object):

    """
    scriptscanner config object for the barium experiment.
    """
    # Folder names within the experiments folder that holder experiments
    exps = 'barium.lib.scripts.experiments.'

    # list in the format (import_path, class_name)
    scripts = [(exps + 'linescan_camera.linescan_camera', 'linescan_camera'), (exps + 'filament_loading.filament_loading', 'filament_loading'),(exps + 'frequency_scan.frequency_scan', 'frequency_scan'), \
               (exps + 'loading_curve_tof.loading_curve_tof', 'loading_curve_tof'),(exps + 'mass_spec.mass_spec','mass_spec')]

    #allowed_concurrent = {}
    #allowed_concurrent['lasermonitor'] = ['lasermonitor']

launch_history = 1000
