# [Dotfiles](https://github.com/AzaanRais/dotfile)

- These are my dotfiles for Alacritty, Bash, Bpytop, Cava, Dunst, Flameshot, Git, GTK-2.0/3.0/4.0, Htop, Kitty, Neofetch, Nitrogen, Phocus, Polybar, Qtile and Zsh.

<br>

## Installation

### 1) Installing [GNU Stow](https://www.gnu.org/software/stow/)
- If you wish to install my dotfiles (I have not configured some programs just yet), you first need to install GNU Stow.

#### Installing from Package Manager
<hr>
You can install GNU Stow from your distribution's package manager because it is highly likely it's going to be available there. If not, you can build it from source and it requires very little dependencies.

<br>

#### Installing from source
<hr>

1. Grab the tarball of the latest version of GNU Stow from here: https://ftp.gnu.org/gnu/stow 

2. Navigate to the directory where you downloaded the package and run

```bash
tar -xvpzf stow-latest.tar.gz
```
3. Navigate inside the directory where the sources have been extracted to and run the following code to compile:

```bash
./configure
make
make install
```

<br>


### 2) Run script.sh
- After that you can simply run script.sh, make sure to backup your own config files though because this will OVERWRITE your pre-existing config.

```bash
git clone git@github.com:AzaanRais/dotfile
cd dotfile
chmod +x script.sh
./script.sh
```