Name:           python-xeddsa
Version:        0.6.0~beta
Release:        11%{?dist}
Summary:        Python implementation of the XEdDSA signature scheme

License:        MIT
URL:            https://github.com/Syndace/%{name}
Source0:        https://github.com/Syndace/%{name}/archive/v%{version_no_tilde}.tar.gz
# For files and directories
%global version_main %(c=%version; echo $c|cut -d~ -f1)

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-cffi
BuildRequires:  python3-pynacl
# Required by setup.py
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
# For tests
BuildRequires:  python3-libnacl
BuildRequires:  python3-pytest

%description
This python library offers an open implementation of the XEdDSA
signature scheme.

It allows to create and verify EdDSA-compatible signatures using
public key and private key formats initially defined for the X25519
and X448 elliptic curve Diffie-Hellman functions.



%package     -n python3-xeddsa
Summary:        Python implementation of the XEdDSA signature scheme

%description -n python3-xeddsa
This python library offers an open implementation of the XEdDSA
signature scheme.

It allows to create and verify EdDSA-compatible signatures using
public key and private key formats initially defined for the X25519
and X448 elliptic curve Diffie-Hellman functions.



%prep
%autosetup -n %{name}-%{version_no_tilde}


%build
%py3_build


%install
%py3_install


%check
%pytest



%files -n python3-xeddsa
%license LICENSE
%doc README.md
# For arch-specific packages: sitearch
%{python3_sitearch}/xeddsa/
%{python3_sitearch}/_crypto_sign.abi3.so
%{python3_sitearch}/XEdDSA-%{version_main}-py%{python3_version}.egg-info/



%changelog
* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.6.0~beta-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0~beta-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 0.6.0~beta-9
- Add explicit build dependancy on python3-setuptools (RHBZ#2142039)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0~beta-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6.0~beta-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0~beta-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0~beta-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.0~beta-4
- Rebuilt for Python 3.10

* Mon Apr 19 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.6.0~beta-3
- Package Review RHBZ#1906287:
  - Use %%pytest to run tests suite

* Sun Feb 14 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.6.0~beta-2
- Package Review RHBZ#1906287:
  - Add more explicit description
  - Remove %%{srcname} variable truely used once
  - Fix the Version tag to match upstream version
  - Use %%{python3_version} in %%files section

* Wed Dec 09 2020 Matthieu Saulnier <fantom@fedoraproject.org> - 0.6.0-1
- Initial package
