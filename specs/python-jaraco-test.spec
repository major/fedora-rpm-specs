Name:           python-jaraco-test
Version:        5.6.0
Release:        %autorelease
Summary:        Testing support by jaraco
License:        MIT
URL:            https://github.com/jaraco/jaraco.test
Source:         %{pypi_source jaraco_test}

BuildArch:      noarch
BuildRequires:  python3-devel
# needs test module which is part of python stdlib
BuildRequires:  python3-test

%global _description %{expand:
Testing support by jaraco.}

%description %_description

%package -n     python3-jaraco-test
Summary:        %{summary}
Requires:       python3-test

%description -n python3-jaraco-test %_description


%prep
%autosetup -p1 -n jaraco_test-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l jaraco


%check
%{py3_test_envvars} %{python3} -m pytest -v


%files -n python3-jaraco-test -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
