def set_label(reason):
    #cause = 0
    natural = ['Lightning']
    accidental = ['Debris Burning', 'Campfire' , 'Equipment Use', 'Children', 'Railroad', 'Smoking',
                  'Powerline', 'Structure', 'Fireworks']
    malicious = ['Arson']
    other = ['Miscellaneous','Missing/Undefined']
    
    if reason in natural:
        cause = 'natural'
    elif reason in accidental:
        cause = 'accident'
    elif reason in malicious:
        cause = 'crime'
    elif reason in other:
        cause = 'other'
    return cause  