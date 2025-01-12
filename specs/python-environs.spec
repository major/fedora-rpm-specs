%global srcname environs

%global _description %{expand: \
Environs is a Python library for parsing environment variables.
It allows you to store configuration separate from your code, as per
The Twelve-Factor App (https://12factor.net/config) methodology.}

Name:       python-%{srcname}
Version:    14.1.0
Release:    %autorelease
Summary:    Python library for parsing environment variables
License:    MIT
URL:        https://github.com/sloria/%{srcname}
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description %{_description}

%generate_buildrequires
%pyproject_buildrequires -x tests

%package -n python3-%{srcname}
Summary:    Python library for parsing environment variables

%description -n python3-%{srcname}
%{_description}

%pyproject_extras_subpkg -n python3-%{srcname} django

%package -n python3-%{srcname}-examples
Summary:    Example files for Environs
BuildArch:  noarch
%description -n python3-%{srcname}-examples
%{_description}

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md CONTRIBUTING.md

%files -n python3-%{srcname}-examples
%license LICENSE
%doc README.md CHANGELOG.md CONTRIBUTING.md examples


%changelog
%autochangelog
