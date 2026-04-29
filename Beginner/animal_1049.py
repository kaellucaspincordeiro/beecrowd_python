animais = {

    "vertebrado": {

        "ave": {
            "carnivoro": "aguia",
            "onivoro": "pomba",
        },

        "mamifero": {
            "onivoro": "homem",
            "herbivoro": "vaca",
        }
    },

    "invertebrado": {

        "inseto": {
            "hematofago": "pulga",
            "herbivoro": "lagarta",
        },

        "anelideo": {
            "hematofago": "sanguessuga",
            "onivoro": "minhoca",
        }
    }
}

tipo_1 = input().strip()
tipo_2 = input().strip()
tipo_3 = input().strip()

print(animais[tipo_1][tipo_2][tipo_3])