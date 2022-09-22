# Enable tests everywhere except EPEL 9, where python-httpretty is not backported.
%if 0%{?rhel} >= 9
%bcond_with    tests
%else
%bcond_without tests
%endif


%global         srcname     adal
%global         forgeurl    https://github.com/AzureAD/azure-activedirectory-library-for-python
Version:        1.2.7
%global         tag         %{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Microsoft Azure Active Directory Authentication Library (ADAL) for Python

License:        MIT
URL:            %forgeurl
Source0:        %forgesource
# Fix tests with httpretty >= 0.9.0
Patch0:         %{name}-1.2.0-tests.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(httpretty)
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
Microsoft Azure Active Directory Authentication Library (ADAL) for Python.}

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
%doc README.md
%license LICENSE


%changelog
%autochangelog
