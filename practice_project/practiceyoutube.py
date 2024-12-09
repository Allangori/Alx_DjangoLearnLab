weight = float(input('Weight:'))
weight_type = input('(K)g or (L)bs:')

if weight_type == 'k' or 'K':
    new_weight_in_Lbs = (weight * 2.20462)
    print('Weight in Lbs: ' + str(new_weight_in_Lbs))
elif weight_type =='l' or 'L':
    new_weight_in_Kgs = (weight/2.20462)
    print('Weight in Kgs: ' + str(new_weight_in_Kgs))