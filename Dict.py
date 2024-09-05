dcionario = { 
          "nome": "String",
          "idade": 40,
          "sexo": "feminino",
          "peso": 68.5,
}

print(f"criando com chaves {dcionario}")

# Pode criar diconário vazio dict() ou
# Pde criar com dados dict(variável=valor, variável=valor)
# Atenção com parênteses () chave não tem aspas e usa-se recebe =. Com chaves {} usa-se aspas na variável e recebe é :
# para ADICIONAR é igual - nomeDiconário["nomeNovaChave"]=valor
# para MUDAR JÁ EXISTENTE -  omeDiconário["nomeChave"]= novoValor
# para REMOVER ITEM - nomeChave = nomeDicinário.pop("nomeChave") 
# para SABER, INTEIRAR sobre chaves - for chave/variável in nomeDicionário - print() 

novoDiconario = dict( calça ="linho", blusa ="tricoline", jaqueta ="lã")

print(f"criando com dict {novoDiconario}")