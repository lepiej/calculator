# Kalkylator

En avansert kalkulator skrevet i Python med menybasert grensesnitt.

## Krav

- Python 3.x
- Bruker `math` modulen som er inkludert i Python standardbibliotek (ingen ekstra installasjon nødvendig)

## Installasjon

For å installere Python, følg instruksjonene på [python.org](https://www.python.org/downloads/).

Last ned og installer Python 3 fra den offisielle nettsiden. Sørg for at `python3` er tilgjengelig i kommandolinjen.

Modulen `math` er en del av Python standardbibliotek og krever ingen ekstra installasjon. Hvis programmet skulle bruke eksterne moduler, kan de installeres med `pip install <modulnavn>`.

## Bruk

Kjør kalkulatoren:

```bash
python3 calculator.py
```

Følg instruksjonene for å velge operasjon fra menyen og skrive inn tall. Programmet kjører i en løkke til du velger å avslutte.

## Eksempel

For å addere 1 + 1, deretter beregne 2^3, og så kvadratrot av 9:

1. Kjør `python3 calculator.py`
2. Velg operasjon: Skriv inn `1` for Addisjon
3. Skriv inn første tall: `1`
4. Skriv inn andre tall: `1`
5. Utdata: `1.0 + 1.0 = 2.0`
6. Velg operasjon: Skriv inn `5` for Potens
7. Skriv inn grunnverdi: `2`
8. Skriv inn eksponent: `3`
9. Utdata: `2.0 ^ 3.0 = 8.0`
10. Velg operasjon: Skriv inn `6` for Kvadratrot
11. Skriv inn tall: `9`
12. Utdata: `Kvadratrot av 9.0 = 3.0`
13. Velg operasjon: Skriv inn `7` for Avslutt
14. Utdata: `Takk for at du brukte kalkulatoren!`

## Funksjoner

- Addisjon
- Subtraksjon
- Multiplikasjon
- Divisjon (med sjekk for divisjon med null)
- Potens (x^y)
- Kvadratrot (med sjekk for negative tall)