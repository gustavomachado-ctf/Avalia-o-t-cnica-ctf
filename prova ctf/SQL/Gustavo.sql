create table produto (
    id_produto INT,
    cod_barras INT,
    data_cadastro DATE);
    
create table fabricante (
    id_fabricante INT,
    nome_fabricante varchar2(50),
    cidade varchar2(20),
    estado varchar2(2),
    data_cadastro DATE,
    data_atualizacao DATE);
    
create table produto_info (
    id_INT,
    cod_interno INT,
    dados_gerais INT,
    data_atualizacao DATE,
    data_cadastro DATE,
    descricao varchar2(60),
    id_fabricante INT,
    id_origem INT,
    id_produto INT);
    
create table origem (
    id_origem INT,
    nome_origem varchar2(50),
    data_cadastro DATE,
    data_atualizacao DATE,
    preferencia INT);

"""
A
"""
SELECT cod_barras
FROM produtos
WHERE data_cadastro >= CURRENT_DATE - INTERVAL '10 days'
  AND data_cadastro <= CURRENT_DATE;

"""
B
"""
SELECT nome_origem
FROM origem
WHERE data_cadastro OR data_atualizacao = 03/2020

"""
C
"""
UPDATE produto
SET nome_fabricante = 'JOAO'
WHERE nome_origem = 'DISTRIBUIDORA TESTE' AND nome_fabricante = 'MARIA';

"""
D
"""
SELECT cod_barras, descricao, nome_fabricante, cod_interno
FROM produto
INNER JOIN produto_info
INNER JOIN fabricante 
GROUP BY cod_barras ORDER BY preferencia ASC  

