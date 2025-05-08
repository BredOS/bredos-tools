#!/usr/bin/python3
fpath = "/etc/grub.d/10_linux"

with open(fpath, "r") as f:
    lines = f.readlines()

output = []

for line in lines:
    if 'echo "menuentry' in line and "${CLASS}" in line:
        indent = line[: len(line) - len(line.lstrip())]
        line_stripped = line.rstrip()

        # Split at ${CLASS} to insert --unrestricted
        pre, post = line_stripped.split("${CLASS}", 1)
        class_injected = f"{pre}${{CLASS}} --unrestricted{post}"

        output.append(f"{indent}if [ x$type != xrecovery ] ; then\n")
        output.append(f"{indent}  {class_injected}\n")
        output.append(f"{indent}else\n")
        output.append(f"{indent}  {line_stripped}\n")
        output.append(f"{indent}fi\n")
    else:
        output.append(line)

with open(fpath, "w") as f:
    f.writelines(output)
