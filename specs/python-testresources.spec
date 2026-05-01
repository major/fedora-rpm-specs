Name:           python-testresources
Version:        2.1.2
Release:        %autorelease
BuildArch:      noarch
Summary:        Testresources, a pyunit extension for managing expensive test resources
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/testing-cabal/testresources
Source:         %{url}/archive/%{version}/testresources-%{version}.tar.gz

%global _description %{expand:
testresources: extensions to python unittest to allow declarative use
of resources by test cases.}


%description %{_description}


%package -n python3-testresources
Summary:        %{summary}
BuildRequires:  python3-devel


%description -n python3-testresources %{_description}


%prep
%autosetup -p 1 -n testresources-%{version}


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -x test


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l testresources


%check
%{python3} -m testtools.run tests.test_suite


%files -n python3-testresources -f %{pyproject_files}
%doc README.rst NEWS


%changelog
%autochangelog
