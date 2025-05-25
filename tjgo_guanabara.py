from selenium import webdriver
import time

# Webdrive chrome abrir navegador , caso queira no firefox, basta substituir chorme por firefox
navegador = webdriver.Chrome()
# get e para  url, lembrando deve ter o hhtps:// antes
navegador.get("https://projudi.tjgo.jus.br/ConsultaJurisprudencia")

# Colocar o navegador em tela cheia
navegador.fullscreen_window()

# PASSO A PASSO DE PESQUISA
# 1. Encontrar o campo de pesquisa e guardar o elemento, esse id , texto, são as tags do html
campo_pesquisa_elemento = navegador.find_element("id", "Texto")

# 2. Enviar o texto para o campo de pesquisa, aqui e so exemplo
campo_pesquisa_elemento.send_keys("indenização por erro médico")

time.sleep(2)
# 2 PASSO BOTÃO DE BUSCAR
# 1. Encontrar o botão e guardar o elemento
botao_elemento = navegador.find_element("id", "formLocalizarBotao")

# Abrir o navegador
# 2. Rolar a tela até o elemento botão (usando o elemento guardado)
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", botao_elemento)

time.sleep(1) # Pausa para a rolagem

# 3. Clicar no elemento botão (usando o elemento guardado)
botao_elemento.click()


# 3 PASSO RESULTADOS
# ESSE CODIGO AQUI E PARA BAIXAR OS 10 PRIEMEIROPDF
blocos_de_resultado = navegador.find_elements("class name", "search-result")

if not blocos_de_resultado:
    print("Nenhum bloco de resultado foi encontrado com a classe 'search-result'. Verifique o nome da classe ou se a pesquisa retornou algo.")
else:
    print(f"Foram encontrados {len(blocos_de_resultado)} blocos de resultado.")
    
    # Loop para passar por cada bloco de resultado encontrado
    for indice, bloco_individual in enumerate(blocos_de_resultado):        
        # Dentro de cada 'bloco_individual', tentamos encontrar o link de download
        try:
            # O XPath ".//a[normalize-space()='Baixar Inteiro teor']" procura por um link (<a>)
            # que tenha o texto exato "Baixar Inteiro teor".
            # O "." no início do XPath significa "procure somente dentro deste bloco_individual".
            link_download_pdf = bloco_individual.find_element("xpath", ".//a[normalize-space()='Baixar Inteiro teor']")
            
            # Rolar a tela até o elemento link_download_pdf para garantir que esteja visível
            navegador.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", link_download_pdf)
            time.sleep(1) # Pausa para a rolagem

            link_download_pdf.click() # Clica no link para iniciar o download
        
            # Pausa para dar tempo ao download de iniciar.
            time.sleep(7) 

        except Exception as e:
            print(f"  ERRO: Não foi possível encontrar ou clicar no link 'Baixar Inteiro teor' no bloco {indice + 1}.")

        



# #localizar o campo de pesquisa
# campo_pesquisa = navegador.find_element("xpath", "//input[@placeholder='Utilize aspas duplas para realizar uma busca exata. Exemplo: \"indenização por erro médico\".']")
# #digitar o termo de pesquisa
# campo_pesquisa.send_keys("indenização por erro médico")
# #aguardar um pouco para ver o que acontece
# time.sleep(5)
# #localizar o botão de pesquisa
# botao_pesquisa = navegador.find_element("xpath", "//button[@class='btn btn-primary']")
# #clicar no botão de pesquisa
# botao_pesquisa.click()
# #aguardar o carregamento da página de resultados
# time.sleep(5)
# #localizar os resultados
# resultados = navegador.find_elements("xpath", "//table[@class='table table-striped table-bordered table-hover']")
# #imprimir os resultados
# for resultado in resultados:
#     print(resultado.text)
# #fechar o navegador
# navegador.quit()
