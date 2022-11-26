'''
 {
    block_shape (string): [
        width: width (int),
        height: height (int)
        points: points (int,int)[]
    ]
 }

'''

blocks = {
    'square-square': [
        {
            'width': 50,
            'height': 100,
            'origin': (0,0),
        },
        {
            'width': 50,
            'height': 100,
            'origin': (50,0),
        }
    ],
    'vertical-square': [
        {
            'width': 33,
            'height': 100,
            'origin': (0,0),
        },
        {
            'width': 67,
            'height': 100,
            'origin': (33,0),
        }
    ],
    'horizontal-square': [
        {
            'width': 100,
            'height': 33,
            'origin': (0,0),
        },
        {
            'width': 100,
            'height': 67,
            'origin': (0,33),
        }
    ],
    'square-square-horizontal': [
        {
            'width': 50,
            'height': 67,
            'origin': (0,0),
        },
        {
            'width': 50,
            'height': 67,
            'origin': (50,0),
        },
        {
            'width': 100,
            'height': 33,
            'origin': (0,67),
        }
    ],
}