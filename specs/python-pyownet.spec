Name:		python-pyownet
Version:	0.10.0.post1
Release:	4%{?dist}
Summary:	Pure python client library for accessing OWFS via owserver protocol

License:	LGPL-3.0-or-later
URL:		https://github.com/miccoli/pyownet
Source0:	%{pypi_source pyownet}
# from https://github.com/miccoli/pyownet/commit/1b2e8d10c6b4b3553b7c80eafbc35871658ddec1
Patch0:		python-pyownet-001-declarative-build.patch
Patch1:		python-pyownet-002-remove-www.google.com-from-tests.patch
# from https://github.com/onkelbeh/HomeAssistantRepository/tree/master/dev-python/pyownet/files
# temporary before 0.11.0 is released
# setup.py chunk manualy removed
Patch2:         python-pyownet-003-2to3.patch

BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pip
BuildRequires:	python3-pytest
BuildRequires:	python3-wheel

%global _description %{expand:
Pyownet is a pure python package that allows network client access to the OWFS
1-Wire File System via an owserver and the owserver network protocol.}

%description %_description

%package -n python3-pyownet
Summary:	Pure python client library for accessing OWFS via owserver protocol

%description -n python3-pyownet %_description

%prep
%autosetup -p1 -n pyownet-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files -n python3-pyownet
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/pyownet/
%{python3_sitelib}/pyownet-%{version}.dist-info/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0.post1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 05 2024 Tomasz Torcz <ttorcz@fedoraproject.org> - 0.10.0.post1-3
- re-include 2to3 patch lost during review

* Thu Dec 28 2023 Tomasz Torcz <ttorcz@fedoraproject.org> - 0.10.0.post1-2
- adjust for building with wheel

* Tue Jan 31 2023 Tomasz Torcz <ttorcz@fedoraproject.org> - 0.10.0.post1-1
- initial package version
