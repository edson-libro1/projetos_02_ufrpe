cadastro = {"02443": {"nome": "paula", "idade":18,"telefone": "99999999"}}

cadastro["3003"]={"nome": "daniel", "idade": "15", "telefone": "30033030"}
for cpf,dados in cadastro.items():
    print(f"{cpf} - {dados["nome"]}, {dados["idade"]}, {dados["telefone"]} ")