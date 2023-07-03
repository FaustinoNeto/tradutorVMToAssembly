class Parser:
    def __init__(self, vm_file):
        self.vm_file = vm_file
        self.commands = []
        self.current_command = None

        # Abre o arquivo e carrega todos os comandos em uma lista
        with open(vm_file, 'r') as file:
            for line in file:
                # Remove espaços em branco e comentários
                line = line.strip()
                if line and not line.startswith('//'):
                    self.commands.append(line)

        self.num_commands = len(self.commands)
        self.command_index = 0

    def hasMoreCommands(self):
        # Verifica se existem mais comandos a serem processados
        return self.command_index < self.num_commands

    def advance(self):
        # Avança para o próximo comando
        if self.hasMoreCommands():
            self.current_command = self.commands[self.command_index]
            self.command_index += 1

    def commandType(self):
        # Retorna o tipo de comando
        if self.current_command.startswith('push'):
            return 'C_PUSH'
        elif self.current_command.startswith('pop'):
            return 'C_POP'
        elif self.current_command.startswith('label'):
            return 'C_LABEL'
        elif self.current_command.startswith('goto'):
            return 'C_GOTO'
        elif self.current_command.startswith('if-goto'):
            return 'C_IF'
        elif self.current_command.startswith('function'):
            return 'C_FUNCTION'
        elif self.current_command.startswith('return'):
            return 'C_RETURN'
        elif self.current_command.startswith('call'):
            return 'C_CALL'
        else:
            return 'C_ARITHMETIC'

    def arg1(self):
        # Retorna o primeiro argumento do comando
        if self.commandType() == 'C_ARITHMETIC':
            return self.current_command
        else:
            return self.current_command.split()[1]

    def arg2(self):
        # Retorna o segundo argumento do comando
        return int(self.current_command.split()[2])
