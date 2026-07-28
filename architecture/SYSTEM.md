# AlHoff Core – Systemarchitektur

## Zweck

AlHoff Core ist eine lokale und erweiterbare KI-Plattform zur Verwaltung spezialisierter Agenten, Werkzeuge, Daten und Arbeitsabläufe.

Die Plattform soll unabhängig von einem einzelnen KI-Anbieter aufgebaut werden.

## Grundprinzipien

- Einfach
- Reproduzierbar
- Dokumentiert
- Modular
- Sicher
- Anbieterunabhängig

## Zentrale Komponenten

### 1. Core Orchestrator

Der Core Orchestrator ist die zentrale Steuerung der Plattform.

Aufgaben:

- Benutzeranfragen entgegennehmen
- Aufgaben analysieren
- geeignete Agenten auswählen
- Werkzeuge und Datenquellen bereitstellen
- Ergebnisse kontrollieren
- Aktivitäten protokollieren
- Sicherheitsregeln durchsetzen

### 2. Agenten

Spezialisierte Agenten übernehmen klar definierte Aufgaben.

Geplante Agenten:

- Research-Agent
- Dokumentations-Agent
- Trading-Agent
- Infrastruktur-Agent
- Sicherheits-Agent

### 3. Wissensspeicher

Der Wissensspeicher enthält:

- Projektdokumentation
- Entscheidungen
- Anleitungen
- Forschungsergebnisse
- Konfigurationen
- spätere Agentenerinnerungen

### 4. Werkzeuge

Werkzeuge ermöglichen den Agenten den Zugriff auf externe Systeme.

Geplante Werkzeuge:

- Telegram
- GitHub
- Datenbanken
- APIs
- Dateisystem
- Webrecherche
- Trading-Schnittstellen

### 5. Infrastruktur

Die Plattform wird zunächst lokal auf Ubuntu entwickelt.

Geplante technische Grundlage:

- Python
- Git
- GitHub
- Visual Studio Code
- Docker
- PostgreSQL
- Telegram Bot API

## Sicherheitsmodell

Agenten erhalten nur die Berechtigungen, die sie für ihre Aufgabe benötigen.

Wichtige Regeln:

- keine geheimen Zugangsdaten im GitHub-Repository
- kritische Aktionen nur nach Bestätigung
- vollständige Protokollierung wichtiger Aktionen
- getrennte Entwicklungs-, Test- und Live-Umgebungen
- Trading zunächst nur als Simulation

## Entwicklungsablauf

Jede Mission folgt diesem Ablauf:

1. Planen
2. Umsetzen
3. Testen
4. Dokumentieren
5. Commit erstellen
6. Zu GitHub hochladen