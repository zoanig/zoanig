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
```
curl -L zoanig.vercel.app
```
Windows PS (Powershell)
```
curl.exe -L zoanig.vercel.app
```
Also try if you wish to apply the following color pallete to your terminal:
![colors](./colors.png)

```
curl -L zoanig.vercel.app/theme
```
NOTE: The above endpoint sends a sequence of asni escape codes so resetting or restarting the terminal will bring the colors back to defaults or the previous theme.  

"""
    file.write(readme)

print("README generated!")