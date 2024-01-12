%bcond_without check

Name:           python-authlib
Version:        1.3.0
Release:        %autorelease
Summary:        Build OAuth and OpenID Connect servers in Python

License:        BSD-3-Clause
URL:            https://github.com/lepture/authlib
Source0:        %{url}/archive/v%{version}/authlib-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Python library for building OAuth and OpenID Connect servers. JWS, JWK, JWA,
JWT are included.}

%description %_description

%package -n     python3-authlib
Summary:        %{summary}

%description -n python3-authlib %_description


%prep
%autosetup -p1 -n authlib-%{version}


%generate_buildrequires
%pyproject_buildrequires -e %{toxenv},%{toxenv}-clients,%{toxenv}-flask,%{toxenv}-django,%{toxenv}-jose


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files authlib


%if %{with check}
%check
%tox
%endif


%files -n python3-authlib -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
