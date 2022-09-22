# Enable tests everywhere except EPEL 9, where python-httpretty is not backported.
%if 0%{?el9} || 0%{?centos} >= 9
%bcond_with    tests
%else
%bcond_without tests
%endif


%global         srcname     msrestazure
%global         forgeurl    https://github.com/Azure/msrestazure-for-python/
Version:        0.6.4
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        The runtime library "msrestazure" for AutoRest generated Python clients

License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel


%if %{with tests}
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(httpretty)
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
The runtime library "msrest" for AutoRest generated Python clients}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%if %{with tests}
%check
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE.md


%changelog
%autochangelog
