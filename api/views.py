from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from zeep import Client

def serialize(obj):
    if isinstance(obj, dict):
        return {key: serialize(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [serialize(item) for item in obj]
    elif hasattr(obj, '__dict__'):
        return serialize(obj.__dict__)
    else:
        return obj

def format_response(response):
    data = response.get('__values__', {})

    erroExecucao = data.get('erroExecucao', None)

    tmcs_colaboradores = data.get('TMCSColaboradores', [])

    colaboradores = []
    for item in tmcs_colaboradores:
        colaborador_data = item.get('__values__', {})

        colaboradores.append({
            "catCnh": colaborador_data.get('catCnh', ' '),
            "codCar": colaborador_data.get('codCar', ''),
            "codCb2": colaborador_data.get('codCb2', ''),
            "codCcu": colaborador_data.get('codCcu', ' '),
            "codFil": colaborador_data.get('codFil', 0),
            "codFor": colaborador_data.get('codFor', 0),
            "codLoc": colaborador_data.get('codLoc', ' '),
            "datAdm": colaborador_data.get('datAdm', ''),
            "datAfa": colaborador_data.get('datAfa', ''),
            "datNas": colaborador_data.get('datNas', ''),
            "dddTel": colaborador_data.get('dddTel', 0),
            "ddiTel": colaborador_data.get('ddiTel', 0),
            "demPsp": colaborador_data.get('demPsp', ''),
            "desSit": colaborador_data.get('desSit', ''),
            "dexCid": colaborador_data.get('dexCid', ''),
            "dscTipCol": colaborador_data.get('dscTipCol', ''),
            "dvaPsp": colaborador_data.get('dvaPsp', ''),
            "emaCom": colaborador_data.get('emaCom', ''),
            "emiCid": colaborador_data.get('emiCid', ''),
            "emiPsp": colaborador_data.get('emiPsp', ''),
            "estCar": colaborador_data.get('estCar', 0),
            "estCid": colaborador_data.get('estCid', ''),
            "estCnh": colaborador_data.get('estCnh', ' '),
            "horAfa": colaborador_data.get('horAfa', '0:00'),
            "nomCcu": colaborador_data.get('nomCcu', None),
            "nomEmp": colaborador_data.get('nomEmp', ''),
            "nomFun": colaborador_data.get('nomFun', ''),
            "nomLoc": colaborador_data.get('nomLoc', ''),
            "nomMae": colaborador_data.get('nomMae', ''),
            "nomPai": colaborador_data.get('nomPai', None),
            "numCad": colaborador_data.get('numCad', 0),
            "numCgc": colaborador_data.get('numCgc', ''),
            "numCid": colaborador_data.get('numCid', ''),
            "numCnh": colaborador_data.get('numCnh', ' '),
            "numCpf": colaborador_data.get('numCpf', ''),
            "numEmp": colaborador_data.get('numEmp', 0),
            "numPsp": colaborador_data.get('numPsp', ''),
            "numTel": colaborador_data.get('numTel', ''),
            "orgCnh": colaborador_data.get('orgCnh', ' '),
            "razSoc": colaborador_data.get('razSoc', ''),
            "sitAfa": colaborador_data.get('sitAfa', 0),
            "tabOrg": colaborador_data.get('tabOrg', 0),
            "tipCol": colaborador_data.get('tipCol', 0),
            "tipIns": colaborador_data.get('tipIns', 0),
            "tipSex": colaborador_data.get('tipSex', ''),
            "titCar": colaborador_data.get('titCar', ''),
            "titRed": colaborador_data.get('titRed', ''),
            "venCnh": colaborador_data.get('venCnh', '')
        })

    return {
        "erroExecucao": erroExecucao,
        "TMCSColaboradores": colaboradores
    }

def format_response_basic_sheet(response):
    data = response.get('__values__', {})

    erroExecucao = data.get('erroExecucao', None)

    numEmp = data.get('numEmp', '')
    numCad = data.get('numCad', '')

    return {
        "erroExecucao": erroExecucao,
        "data": {
            "numEmp": numEmp,
            "numCad": numCad,
        },
    }

def generate_dynamic_object(parameters):
    mapping = {
        "codigoEmpresa": "numEmp",
        "dataAdmissao": "datAdm",
        "codigoSituacao": "sitAfa",
        "codigoCargo": "codCar",
        "codigoEscala": "codEsc",
        "codigoFilial": "codFil",
        "indicativoAdmissao": "indAdm",
        "codigoLocal": "numLoc",
        "tipoEstabilidade": "codEtb",
        "numCarteiraTrabalho": "numCtp",
        "indicacaoRecolhimentoContribuicaoSindicato": "pagSin",
        "geracaoFichaMedica": "codFicFmd",
        "escalaValeTransporte": "escVtr",
        "categoriaeSocial": "cateSo",
        "tipoOperacao": "tipOpe",
        "codigoVinculo": "codVinHvi",
        "admissaoeSocial": "admeSo",
        "serieCarteiraTrabalho": "serCtp",
        "numeroCadastro": "numCad",
        "tipoApuracao": "apuPonApu",
        "codigoMotivoAlteracaoCargo": "codMotHca",
        "codigoTurmaEscala": "codTmaHes",
        "tipoAdmissaoFilial": "tipAdmHfi",
        "turnOverEntrada": "conTovHlo",
        "digitoVerificadorCarteiraTrabalho": "digCar",
        "cadastroFolhaDePagamento": "cadFol",
        "dataFinalEscalaValeTransporte": "fimEvt",
        "nomeFuncionario": "nomFun",
        "seguroDesemprego": "segDes",
        "observacoesIniciaisEstabilidade": "obsIniHeb",
        "dataExpedicaoCarteiraTrabalho": "dexCtp",
        "modoPagamento": "modPag",
        "codigoPontoEmbarque": "ponEmb",
        "apelidoColaborador": "apeFun",
        "codigoDefinicaoSituacao": "codDSiApu",
        "dataTransferenciaOuEntradaFilial": "DatEntHfi",
        "codigoMotivoAlteracao": "codMotHsa",
        "categoriaeSocialOrigem": "catAnt",
        "localTrabalhoRais": "locTraHlo",
        "observacoesFinaisEstabilidade": "obsFimHeb",
        "ufCarteiraTrabalho": "estCtp",
        "tipoContrato": "tipCon",
        "codigoSindicato": "codSinHsi",
        "tipoSalarioColaborador": "tipSalHsa",
        "tipoInscricaoEmpregadorAnterior": "tInAnt",
        "cpfColaborador": "numCpf",
        "sexoColaborador": "tipSex",
        "sindicalizado": "socSinHsi",
        "codigoEstruturaCargo": "codEstHsa",
        "cnpjOrigem": "cnpjAn",
        "numeroPis": "numPis",
        "tipoChavePix": "tpcPix",
        "assinalamentoParaPPR": "assPpr",
        "estadoCivil": "estCiv",
        "possuiBancoHoras": "possBHHsi",
        "classeSalarial": "claSalHsa",
        "dataAdmissaoOrigem": "admAnt",
        "dataCadastroPisPasep": "dcdPis",
        "chavePix": "chvPix",
        "contaBancaria": "conBan",
        "grauDeInstrucao": "graIns",
        "nivelSalarial": "nivSalHsa",
        "matriculaOrigem": "matAnt",
        "optanteFGTS": "tipOpc",
        "digBan": "digBan",
        "dataNascimento": "datNas",
        "valorSalario": "valSalHsa",
        "dataOpcaoFGTS": "datOpc",
        "periodoPagamento": "perPag",
        "complementoSalario": "cplSalHsa",
        "ressarcimentoOnus": "resOnu",
        "numeroContaFGTS": "conFgt",
        "tipoAposentadoria": "tipApo",
        "codigoNacionalidade": "codNac",
        "percentualJurosFGTS": "perJur",
        "codigoMovimentacaoSefip": "movSef",
        "recebeAdiantamentoSalarial": "recAdi",
        "recebe13Salario": "rec13S",
        "constaRais": "lisRai",
        "numeroCartaoPontoQuadroChapeira": "codCha",
        "manCgcAfao": "manCgcAfa",
        "pessoaComDeficiencia": "defFis",
        "manRemAfao": "manRemAfa",
        "colaboradorReabilitado": "benRea",
        "cotaPessoaDeficiencia": "cotDef",
        "codigoRacaEtnia": "racCor",
        "categoriaSEFIP": "catSef",
        "dataInclusao": "datInc",
        "horaInclusao": "horInc",
    }

    return {
        mapping.get(key): value
        for key, value in parameters.items()
        if key in mapping and value not in [None, "", []]
    }

@api_view(['GET'])
def api_status(request):
    return Response({"status": "API is running"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def receive_data(request):
    try:
        data = request.data
        p_version = data.get('version')
        p_wsdl = data.get('wsdl')
        wsdl = f"http://rubiweb.rpl.eng.br:8182/{p_version}/{p_wsdl}?wsdl"
        client = Client(wsdl=wsdl)

        method = data.get('method')
        body_params = data.get('params', {})
        parameters = body_params.get('parameters', {})

        params = {
            "user": body_params.get('user'),
            "password": body_params.get('password'),
            "encryption": body_params.get('encryption'),
            "parameters": {
                "numCpf": parameters.get('numCpf')
            }
        }

        response = client.service[method](**params)

        response_dict = serialize(response)

        mounted_response = format_response(response_dict)

        return Response({"data": mounted_response}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def send_basic_sheet(request):
    try:
        data = request.data
        p_version = data.get('version')
        p_wsdl = data.get('wsdl')
        wsdl = f"http://rubiweb.rpl.eng.br:8182/{p_version}/{p_wsdl}?wsdl"
        client = Client(wsdl=wsdl)

        method = data.get('method')
        body_params = data.get('params', {})
        parameters = body_params.get('parameters', {})

        treatedParameters = generate_dynamic_object(parameters)

        params = {
            "user": body_params.get('user'),
            "password": body_params.get('password'),
            "encryption": body_params.get('encryption'),
            "parameters": treatedParameters
        }

        response = client.service[method](**params)

        response_dict = serialize(response)

        mounted_response = format_response_basic_sheet(response_dict)

        return Response({"data": mounted_response}, status=status.HTTP_200_OK)

    except Exception as e:
        print(f"err: {e}")
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)