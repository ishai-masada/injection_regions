chord_position = input('enter the desired chord position: ')
span_position = input('enter the desired chord position: ')
ps_ss = input('choose either pressure side or suction side (ps/ss): ')

points = []
if ps_ss == 'pressure side':
    for curve in lower_curves:
        points.append(curve[chord_position]) 

else:
    pass
