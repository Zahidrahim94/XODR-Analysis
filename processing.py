import xml.etree.ElementTree as ET

def count_objects_and_signals(xodr_file):
    # Load the XODR file
    with open(xodr_file, 'r') as file:
        xodr_data = file.read()

    # Remove invalid characters from the XODR file
    xodr_data = ''.join(c for c in xodr_data if c <= '\uFFFF')

    # Parse the XODR data
    root = ET.fromstring(xodr_data)

    # Count objects by type
    object_counts = {}
    for obj in root.findall('.//objects/object'):
        obj_type = obj.get('type')
        if obj_type in object_counts:
            object_counts[obj_type] += 1
        else:
            object_counts[obj_type] = 1

    # Count signals by type and sub-type
    signal_counts = {}
    for signal in root.findall('.//signals/signal'):
        signal_type = signal.get('type')
        signal_subtype = signal.get('subtype')
        if signal_type in signal_counts:
            if signal_subtype in signal_counts[signal_type]:
                signal_counts[signal_type][signal_subtype] += 1
            else:
                signal_counts[signal_type][signal_subtype] = 1
        else:
            signal_counts[signal_type] = {signal_subtype: 1}

    return object_counts, signal_counts
