# Django E-Commerce (Lernprojekt)

Eine kleine, eigene E-Commerce Plattform als Lernprojekt — gebaut mit **Django (neueste Version)**, **Django Templates** und **PostgreSQL**.

## Ziele (MVP)
- Produktkatalog (Kategorien, Produktdetail, Suche, Pagination)
- Warenkorb (Session-basiert)
- Checkout + Bestellungen (Order/OrderItems als Snapshot)
- Auth (Registrierung/Login, Profil, Bestellhistorie)
- Admin-Bereich zur Pflege von Produkten und Bestellungen

## Tech-Stack
- Django (Templates)
- PostgreSQL
- (optional) Docker für lokale DB
- (optional) Stripe für Payments

---

## Lokales Setup (Entwicklung)

### Voraussetzungen
- Python 3.12+ (oder deine bevorzugte aktuelle Version)
- PostgreSQL (lokal) **oder** Docker

### Konfiguration
Lege eine `.env` Datei an (nicht committen). Beispiel:

```env
DEBUG=1
SECRET_KEY=change-me
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=shop
DB_USER=shop
DB_PASSWORD=shop
DB_HOST=127.0.0.1
DB_PORT=5432
