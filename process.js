const USER = 'docbrasil';
const PASSWD = '@Doc-Brasil1';

const payload = {
  // numEmp
  codigoEmpresa: 25, // int

  // datAdm
  dataAdmissao: null, // string(date)

  // sitAfa
  codigoSituacao: 1, // int

  // codCar
  codigoCargo: null, // string

  // codEsc
  codigoEscala: 1, // int

  // codFil
  codigoFilial: 1, // int

  // indAdm
  indicativoAdmissao: 1, // int
  // 1 - Normal
  // 2 - Decorrente de Ação Fiscal (celetista)
  // 3 - Decorrente de Decisão Judicial
  // 4 - Tomou posse mas não entrou exercício (estatutário)

  // numLoc
  codigoLocal: '01', // string

  // numCtp
  numCarteiraTrabalho: null, // int

  // pagSin
  indicacaoRecolhimentoContribuicaoSindicato: null, // string
  // S - Já recolheu ao sindicato no ano
  // P - Colaborador admitido em Dezembro, será descontado na primeira competência do Próximo Ano (*)
  // N - Ainda não recolheu
  // M - Profissional liberal que recolhe para sua classe profissional
  // (*) A opção 'P' só estará disponível quando a data de admissão for na competência Dezembro.

  // codFicFmd
  geracaoFichaMedica: 'AUTO', // string

  // escVtr
  escalaValeTransporte: 9, // int

  // cateSo
  categoriaeSocial: 101, // int
  // 101 - Empregado - Geral
  // 102 - Empregado - Trabalhador Rural por Pequeno Prazo da Lei 11.718/2008
  // 103 - Empregado - Aprendiz
  // 104 - Empregado - Doméstico
  // 105 - Empregado - contrato a termo firmado nos termos da Lei 9601/98
  // 106 - Empregado - contrato por prazo determinado nos termos da Lei 6019/74
  // 107 - Trabalhador não vinculado ao RGPS com direito ao FGTS
  // 201 - Trabalhador Avulso - Portuário
  // 202 - Trabalhador Avulso - Não Portuário (Informação do Sindicato)
  // 203 - Trabalhador Avulso - Não Portuário (Informação do Contratante)
  // 301 - Servidor Público - Titular de Cargo Efetivo
  // 302 - Servidor Público - Ocupante de Cargo exclusivo em comissão
  // 303 - Servidor Público - Exercente de Mandato Eletivo
  // 304 - Servidor Público - Agente Público
  // 305 - Servidor Público vinculado a RPPS indicado para conselho ou órgão representativo, na condição de representante do governo, órgão ou entidade ad administração pública.
  // 401 - Dirigente Sindical - Em relação a Remuneração Recebida no Sindicato.
  // 701 - Contrib. Individual - Autônomo contratado por Empresas em geral
  // 702 - Contrib. Individual - Autônomo contratado por Contrib. Individual, por pessoa física em geral, ou por missão diplomática e repartição consular de carreira estrangeiras
  // 703 - Contrib. Individual - Autônomo contratado por Entidade Beneficente de Assistência Social isenta da cota patronal
  // 704 - Excluído.
  // 711 - Contrib. Individual - Transportador autônomo contratado por Empresas em geral
  // 712 - Contrib. Individual - Transportador autônomo contratado por Contrib. Individual, por pessoa física em geral, ou por missão diplomática e repartição consular de carreira estrangeiras
  // 713 - Contrib. Individual - Transportador autônomo contratado por Entidade Beneficente de Assistência Social isenta da cota patronal
  // 721 - Contrib. Individual - Diretor não empregado com FGTS
  // 722 - Contrib. Individual - Diretor não empregado sem FGTS
  // 731 - Contrib. Individual - Cooperado que presta serviços a empresa por intermédio de cooperativa de trabalho
  // 732 - Contrib. Individual - Cooperado que presta serviços a Entidade Beneficente de Assistência Social isenta da cota patronal ou para pessoa física
  // 733 - Contrib. Individual - Cooperado eleito para direção da Cooperativa
  // 734 - Contrib. Individual - Transportador Cooperado que presta serviços a empresa por intermédio de cooperativa de trabalho
  // 735 - Contrib. Individual - Transportador Cooperado que presta serviços a Entidade Beneficente de Assistência Social isenta da cota patronal ou para pessoa física
  // 736 - Contrib. Individual - Transportador Cooperado eleito para direção da Cooperativa.
  // 741 - Contrib. Individual - Cooperado filiado a cooperativa de produção.
  // 751 - Contrib. Individual - Micro Empreendedor Individual, quando contratado por PJ
  // 781 - Ministro de confissão religiosa ou membro de vida consagrada, de congregação ou de ordem religiosa
  // 901 - Estagiário
  // 902 - Médico residente ou residente em área profissional da saúde
  // 903 - Bolsista
  // 904 - Participante de curso de formação, com etapa de concurso público, sem vínculo de emprego/estatutário
  // 905 - [Válida até 09/05/2021] Atleta não profissional em formação que receba bolsa
  // 9995 - Beneficiário Ente Público
  // 9996 - Beneficiário Ente Público - Somente Cadastro Benefício
  // 9997 - Demitido com data anterior à sucessão (categoria exclusiva Senior)
  // 9999 - Não se aplica

  // tipOpe
  tipoOperacao: 'I', // string
  // I - Inclusão
  // A - Alteração
  // E - Exclusão

  // codVinHvi
  codigoVinculo: null, // int

  // admeSo
  admissaoeSocial: null, // int
  // 1 - Admissão
  // 2 - Transferência de empresa do mesmo grupo econômico
  // 3 - Transferência de empresa consorciada ou de consórcio
  // 4 - Transferência por motivo de sucessão, incorporação, cisão ou fusão
  // 9 - Trabalhador Cedido (específico Senior)

  // serCtp
  serieCarteiraTrabalho: null, // int

  // numCad
  numeroCadastro: null, // int

  // apuPonApu
  tipoApuracao: 1, // int
  // 1 - Normal
  // 2 - Dispensado do Ponto
  // 3 - Somente Refeitório
  // 4 - Dispensado do Ponto - Desconsidera Todas Marcações
  // 5 - Sem Controle de Ponto e Refeitório
  // 6 - Dispensado do Ponto - Desconsidera Marcações de Ponto

  // codMotHca
  codigoMotivoAlteracaoCargo: 1, // int

  // codTmaHes
  codigoTurmaEscala: 1, // int

  // tipAdmHfi
  tipoAdmissaoFilial: null, // int
  // 1 - Primeiro Emprego
  // 2 - Reemprego
  // 3 - Transferência com Ônus
  // 4 - Transferência sem Ônus
  // 5 - Incorporação / Fusão / Cisão / Outros
  // 6 - Reintegração
  // 7 - Recondução (Servidor Público)
  // 8 - Reversão / Readaptação (Servidor Público)

  // digCar
  digitoVerificadorCarteiraTrabalho: null, // int

  // fimEvt
  dataFinalEscalaValeTransporte: null, // string(date)

  // nomFun
  nomeFuncionario: null, // string

  // segDes
  seguroDesemprego: null, // int

  // dexCtp
  dataExpedicaoCarteiraTrabalho: null, // string(date)

  // modPag
  modoPagamento: null, // string
  // C - Em cheque
  // R - Relação bancária
  // D - Em dinheiro
  // O - Ordem de Pagamento
  // P - Pix

  // ponEmb
  codigoPontoEmbarque: 0, // int

  // apeFun
  apelidoColaborador: null, // string

  // codDSiApu
  codigoDefinicaoSituacao: null, // int

  // codMotHsa
  codigoMotivoAlteracao: null, // int

  // estCtp
  ufCarteiraTrabalho: null, // string

  // tipCon
  tipoContrato: null, // int

  // codSinHsi
  codigoSindicato: null, // int

  // tipSalHsa
  tipoSalarioColaborador: null, // int

  // numCpf
  cpfColaborador: null, // string

  // tipSex
  sexoColaborador: null, // string

  // socSinHsi
  sindicalizado: null, // string

  // codEstHsa
  codigoEstruturaCargo: null, // int

  // numPis
  numeroPis: null, // int

  // tpcPix
  tipoChavePix: null, // string
  // 01 - Telefone
  // 02 - E-mail
  // 03 - CPF/CNPJ
  // 04 - Chave Aleatória
  // 05 - Conta Bancária

  // estCiv
  estadoCivil: null, // int
  // 1 - Solteiro
  // 2 - Casado
  // 3 - Divorciado
  // 4 - Viúvo
  // 5 - Concubinato
  // 6 - Separado
  // 9 - Outros

  // possBHHsi
  possuiBancoHoras: 'N', // string

  // dcdPis
  dataCadastroPisPasep: null, // string(date)

  // chvPix
  chavePix: null, // string

  // conBan
  contaBancaria: null, // int

  // graIns
  grauDeInstrucao: null, // int
  // 1 - Analfabeto
  // 2 - 4ª Série Incompleta
  // 3 - 4ª Série Completa
  // 4 - 5ª a 8ª Série Incompleta
  // 5 - 1º Grau Completo (1ª a 8ª Série)
  // 6 - 2º Grau Incompleto
  // 7 - 2º Grau Completo
  // 8 - Superior Incompleto
  // 9 - Superior Completo
  // 10 - Pós-Graduação
  // 11 - Mestrado
  // 12 - Doutorado
  // 13 - Ph.D.

  // tipOpc
  optanteFGTS: null, // string
  // S - Para optante
  // N - Para não optante

  // digBan
  digBan: null, // string

  // datNas
  dataNascimento: null, // string(date)

  // valSalHsa
  valorSalario: null, // double
  // Mask: #####,##

  // datOpc
  dataOpcaoFGTS: null, // string(date)

  // perPag
  periodoPagamento: null, // string
  // M - Mensal
  // S - Semanal
  // Q - Quinzenal

  // cplSalHsa
  complementoSalario: null, // double
  // Mask: #####,##

  // conFgt
  numeroContaFGTS: null, // int

  // tipApo
  tipoAposentadoria: 0, // int
  // 1 - Tempo Serviço
  // 2 - Tempo Serviço Proporcional
  // 3 - Idade
  // 4 - Invalidez
  // 5 - Invalidez Acidente Trabalho
  // 6 - Invalidez Doença Profissional
  // 7 - Compulsória
  // 8 - Especial

  // codNac
  codigoNacionalidade: 10, // int
  // Padrão para Brasil: 10

  // perJur
  percentualJurosFGTS: 3, // int
  // Informar percentual de juros do FGTS.
  // Este dado será utilizado quando a empresa deseja acompanhar
  // o saldo do FGTS do colaborador ou para cálculos em atraso,
  // onde os coeficientes são diferenciados para percentual de juros
  // Para optantes após 1971 a informação válida é 3,
  // se a opção for anterior poderá ou não ser 6,
  // dependendo de ter sido retroativa após 1971.

  // recAdi
  recebeAdiantamentoSalarial: null, // string
  // S - Sim
  // N - Não

  // rec13S
  recebe13Salario: null, // string
  // S - Sim
  // N - Não

  // lisRai
  constaRais: 'N', // string
  // S - Quando deve ser informado na Rais
  // N - Para não constar da Rais

  // codCha
  numeroCartaoPontoQuadroChapeira: null, // string

  // manCgcAfa
  manCgcAfa: '', // string

  // defFis
  pessoaComDeficiencia: null, // string
  // S - Sim
  // N - Não

  // manRemAfa
  manRemAfa: null, // string

  // benRea
  colaboradorReabilitado: null, // string
  // S - Sim
  // N - Não

  // cotDef
  cotaPessoaDeficiencia: null, // string
  // S - Sim
  // N - Não

  // racCor
  codigoRacaEtnia: null, // string

  // catSef
  categoriaSEFIP: null, // int
  // 01 - Empregado;
  // 02 - Trabalhador avulso;
  // 03 - Trabalhador não vinculado ao RGPS, mas com direito ao FGTS;
  // 04 - Empregado sob contrato de trabalho por prazo determinado (Lei n* 9.601/98);
  // 05 - Contribuinte Individual - Diretor não empregado com FGTS (Lei nº 8.036/90, art. 16);
  // 06 - Empregado Doméstico;
  // 07 - Menor Aprendiz ( Lei 10.097/2000);
  // 11 - Contribuinte Individual - Diretor não empregado e demais empresários sem FGTS;
  // 12 - Demais Agentes Públicos;
  // 13 - Contribuinte Individual - Trabalhador autônomo ou a este equiparado, inclusive o operador de máquina com contribuição sobre remuneração;
  // 14 - Contribuinte Individual - Trabalhador autônomo ou a este equiparado, inclusive o operador de máquina com contribuição sobre salário-base;
  // 15 - Contribuinte Individual - Transportador autônomo com contribuição sobre remuneração;
  // 16 - Contribuinte Individual - Transportador autônomo com contribuição sobre salário-base;
  // 17 - Contribuinte Individual - Cooperado que presta serviços a empresas contratantes de Cooperativa de Trabalho;
  // 18 - Contribuinte Individual - Transportador Cooperado que presta serviços a empresas contratantes de Cooperativa de Trabalho;
  // 19 - Agente Político;
  // 20 - Servidor Público Ocupante, exclusivamente, de cargo em comissão; Servidor Público Ocupante de cargo temporário ;
  // 21 - Servidor Público titular de cargo efetivo, magistrado, membro do Ministério Público e do Tribunal e Conselho de Contas.

  // datInc
  dataInclusao: null, // string(date)

  // horInc
  horaInclusao: null, // string(date)
}

