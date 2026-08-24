from profile_generater import generate_fetch_layout, DATA, ASCII_ART

with open('README.md', 'w') as file:
    profile = generate_fetch_layout(DATA, ASCII_ART, color=False)
    readme=f"""<pre>
<b>zoanig@github.com:~$</b> fastfetch
<code>
{profile}
</code>
</pre>
"""
    file.write(readme)

print("README generated!")