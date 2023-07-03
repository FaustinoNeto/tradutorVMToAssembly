class CodeWriter:
    def __init__(self, asm_file):
        self.asm_file = asm_file
        self.writeCode('// Bootstrap code')
        self.writeCode('@256')
        self.writeCode('D=A')
        self.writeCode('@SP')
        self.writeCode('M=D')
        self.writeCodeCall('Sys.init', 0)  # Chama a função Sys.init para iniciar o programa

    def writeCode(self, code):
        # Escreve o código assembly no arquivo
        with open(self.asm_file, 'a') as file:
            file.write(code + '\n')

    def writeArithmetic(self, command):
        # Escreve o código assembly para comandos aritméticos
        if command == 'add':
            self.writeCode('@SP')
            self.writeCode('AM=M-1')
            self.writeCode('D=M')
            self.writeCode('A=A-1')
            self.writeCode('M=D+M')
        elif command == 'sub':
            self.writeCode('@SP')
            self.writeCode('AM=M-1')
            self.writeCode('D=M')
            self.writeCode('A=A-1')
            self.writeCode('M=M-D')
        # Implemente os outros comandos aritméticos aqui

    def writePush(self, segment, index):
        # Escreve o código assembly para o comando push
        if segment == 'constant':
            self.writeCode('@' + str(index))
            self.writeCode('D=A')
        elif segment == 'local':
            self.writeCode('@LCL')
            self.writeCode('D=M')
            self.writeCode('@' + str(index))
            self.writeCode('A=A+D')
            self.writeCode('D=M')
        # Implemente os outros segmentos para push aqui

        # Incrementa SP e armazena o valor no topo da pilha
        self.writeCode('@SP')
        self.writeCode('A=M')
        self.writeCode('M=D')
        self.writeCode('@SP')
        self.writeCode('M=M+1')

    def writePop(self, segment, index):
        # Escreve o código assembly para o comando pop
        if segment == 'local':
            self.writeCode('@LCL')
            self.writeCode('D=M')
            self.writeCode('@' + str(index))
            self.writeCode('D=D+A')
            self.writeCode('@R13')  # Registrador temporário para armazenar o endereço
            self.writeCode('M=D')
        # Implemente os outros segmentos para pop aqui

        # Armazena o valor no topo da pilha no endereço calculado
        self.writeCode('@SP')
        self.writeCode('AM=M-1')
        self.writeCode('D=M')
        self.writeCode('@R13')
        self.writeCode('A=M')
        self.writeCode('M=D')

    def close(self):
        # Fecha o arquivo
        with open(self.asm_file, 'a') as file:
            file.close()
