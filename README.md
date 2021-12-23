# BudjettiSovellus

Sovelluksen avulla on tarkoitus voida pitää kirjaa kotitalouden tuloista ja menoista. Sovellus ei ole täydellinen, mutta käyttöliittymä toimii sulavasti, kuten myös tulon tai menon lisäys, sekä yhteenlaskettuja tuloja, menoja että budjettitilannetta voi tarkastella kotinäkymässä. Lisäksi voi avata erillisen tulo- ja menoerittely -näkymän, josta näkee tulojen kuvaukset summien lisäksi.

## Releaset

- [Loppupalautus 23.12.2021](https://github.com/ereborinkorppi/ot-harjoitustyo/releases)

## Huomio Python-versiosta

Sovellus on tarkoitettu toimivaksi Python-versioille 3.8<.

## Dokumentaatio

- [Käyttöohje](./dokumentaatio/kayttohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Testausdokumentti](./dokumentaatio/testausdokumentti.md)

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
