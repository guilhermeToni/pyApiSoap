import json
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

def format_response_basic_sheet(response_dict):
    data = response.get('__values__', {})

    erroExecucao = data.get('erroExecucao', None)

    numEmp = data.get('numEmp', '')

    return {
        "erroExecucao": erroExecucao,
        "data": {
            "numEmp": numEmp,
            "numCad": numCad,
        },
    }

def generate_dynamic_object(parameters):
    mapping = {
        "numEmp": "numEmp",
        "datAdm": "datAdm",
        "sitAfa": "sitAfa",
        "codCar": "codCar",
        "codEsc": "codEsc",
        "codFil": "codFil",
        "indAdm": "indAdm",
        "numLoc": "numLoc",
        "codEtb": "codEtb",
        "numCtp": "numCtp",
        "codFicFmd": "codFicFmd",
        "pagSin": "pagSin",
        "codFicFmd": "codFicFmd",
        "escVtr": "escVtr",
        "tipOpe": "tipOpe",
        "codVinHvi": "codVinHvi",
        "admeSo": "admeSo",
        "iniEtbHeb": "iniEtbHeb",
        "serCtp": "serCtp",
        "depIrf": "depIrf",
        "conRho": "conRho",
        "numCad": "numCad",
        "apuPonApu": "apuPonApu",
        "codTmaHes": "codTmaHes",
        "tipAdmHfi": "tipAdmHfi",
        "conTovHlo": "conTovHlo",
        "fimEtbHeb": "fimEtbHeb",
        "conFinCcu": "conFinCcu",
        "digCar": "digCar",
        "depSaf": "depSaf",
        "cadFol": "cadFol",
        "fimEvt": "fimEvt",
        "nomFun": "nomFun",
        "artCltApu": "artCltApu",
        "turInt": "turInt",
        "conTovHfi": "conTovHfi",
        "conTosHlo": "conTosHlo",
        "dexCtp": "dexCtp",
        "modPag": "modPag",
        "verInt": "verInt",
        "ponEmb": "ponEmb",
        "codMotHsa": "codMotHsa",
        "catAnt": "catAnt",
        "locTraHlo": "locTraHlo",
        "estCtp": "estCtp",
        "tipCon": "tipCon",
        "codSinHsi": "codSinHsi",
        "tipSalHsa": "tipSalHsa",
        "tInAnt": "tInAnt",
        "natDesHna": "natDesHna",
        "numCpf": "numCpf",
        "busHor": "busHor",
        "tipSex": "tipSex",
        "socSinHsi": "socSinHsi",
        "codEstHsa": "codEstHsa",
        "numPis": "numPis",
        "tpcPix": "tpcPix",
        "tpCtBa": "tpCtBa",
        "possBHHsi": "possBHHsi",
        "claSalHsa": "claSalHsa",
        "admAnt": "admAnt",
        "dcdPis": "dcdPis",
        "chvPix": "chvPix",
        "conBan": "conBan",
        "nivSalHsa": "nivSalHsa",
        "matAnt": "matAnt",
        "tipOpc": "tipOpc",
        "datNas": "datNas",
        "valSalHsa": "valSalHsa",
        "onuSce": "onuSce",
        "datOpc": "datOpc",
        "perPag": "perPag",
        "cplSalHsa": "cplSalHsa",
        "resOnu": "resOnu",
        "conFgt": "conFgt",
        "tipApo": "tipApo",
        "perJur": "perJur",
        "movSef": "movSef",
        "recAdi": "recAdi",
        "rec13S": "rec13S",
        "emiCar": "emiCar",
        "codCha": "codCha",
        "defFis": "defFis",
        "benRea": "benRea",
        "cotDef": "cotDef",
        "racCor": "racCor",
        "ratEve": "ratEve",
        "catSef": "catSef",
        "datInc": "datInc",
        "horInc": "horInc",
    }

    return {
        mapping.get(key, key): value for key, value in parameters.items() if value not in [None, "", []]
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
        print(f"response: {response_dict}")

        # mounted_response = format_response_basic_sheet(response_dict)

        return Response({"data": response_dict}, status=status.HTTP_200_OK)

    except Exception as e:
        print(f"err: {e}")
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)