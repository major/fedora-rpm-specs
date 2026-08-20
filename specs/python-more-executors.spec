%global srcname more-executors
%global srcname_py more_executors

Summary: A library of composable Python executors and futures
Name: python-%{srcname}
Version: 2.11.4
Release: %autorelease
License: GPL-3.0-or-later
BuildArch: noarch
URL: https://github.com/rohanpm/%{srcname}
Source0: %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz


%description
This library is intended for use with the concurrent.futures module.
It includes a collection of Executor implementations in order to extend
the behavior of Future objects.

%package -n python3-%{srcname}
Summary:	%{summary}

BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros   
BuildRequires: python3-setuptools
BuildRequires: python3-wheel          
BuildRequires: python3-pip 
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pyhamcrest)
BuildRequires: python3dist(six)
BuildRequires: python3dist(mypy)

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This library is intended for use with the concurrent.futures module.
It includes a collection of Executor implementations in order to extend
the behavior of Future objects.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%pyproject_wheel

%generate_buildrequires
%pyproject_buildrequires

%install
%pyproject_install

%check
%pytest -v -k "not test_or_propagate_traceback"

%files -n python3-%{srcname}
%doc README.md
%license LICENSE

%{python3_sitelib}/%{srcname_py}/
%{python3_sitelib}/%{srcname_py}-%{version}.dist-info/

%changelog
%autochangelog