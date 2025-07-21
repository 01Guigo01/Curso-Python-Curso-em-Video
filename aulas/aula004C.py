import emoji

# Usamos a função emojize() para converter o código :earth_americas: no emoji real.
# O segundo argumento, language='alias', garante que ele reconheça os códigos mais comuns.
print(emoji.emojize("Hello World :earth_americas:", language='alias'))