%global srcname pyaes


Name:       python-%{srcname}
Version:    1.6.1
Release:    14%{?dist}
Summary:    Pure-Python implementation of AES block-cipher and common modes of operation
License:    MIT

URL:        https://github.com/ricmoo/%{srcname}
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:     python-pyaes-0001-Use-relative-imports-during-tests.patch
Patch2:     %{url}/pull/51.patch
BuildArch:  noarch


%description
A pure-Python implementation of the AES block cipher algorithm and the common
modes of operation (CBC, CFB, CTR, ECB and OFB).


%package -n python3-%{srcname}
Summary:  %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pycrypto)
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
A pure-Python implementation of the AES block cipher algorithm and the common
modes of operation (CBC, CFB, CTR, ECB and OFB).


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pyaes


%check
%pyproject_check_import
%{__python3} tests/test-aes.py
%{__python3} tests/test-blockfeeder.py
%{__python3} tests/test-util.py


%files -n python3-%{srcname}  -f %{pyproject_files}
%license LICENSE.txt
%doc README.md


%changelog
%autochangelog
