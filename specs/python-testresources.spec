Name:           python-testresources
Version:        2.0.2
Release:        %autorelease
Summary:        Testresources, a pyunit extension for managing expensive test resources
# mostly Apache-2.0 or BSD-3-Clause
# testresources/tests/TestUtil.py is GPL-2.0-or-later
License:        (Apache-2.0 OR BSD-3-Clause) AND GPL-2.0-or-later
URL:            https://github.com/testing-cabal/testresources
Source:         %{pypi_source testresources}
BuildArch:      noarch

%global _description %{expand:
testresources: extensions to python unittest to allow declarative use
of resources by test cases.}


%description %{_description}


%package -n python3-testresources
Summary:        %{summary}
BuildRequires:  python3-devel


%description -n python3-testresources %{_description}


%prep
%setup -q -n testresources-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l testresources


%check
%{python3} -m testtools.run testresources.tests.test_suite


%files -n python3-testresources -f %{pyproject_files}
# AUTHORS and COPYING are already included and marked as licenses, but
# Apache-2.0 and BSD are not.
%license Apache-2.0 BSD
%doc README.rst NEWS doc


%changelog
%autochangelog
