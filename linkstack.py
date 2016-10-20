import sys 



class LinkStack:
    def __init__(self):
        self.stack = self.read_stack()
        self.stack_size = len(self.stack)


    def read_stack(self):
        f = open('stack.txt', 'a+').close()
        txt = open('stack.txt', 'rU').read()
        lines = txt.splitlines()
        line_list = [line for line in lines if line]
        return line_list


    def write_stack(self, stack):
        txt = open('stack.txt', 'wb')
        for line in stack:
            txt.write('{}\n'.format(line))


    def print_links(self):
        print '\nStored links:\n'
        for i in range(0, self.stack_size):
            print '[{}] {}'.format(i + 1, self.stack[i])
        print '\n'


    def add(self):
        link = raw_input('Enter link: ')
        if link and not link in self.stack:
            self.stack.insert(0, link)
            self.stack_size = len(self.stack)
            self.write_stack(self.stack)
            print '\nLink added!\n'


    def delete(self):
        self.print_links()
        try: 
            num = int(raw_input('\nEnter line number of link to remove: '))
            if (num - 1) <= self.stack_size:
                self.stack.pop(num - 1)
                self.stack_size = len(self.stack)
                self.write_stack(self.stack)
                print '\nLink removed\n'
        except ValueError:
            print '\nWrong number input\n'


root = LinkStack()
help = '''\nAvailable commands: 
(a)dd new link to storage
(p)rint all stored links
(d)elete link
(q)uit the LinkStack\n'''

while(True):
    print help
    try:
        command = raw_input('Command: ').upper().rstrip()
        if command == 'A':
            root.add()
        elif command == 'P':
            root.print_links()
        elif command == 'D':
            root.delete()
        elif command == 'Q':
            break
        else:
            print '\nUnknown command\n'
    except SystemExit as e:
        pass
    except KeyboardInterrupt:
        sys.exit()

