Name:           python-xeddsa
Version:        1.1.0
Release:        7%{?dist}
Summary:        Python implementation of the XEdDSA signature scheme

License:        MIT
URL:            https://github.com/Syndace/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          relax-setuptools.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  libxeddsa-devel
BuildRequires:  libsodium-devel
# docs
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-autodoc-typehints)
BuildRequires:  texinfo

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
%autosetup -n %{name}-%{version}



%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd docs/
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook xeddsa.texi
popd # texinfo
popd # docs

%install
%pyproject_install
%pyproject_save_files -l xeddsa

# Install docbook docs
install -pDm0644 docs/texinfo/xeddsa.xml \
 %{buildroot}%{_datadir}/help/en/python-xeddsa/xeddsa.xml

%files -n python3-xeddsa  -f %{pyproject_files}
%doc README.md
%{python3_sitearch}/_libxeddsa.abi3.so
%dir  %{_datadir}/help/en/
%lang(en) %{_datadir}/help/en/python-xeddsa/


%changelog
* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 1.1.0-7
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 1.1.0-6
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jun 08 2025 Python Maint <python-maint@redhat.com> - 1.1.0-4
- Rebuilt for Python 3.14

* Sun Jun 08 2025 Benson Muite <fed500@fedoraproject.org> - 1.1.0-3
- Remove unnecessary Requires

* Sun Jun 08 2025 Python Maint <python-maint@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.14

* Sun Jun 08 2025 Benson Muite <fed500@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0
- Use newer packaging macros
- Build documentation

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 1.0.3-3
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Sep 19 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3
- Cleanup BuildRequires list

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.0.2-4
- Rebuilt for Python 3.13

* Mon May 20 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 1.0.2-3
- Move the Requires tag into the python3 subpackage

* Sun May 12 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 1.0.2-2
- Add missing Requires tag

* Wed May 8 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2
- Remove %%check section because it is useless
- Disable debuginfo subpackage because it is empty

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0~beta-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0~beta-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0~beta-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

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
