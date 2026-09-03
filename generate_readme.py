from profile_generater import generate_fetch_layout, DATA, ASCII_ART

with open('README.md', 'w') as file:
    profile = generate_fetch_layout(DATA, ASCII_ART, color=False, newline=False)
    readme=f"""<pre>
<code>
{profile}
</code>
</pre>
Try In Your Terminal:
Linux / Mac / Windows CMD
```shell
curl -L zoanig.vercel.app
```
Windows PS (Powershell)
```shell
curl.exe -L zoanig.vercel.app
```

"""
    file.write(readme)

print("README generated!")