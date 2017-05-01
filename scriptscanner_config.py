class config(object):

    """
    scriptscanner config object for the barium experiment.
    """
    # Folder names within the experiments folder that holder experiments
    exps = 'barium.lib.scripts.experiments.'

    # list in the format (import_path, class_name)
    scripts = [(exps + 'linescan_camera.linescan_camera', 'linescan_camera'),
               (exps + 'laser_stability_monitor.laser_stability_monitor', 'laser_stability_monitor'),
               (exps + 'frequency_scan.frequency_scan', 'frequency_scan'),
               (exps + 'probe_line_scan.probe_line_scan', 'probe_line_scan'),
               (exps + 'mass_spec.mass_spec','mass_spec')]

    # This allows running multiple experiments at the same time. Use the name defined
    # below the class definition i.e. name = "exp name"
    allowed_concurrent = {}
    allowed_concurrent['Laser Monitor'] = ['Laser Monitor', 'Probe Line Scan']


launch_history = 1000
