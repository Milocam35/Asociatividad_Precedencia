# Modificación de Precedencia y Asociatividad en Gramáticas: Proyecto README

## Descripción del Proyecto

Este proyecto se enfoca en la modificación de la precedencia y la asociatividad en una gramática específica utilizando herramientas como ANTLR, Flex y Bison. El objetivo principal es crear cuatro variantes de la gramática original, cada una con un conjunto diferente de reglas de precedencia y asociatividad, seguido por la implementación de pruebas para verificar el comportamiento de cada variante.

## Objetivos

1. **Definir la gramática original**: Establecer una gramática inicial utilizando ANTLR y Flex con Bison para el lenguaje en cuestión.

2. **Generar analizadores léxicos y sintácticos**: Utilizar ANTLR y Flex con Bison para generar los analizadores léxicos y sintácticos necesarios basados en la gramática definida en ANTLR.

3. **Crear variantes de la gramática**: Desarrollar tres variantes adicionales de la gramática original, cada una con cambios específicos en la precedencia y la asociatividad.
   
   - **Prueba 1: Precedencia y asociatividad normales**: Mantendrá la precedencia y la asociatividad estándar del lenguaje.
   
   - **Prueba 2: Precedencia modificada**: Se realizarán ajustes en la precedencia de ciertos operadores para observar cómo afecta el análisis sintáctico.
   
   - **Prueba 3: Asociatividad modificada**: Se modificará la asociatividad de ciertos operadores para evaluar su impacto en la interpretación de expresiones.
   
   - **Prueba 4: Precedencia y asociatividad modificada**: Se combinarán ajustes tanto en la precedencia como en la asociatividad para evaluar su interacción.

## Ejecución del Programa en ANTLR

Para ejecutar el programa, sigue estos pasos (Importante tener en cuenta que CalculadoraNombreElegido se refiere a el nombre del archivo .g4 que desea ejecuta - Ejemplo: "CalculadoraAso.g4"):

1. **Generar código con ANTLR**:
   ```bash
   $ antlr4 -Dlanguage=Python3 -visitor CalculadoraNombreElegido.g4
   $ python3 MainCalculadora.py EjemploEntradaCalc.txt
