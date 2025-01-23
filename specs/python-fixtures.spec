# See bootstrapping instructions in python-testtools spec file.
%bcond bootstrap 0

Name:           python-fixtures
Version:        4.2.2
Release:        %autorelease
Summary:        Fixtures, reusable state for writing clean tests and more
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/testing-cabal/fixtures
Source:         %{pypi_source fixtures}
BuildArch:      noarch


%global _description %{expand:
Fixtures defines a Python contract for reusable state / support logic,
primarily for unit testing.  Helper and adaption logic is included to make it
easy to write your own fixtures using the fixtures contract.  Glue code is
provided that makes using fixtures that meet the Fixtures contract in unittest
compatible test cases easy and straight forward.}


%description
%{_description}


%package -n python3-fixtures
Summary:        %{summary}
BuildRequires:  python3-devel


%description -n python3-fixtures
%{_description}


%if %{without bootstrap}
%pyproject_extras_subpkg -n python3-fixtures streams
%endif


%prep
%autosetup -p1 -n fixtures-%{version}

%generate_buildrequires
%pyproject_buildrequires %{!?with_bootstrap:-t -x streams}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files fixtures


%check
%if %{with bootstrap}
# Exclude modules that import testtools, which we don't have available yet
# during bootstrap.
%pyproject_check_import -e 'fixtures.tests.*'
%else
%tox
%endif


%files -n python3-fixtures -f %{pyproject_files}
%license Apache-2.0 BSD
%doc README.rst GOALS NEWS


%changelog
%autochangelog
