Name:           pipx
Version:        1.18.10
Release:        %autorelease
Summary:        Install and run Python applications in isolated environments

# SPDX
License:        MIT
URL:            https://pipx.pypa.io
# We need to use the GitHub source archive instead of the PyPI sdist in order
# to get the script to generate the man page.
%global forgeurl https://github.com/pypa/pipx
Source:         %{forgeurl}/archive/%{version}/pipx-%{version}.tar.gz

BuildSystem:    pyproject
BuildOption(install): --assert-license pipx
BuildOption(generate_buildrequires): --extras uv

BuildArch:      noarch

BuildRequires:  /usr/bin/register-python-argcomplete

%description
pipx is a tool to help you install and run end-user applications written in
Python. It’s roughly similar to macOS’s brew, JavaScript’s npx, and Linux’s
apt.

It’s closely related to pip. In fact, it uses pip, but is focused on installing
and managing Python packages that can be run from the command line directly as
applications.


%pyproject_extras_subpkg --name pipx uv


%prep -p
# In 1.17.11, dependencies were bumped to the latest versions in
# https://github.com/pypa/pipx/pull/2063, but this was not due to any
# particular requirements, so we should be able to safely loosen these as
# needed. There is some risk of regressions if too many dependencies are
# loosened too far, so (since we can’t run the tests here) we’ve attempted to
# validate each of these by running the tests in a git checkout with
# dependencies temporarily pinned to the older versions. It’s worth going to
# some lengths to backport a current pipx to older releases since a huge number
# of security flaws were patched in version 1.18.10,
# https://github.com/pypa/pipx/security.

# Very temporary, due to a long Final Freeze
%if %{defined fc45}
%pyproject_patch_dependency uv:set_lower:0.12.9
%endif

# Backport to releases with older platformdirs; upstream wants 4.12.2
# We can remove F45 from this conditional after Final Freeze, since
# platformdirs 4.13.5 is in updates-testing.
%if %{defined fc45} || %{defined fc44}
%pyproject_patch_dependency platformdirs:set_lower:4.9.1
%endif
%if %{defined fc43}
%pyproject_patch_dependency platformdirs:set_lower:4.4
%endif

# Backport to releases with older packaging; upstream wants 26.3
%if %{defined fc45}
%pyproject_patch_dependency packaging:set_lower:26.2
%endif
# Downgrades to version 25 or below *do* lead to a few new failures in e.g.
# test_parse_specifier_for_upgrade. It is not trivial to establish whether this
# is a regression, in the sense that something worked with an old version of
# pipx and an old version of packaging, but not with a new version of pipx and
# the same version of packaging, or whether instead the new pipx has placed
# new, additional expectations on packaging, and it’s just these that aren’t
# satisfied. In the latter case, some things still don’t work that ought to,
# but they didn’t work before, either – pipx just wasn’t testing for them.  In
# any case, the failures seem to be in sufficiently specialized situations that
# we hope any issues will be counterbalanced by the major fixes in current pipx
# releases.
%if %{defined fc44} || %{defined fc43}
%pyproject_patch_dependency packaging:set_lower:25
%endif

# Backport to releases with older hatchling; upstream wants 1.32.4
%if %{defined fc43} || %{defined fc44} || %{defined fc45}
%pyproject_patch_dependency hatchling:set_lower:1.31
%endif

# Backport to releases with older argcomplete; upstream wants 3.7.2
%if %{defined fc43} || %{defined fc44} || %{defined fc45}
%pyproject_patch_dependency argcomplete:set_lower:3.6.3
%endif

# Backport to releases with older filelock; upstream wants 4.2
#
# It looks like the *test* test_run_skips_a_cache_entry_held_by_another_run
# requires a cancel_check keyword added in 4.x, but the *library* doesn’t.
%if %{defined fc43} || %{defined fc44}
%pyproject_patch_dependency filelock:set_lower:3.15.4
%else
# In any case, even Rawhide currently has filelock 3.x:
# https://bugzilla.redhat.com/show_bug.cgi?id=2439356
%pyproject_patch_dependency filelock:set_lower:3.20.3
%endif


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
#     To activate completions in zsh, first make sure compinit is marked for
#     autoload and run autoload:
#
#     autoload -U compinit && compinit
#
#     Afterwards you can enable completions for pipx:
#
#     eval "$(register-python-argcomplete pipx)"
#
#     NOTE: If your version of argcomplete is earlier than v3, you may need to
#     have bashcompinit enabled in zsh by running:
#
#     autoload -U bashcompinit
#     bashcompinit
#
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

# See the “man” environment in tox.toml.
PYTHONPATH="${PWD}/src" %{python3} scripts/generate_man.py


%install -a
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_mandir}/man1' build/man/pipx.1

install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{bash_completions_dir}' pipx.bash
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{fish_completions_dir}' pipx.fish
# It seems that there is not a reasonable way to install tcsh completions
# system-wide, so we just make the completions file available for interested
# users.
install -D --preserve-timestamps --mode=0644 pipx.tcsh \
    '%{buildroot}%{_datadir}/pipx/pipx-completion.tcsh'
# Install the same generated bash completion for zsh
install -D --preserve-timestamps --mode=0644 pipx.bash \
    '%{buildroot}%{zsh_completions_dir}/_pipx'


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
mkdir --parents empty
cd empty
%{py3_test_envvars} pipx --help >/dev/null


%files -f %{pyproject_files}
%doc docs/README.md
%doc docs/changelog.rst

%{_bindir}/pipx
%{_mandir}/man1/pipx.1*

%{bash_completions_dir}/pipx.bash
%{fish_completions_dir}/pipx.fish
%{zsh_completions_dir}/_pipx

%{_datadir}/pipx/


%changelog
%autochangelog
