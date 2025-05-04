Name:           pipx
Version:        1.7.1
Release:        %autorelease
Summary:        Install and run Python applications in isolated environments

# SPDX
License:        MIT
URL:            https://pypa.github.io/pipx
# We need to use the GitHub source archive instead of the PyPI sdist in order
# to get the script to generate the man page.
%global forgeurl https://github.com/pypa/pipx
Source:         %{forgeurl}/archive/%{version}/pipx-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l pipx
BuildOption(generate_buildrequires): -x full,graph,junit,sarif

BuildArch:      noarch

# noxfile.py: MAN_DEPENDENCIES
BuildRequires:  python3dist(argparse-manpage[setuptools])

BuildRequires:  /usr/bin/register-python-argcomplete

%description
pipx is a tool to help you install and run end-user applications written in
Python. It’s roughly similar to macOS’s brew, JavaScript’s npx, and Linux’s
apt.

It’s closely related to pip. In fact, it uses pip, but is focused on installing
and managing Python packages that can be run from the command line directly as
applications.


%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%build -a
# Generate shell completions. “pipx completions” says:
#
# Add the appropriate command to your shell's config file
# so that it is run on startup. You will likely have to restart
# or re-login for the autocompletion to start working.
#
# bash:
#     eval "$(register-python-argcomplete pipx)"
#
# zsh:
#     To activate completions for zsh you need to have
#     bashcompinit enabled in zsh:
#
#     autoload -U bashcompinit
#     bashcompinit
#
#     Afterwards you can enable completion for pipx:
#
#     eval "$(register-python-argcomplete pipx)"
#
# tcsh:
#     eval `register-python-argcomplete --shell tcsh pipx`
#
# fish:
#     # Not required to be in the config file, only run once
#     register-python-argcomplete --shell fish pipx >~/.config/fish/completions/pipx.fish
for sh in bash tcsh fish
do
  # We don’t need to be able to import pipx for this command to work.
  register-python-argcomplete --shell "${sh}" pipx > "pipx.${sh}"
done

# noxfile.py: build_man()
PYTHONPATH="${PWD}/src" %{python3} scripts/generate_man.py


%install -a
install -p -m 0644 -D -t '%{buildroot}%{_mandir}/man1' pipx.1

install -p -m 0644 -D -t '%{buildroot}%{bash_completions_dir}' pipx.bash
install -p -m 0644 -D -t '%{buildroot}%{fish_completions_dir}' pipx.fish
# It seems that there is not a reasonable way to install tcsh completions
# system-wide, so we just make the completions file available for interested
# users.
install -p -m 0644 -D pipx.tcsh \
    '%{buildroot}%{_datadir}/pipx/pipx-completion.tcsh'
# Note that there are no “native” zsh completions, so we do not attempt to
# install anything. This could change if an actual zsh user recommends a
# different plan.


%check -a
# It’s just not practical to run the tests. For most of them, we need either
# (by default) a bundle of sample wheels from PyPI–which is arch-specific, as
# some of them have compiled extensions—or network access. Previously, we tried
# to disentangle the tests that did not require PyPI packages, but this has
# become onerous.
#
# Instead, we “smoke-test” the installation by running the command-line tool
# and confirming it can print its help output without crashing.

# Make sure the source copy of the package is not in the Python path.
mkdir -p empty
cd empty

PYTHONPATH=%{buildroot}%{python3_sitelib} \
    %{buildroot}%{_bindir}/pipx --help >/dev/null


%files -f %{pyproject_files}
%doc docs/*.md

%{_bindir}/pipx
%{_mandir}/man1/pipx.1*

%{bash_completions_dir}/pipx.bash
%{fish_completions_dir}/pipx.fish

%{_datadir}/pipx/


%changelog
%autochangelog
