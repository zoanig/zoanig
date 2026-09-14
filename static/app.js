window.addEventListener("load", async () => {
    await document.fonts.ready;

    const terminal = document.querySelector(".termwin");

    if (!terminal) return;

    const prompt = terminal.querySelector(".prompt");
    const output = terminal.querySelector(".output");

    if (!prompt || !output) return;

    const command = prompt.textContent.trim();

    const lines = [
        ...terminal.querySelectorAll(
            ".ascii pre, .ascii p, .term-content > p"
        )
    ];

    const cursor = document.createElement("span");
    cursor.className = "terminal-cursor";

    const sleep = ms =>
        new Promise(resolve => setTimeout(resolve, ms));


    async function typeCommand() {
        prompt.textContent = "";

        for (const char of command) {
            prompt.appendChild(
                document.createTextNode(char)
            );

            prompt.appendChild(cursor);

            const delay =
                char === " "
                    ? 30
                    : Math.random() * 25 + 25;

            await sleep(delay);
        }

        await sleep(400);
    }


    async function revealOutput() {
        cursor.remove();

        output.style.visibility = "visible";

        for (const line of lines) {
            line.style.visibility = "visible";

            await sleep(
                Math.random() * 40 + 35
            );
        }
    }


    async function playTerminal() {
        prompt.textContent = "";

        output.style.visibility = "hidden";

        lines.forEach(line => {
            line.style.visibility = "hidden";
        });

        prompt.appendChild(cursor);

        await typeCommand();
        await revealOutput();
    }


    playTerminal();
});

let hash = window.location.hash.replace('#', '');
if (hash == "") {
    hash = 'home'
}
const anchor = document.getElementById(`hash-${hash}`)
anchor.classList.add('active')


window.addEventListener("hashchange", () => {
    const header = document.getElementById('header');
    const children = header.querySelectorAll('a');
    children.forEach(child => {
    child.classList.remove('active');
    });
    const hash = window.location.hash.replace('#', '');
    const anchor = document.getElementById(`hash-${hash}`)
    anchor.classList.add('active') 
})

window.addEventListener('scroll', () => {
  const header = document.getElementById('header');
  
  if (window.scrollY > 10) {
    header.classList.add('scrolled');
  } else {
    header.classList.remove('scrolled');
  }
});

function getStaticUrl(filePath) {
    return window.DjangoStaticUrl + filePath;
}

const techstack = JSON.parse(document.getElementById('d_sections').textContent)[1]['fields'];
const about_content = document.getElementById('about-content')
for (const [key, value] of Object.entries(techstack)) {
  if (key != "Expertise") {
    let stacks = value.split(", ")
    if (stacks.includes("JS/TS")) {
        const index = stacks.indexOf("JS/TS")
        stacks.splice(index, 0, "JS")
        stacks.splice(index + 1, 0, "TS")
        stacks.splice(index + 2, 1)
    
    }
    const child = document.createElement('div')
    child.classList.add('about-child')
    const childsec = document.createElement('div')
    stacks.forEach((stack) => {
        const icon = getStaticUrl(`icons/${stack.toLowerCase()}.svg`)
        childsec.innerHTML += `
            <div>
                <img class='icon' src='${icon}' alt='no'>
                <p>${stack}</p>
            </div>
        `
    })
    child.innerHTML = `
    <div>
        <h2>${key}</h2>
        <div>
            ${childsec.innerHTML}
        </div>
    </div>

    `
    about_content.appendChild(child)
  }
}

const sections = document.querySelectorAll("section");

// 2. Configure the observer options
const options = {
  root: null,         // Use the viewport as the root
  rootMargin: '-20% 0px -60% 0px', // Shrink the active target zone to the top-middle of the screen
  threshold: 0        // Trigger as soon as the element crosses the boundary
};

// 3. Create the callback function that runs on scroll intersection
const observerCallback = (entries) => {
  entries.forEach((entry) => {
    // Only update if the section is actively entering our target viewport zone
    if (entry.isIntersecting) {
      const id = entry.target.getAttribute('id');
      
      // Update the URL hash without triggering a page jump/flicker
      history.replaceState(null, null, `#${id}`);
    }
  });
};

// 4. Initialize the IntersectionObserver
const observer = new IntersectionObserver(observerCallback, options);

// 5. Tell the observer to watch each section
sections.forEach((section) => observer.observe(section));