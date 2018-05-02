class config(object):

    """
    scriptscanner config object for the barium experiment.
    """
    # Folder names within the experiments folder that holder experiments
    exps = 'barium.lib.scripts.experiments.'

    # list in the format (import_path, class_name)
    scripts = [(exps + 'optical_pumping.optical_pumping', 'optical_pumping'),
               (exps + 'rabi_flopping.rabi_flopping','rabi_flopping'),
               (exps + 'microwave_sweep.microwave_sweep','microwave_sweep'),
               (exps + 'bright_state_detection.bright_state_detection', 'bright_state_detection'),
               (exps + 'd32_measurement.d32_measurement', 'd32_measurement'),
               (exps +  'mm_compensation.mm_compensation', 'mm_compensation'),
               (exps +  'probe_line_scan.probe_line_scan', 'probe_line_scan'),
               #(exps +  'frequency_sweep.frequency_sweep', 'frequency_sweep'),
               (exps + 'ramsey.ramsey','ramsey'),
               (exps + 'frequency_scan.frequency_scan','frequency_scan'),
               (exps + 'laser_stability_monitor.laser_stability_monitor','laser_stability_monitor'),
               (exps + 'shelving.shelving','shelving'),
               (exps + 'shelving_133.shelving_133','shelving_133')
               ]

    # This allows running multiple experiments at the same time. Use the name defined
    # below the class definition i.e. name = "exp name"
    allowed_concurrent = {}
    allowed_concurrent['Laser Monitor'] = ['Laser Monitor', 'Probe Line Scan']


launch_history = 1000
