# Non Exact Match

**Conteúdo da Disciplina**: Programação Dinamica<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 15/0122837  |  Davi Alves Bezerra |

## Sobre 
![image](https://user-images.githubusercontent.com/34287081/216735801-ec20d696-bf54-45f6-aa6a-e60c104e6180.png)

O objetivo deste projeto é comparar formas de buscar um texto em outro texto que pode estar errado. Além da tarefa de encontrar a string alvo temos que comparar com a string real para mensurar a sua "similaridade". Foi usado Levenshtein distance (LD) nas comparações e a string mais longa em comum (LCS) para busca do texto. LCS como longest common substring é só uma adaptação para considerar a maior substring em comum ao invés da subsequencia. 

Na comparação também é apresentado o uso de ngram para criar uma nova sequencia a partir do texto em que se deseja buscar. Esse ngram está setado para sempre ter como grau dos "ngrams" o tamanho do texto a ser procurado. 

E por fim há um "in" do python, que é basicamente o algortimo de Boyer-Moore simplificado. Ele terá o retorno True sempre que encontrar aquela palavra exata no texto, caso contrario retornara False. Poderiamos testar também com o "find" do python, mas é limitado a um padrão exato. Ou ainda poderiamos usando regex para encontrar o padrão, porém textos comuns, semanticamente falando não vão seguir um padrão a nivel de ser detectado.

## Screenshots
### Texto alvo x texto da busca
Escolha um texto que deseja procurar dentro de outro, onde você não tem certeza se está correto.
![image](https://user-images.githubusercontent.com/34287081/216736044-0d7fd8aa-809b-4fed-80e6-8ad39b18f6cc.png)

### Métricas da busca
Nas métricas da busca há o texto mais proximo encontrado. Esse texto segue da distancia para o texto buscado.
![image](https://user-images.githubusercontent.com/34287081/216736108-8b057047-3569-4b6a-800c-004c7b0b4739.png)


## Instalação 
**Linguagem**: Python 3.8.13<br>
**Framework**: streamlit<br>

## Uso 
Instale todas as dependencias a partir do requirements
```
pip install -r requirements.txt
```

Por fim basta executar o comando do streamlit
```
streamlit run app.py
```




