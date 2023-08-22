**Ilustração da Estrutura de Arquivos em Árvore**

```shell
cd .\Programacao_Orientada_a_Objetos\Projeto_Final\
python -Bc "for p in __import__('pathlib').Path('.').rglob('*.py[co]') : p.unlink()"
python -Bc "for p in __import__('pathlib').Path('.').rglob('__pycache__') : p.rmdir()"
tree /F
```