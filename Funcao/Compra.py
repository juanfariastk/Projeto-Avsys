#Compra de fato a cadeira escolhida 
def comprar_cadeira(aeroporto, vendas, nome, assento_escolhido, voo_escolhido):
    codigo_voo = aeroporto.gerar_codigo(voo_escolhido)
    cidades_voo = aeroporto.dados_aviao_id(voo_escolhido)
    aeroporto.comprar_cadeira(voo_escolhido, assento_escolhido)
    id_compra_atual = vendas.comprar(nome, assento_escolhido, cidades_voo[1], cidades_voo[2], codigo_voo, voo_escolhido)
    vendas.criar_recibo(id_compra_atual)