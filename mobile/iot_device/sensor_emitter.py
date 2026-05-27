import requests
import time
import random

BASE_URL = "http://127.0.0.1:8000"

TOKEN_URL = f"{BASE_URL}/token"

ESTACIONES_URL = f"{BASE_URL}/estaciones/"

LECTURAS_URL = f"{BASE_URL}/lecturas/"


def obtener_token():

    try:

        response = requests.post(TOKEN_URL)

        if response.status_code == 200:

            token = response.json()["access_token"]

            print("[OK] Token JWT obtenido")

            return token

    except Exception as e:

        print(f"[ERROR] Token: {e}")

    return None


def obtener_estaciones():

    try:

        response = requests.get(ESTACIONES_URL)

        if response.status_code == 200:

            return response.json()

    except Exception as e:

        print(f"[ERROR] Estaciones: {e}")

    return []


def generar_lectura():

    return round(
        random.uniform(20, 90),
        2,
    )


def enviar_lectura(
    token,
    estacion_id,
    valor,
):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "valor": valor,
        "estacion_id": estacion_id,
    }

    try:

        response = requests.post(
            LECTURAS_URL,
            json=payload,
            headers=headers,
        )

        if response.status_code == 201:

            print(
                f"[OK] Estación {estacion_id} -> {valor} cm"
            )

            if valor > 70:

                print(
                    "🚨 [ALERTA] Nivel crítico detectado"
                )

        else:

            print(
                f"[ERROR] Estación {estacion_id}"
            )

    except Exception as e:

        print(
            f"[CRÍTICO] {e}"
        )


def main():

    token = obtener_token()

    if not token:

        print("No se pudo iniciar")

        return

    print("==========================")
    print("   SMAT IOT AUTO SENSOR")
    print("==========================")

    while True:

        estaciones = obtener_estaciones()

        if not estaciones:

            print(
                "No hay estaciones registradas"
            )

        for estacion in estaciones:

            estacion_id = estacion["id"]

            valor = generar_lectura()

            enviar_lectura(
                token,
                estacion_id,
                valor,
            )

        print(
            "\nNueva telemetría en 5 segundos...\n"
        )

        time.sleep(5)


if __name__ == "__main__":

    main()