%global srcname  Cerberus
%global slugname cerberus
%global pkgname  python-cerberus
%global forgeurl https://github.com/pyeve/cerberus

%global common_description %{expand:
Cerberus is a lightweight and extensible data validation library for Python.

Cerberus provides type checking and other base functionality out of the box
and is designed to be non-blocking and easily extensible, allowing for custom
validation. It has no dependancies and is thoroughly tested.
}

%bcond_without tests

Name:           %{pkgname}
Version:        1.3.4
%forgemeta
# Remove -b4 when upgrading to a newer version:
Release:        %autorelease -b4
Summary:        Lightweight, extensible data validation library for Python
License:        ISC
URL:            %{forgeurl}
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%description %{common_description}

%package -n python3-%{slugname}
Summary: %{summary}

%description -n python3-%{slugname} %{common_description}

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:-x test}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{slugname}

%if %{with tests}
%check
%pytest -vv %{slugname}/tests
%endif

%files -n python3-%{slugname}
%license LICENSE
%doc README.rst AUTHORS CHANGES.rst
%{python3_sitelib}/%{srcname}-%{version}.dist-info
%{python3_sitelib}/%{slugname}/

%changelog
%autochangelog