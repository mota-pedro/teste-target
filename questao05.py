def inverter_string(string):
    nova_string = ''
    const = 0

    while const < len(string):
        nova_string = nova_string + string[(len(string)-1)-const]
        const = const + 1

    return nova_string

minha_string = input()

print(inverter_string(minha_string))
