%global srcname authlib
%global pypi_name Authlib

Name:           python-%{srcname}
Version:        1.2.1
Release:        %autorelease
Summary:        Build OAuth and OpenID Connect servers in Python

License:        BSD
URL:            https://github.com/lepture/authlib
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Python library for building OAuth and OpenID Connect servers. JWS, JWK, JWA,
JWT are included.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -e %{toxenv},%{toxenv}-clients,%{toxenv}-flask,%{toxenv}-django,%{toxenv}-jose


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files authlib


%check
%tox


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
