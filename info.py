#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Info and substitution dicts for sims module. """
from __future__ import print_function, division
from .rkeys import rkeys

stage_scan_types = {
    0: 'stage scan',
    1: 'beam scan',
    2: 'image scan',
}

# large scale, movement control, small scale
# spot/line/image, beam/stage, raster/static
file_types = {
    21: 'depth profile',
    22: 'line scan, stage control',
    26: 'isotope image',
    27: 'image',
    29: 'grain mode image',
    31: 'SIBC file',
    35: 'beam stability file',
    39: 'line scan image',
    41: 'stage scan image',
}

supported_file_types = [ 21, 22, 26, 27, 29, 39, 41 ]

peakcenter_sides = {
    0: 'left',
    1: 'right',
    2: 'both'
}

exit_slit_size_labels = {
    0: 'normal',
    1: 'large',
    2: 'extra large'
}

exit_slit_labels = {
    0: 'slit 1',
    1: 'slit 2',
    2: 'slit 3'
}

detectors = {
    0: 'EM',
    1: 'FC'
}

header_info = {
    # peek
    'file version':             'Version number of the file format specification; so far 11 or 4108 (int)',
    'file type':                'File format type; see sims.file_type and sims.supported_file_types. (int)',
    'header size':              'Size of the entire header in bytes. (int)',
    'byte order':               'Byteorder character for Python\'s struct.unpack(); < for little endian, > for big endian; not in Cameca file. (str)',
    # end peek
    # main header
    'sample type':              '? (int)',
    'data included':            'Whether there is data in this file. (bool)',
    'sample x':                 'X position of sample stage in nm. (int)',
    'sample y':                 'Y position of sample stage in nm. (int)',
    'analysis type':            'Cameca supplied name of analysis type, e.g. \"IMAGE MODE\"; 32 character max. (str)',
    'user name':                'Name of the operator; 16 characters max. (str)',
    'sample z':                 'Z position of sample stage in nm. (int)',
    'date':                     'Date and time of file creation, presumably in local timezone. (datetime obj)',
    # if IMAGE or LINE SCAN IMAGE
    'original filename':        'Filename as stored in the file; 16 characters max (str)',
    'analysis duration':        'Total time of analysis run in seconds. (int)',
    'cycles':                   'Number of cycles, a.k.a. planes. (int)',
    'scan type':                'When file type is 41 (stage scan), scan type is one of: sample scan (0), beam scan (1), or image scan (2). For the other scan types, the number -> name translation of the scan type is unknown and left as a stringified number. (str)',
    'magnification':            '? (int)',
    'size type':                '? (int)',
    'size detector':            '? (int)',
    'beam blanking':            'Whether beam blanking is performed. (bool)',
    'presputtering':            'Whether presputtering was done. (bool)',
    'presputtering duration':   'Duration of presputtering in cycles. (int)',
    # elif STAGE SCAN IMAGE (only add new)
    'steps':                    'Total number of steps in a stage scan, equals steps x * steps y. (int)',
    'steps x':                  'Number of steps in X direction in a stage scan. (int)',
    'steps y':                  'Number od steps in Y direction in a stage scan. (int)',
    'step size':                'Physical distance between two steps in microns in a stage scan (int)',
    # waittime could be cts/px in microsec. but then should be called pixel waittime
    'step waittime':            'Waiting time between two points in ?? in a stage scan (float)',
    # endif
    'masses':                   'Number of masses. (int)',
    'mass table ptr':           '???; a number for each mass. (list[int])',
    'AutoCal': {
        'AutoCal':              'Stores mass autocalibration information. (dict)',
        'has autocal':          'Whether AutoCal information is stored. (bool)',
        'label':                'Species label; 64 characters max. (str)',
        'begin':                'Start of autocalibration in ?? (int)',
        'duration':             'Duration of autocalibration in ?? (int)',
    },
    'HVControl': {
        'HVControl':            'Stores HVControl information. (dict)',
        'has hvcontrol':        'Whether HVControl is stored. (bool)',
        'label':                'Species label of reference mass; 64 characters max. (str)',
        'begin':                'Cycle number at which HVControl starts. (int)',
        'duration':             'Duration of HVControl in cycles. (int)',
        'limit low':            'Lower limit in Volt. (float)',
        'limit high':           'Upper limit in Volt. (float)',
        'step':                 'Step size in Volt. (float)',
        'bandpass width':       'Width of the bandpass filter in eV. (int)',
        'count time':           'Duration of HVControl in seconds. (float)'
    },
    'MassTable': {          
        'MassTable':            'Stores a table with info for each mass. MassTable is a list, where each item is a dict containing the info for that mass. (list(dict))',
        'count time':           'Measurement time per plane in seconds; for stage scans this is the time per point (single point or image). (float)',
        'detector':             '? (int)',
        'b field':              'Magnetic field in bits. (int)',
        'mass':                 'Mass in AMU. (float)',
        'matrix or trace':      '? (int)',
        'offset':               '? (int)',
        'type mass':            'Either type mass or type mass alt is defined, the specs are unclear. No idea what either do. ? (int)',
        'type mass alt':        'Either type mass or type mass alt is defined, the specs are unclear. No ieda what either do. ? (int)',
        'wait time':            '? (float)',
    },
    'Species': {
        'Species':              'Stores information information about the measured species. (dict)',
        'numeric flag':         '? (int)',
        'numeric value':        '? (int)',
        'elements':             'Number of elements. (int)',
        'charges':              'Number of charges. (int)',
        'charge label':         'Charge sign. Single character. (str)',
        'label':                'Species label; 64 characters max. (str)',
        'atomic number':        'Atomic number of each element in this species. List is always 5 long. (list(int))',
        'isotope number':       'Isotope offset from main atomic mass, e.g. atom.no. 8 (oxygen) and isotope number 2 is 18O. List is always 5 long. (list(int))',
        'stoich number':        'Stoichiometric number: how many of each element with atomic number and isotope number. List is always 5 long. (list(int))',
    },
    'SigRef': {
        'SigRef':               'Stores SigRef information. (dict)',
        'has sigref':           'Whether SigRef is stored. (bool)',
        'detector':             '? (int)',
        'offset':               '? (int)',
        'quantity':             '? (int)',
    },
    'PolyList': {
        'PolyList':             'A list with each item a \'Species\' dict. (list(dict))',
    },
    'ChampsList': {
        'ChampsList':           'The struct is present in certain files, but always length 0. Don\'t know how to read. (?)',
    },
    'OffsetList': {
        'OffsetList':           'The struct is present in certain files, but always length 0. Don\'t know how to read. (?)',
    },
    # NanoSIMSHeader
    'NanoSIMSHeader': {
        'NanoSIMSHeader':       'Stores information specific to the nanoSIMS machine. (dict)',
        'nanosimsheader version': 'Version numbering independent of file version. (int)',
        'regulation mode':      '? (int)',
        'mode':                 '? (int)',
        'grain mode':           'Whether this is a grain mode scan (either Cameca or CIW style). (bool)',
        'semigraphic mode':     '? (int)',
        'delta x':				'? (int)',
        'delta y':				'? (int)',
        'working frame width':	'Width of working frame in pixels. (int)',
        'working frame height':	'Height of working frame in pixels. (int)',
        'scanning frame x':     'X position (width) of scanning frame with respect to working frame in pixels. (int)',
        'scanning frame y':     'Y position (height of scanning frame with respect to working frame in pixels. (int)',
        'scanning frame width':	'Width of scanning frame in pixels. (int)',
        'scanning frame height':'Height of scanning frame in pixels. (int)',
        'nx lowb':				'? exactly same as nx low (scan frame x). (int)',
        'nx highb':				'? exactly same as nx high (scan frame width). (int)',
        'ny lowb':				'? exactly same as ny low (scan frame y). (int)',
        'ny highb':				'? exactly same as ny high (scan frame height). (int)',
        'detector type':		'? (int)',
        'electron scan':		'? (int)',
        'scanning mode':		'? (int)',
        'blanking comptage':	'? (int)',
        'b fields':				'Number of B Fields used. (int)',
        'presputtering raster': 'Size of the presputtering raster in microns. (int)',
        'baseline measurements': 'Number of baseline measurements done. (int)',
        'baseline Pd offset':   '? (float)',
        'baseline frequency':   '? (int)',
    },
    'PeakCenter': {
        'PeakCenter':           'Stores information about peak centering. (dict)',
        'has peakcenter':		'Whether peak centering is done. (bool)',
        'start':                'Before which cycle first peak centering is done. (int)',
        'frequency':            'Number of cycles after which peak centering is done. (int)',
        'e0p offset':           'Offset in bits applied to E0P during peak centering. (int)',
    },
    'SibCenter': {
        'SibCenter':            'Stores information about horizontal or vertical secondary ion beam centering. (dict)',
        'detector':             'Which detector (by 0-index) is used for SIB centering. (int or None)',
        'start':                'Start value for SIB centering in bits. (int)',
        'step size':            'Step size for SIB centering in bits. (int)',
        'center':               'Initial guess for position of SIB centering maximum in Volt. (float)',
        '50% width':            'Initial guess for width of SIB peak at 50 % of maximum. (float)', 
        'count time':           'Dwell time per step in seconds. (float)',
        'has sib center':       'Whether SIB centering is enabled. (bool)',
        'b field index':        'Which B field (by 0-index) is used during SIB centering. (int or None)',
    },
    'EnergyCenter': {
        'EnergyCenter':         'Stores information about energy centering. (dict)',
        'detector':             'Which detector (by 0-index) is used for energy centering. (int or None)',
        'start':                'Start value for energy centering in bits. (int)',
        'step size':            'Step size for energy centering in bits. (int)',
        'center':               'Initial guess for position of energy centering maximum in Volt. (float)',
        'delta':                '? OpenMIMS: /* Delta between max and 10% in Volts */ (float)',
        'count time':           'Dwell time per step in seconds. (float)',
        'has energy center':    'Whether energy centering is enabled. (bool)',
        'b field index':        'Which B field (by 0-index) is used during energy centering. (int or None)',
        'frequency':            'How often is energy centering done in cycles. (int)',
        'wait time':            'Time to wait in seconds before starting energy centering. (int)'
    },
    'E0SCenter': {
        'E0SCenter':            'Stores information about E0S centering. (dict)',
        'detector':             'Which detector (by 0-index) is used for E0S centering. (int or None)',
        'start':                'Start value for E0S centering in bits. (int)',
        'step size':            'Step size for E0S centering in bits. (int)',
        'steps':                '?? number of steps, or number of times E0S done; or only before or before and after SIB center. (int)',
        'center':               'Initial guess for position of E0S centering maximum in Volt. (float)',
        '80% width':            'Initial guess for width of SIB peak at 80 % of maximum. (float)', 
        'count time':           'Dwell time per step in seconds. (float)',
        'has e0s center':       'Whether E0S centering is enabled. (bool)',
        'b field index':        'Which B field (by 0-index) is used during SIB centering. (int or None)',
    },
    'BFields': {
        'BFields':              'List of all B fields used. Each item in the list is a dict with B field info. (list(dict))',
        'b field selected':     'Whether this B field is selected. (bool)',
        'b field':              'B field strength in bits. (int)',
        'wait time':            '? (int)',
        'time per pixel':       'Dwell time in microseconds per pixel. (int)',
        'time per point':       'Total measurement time per plane in seconds; for stage scan: total time per point (beam scan) or image (image scan). (float)',
        'computed':             '? (int)',
        'e0w offset':           'E0W offset in bits. (int)',
        'q':                    'Value of quadrupole Q in bits. (int)',
        'lf4':                  'Value of LF4 in bits. (int)',
        'hex':                  'Value of hexapole Hex in bits. (int)',
        'frames':               'Number of frames. (int)',
    },
    'Trolleys': {
        'Trolleys':             'List of all trolleys used in this particular B field. Each item in the list is a dict with trolley info. (list(dict))',
        'label':                'Species label; 64 characters max. (str)',
        'mass':                 'Mass in AMU. (float)',
        'radius':               'Radius of the ion beam trough the magnetic field in mm. (float)',
        'deflection plate 1':   'Deflection on plate 1 in bits. (int)',
        'deflection plate 2':   'Deflection on plate 2 in bits. (int)',
        'detector':             'Detector selected on this trolley, see sims.detectors. (str)',
        'exit slit':            'Exit slit selected for the detector, not used in nanoSIMS, see SecIonBeam dict instead. (int)',
        'real trolley':         'Whether this is a real trolley; fixed detector counts as trolley, secondary electron FC does not. (bool)',
        'trolley index':	    'An index counting the trolleys, corresponds to the index in the MassTable; secondary electron has index -2, but comes in the MassTable (and in the data) at index 5 if all trolleys are used; that is after the 5th trolley, probably because the older nanoSIMS before the Large addition of trolleys 6 and 7, recorded the SE after the ion data). (int)',
        'peakcenter index':	    'Index for trolleys which have peak centering. (int)', 
        'peakcenter follow':	'For trolleys which do not have peak centering, this trolley will follow the trolley with this peak centering index. (int)',
        # focus is called polarization in OpenMIMS
        'focus':    			'Focus applied to detector. (float)',
        'hmr start':			'Start point of deflection in high mass resolution scan in Volt. (float)',
        'hmr start plate 1':	'Start value of plate 1 in a high mass resolution scan in bits. (? identical to "deflector plate 1"?) (int)',
        'hmr start plate 2':	'Start value of plate 2 in a high mass resolution scan in bits. (? identical to "deflector plate 2"?) (int)',
        'hmr step':		        'Size of each step in a high mass resolution scan in bits. (int)',
        'hmr points':	        'Number of steps in a high mass resolution scan. (int)',
        'hmr count time':       'Dwell time per step in a high mass resolution scan in seconds. (float)',
        'used for baseline':	'Whether this trolley is used for baseline measurements. (bool)',
        'peakcenter 50% width':	'Initial guess for the width of the peak at 50 % of the peak maximum in Volt. (float)',
        'peakcenter side':		'Which side of the peak to use for peak centering: left, right, or both. (str)',
        'peakcenter count time': 'Dwell time per step during peak centering in seconds. (float)',
        'used for sib center':	'Whether this trolley is used for secondary ion beam centering. (bool)',
        'unit correction':		'? baseline correction (int)',
        'deflection':			'Deflection on the plates in Volt. (float)',
        'used for energy center': 'Whether this trolley is used for energy centering. (bool)',
        'used for e0s center':	'Whether this trolley is used for E0S centering. (bool)',
        'used for phd scan':    'Whether a pulse height distribution scan is done for this trolley. (bool)',
        'phd start':            'Start point of the threshold for pulse height distribution scans in bits. (int)',
        'phd step size':        'Step size for pulse height distribution scan. (int)',
        'phd points':           'Number of points recorded in pulse height distribution scan. (int)',
        'phd count time':       'Dwell time per point in pulse height distribution scan in seconds. (float)',
        'phd scan repeat':      'Number of repeated scans for pulse height distribution scan. (int)'
    },
    'SIMSHeader': {
        'SIMSHeader':           'Header for non-nanoSIMS machines. (dict)',
        'simsheader version':   'Version number of the SIMSHeader subdict. (int)',
        'original filename':    'Filename stored in the file, 256 characters max. (str)',
        'matrix':               'Matrix material, 256 characters max. (str)',
        'sigref auto':          'Whether sigref is automatic or manual. (bool)',
        'sigref points':        'Number of points for sigref. (int)',
        'sigref delta':         '?? (int)',
        'sigref scan time':     'Sigref scanning time in seconds. (float)',
        'sigref measure time':  'Sigref measureing time in seconds (int)',
        'sigref beam time':     'Time in seconds beam was actually on during sigref. (int)',
        'has eps centering':    'Whether centering is done during peak switching. (bool)',
        'has eps':              'Whether peak switching is done. (bool)',
        'central energy':       '?? (int)',
        'b field':              'B field of the central mass. (int)',
        'ref mass tube hv':     '?? (float)',
        'ref mass tube hv max var': '?? (float)',
        'sample rotation':      'Whether sample is rotating. (bool)',
        'sample rotation synced': 'Whether sample rotation is synchronized with acquisition. (bool)',
        'sample rotation speed': 'Sample rotation speed in turns/minute. (int)',
        'sample name':          'Name of the sample, 80 characters max. (str)',
        'user name':            'Name of the operator, 30 characters max. (str)',
        'method name':          'Name of the method, 256 characters max. (str)',
        'CentralSpecies':       'Species dict of the central mass. (dict)',
        'ReferenceSpecies':     'Species dict of the reference mass. (dict)'
    },
    # Analytical parameters
    'analysis version':         'Version number that determines layout of Analytical Parameters section: PrimaryBeam, SecondaryBeam, Detectors dicts. (int)',
    'n50large':                 'Whether this is a nanoSIMS N50 Large. (bool)',
    'comment':                  'Operator comments, 256 characters max. (str)',
    'PrimaryBeam': {
        'PrimaryBeam':          'Stores information that determine the shape of the primary beam. (dict)',
        'source':               'Source name, 8 characters max. (str)',
        'current start':        'Primary beam current measured by FCp at start of experiment in pA. (int)',
        'current end':          'Primary beam current measured by FCp at end of experiment in pA. (int)',
        'lduo':                 'Value of Lduo lens in Volt. (int)',
        'l1':                   'Value of L1 lens in Volt. (int)',
        'dduo':                 'Numerical positon of diaphragm Dduo. (int)',
        'dduo widths':          'Width of diaphragm Dduo at each position in microns, length of list is always 10. (list(int))',
        'd0':                   'Numerical position of diaphragm D0. (int)',
        'd0 widths':            'Width of diaphragm D0 at each position in microns, length of list is always 10. (list(int))',
        'd1':                   'Numerical position of diaphragm D1. (int)',
        'd1 widths':            'Width of diaphragm D1 at each position in microns, length of list is always 10. (list(int))',
        'raster':               'Physical size of the rastered image in microns. (float)',
        'oct45':                'Value of the octapole at 45 degrees in Volt. (float)',
        'oct90':                'Value of the octapole at 90 degrees in Volt. (float)',
        'e0p':                  'Value of E0P lens in Volt. (float)',
        'pressure analysis chamber': 'Pressure in the analysis chamber in torr. (str)',
        'l0':                   'Value of L0 lens in Volt. (int)',
        'hv cesium':            'Cesium source high potential in Volt. (int)',
        'hv duo':               'Duo plasmatron source high potential in Volt. (int)',
        'dcs':                  'Numerical position of diaphragm Dcs. (int)',
        'dcs widths':           'Width of diaphragm D1 at each position in microns, length of list is always 10. (list(int))'
    },
    'SecondaryBeam': {
        'SecondaryBeam':        '',
        'e0w':                  'Value of lens E0W in Volt. (float)',
        'es':                   'Numerical position of the entrance slit ES. (int)',
        'es widths':            'Width of entrance slit ES at each position in microns, length of list is always 5. (list(int))',
        'es heights':           'Height of entrance slit ES at each position in microns, length of list is always 5. (list(int))',
        'as':                   'Numerical position of the aperture slit AS. (int)',
        'as widths':            'Width of aperture slit AS at each position in microns, length of list is always 5. (list(int))',
        'as heights':           'Height of aperture slit AS at each position in microns, length of list is always 5. (list(int))',
        'ens':                  'Position of the energy slit EnS in ??. (float)',
        'ens width':            'Width of energy slit EnS in ??. (float)',
        'e0s':                  'Value of lens E0S in Volt. (float)',
        'pressure multicollection chamber': 'Pressure in the multicollection chamber in torr, 32 characters max. (str)'
    },
    'Detectors': {
        'Detectors':            'Dictionary that contains information for each detector. Detector names are keys to the dictionary and can be Detector1 - Detector5 (Detector7 for N50 Large), LD, FCs, EMBig, TIC. (dict)',
        'exit slit':            'Numerical position of exit slit, see sims.exit_slit_labels. (int)',
        'exit slit heights':    'Height in micron for each exit slit position and each exit slit size; coordinates (size, position) give the actual height set for this detector. (list(list(int)))',
        'exit slit label':      'Label of exit slit position, see sims.exit_slit_labels. (str)',
        'exit slit size':       'Numerical size of exit slit series, see sims.exit_slit_size_labels. (int)',
        'exit slit size label': 'Label of exit slit size series, see sims.exit_slit_size_labels. (str)',
        'exit slit widths':     'Width in micron for each exit slit position and each exit slit size; coordinates (size, position) give the actual width set for this detector. (list(list(int)))',
        'fc background negative':   'Faraday cup background signal measured in negative mode in counts/s (int)',
        'fc background positive':   'Faraday cup background signal measured in positive mode in counts/s (int)',
        'em yield':             'Electron multiplier relative yield in percent. (float)',
        'em background':        'Electron multiplier background signal in counts/s. (int)',
        'em deadtime':          'Electron multiplier deadtime in nanoseconds. (int)',
        'detector':             'Label of selected detector, see sims.detectors. (str)',
    },
    'Presets': {
        'Presets':              'Dictionary containing 2 subdicts: Measure and Presputter. Each subdict contains two subdicts: Lenses and Slits. Each inner subdict contains at least isf filename, preset name, calibration date, selected, and (number of) parameters. In addition, \"parameter\" parameters are stored as name:value pairs. Parameter IDs are also stored in the sims file, but only used in this dictionary if name is not available. (dict)',
        'isf filename':         'Filename of the instrument settings file that has all settings stored. 256 characters max. (str)',
        'preset name':          'Label of this preset, 224 characters max (str)',
        'calibration date':     'Date of last \"Calib\". (datetime object)',
        'selected':             'Whether this preset is active in this experiment. (bool)',
        'parameters':           'Number of parameters stored in this preset. (int)'
    },
    'Image': {
        'Image':                'Stores the image header. (dict)',
        'header size':          'Size of the image header, currently always 84 bytes. (int)',
        'type':                 '? (int)',
        'width':                'Image width in pixels. (int)',
        'height':               'Image height in pixels. (int)',
        'bytes per pixel':      'Number of bytes used to store each data point. 2 (16-bit) or 4 (32-bit). (int)',
        'masses':               'Number of masses stored in the data. (int)',
        'planes':               'Number of \'planes\' (repeated measurements, stacked images, cycles) in the data. (int)',
        'raster':               'Width (or height?) of the image in nanometers. (int)',
        'original filename':    'Filename as stored in the file; 64 characters max (str)',
    }
}

# Run this on import, so that the paths are generated only once
header_info_paths = rkeys(header_info)