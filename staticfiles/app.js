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