# BudjettiSovellus

Sovelluksen avulla on tarkoitus voida pitää kirjaa kotitalouden tuloista ja menoista. Sovellus on vielä kehityksessä, mutta käyttöliittymä aukeaa jo ja tulon tai menon lisäys toimii, sekä tuloja, menoja ja budjettitilannetta voi tarkastella kotinäkymässä.

## Huomio Python-versiosta

Sovellus on tarkoitettu toimivaksi Python-versioille 3.8<.

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Riippuvuudet asennetaan komennolla:

```bash
poetry install
```

2. Esimmäisellä kerralla alustetaan ohjelma (luodaan tietokanta valmiiksi):

```bash
poetry run invoke build
```

3. Ohjelma käynnistetään komennolla:

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

### Koodinlaatu

Laaturaportti luodaan komennolla:

```bash
poetry run invoke lint
```
