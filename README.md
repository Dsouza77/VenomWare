# ☣️ VenomWare ☣️

"Ransoware", script para criptografar arquivos.

---

## 📝 Descrição

Este projeto foi desenvolvido com o objetivo de criar um script "base" para o desenvolvimento
de Ransowares com fins não maliciosos. 

🚨OBS: Projeto feito para fins de estudos, trabalhos acadêmicos e projetos pessoais.
Não me responsabilizo pelo mal uso do projeto!🚨

## 🗃️ Funcionalidades:

✔️ Percorrer a pasta indicada contando subdiretórios;
✔️ Criptografar todos arquivos encontrados;
✔️ Opção de exceção de arquivo (possibilidade de não processar arquivos como: .png, .zip...com a escolha do usuário);
✔️ Relatório de arquivos criptografados no terminal;
✔️ Descriptografar todos arquivos percorridos em pastas que foi processada.

## 🗃️ Exceções/Futuras melhorias:

❌Incompatibilidade com arquivos grandes:
    A biblioteca "cryptography" ultiliza a tecnologia Fernet para criptografar seus arquivos. No entanto,
    todo processo de criptografia é feito direto na memória ram do dispositivo, com isso, fica negligente
    o uso da tecnologia em arquivos grandes.
    ☑️Solução: Irei prover logo mais uma atualização para que verifique durante o processamento, arquivos maiores
    de no mínimo 5gb e criptografe o mesmo em partes (blocos) para compatibilidade e melhor otimização do código.
    

---

## 💻 Tecnologias e Bibliotecas

- **Python 3.10+**
- Biblioteca `cryptography` – usada para criptografia
- Biblioteca `os` – usada para manipulações de arquivos
- Biblioteca `time` – usada para gerenciar tempo de execução (não obrigatória)

---

## 📄 Licença

Projeto desenvolvido para fins acadêmicos/pessoal, proveito aberto para relações de estudos.
