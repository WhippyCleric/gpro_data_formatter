import sys

from car_setup import CarSetup
from practice_lap import PracticeLap
from qualy_data import QualyData
from racing_lap import RacingLap


def _extract_pertinent_lines(source, key_to_end):
    current_key = None
    key_to_data = {}
    lines = source.split('\n')

    for line in lines:
        processed = False
        while not processed:
            if current_key:
                if line == key_to_end[current_key]:
                    current_key = None
                else:
                    key_to_data[current_key].append(line)
                    processed = True
            else:
                for key in list(key_to_end):
                    if line.startswith(key):
                        current_key = key
                        key_to_data[current_key] = []
                        break
                processed = True
    return key_to_data


def _process_practice_data(lines):
    laps = []
    for line in lines:
        split_by_tab = line.split('\t')
        if len(split_by_tab) == 12 and split_by_tab[0].isnumeric():
            laps.append(PracticeLap(split_by_tab))
    return laps


def _process_qualy(setups_used, risks_used, lap_times):
    q1_setup = CarSetup(setups_used[1].split('\t')[1:8])
    q1_time = lap_times[1].split('\t')[0].split(' ')[0]
    q1_risk = risks_used[1].split('\t')[0]
    q1 = QualyData(q1_time, q1_risk, q1_setup)
    q2_setup = CarSetup(setups_used[2].split('\t')[1:8])
    q2_time = lap_times[1].split('\t')[1].split(' ')[0]
    q2_risk = risks_used[1].split('\t')[1].strip()
    q2 = QualyData(q2_time, q2_risk, q2_setup)
    return q1, q2


def _process_race_laps(laps):
    racing_laps = []
    for lap in laps:
        racing_laps.append(RacingLap(lap.split('\t')))
    return racing_laps


if __name__ == "__main__":
    args = sys.argv[1:]
    source_filename = args[0]
    source_file = open(source_filename, 'r')
    source_text = source_file.read()
    key_to_end_marker = {
        'Practice laps data': '',
        'Setups used': '',
        'Risks used': '',
        'Lap times': '',
        'Car wear & lap information': 'Lap	Lap time	Pos	Tyres	Weather	Temp	Hum	Events',
        'Lap	Lap time	Pos': ''
    }
    data = _extract_pertinent_lines(source_text, key_to_end_marker)
    practice_laps = _process_practice_data(data['Practice laps data'])
    qualy_data_1, qualy_data_2 = _process_qualy(data['Setups used'],
                                                data['Risks used'],
                                                data['Lap times'])
    race_laps = _process_race_laps(data['Lap	Lap time	Pos'])
    for x in race_laps:
        print(str(x))
