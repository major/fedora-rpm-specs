%bcond_without  tests

%global         srcname     circuitbreaker

Name:           python-%{srcname}
Version:        2.0.0
Release:        %autorelease
Summary:        Python "Circuit Breaker" implementation

License:        BSD-3-Clause
URL:            https://github.com/fabfuel/circuitbreaker
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-mock)
%endif

%global _description %{expand:
This is a Python implementation of the "Circuit Breaker" Pattern.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.rst
%doc README.rst


%changelog
%autochangelog
