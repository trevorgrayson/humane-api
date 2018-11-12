from runme.util import is_heading, is_code


class RunMe(object):

    def __init__(self, readme):
        self.commands = {}

        in_code = False
        cmd = None

        for line in readme:
            line = line.strip()

            if is_heading(line, 2):
                cmd = line.strip('#').strip().title().replace(' ', '')
                cmd = cmd[0].lower() + cmd[1:]
                self.commands[cmd] = self.commands.get(cmd, [])

            elif is_code(line):
                if in_code:
                    in_code = None
                    cmd = None
                else:
                    in_code = True

            elif in_code and cmd:
                if line and line[0] != '#':
                    self.commands[cmd].append(line)

