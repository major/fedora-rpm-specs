# This package corresponds to three PyPI projects (typer-slim, typer,
# typer-cli) all co-developed in one repository. Since the three are versioned
# identically and released at the same time, it makes sense to build them from
# a single source package.
Name:           python-typer
Version:        0.15.1
Release:        %autorelease
Summary:        Build great CLIs; easy to code; based on Python type hints

# SPDX
License:        MIT
URL:            https://typer.tiangolo.com/
%global forgeurl https://github.com/tiangolo/typer
Source0:        %{forgeurl}/archive/%{version}/typer-%{version}.tar.gz
# Hand-written for Fedora in groff_man(7) format based on typer --help.
Source10:       typer.1
# To get help text for
#   typer [PATH_OR_MODULE] utils --help
# first create empty file x.py, then run:
#   PYTHONPATH="${PWD}" typer x utils --help.
Source11:       typer-utils.1
# …and similarly,
#   PYTHONPATH="${PWD}" typer x utils docs --help.
Source12:       typer-utils-docs.1

BuildArch:      noarch

BuildRequires:  python3-devel

# Since requirements-tests.txt contains overly-strict version bounds and many
# unwanted linting/coverage/typechecking/formatting dependencies
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters),
# we just list the few test dependencies we *do* want manually rather than
# trying to patch the requirements file. We preserve upstream’s lower bounds
# but remove upper bounds, as we must try to make do with what we have.
BuildRequires:  %{py3_dist pytest} >= 4.4
BuildRequires:  %{py3_dist pytest-xdist} >= 1.32

%global common_description %{expand:
Typer is a library for building CLI applications that users will love using and
developers will love creating. Based on Python type hints.  Typer CLI

This package, typer-cli, only provides a command typer in the shell with the
same functionality of python -m typer.

The only reason why this is a separate package is to allow developers to opt
out of the typer command by installing typer-slim, that doesn’t include
typer-cli.}

%description %{common_description}


%package -n     python3-typer-slim
Summary:        %{summary}

%if %[ %{defined fc41} || %{defined fc42} || %{defined fc43} ]
# The python3-typer-slim package was introduced in F41; it corresponds roughly
# to the python3-typer (vs. python3-typer+all) in F40.
Obsoletes:      python3-typer < 0.12.1-1
Conflicts:      python3-typer < 0.12.1-1
%endif

%description -n python3-typer-slim %{common_description}


%package -n     python3-typer
Summary:        %{summary}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-typer-cli = %{version}-%{release}
Requires:       python3-typer-slim = %{version}-%{release}

%if %[ %{defined fc41} || %{defined fc42} || %{defined fc43} ]
# The python3-typer+all metapackage package was removed in F41; since
# python3-typer-slim was introduced, python3-typer is the closest replacement.
Obsoletes:      python3-typer+all < 0.12.1-1
Conflicts:      python3-typer+all < 0.12.1-1
%endif

%description -n python3-typer %{common_description}


%package -n     python3-typer-cli
Summary:        %{summary}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-typer-slim = %{version}-%{release}

%description -n python3-typer-cli %{common_description}


%pyproject_extras_subpkg -n python3-typer-slim -i %{python3_sitelib}/typer_slim-%{version}.dist-info standard


%prep
%autosetup -n typer-%{version} -p1


%generate_buildrequires
export TIANGOLO_BUILD_PACKAGE='typer-slim'
%pyproject_buildrequires -x standard
(
  export TIANGOLO_BUILD_PACKAGE='typer'
  %pyproject_buildrequires
) | grep -vE '\btyper\b'
(
  export TIANGOLO_BUILD_PACKAGE='typer-cli'
  %pyproject_buildrequires
) | grep -vE '\btyper\b'


%build
export TIANGOLO_BUILD_PACKAGE='typer-slim'
%pyproject_wheel
export TIANGOLO_BUILD_PACKAGE='typer'
%pyproject_wheel
export TIANGOLO_BUILD_PACKAGE='typer-cli'
%pyproject_wheel



%install
%pyproject_install

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}'

install -d \
    '%{buildroot}%{bash_completions_dir}' \
    '%{buildroot}%{zsh_completions_dir}' \
    '%{buildroot}%{fish_completions_dir}'
export PYTHONPATH='%{buildroot}%{python3_sitelib}'
export _TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION=1
'%{buildroot}%{_bindir}/typer' --show-completion bash \
    > '%{buildroot}%{bash_completions_dir}/typer'
'%{buildroot}%{_bindir}/typer' --show-completion zsh \
    > '%{buildroot}%{zsh_completions_dir}/_typer'
'%{buildroot}%{_bindir}/typer' --show-completion fish \
    > '%{buildroot}%{fish_completions_dir}/typer.fish'


%check
# See scripts/test.sh. We do not run the linters (scripts/lint.sh, i.e.,
# mypy/black/isort).
export TERMINAL_WIDTH=3000
export _TYPER_FORCE_DISABLE_TERMINAL=1
export _TYPER_RUN_INSTALL_COMPLETION_TESTS=1

# These cannot find the typer package because the tests override PYTHONPATH.
ignore="${ignore-} --ignore=tests/test_tutorial/test_subcommands/test_tutorial001.py"
ignore="${ignore-} --ignore=tests/test_tutorial/test_subcommands/test_tutorial003.py"

mkdir _stub
cat > _stub/coverage.py <<'EOF'
from subprocess import run
from sys import argv, executable, exit
if len(argv) < 3 or argv[1] != "run":
    exit(f"Unsupported arguments: {argv!r}")
exit(run([executable] + argv[2:]).returncode)
EOF
export PYTHONPATH="${PWD}/_stub:%{buildroot}%{python3_sitelib}"

%pytest -k "${k-}" ${ignore-} -n auto -v -rs


%files -n python3-typer-slim
%license LICENSE
%doc README.md
%doc docs/release-notes.md

%{python3_sitelib}/typer/
%{python3_sitelib}/typer_slim-%{version}.dist-info/


%files -n python3-typer
%{python3_sitelib}/typer-%{version}.dist-info/


%files -n python3-typer-cli
%{python3_sitelib}/typer_cli-%{version}.dist-info/

%{_bindir}/typer
%{_mandir}/man1/typer*.1*
%{bash_completions_dir}/typer
%{zsh_completions_dir}/_typer
%{fish_completions_dir}/typer.fish


%changelog
%autochangelog
