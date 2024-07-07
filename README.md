# One Dark Cloud Theme

Dark theme for VSCode inspired by Atom's [One Dark Theme](https://github.com/atom/atom/tree/master/packages/one-dark-syntax) with tweaks to make it feel "soft" and "plushy" on the eyes!

Includes progressive coloring for up-to 8 `.json` levels.

![Preview](preview.png)

## Install

Install directly from [VSCode marketplace](https://marketplace.visualstudio.com/items?itemName=oleg-moroz.one-dark-cloud-theme) or manually from CLI:

```bash
code --install-extension one-dark-cloud-theme
```

## WSL terminal

In the WSL terminal, you may notice some directories are highlighted with green when using `ls`.

This is a WSL quirk which can be fixed by adding the following to WSL's `~/.bashrc`:

```bash
LS_COLORS="ow=01;36"
```
