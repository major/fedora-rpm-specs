Name:           python-typer
Version:        0.7.0
Release:        %autorelease
Summary:        Build great CLIs; easy to code; based on Python type hints

# SPDX
License:        MIT
URL:            https://typer.tiangolo.com/
Source0:        https://github.com/tiangolo/typer/archive/%{version}/typer-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

Obsoletes:      python-typer-doc < 0.4.0-5

%global common_description %{expand:
Typer is a library for building CLI applications that users will love using and
developers will love creating. Based on Python 3.6+ type hints.

The key features are:

  • Intuitive to write: Great editor support. Completion everywhere. Less time
    debugging. Designed to be easy to use and learn. Less time reading docs.
  • Easy to use: It’s easy to use for the final users. Automatic help, and
    automatic completion for all shells.
  • Short: Minimize code duplication. Multiple features from each parameter
    declaration. Fewer bugs.
  • Start simple: The simplest example adds only 2 lines of code to your app: 1
    import, 1 function call.
  • Grow large: Grow in complexity as much as you want, create arbitrarily
    complex trees of commands and groups of subcommands, with options and
    arguments.

Typer is FastAPI’s little sibling.

And it’s intended to be the FastAPI of CLIs.}

%description %{common_description}


%package -n     python3-typer
Summary:        %{summary}

%description -n python3-typer %{common_description}


%pyproject_extras_subpkg -n python3-typer all


%prep
%autosetup -n typer-%{version}
cp -p pyproject.toml pyproject.toml.bak
# We have flit 3.x in Fedora 34 and later, so we must try to use it.
sed -r -i 's/(flit_core[[:blank:]]*>=2[^,]*),<3\b/\1/' pyproject.toml
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/\b(mypy|black|isort|pytest-cov|coverage) /d' pyproject.toml
find tests -type f -exec \
    gawk '/"coverage", "run"/ { print FILENAME; nextfile }' '{}' '+' |
  xargs -r -t sed -r -i 's@"coverage", "run"@"%{python3}"@g'
# Loosen certain strict maximum versions; we must work with what we have
sed -r -i 's/\b(pytest(-xdist)?)([[:blank:]]*>=[^,]*),[^"]+/\1\3/' pyproject.toml

# Remove bundled js-termynal 0.0.1; since we are not building documentation, we
# do this very bluntly:
rm -rvf docs/js docs/css


%generate_buildrequires
%pyproject_buildrequires -x all,test

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files typer


%check
# See scripts/test.sh. We do not run the linters (scripts/lint.sh, i.e.,
# mypy/black/isort).
./scripts/test-files.sh
# Shell completion tests need us to be running under a supported shell, i.e.
# bash rather than sh. Unfortunately, shell detection with shellingham is so
# thorough we cannot fool it by any combination of:
#  - export SHELL=/bin/bash
#  - bash -c '%%pytest'
#  - %%check -p /bin/bash
# so we must simply skip the affected tests.
k="${k-}${k+ and }not test_show_completion and not test_install_completion"
%pytest -k "${k-}" -n %{_smp_build_ncpus}


%files -n python3-typer -f %{pyproject_files}
%license LICENSE
%doc CONTRIBUTING.md
%doc README.md


%changelog
%autochangelog
