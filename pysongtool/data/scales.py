scales_list = {
    'major': {
        'notes': [2, 4, 5, 7, 9, 11],
        'chords': ['maj', 'min', 'min', 'maj', 'maj', 'min', 'dim'],

        'modes': {
            1: {
                'name': 'Ionian',
                'aliases': ['Major']
            },

            2: {
                'name': 'Dorian',
                'aliases': []
            },

            3: {
                'name': 'Phrygian',
                'aliases': []
            },

            4: {
                'name': 'Lydian',
                'aliases': []
            },

            5: {
                'name': 'Mixolydian',
                'aliases': []
            },

            6: {
                'name': 'Aeolian',
                'aliases': ['Natural Minor', 'Minor']
            },

            7: {
                'name': 'Locrian',
                'aliases': []
            }
        }
    },

    'minor': {
        'notes': [2, 3, 5, 7, 8, 10],
        'chords': ['min', 'dim', 'maj', 'min', 'min', 'maj', 'maj'],

        'modes': {}
    },

    'harmonic minor': {
        'notes': [2, 3, 5, 7, 8, 11],
        'chords': ['min', 'dim', 'aug', 'min', 'maj', 'maj', 'dim'],

        'modes': {
            1: {
                'name': 'Harmonic Minor',
                'aliases': []
            },

            2: {
                'name': 'Locrian Natural 6',
                'aliases': []
            },

            3: {
                'name': 'Phrygian Dominant',
                'aliases': [
                    'Spanish Gypsy',
                    'Freygish'
                ]
            },

            4: {
                'name': 'Dorian #4',
                'aliases': []
            },

            5: {
                'name': 'Mixolydian b2',
                'aliases': []
            },

            6: {
                'name': 'Lydian #2',
                'aliases': []
            },

            7: {
                'name': 'Super Locrian bb7',
                'aliases': []
            }
        }
    },

    'melodic minor': {
        'notes': [2, 3, 5, 7, 9, 11],
        'chords': ['min', 'min', 'aug', 'maj', 'maj', 'dim', 'dim'],

        'modes': {
            1: {
                'name': 'Melodic Minor',
                'aliases': ['Jazz Minor']
            },

            2: {
                'name': 'Dorian b2',
                'aliases': ['Phrygian Natural 6']
            },

            3: {
                'name': 'Lydian Augmented',
                'aliases': []
            },

            4: {
                'name': 'Lydian Dominant',
                'aliases': ['Acoustic Scale']
            },

            5: {
                'name': 'Mixolydian b6',
                'aliases': []
            },

            6: {
                'name': 'Locrian Natural 2',
                'aliases': ['Half-Diminished Scale']
            },

            7: {
                'name': 'Super Locrian',
                'aliases': ['Altered Scale']
            }
        }
    }
}