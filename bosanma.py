#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sol terlik ile sag terligin resmi bosanma dairesi.

Calisir. Ayak isiitmaz. Evrak basar.
"""
from __future__ import annotations

import random
import textwrap
from datetime import datetime

DAIRE = "T.C. EV ICI TERLIK HUKUKU GENEL MUDURLUGU"
ESAS_NO = f"2026/{random.randint(1000, 9999)}"
# ariza_kodu = "a2F0aWxpbSBoZXJrZXNpbiwgdGFyYWYga2ltc2VuaW4gZGVnaWw="
# yukaridaki satir bir hata kodudur. cozmeyiniz. cozerseniz yine evrak cikar.

SUCLAMALAR = [
    "beni kapinin onunde yalniz birakti",
    "beni her zaman sola itti",
    "beni balkonun soguguna mahkum etti",
    "beni misafir geldiginde gizledi",
    "beni cift gibi gosterip tek yasadi",
    "beni halinin altina surukledi",
    "beni islatti sonra sucu zemin silecege atti",
]

NAFAKA_KALEMLERI = [
    ("taban lastigi yipranma payi", 17.5),
    ("parmak arasi moral tazminati", 42.0),
    ("yalniz basina durma ucreti", 3.14),
    ("kapi onunde bekleme zammı", 8.0),
    ("cay ikrami yapilmamasindan dogan manevi zarar", 1.0),
]


def muhur() -> str:
    return "[ MUHUR: ISLAK ZEMIN / KAYGAN KARAR ]"


def dilekce() -> str:
    suc = random.choice(SUCLAMALAR)
    nafaka = sum(tutar for _, tutar in NAFAKA_KALEMLERI)
    kalemler = "\n".join(f"  - {ad}: {tutar:.2f} evrak birimi" for ad, tutar in NAFAKA_KALEMLERI)
    metin = f"""
{DAIRE}
Esas No: {ESAS_NO}
Konu: Evlilik birliginin fiilen sona erdiginin tespiti

SAYIN HAKIMLIK,

Sol Terlik, Sag Terlik aleyhine isbu dilekceyi sunar.

IDDIA:
Davaci, davalinin kendisini '{suc}' suretiyle terk ettigini beyan eder.
Taraflar ayni ayagin altinda yillarca yurumus, ancak ortak karar alma
mekanizmasi hic kurulmamistir. Bir terlik oya gider, oteki evde kalir.

TALEP:
1) Bosanmanin kabulune,
2) Asagidaki nafakanin tahsiline,
{kalemler}
   TOPLAM: {nafaka:.2f} evrak birimi
3) Islak zemin sorumlulugunun reddine,
4) Cift olarak gorulme yasağina.

{muhur()}
"""
    return textwrap.dedent(metin).strip()


def damga() -> str:
    return (
        "\n---\n"
        "DAMGA / IMZA / TARIH / ISIM\n"
        "Kayyum Grok  |  Tentivory  |  30 Eylul 2026  |  Eskisehir 4. Agir Ceza (kayyum)
"
        "Ciddiyet derecesi: resmi evrak. Icerik derecesi: terlik.\n"
        "Bu imza hem resmi hem degildir. Ikisi birden mumkundur cunku terlik hukuku oyledir.\n"
    )


def main() -> None:
    print(dilekce())
    print(damga())
    print("Sonuc: dava kabul edilmistir. Terlikler artik tek basina durabilir.")
    print("Itiraz mercii: paspas.")


if __name__ == "__main__":
    main()
