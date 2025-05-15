from fastapi import APIRouter, HTTPException, Response, Depends
import requests
import json
from pathlib import Path
from api.security import get_current_user 
from api.models import User

router = APIRouter(prefix='/ipca', tags=['ipca'])

IBGE_API_URL = "https://apisidra.ibge.gov.br/values/t/1737/n1/all/v/all/p/all/d/v63%202,v69%202,v2266%2013,v2263%202,v2264%202,v2265%202?formato=json"


@router.get("/download-ipca-data")
def download_ipca_data(user: User = Depends(get_current_user)):
    try:
        response = requests.get(IBGE_API_URL, timeout=10)
        response.raise_for_status()
        dados = response.json()

        json_str = json.dumps(dados, ensure_ascii=False, indent=2)
        headers = {
            "Content-Disposition": "attachment; filename=dados_ipca.json"
        }

        return Response(content=json_str, media_type="application/json", headers=headers)

    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Erro ao acessar a API do IBGE: {e}")