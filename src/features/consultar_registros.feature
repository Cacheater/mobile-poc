@regresion
Feature: Como usuario de la app necesito validar que puedo consultar los registros para asegurar que se han guardado correctamente

    @hp @mobile @adr
    Scenario Outline: En el que valido que el registro con nombre David Chavez Avila se muestre en la pantalla de Consultar Registros
        Given Inicio sesión en la app con un usuario valido <usuario>
        When Consulto los registro existentes
        Then Verifico que se se muestre eel registro: <registro>
        Examples:
            | usuario | registro                     |
            | JOSY    | 4 - DAVID CHAVEZ AVILA       |
            | JOSY    | 6 - MARIA ORTEGON OROZCO     |
            | JOSY    | 10 - ANA MARIA AVILA RAMIREZ |