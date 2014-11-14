# -*- coding: utf-8 -*-
from lettuce import step, world
import sys
sys.path.append("../app")
from Tenis import Tenis


@step(u'Dado: Jugador 1 consigue anotar')
def dado_jugador_1_consigue_anotar(step):
    pass


@step(u'Cuando: El score es "([^"]*)" - "([^"]*)"')
def cuando_el_score_es_group1_group1(step, score1, score2):
    world.match = Tenis()
    world.match.puntajePlayer1 = score1
    world.match.puntajePlayer2 = score2


@step(u'Dado: Jugador 2 consigue anotar')
def dado_jugador_2_consigue_anotar(step):
    pass


@step(u'Entonces: El puntaje del jugador 2 es "([^"]*)"')
def entonces_el_puntaje_del_jugador_2_es_group1(step, score2):
    world.match.puntoPlayer2()
    assert world.match.puntajePlayer2 == score2, 'El resultado es %s y el esperado es %s' % (
        world.match.puntajePlayer2, score2)


@step(u'Entonces: El puntaje del jugador 1 es "([^"]*)"')
def entonces_el_puntaje_de_el_jugador_1_group1(step, score1):
    world.match.puntoPlayer1()
    assert world.match.puntajePlayer1 == score1, 'El resultado es %s y el esperado es %s' % (
        world.match.puntajePlayer1, score1)
