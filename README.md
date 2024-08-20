# Transcrição de Texto para Braille

Este projeto foi desenvolvido como parte de uma cartilha para um projeto da faculdade. Decidi adaptar a cartilha para Braille e, ao pesquisar softwares existentes, percebi que muitos não especificavam se o Braille era para português do Brasil (pt-BR). Além disso, encontrei diferenças nos pontos Braille entre os softwares. 

Para garantir uma transcrição precisa, mesmo sem revisão completa, criei este mapeamento baseado em um abecedário brasileiro de braille encontrado online.

## Funcionalidades

- **Transcrição de letras minúsculas e maiúsculas**: Suporte para letras com acentos e caracteres especiais como cedilha.
- **Suporte a números e símbolos**: Números e alguns operadores matemáticos básicos, bem como pontuação e símbolos especiais, são incluídos.
- **Saída em arquivo**: A transcrição é realizada e salva em um arquivo `.txt` para fácil acesso e revisão.

## Como Usar

1. **Execute o script**:

    Certifique-se de que o arquivo `transcricao.txt` contém o texto que você deseja transcrever. Então, execute o script Python:

    ```bash
    python Braille.py
    ```

2. **Resultado**:

    ```bash
    Texto Original:
    (Aqui será mostrado o texto original)

    Texto em Braille:
    (Aqui será mostrado o texto transcrito em Braille)
    ```

    O texto transcrito em Braille será salvo no arquivo `transcrito.txt`.

## Limitações

Este projeto foi desenvolvido utilizando um abecedário Braille encontrado online. No entanto, **não sou especialista em Braille** e, portanto, pode haver imprecisões na transcrição. Abaixo estão algumas das áreas que precisam de revisão:

- **Maiúsculas**: A forma correta de usar o indicador de maiúsculas precisa ser confirmada.
- **Variações de caracteres**: Não estou totalmente seguro de como e quando utilizar as variações de acentuação e outros modificadores no Braille.
- **Símbolos especiais**: A interpretação e mapeamento de símbolos como operadores matemáticos e pontuação podem não estar corretos.

**Nota:** Recomendo fortemente que este projeto seja revisado por alguém com conhecimento em Braille para corrigir possíveis erros e melhorar a precisão da transcrição.

## Contribuições

Contribuições são bem-vindas! Se você tem experiência em Braille e deseja ajudar a melhorar este projeto, fique à vontade para abrir uma issue ou enviar um pull request.
