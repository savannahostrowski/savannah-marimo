import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Hey there, I'm Savannah Bailey[^1]!

    I'm a [Python](https://github.com/python/cpython) Core Developer, primarily working on the JIT[^2]. I also work at [Snowflake](https://www.snowflake.com/en/) on Python developer experience and Notebooks. I'm also part of the Faster CPython team and a member of the [Jupyter Foundation Governing Board](https://jupyter.org/governance/people.html#jupyter-foundation-governing-board).

    As you can tell, I really like Python (it was my first programming language, after all)! I also really love containers, compilers, DevOps, open source software, and cats. Outside of my work in Python, you're most likely to find me hacking on random projects like this one, working on ceramics, gardening, or reading a good book.

    You can find me many places on the Internet, like [GitHub](https://github.com/savannahostrowski), [Bluesky](https://bsky.app/profile/savannah.dev), and [LinkedIn](https://www.linkedin.com/in/savannahostrowski/). You'll also be able to find me IRL at [EuroPython](https://ep2025.europython.eu/) in July, where I'll be giving my first keynote.

    ...and yes, this is an executable Python (Marimo) notebook, running in a container — in your browser. Python is the future!

    [^1]: You may also know me as Savannah Ostrowski.
    [^2]: I've authored and co-authored some PEPs around the JIT - [PEP 744](https://peps.python.org/pep-0744/) and [PEP 774](https://peps.python.org/pep-0774/).
    """
    )
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.sidebar(
        [
            mo.nav_menu(
                {
                    "Links": {
                        "https://bsky.app/profile/savannah.dev": f"{mo.icon('logos:bluesky')} Bluesky",
                        "https://github.com/savannahostrowski": f"{mo.icon('logos:github-octocat')} GitHub",
                        "https://www.linkedin.com/in/savannahostrowski/": f"{mo.icon('logos:linkedin-icon')} LinkedIn",
                    },
                },
                orientation="vertical",
            ),
        ]
    )

    return


if __name__ == "__main__":
    app.run()
