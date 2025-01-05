# This package has support for integrating with Pydantic, including tests that
# require Pydantic; but both python-pydantic-core and python-pydantic use
# python-inline-snapshot in their tests, creating a dependency cycle. We can
# break it by disabling the Pydantic integration tests during bootstrapping.
%bcond bootstrap 0
%bcond pydantic_tests %{without bootstrap}

Name:           python-inline-snapshot
Version:        0.18.2
Release:        %autorelease
Summary:        Golden master/snapshot/approval testing library

# SPDX
License:        MIT
URL:            https://github.com/15r10nk/inline-snapshot
Source:         %{pypi_source inline_snapshot}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  tomcli

%global common_description %{expand:
Golden master/snapshot/approval testing library which puts the values right
into your source code.}

%description %{common_description}


%package -n python3-inline-snapshot
Summary:        %{summary}

%description -n python3-inline-snapshot %{common_description}


%prep
%autosetup -n inline_snapshot-%{version} -p1

# Remove linters, typecheckers, formatters, coverage analysis tools, etc. from
# the “dev” dependency group so we can use it to generate BuildRequires.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem --no-first --type regex \
    dependency-groups.dev '(mypy|pyright|coverage)\b.*'
%if %{without pydantic_tests}
tomcli set pyproject.toml lists delitem --no-first --type regex \
    dependency-groups.dev '(pydantic)\b.*'
%endif


%generate_buildrequires
%pyproject_buildrequires -g dev


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l inline_snapshot


%check
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
ignore="${ignore-} --ignore=tests/test_typing.py"
%if %{without pydantic_tests}
ignore="${ignore-} --ignore=tests/test_pydantic.py"
%endif

# Ignore all DeprecationWarning messages; they may pop up from anywhere in our
# dependency tree, and this can cause tests that expect precisely-matching
# pytest output to fail unnecessarily.
export PYTHONWARNINGS='ignore::DeprecationWarning'

%pytest ${ignore-} -vv -rs


%files -n python3-inline-snapshot -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
