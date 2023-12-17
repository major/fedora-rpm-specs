Name:           pipx
Version:        1.3.3
Release:        %autorelease
Summary:        Install and run Python applications in isolated environments

# SPDX
License:        MIT
URL:            https://pypa.github.io/pipx
# We need to use the GitHub source archive instead of the PyPI sdist in order
# to get the script to generate the man page.
%global forgeurl https://github.com/pypa/pipx
Source:         %{forgeurl}/archive/%{version}/pipx-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# noxfile.py: MAN_DEPENDENCIES
BuildRequires:  python3dist(argparse-manpage[setuptools])

BuildRequires:  /usr/bin/register-python-argcomplete

# The Markdown documentation is meant to be build with mkdocs. The HTML result
# is unsuitable for packaging due to various bundled and pre-minified
# JavaScript and CSS.  See https://bugzilla.redhat.com/show_bug.cgi?id=2006555
# for discussion of similar problems with Sphinx and Doxygen.
#
# We used to choose to install the Markdown documentation sources, as they are
# relatively readable without further processing but we’ve decided this isn’t
# really worthwile.
Obsoletes:      pipx-doc < 1.1.0-9

%description
pipx is a tool to help you install and run end-user applications written in
Python. It’s roughly similar to macOS’s brew, JavaScript’s npx, and Linux’s
apt.

It’s closely related to pip. In fact, it uses pip, but is focused on installing
and managing Python packages that can be run from the command line directly as
applications.


%prep
%autosetup


%generate_buildrequires
# We do not run the tests; but we add the runtime requirements as BR’s anyway
# so that the build will fail if some are not available in the distribution.
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

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


%install
%pyproject_install
%pyproject_save_files -l pipx

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


%check
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

# We separately do an import smoke test, although we must note that the package
# does not provide an API designed for external use.
%pyproject_check_import


%files -f %{pyproject_files}
%doc README.md

%{_bindir}/pipx
%{_mandir}/man1/pipx.1*

%{bash_completions_dir}/pipx.bash
%{fish_completions_dir}/pipx.fish

%{_datadir}/pipx/


%changelog
%autochangelog
