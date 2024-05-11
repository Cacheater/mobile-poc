
Feature: Como usuario de la app necesito validar que mis contraseñas son valida para saber cuantos usuarios validos tengo


  Scenario Outline: En el que valido la app con diferentes contraseñas y passwords
    Given Abro la app para poder iniciar sesion
    When Inicio sesion con <usuario> y <password>
    Then Valido que se abra el home de la app
    Examples:
        |usuario| password  |
        |JOSY   | Test1234  |
        |JOSY43   | Test4321  |
        |JOSY21   | Test2341  |