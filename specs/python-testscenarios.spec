Name:           python-testscenarios
Version:        0.6.1
Release:        %autorelease
Summary:        Testscenarios, a pyunit extension for dependency injection
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/testing-cabal/testscenarios
Source:         %{pypi_source testscenarios}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
testscenarios provides clean dependency injection for python unittest style
tests. This can be used for interface testing (testing many implementations via
a single test suite) or for classic dependency injection (provide tests with
dependencies externally to the test code itself, allowing easy testing in
different situations).}


%description %{_description}


%package -n python3-testscenarios
Summary:        %{summary}


%description -n python3-testscenarios %{_description}


%prep
%autosetup -p1 -n testscenarios-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files testscenarios


%check
%pyproject_check_import
%{py3_test_envvars} %{python3} -m testtools.run testscenarios.test_suite


%files -n python3-testscenarios -f %{pyproject_files}
%license Apache-2.0 BSD
%doc GOALS HACKING NEWS README.rst doc/


%changelog
%autochangelog
