Name:           python-typer
Version:        0.23.0
Release:        %autorelease
Summary:        Build great CLIs; easy to code; based on Python type hints

# SPDX
License:        MIT
URL:            https://typer.tiangolo.com/
%global forgeurl https://github.com/fastapi/typer
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

BuildSystem:            pyproject
BuildOption(install):   -l typer

BuildArch:      noarch

# Since the “tests” dependency group contains overly-strict version bounds and
# many unwanted linting/coverage/typechecking/formatting dependencies
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters),
# we just list the few test dependencies we *do* want manually rather than
# trying to patch pyproject.toml. We preserve upstream’s lower bounds but
# remove upper bounds, as we must try to make do with what we have.
BuildRequires:  %{py3_dist pytest} >= 4.4
BuildRequires:  %{py3_dist pytest-xdist} >= 1.32

%global common_description %{expand:
Typer is a library for building CLI applications that users will love using and
developers will love creating. Based on Python type hints.}

%description %{common_description}


%package -n     python3-typer
Summary:        %{summary}

%if %{defined fc44} || %{defined fc45} || %{defined fc46}
Obsoletes:      python3-typer-slim < 0.23.0-1
Obsoletes:      python3-typer-slim+standard < 0.23.0-1
Obsoletes:      python3-typer-cli < 0.23.0-1
%endif

%if %{defined fc44} || %{defined fc45}
# A file conflict existed between erlang-dialyzer and python3-typer-cli. It was
# resolved by renaming erlang-dialyzer’s typer executable to erlang-typer:
# https://src.fedoraproject.org/rpms/erlang/pull-request/6
#
# This change was made for Fedora 43, so we can remove the Conflicts for
# previous versions after Fedora 45.
#
# File conflicts: /usr/bin/typer with erlang-dialyzer
# https://bugzilla.redhat.com/show_bug.cgi?id=2359557
# File conflicts: /usr/bin/typer between erlang-dialyzer and python3-typer-cli
# https://bugzilla.redhat.com/show_bug.cgi?id=2359567
Conflicts:      erlang-dialyzer < 26.2.5.13-2
%endif

%description -n python3-typer %{common_description}


%install -a
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


%check -a
# See scripts/test.sh. We do not run the linters (scripts/lint.sh, i.e.,
# mypy/black/isort).
export TERMINAL_WIDTH=3000
export _TYPER_FORCE_DISABLE_TERMINAL=1
export _TYPER_RUN_INSTALL_COMPLETION_TESTS=1

# These cannot find the typer package because the tests override PYTHONPATH.
ignore="${ignore-} --ignore=tests/test_tutorial/test_subcommands/test_tutorial001.py"
ignore="${ignore-} --ignore=tests/test_tutorial/test_subcommands/test_tutorial003.py"
# This fails in mock but not in a git checkout. We have not found it worth
# investigating, but help is welcome.
ignore="${ignore-} --ignore=tests/test_tutorial/test_printing/test_tutorial004.py"

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


%files -n python3-typer -f %{pyproject_files}
%doc README.md
%doc docs/release-notes.md

%{_bindir}/typer
%{_mandir}/man1/typer*.1*
%{bash_completions_dir}/typer
%{zsh_completions_dir}/_typer
%{fish_completions_dir}/typer.fish


%changelog
%autochangelog
