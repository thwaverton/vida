from selenium import webdriver
import time

navegador = webdriver.Chrome()
navegador.get("https://projudi.tjgo.jus.br/ConsultaJurisprudencia")
navegador.fullscreen_window()

campo_pesquisa_elemento = navegador.find_element("id", "Texto")
campo_pesquisa_elemento.send_keys("indenização por erro médico")
time.sleep(2)

botao_elemento = navegador.find_element("id", "formLocalizarBotao")
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", botao_elemento)
time.sleep(1)
botao_elemento.click()
time.sleep(3)

blocos_de_resultado = navegador.find_elements("class name", "search-result")

if blocos_de_resultado:
    print(f"\n--- {len(blocos_de_resultado)} RESULTADOS ENCONTRADOS ")
    for indice, bloco_individual in enumerate(blocos_de_resultado):
        try:
            navegador.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'auto'});", bloco_individual)
            time.sleep(0.5)
            
            texto_do_bloco = bloco_individual.text
            
            print(f"\n--- TEXTO DO RESULTADO {indice + 1} ")
            print(texto_do_bloco)
            print("="*30)

        except Exception as e:
            print(f"ERRO ao processar o texto do bloco {indice + 1}. Erro: {e}")
        time.sleep(0.2)
else:
    print(f"Não tem resultado para essa essa pesquisa ")

time.sleep(3)
navegador.quit()