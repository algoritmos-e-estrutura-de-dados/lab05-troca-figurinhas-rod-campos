def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
    if len(figurinhas_do_joao) >= len(figurinhas_da_maria):
        ma = figurinhas_do_joao
        me = figurinhas_da_maria
    else:
        me = figurinhas_do_joao
        ma = figurinhas_da_maria

    ma_copy = ma.copy()
    me_copy = me.copy()
    for i in range(len(me)):
        for j in range(len(ma)):

            if ma[j] == me[i]:
                for k in range(len(ma_copy)):

                    if int(me_copy[k]) == int(ma[j]):
                        me_copy.pop(k)
                        if len(ma_copy) == 0:
                            print(0)
                        else:
                            print(len(me_copy))
                        break
            elif ma[j] is not me[i]:
                print(len(me_copy))
                break


if _name_ == '_main_':

    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_do_joao = input().split(' ')


    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao)
