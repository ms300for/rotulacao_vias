# rotulacao_vias
Programa criado para rotulação de caracteristicas de vias laterais de rodovias.

O programa "rotulacao_lateral" refere-se a lateral da pista. O mesmo separa as imagens rotuladas e cria um arquivo contendo os rótulos da região lateral relacionados a classificação do ICM: rótulos qualitativos para condição de vegetação, drenagem e sinalização.

O programa salva os rótulos em um arquivo CSV, onde cada linha possui 5 informações:

nome do arquivo; rótulo sobre vegetação; rótulo sobre sinalização; rótulo sobre equipamentos de drenagem; informação da existência de placas.

Os rótulos são valores numéricos, determinados como:

- 0: classificação "ruim"
- 1: classificação "regular"
- 2: classificação "Bom"
- 3: classificação "Bom" (válido apenas para drenagem, representa a não existência de dispositivos)

Quanto a informação sobre placas:

- 0: Inexistência de placas na imagem
- 1: Existência de placas na imagem

# Rotulação pavimentos
Programa criado para rotulação de defeitos em pavimentos asfálticos.

O programa possui 5 rótulos diferentes, sendo eles:

- Buracos:  referente à imagens contendo um ou mais buracos
- Remendos: referente à imagens contendo um ou mais remendos
- Trincas:  referente à imagens contendo um ou mais regiões trincadas
- Limpa:    referente à imagens cujo pavimento não apresenta algum tipo de dano
- Multidefeitos: referente à imagens que apresentem mais de um tipo de defeito (ex: um buraco e remendos)
- Outros: imagens que possam não ser classificadas nas categorias apresentadas anteriormentes, ou que necessitem de uma análise especial

As imagens coletadas devem, prioritariamente, conter defeitos isolados por tipo, evitando-se assim mais de um tipo de defeito na mesma imagem.
