# This package has support for integrating with Pydantic, including tests that
# require Pydantic; but both python-pydantic-core and python-pydantic use
# python-inline-snapshot in their tests, creating a dependency cycle. We can
# break it by disabling the Pydantic integration tests during bootstrapping.
%bcond bootstrap 0
# We may also need to disable Pydantic integration tests for a longer period,
# e.g. while waiting for Pydantic to support a new Python version.
%bcond pydantic_fti 0
%bcond pydantic_tests %[ %{without bootstrap} && %{without pydantic_fti} ]

Name:           python-inline-snapshot
Version:        0.32.7
Release:        %autorelease
Summary:        Golden master/snapshot/approval testing library

# SPDX
License:        MIT
URL:            https://github.com/15r10nk/inline-snapshot
Source:         %{pypi_source inline_snapshot}

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -g dev -x black,dirty-equals
BuildOption(install):   -l inline_snapshot

BuildArch:      noarch

%global common_description %{expand:
Golden master/snapshot/approval testing library which puts the values right
into your source code.}

%description %{common_description}


%package -n python3-inline-snapshot
Summary:        %{summary}

%description -n python3-inline-snapshot %{common_description}


%pyproject_extras_subpkg -n python3-inline-snapshot black,dirty-equals


%prep -a
%pyproject_patch_dependency black:drop_upper
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
%pyproject_patch_dependency mypy:ignore
%pyproject_patch_dependency pyright:ignore
%pyproject_patch_dependency coverage:ignore
%pyproject_patch_dependency coverage-enable-subprocess:ignore
%if %{without pydantic_tests}
%pyproject_patch_dependency pydantic:ignore
%endif


%check -a
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
ignore="${ignore-} --ignore=tests/test_typing.py"
%if %{without pydantic_tests}
ignore="${ignore-} --ignore=tests/test_pydantic.py"
%endif

# Ignore all DeprecationWarning messages; they may pop up from anywhere in our
# dependency tree, and this can cause tests that expect precisely-matching
# pytest output to fail unnecessarily.
export PYTHONWARNINGS='ignore::DeprecationWarning'

# Note that tests expect black-formatted generated code, and we cannot
# meaningingfully test the package without black; there would be 100+ test
# failures.

%pytest ${ignore-} -vv -rs


%files -n python3-inline-snapshot -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
