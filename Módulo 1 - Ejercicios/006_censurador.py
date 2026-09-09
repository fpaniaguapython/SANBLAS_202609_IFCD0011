'''
Solicitar al usuario un post para una red social
Censurar las palabras malsonantes del post
- gilipollas - *
- brócoli - *
- idiota - *
'''
post = input('Introduce el post:')
PALABRA_PROHIBIDA_1 = 'gilipollas'
PALABRA_PROHIBIDA_2 = 'brócoli'
PALABRA_PROHIBIDA_3 = 'idiota'
MARCA_CENSURA = '[***]'

# Alterantiva 1
post_censurado = post.replace(PALABRA_PROHIBIDA_1, MARCA_CENSURA)
post_censurado = post_censurado.replace(PALABRA_PROHIBIDA_2, MARCA_CENSURA)
post_censurado = post_censurado.replace(PALABRA_PROHIBIDA_3, MARCA_CENSURA)

# Alternativa 2 (METHOD CHAINING)
post_censurado = post.replace(
    PALABRA_PROHIBIDA_1, MARCA_CENSURA).replace(
        PALABRA_PROHIBIDA_2, MARCA_CENSURA).replace(
            PALABRA_PROHIBIDA_3, MARCA_CENSURA)

print(post_censurado)