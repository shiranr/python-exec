class Application:
    def run(self, args):
        loc = {}
        config = dict()
        file_to_exec = open(args.file_path)
        exec(file_to_exec.read(), config, loc)
        result = loc.get(args.invoke_function)(args.linter_files)
        file_to_exec.close()
        return result
