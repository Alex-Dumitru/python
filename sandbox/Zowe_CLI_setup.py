import os
import subprocess

#get the PATH env var
my_env = os.environ.copy()

def run_shell_command(command):
    process = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    return (out, err, process)

def run_command(command, wait=False):
    try:
        if (wait):
            p = subprocess.Popen(
                [command], 
                stdout = subprocess.PIPE,
                shell = True,
                env=my_env)
            p.wait()
        else:
            p = subprocess.Popen(
                [str(command)], 
                shell = True,
                env=my_env, 
                stdin = None, stdout = None, stderr = None, close_fds = True)
        (result, error) = p.communicate()
    except subprocess.CalledProcessError as e:
        sys.stderr.write(
            "common::run_command() : [ERROR]: output = %s, error code = %s\n" 
            % (e.output, e.returncode))
    return result
# try:
#     node_exists = subprocess.call(["nodee -v"], shell=True, sysout=subprocess.PIPE, syserr=subprocess.PIPE)
# except Exception as ex:
#     print(ex)

# subprocess.Popen(["echo asdasd"], shell=True, env=my_env)
# print(run_shell_command("node -V"))
run_command("echo 123")
