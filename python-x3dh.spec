Name:           python-x3dh
Version:        0.5.9~beta
Release:        10%{?dist}
Summary:        Python implementation of the X3DH key agreement protocol

License:        MIT
URL:            https://github.com/Syndace/%{name}
Source0:        https://github.com/Syndace/%{name}/archive/v%{version_no_tilde}.tar.gz
# backport from upstream
# commit: a38d9ecff2f2735b220d1416c003c757ac3eff57
# XEdDSA 0.6.0 has been released
Patch0:         XEdDSA-version-bump.patch
# For files and directories
%global version_main %(c=%version; echo $c|cut -d~ -f1)

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-cryptography
BuildRequires:  python3-xeddsa
# For tests
# "nacl" is also a runtime requirement
BuildRequires:  python3-pynacl
BuildRequires:  python3-pytest

%description
This python library offers an implementation of the Extended Triple
Diffie-Hellman key agreement protocol (X3DH).

X3DH establishes a shared secret key between two parties who mutually
authenticate each other based on public keys. X3DH provides forward
secrecy and cryptographic deniability.



%package     -n python3-x3dh
Summary:        Python implementation of the X3DH key agreement protocol
Requires:       python3-pynacl

%description -n python3-x3dh
This python library offers an implementation of the Extended Triple
Diffie-Hellman key agreement protocol (X3DH).

X3DH establishes a shared secret key between two parties who mutually
authenticate each other based on public keys. X3DH provides forward
secrecy and cryptographic deniability.



%prep
%autosetup -n %{name}-%{version_no_tilde}


%build
%py3_build


%install
%py3_install


%check
%pytest



%files -n python3-x3dh
%license LICENSE
%doc README.md
# For noarch packages: sitelib
%{python3_sitelib}/x3dh/
%{python3_sitelib}/X3DH-%{version_main}-py%{python3_version}.egg-info/



%changelog
* Fri Nov 25 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 0.5.9~beta-10
- Add explicit build dependancy on python3-setuptools (RHBZ#2142043)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9~beta-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.5.9~beta-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9~beta-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9~beta-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.9~beta-5
- Rebuilt for Python 3.10

* Sat Apr 17 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.5.9~beta-4
- Package Review RHBZ#1916510:
  - Short the Summary
  - Add nacl python module as build requirement and runtime requirement
  - Use %%pytest to run tests suite

* Sun Feb 14 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.5.9~beta-3
- Package Review RHBZ#1916510:
  - Add more explicit description
  - Remove %%{srcname} variable truely used once
  - Fix the Version tag to match upstream version
  - Use %%{python3_version} in %%files section

* Mon Jan 18 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.5.9-2
- Add Patch0 to fix installation package
  Backport from upstream commit: a38d9ecf  

* Thu Dec 10 2020 Matthieu Saulnier <fantom@fedoraproject.org> - 0.5.9-1
- Initial package
