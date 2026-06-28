Name:           python-typer
Version:        0.26.8
Release:        %autorelease
Summary:        Build great CLIs; easy to code; based on Python type hints

# The entire source is MIT, except the forked/vendored copy of Click in
# typer/_click/, which is BSD-3-Clause. Upstream has declined to adjust the
# license expression in pyproject.toml, but we carry a downstream patch that
# does so. See the comments about that patch for more detail.
License:        MIT AND BSD-3-Clause
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

# Consider adding Click license text and SPDX identifier to .dist-info metadata
# https://github.com/fastapi/typer/discussions/1817
#
# Upstream declined to make these changes, saying that “We want to be careful
# not to make any further changes that end up being irreversible, and that
# could affect or confuse users more downstream.” They hope to eventually
# reimplement all of the Click-derived, BSD-3-Clause-licensed code from scratch
# with MIT-licensed code.
#
# Because we believe that strictly-accurate metadata is valuable in the
# packaged library, and these changes accurately reflect the current license
# status of the package, we choose to carry these changes downstream-only.
#
# [PATCH 1/2] Install the license text for Click in `.dist-info`
#
# This ensures that the package metadata contains all applicable license texts.
# The file ends up in `typer-….dist-info/licenses/typer/_click/LICENSE.txt`
# (vs. `typer-….dist-info/licenses/LICENSE` for the main MIT license text),
# which is perhaps slightly awkward but accomplishes the goal.
#
# [PATCH 2/2] Update the SPDX license expression to include Click’s license
#
# Change the license field in the metadata from `MIT` to `MIT AND BSD-3-Clause`
# to reflect the presence of code under the latter license in `typer/_click/`.
Patch:          typer-0.26.5-click-license.patch

BuildSystem:    pyproject
BuildOption(install): --assert-license typer

BuildArch:      noarch

# Since the “tests” dependency group contains overly-strict version bounds and
# many unwanted linting/coverage/typechecking/formatting dependencies
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters),
# we just list the few test dependencies we *do* want manually rather than
# trying to patch pyproject.toml. We preserve upstream’s lower bounds but
# remove upper bounds, as we must try to make do with what we have.
BuildRequires:  %{py3_dist pytest} >= 9
BuildRequires:  %{py3_dist pytest-xdist} >= 1.32

%global common_description %{expand:
Typer is a library for building CLI applications that users will love using and
developers will love creating. Based on Python type hints.}

%description %{common_description}


%package -n     python3-typer
Summary:        %{summary}

# Since version 0.26.0, Typer vendors Click. This is an intentional and
# permanent upstream decision, and upstream plans to diverge from Click
# upstream, removing unused code and more tightly integrating the vendored
# implementation with the rest of Typer. There is therefore no prospect of
# returning to using an external copy of Click or for unbundling downstream.
# See [1] for a summary of the decision and its rationale and consequences, [2]
# for a fuller rationale, and [3] for documentation that Click 8.3.1 was the
# basis for the vendored copy.
#
# [1] https://github.com/fastapi/typer/blob/0.26.0/docs/release-notes.md#breaking-changes
# [2] https://typer.tiangolo.com/tutorial/click
# [3] https://github.com/fastapi/typer/pull/1774
Provides:       bundled(python3dist(click)) = 8.3.1

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
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_mandir}/man1' \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}'

install --directory \
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
# This suffers from some combination of Python path issues in our test
# environment. It’s not worth going to great lengths to make it work.
k="${k-}${k+ and }not test_binary_stderr"

mkdir _stub
cat > _stub/coverage.py <<'EOF'
from subprocess import run
from sys import argv, executable, exit
if len(argv) < 3 or argv[1] != "run":
    exit(f"Unsupported arguments: {argv!r}")
exit(run([executable] + argv[2:]).returncode)
EOF
export PYTHONPATH="${PWD}/_stub:%{buildroot}%{python3_sitelib}"

%pytest -k "${k-}" ${ignore-} --numprocesses auto --verbose -rs


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
