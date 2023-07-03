from codewriter import CodeWriter
from parser import Parser

import sys

if len(sys.argv) != 2:
    print('Usage: python VMTranslator.py <input.vm>')
    sys.exit(1)

vm_file = sys.argv[1]
asm_file = vm_file.replace('.vm', '.asm')

parser = Parser(vm_file)
code_writer = CodeWriter(asm_file)

while parser.hasMoreCommands():
    parser.advance()
    command_type = parser.commandType()

    if command_type == 'C_ARITHMETIC':
        code_writer.writeArithmetic(parser.arg1())
    elif command_type in ['C_PUSH', 'C_POP']:
        code_writer.writePushPop(command_type, parser.arg1(), parser.arg2())
    

code_writer.close()
