# -*- coding: utf-8 -*-
# language: es

Funcionalidad: Llevar un registro correcto en
    un marcador en un partido de tenis
    
Escenario: El jugador uno anota desde 0
    Dado: Jugador 1 consigue anotar
    Cuando: El score es "0" - "0"
    Entonces: El puntaje del jugador 1 es "15"

Escenario: El jugador 1 anota cuando tiene 40 puntos y el jugador 2 también
    Dado: Jugador 1 consigue anotar
    Cuando: El score es "40" - "40"
    Entonces: El puntaje del jugador 1 es "Advantage"

Escenario: El jugador 1 anota cuando tiene 40 puntos y el jugador 2 tiene advantage
    Dado: Jugador 1 consigue anotar
    Cuando: El score es "40" - "Advantage"
    Entonces: El puntaje del jugador 1 es "40"  
    
Escenario: El jugador 2 anota cuando tiene 30 puntos y el jugador 1 también
    Dado: Jugador 2 consigue anotar
    Cuando: El score es "30" - "30"
    Entonces: El puntaje del jugador 2 es "40"
    
Escenario: El jugador 2 anota cuando tiene 40 puntos y el jugador 1 también
    Dado: Jugador 2 consigue anotar
    Cuando: El score es "40" - "40"
    Entonces: El puntaje del jugador 2 es "Advantage"

Escenario: El jugador 2 anota cuando tiene 40 puntos y el jugador 1 tiene 30
    Dado: Jugador 2 consigue anotar
    Cuando: El score es "30" - "40"
    Entonces: El puntaje del jugador 2 es "Set to Player 2"
