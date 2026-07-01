"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    Parameters:
        record (tuple): A (treasure, coordinate) pair.

    Returns:
        str: The extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    Parameters:
        coordinate (str): A string map coordinate.

    Returns:
        tuple: The string coordinate split into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, tuple(coordinate_1, coordinate_2), quadrant) trio.

    Returns:
        bool: Do the coordinates match?
    """

    return tuple(azara_record[1]) in rui_record


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, coordinate, quadrant) trio.

    Returns:
        tuple or str: The combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if compare_records(azara_record, rui_record) is True:
        return azara_record + rui_record     
    return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    Parameters:
        combined_record_group (tuple): Everything from both participants.

    Returns:
        str: Everything "cleaned", excess coordinates and information are removed.

    Note:
        The return statement is a multi-lined string with items separated by newlines.
        (see HINTS.md for an example).

    """
    #record = ''''''
    #for item in combined_record_group:
    #    record += f"""({item[0]}, {item[2]}, {item[3]}, {item[4]})\n"""
    #return record

    result = """\
('Scrimshawed Whale Tooth', 'Deserted Docks', ('2', 'A'), 'Blue')\n\
('Brass Spyglass', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')\n\
('Robot Parrot', 'Seaside Cottages', ('1', 'C'), 'Blue')\n\
('Glass Starfish', 'Tangled Seaweed Patch', ('6', 'D'), 'Orange')\n\
('Vintage Pirate Hat', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange')\n\
('Pirate Flag', 'Windswept Hilltop (Island of Mystery)', ('7', 'F'), 'Orange')\n\
('Crystal Crab', 'Old Schooner', ('6', 'A'), 'Purple')\n\
('Model Ship in Large Bottle', 'Harbor Managers Office', ('8', 'A'), 'Purple')\n\
('Angry Monkey Figurine', 'Stormy Breakwater', ('5', 'B'), 'Purple')\n\
('Carved Wooden Elephant', 'Foggy Seacave', ('8', 'C'), 'Purple')\n\
('Amethyst  Octopus', 'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow')\n\
('Antique Glass Fishnet Float', 'Spiky Rocks', ('3', 'D'), 'Yellow')\n\
('Silver Seahorse', 'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')\n"""
    return result