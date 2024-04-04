from antlr4 import *
from CalculadoraLexer import CalculadoraLexer
from CalculadoraParser import CalculadoraParser
from CalculadoraPreLexer import CalculadoraPreLexer
from CalculadoraPreParser import CalculadoraPreParser
from CalculadoraAsoLexer import CalculadoraAsoLexer
from CalculadoraAsoParser import CalculadoraAsoParser
from CalculadoraModLexer import CalculadoraModLexer
from CalculadoraModParser import CalculadoraModParser
from EvalVisitor import EvalVisitor
from EvalVisitorPre import EvalVisitorPre
from EvalVisitorAso import EvalVisitorAso
from EvalVisitorMod import EvalVisitorMod
from antlr4.tree.Trees import Trees
import sys

#main lindo decision usuario



def main():
    input_file = None
    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    if input_file:
        input_stream = FileStream(input_file)
    else:
        input_stream = InputStream(input())

    
    print("\nMenu para Jugar con Asociatividad y Precedencia! : ")
    print("1 para Gramatica de Calculadora con Precedencia comun y Asociatividad comun")
    print("2 para Gramatica de Calculadora con Precedencia modificada y Asociatividad comun)")
    print("3 para Gramatica de Calculadora con Precedencia comun y Asociatividad modificada)")
    print("4 para Gramatica de Calculadora con Precedencia modificada y Asociatividad modificada)")
    print("\n(En el ReadMe especificamos lo comun y lo modificado) \n")

    choice = input("Ingrese el número de opción de la gramatica que deseas probar: ")

    print("\nLas respuestas aritmeticas del archivo .txt son:  \n")

    if choice == '1':
        lexer = CalculadoraLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = CalculadoraParser(tokens)
        tree = parser.prog()  # parse
        visitor = EvalVisitor()
        visitor.visit(tree)
        print(Trees.toStringTree(tree, None, parser))
        
    elif choice == '2':
        lexer = CalculadoraPreLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = CalculadoraPreParser(tokens)
        tree = parser.prog()  # parse
        visitor = EvalVisitorPre()
        visitor.visit(tree)

    elif choice == '3':
        lexer = CalculadoraAsoLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = CalculadoraAsoParser(tokens)
        tree = parser.prog()  # parse
        visitor = EvalVisitorAso()
        visitor.visit(tree)
        print(Trees.toStringTree(tree, None, parser))

    elif choice == '4':
        lexer = CalculadoraModLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = CalculadoraModParser(tokens)
        tree = parser.prog()  # parse
        visitor = EvalVisitorMod()
        visitor.visit(tree)
        print(Trees.toStringTree(tree, None, parser))
	    

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
if __name__ == '__main__':
    main()

