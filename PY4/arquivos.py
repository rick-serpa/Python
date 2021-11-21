#conteudo = 'Conteudo vindo de outra forma'
#conteudo += '\npara escrever em mais linhas'
#arq = open('arquivo.txt','w')
#arq.write('Primeira linha')
#arq.write('\nSegunda linha')
#arq.writelines(conteudo)
#arq.close()

#arquivo = open('arquivo.txt','r')
#for linha in arquivo:
#    print(linha.rstrip())
#arquivo.close()

#arquivo = open('teste.txt','r')
#for x in arquivo:
#    print(x)
#arquivo.close

def listar(pItens):
    if ( len(pItens) == 0):
        return 'Não há itens cadastrados.'
    gravaLogDados('Listou os itens')
    return pItens
    
def cadastrar(pItem,pItens):
    if(pItem in pItens):
        return pItem + 'Já esta cadastrado'
    pItens.append(pItem)
    gravaLogDados('Cadastrou' + pItem + '-')
    return(pItem + 'Cadastrado com sucesso!')

def excluir(pItem,pItens):
    if(pItem in pItens):
        pItens.remove(pItem)
        gravaLogDados('Excluiu' + pItem + '-')
        return pItem + 'Excluido com sucesso.'
    return pItem + 'Não esta cadastrado'

def excluir2(pItem,pItens):
    if ( len(pItens) > 0 ):
        if (pItem in pItens):
            for item in range(0,len(pItens)):
                if( pItens[item] == pItem):
                  pItens.pop(item)
                return pItem + 'Excluido com sucesso.'
        return pItem + 'Não está cadastrado'
    return 'Lista vazia'

def alterar(pItem, pItens):
    if( pItem in pItens):
        for x in range(0,len(pItens)):
            if( pItens[x] == pItem):
                novo = input('Informe o novo nome do item: ')
                if ( novo in pItens):
                    return novo + 'Já está cadastrado'
                pItens[x] = novo
                gravaLogDados('Alterou' + pItem + 'para ' + novo + '-')
                return pItem + ' alterado para ' + novo + 'com sucesso.'
    return pItem + 'não está cadastrado'

def gravaLogDados(pMsg, pTipo = 1):
    if (pTipo == 1):
        arq = open('log.txt','a')
        arq.write(pMsg + '\n')
        arq.close()
    else:
        arq = open('dados.txt','w')
        arq.write(pMsg)
        arq.close()

def lerArquivo(pTipo = 1):
    if(pTipo == 1):
        arq = open('log.txt','r')
        for linha in arq:
            print(linha.rstrip)
        arq.close()
   