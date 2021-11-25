# BudjettiSovellus

Sovelluksen avulla on tarkoitus voida pitää kirjaa kotitalouden tuloista ja menoista. Sovellus on vielä kehityksessä, mutta käyttöliittymä aukeaa jo ja tulon tai menon lisäys toimii (nämä tosin eivät näy vielä itse sovelluksessa).

## Huomio Python-versiosta

Sovellus on tarkoitettu Python-versiolle 3.8<, mutta toimintaa on jouduttu testaamaan myös versiolla 3.6.

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Riippuvuudet asennetaan komennolla:

```bash
poetry install
```

2. Ohjelma käynnistetään komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelma käynnistetään komennolla:

```bash
poetry run invoke start
```

### Testaus

Testaus suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportti luodaan komennolla:

```bash
poetry run invoke coverage-report
```

Raportti muodostuu _htmlcov_-hakemistoon.
