frutas = ['banana', 'maçã', 'manga', 'uva'] 
vegetais = ['alface', 'espinafre', 'couve', 'brócolis']
for i, fruta in zip(range(1,len(frutas)+1), frutas):
    print('{}ª combinação: '.format(i))
    for vegetal in vegetais:
        print('{} e {}'.format(fruta, vegetal))