function getFieldValue() {
  const previousStepName = 'User';
  const group = 'Cadastro de Colaborador';

  const fieldNames = Object.keys(payload);
  for (const fieldName of fieldNames) {
    payload[fieldName] = props.get(`${previousStepName}.${group}.${fieldName}`);
  }
}

getFieldValue();

const allFieldsAreFilled = Object.values(payload).every(value => !!value);
if (!allFieldsAreFilled) {
  throw new Error('Fill are fields!');
}

try {
  const url = 'https://pyapisoap.onrender.com/api/v1/send/';
  const body = {
    version: 'g5-senior-services',
    wsdl: 'rubi_Synccom_senior_g5_rh_fp_fichaBasica',
    method: 'FichaBasica_6',
    params: {
      user: USER,
      password: PASSWD,
      encryption: 0,
      parameters: {
        ...payload,
      }
    }
  };
  const options = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', },
    body
  };

  Process.updateProcessProperties(self, { body, options });

  const response = await fetch(url, options);
  if (!response.ok) {
    Process.updateProcessProperties(self, {  error: 'Fail to fetch data', response: JSON.stringify(response) });
    throw new Error('Fail to send request');
  }
  const jsonResponse = await response.json();
  Process.updateProcessProperties(self, {  jsonResponse });
} catch (err) {
  Process.updateProcessProperties(self, {  catch: JSON.stringify(err) });
}
