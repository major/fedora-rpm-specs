Name:           python-x3dh
Version:        1.2.0
Release:        2%{?dist}
Summary:        Python implementation of the X3DH key agreement protocol

License:        MIT
URL:            https://github.com/Syndace/%{name}
Source:         https://github.com/Syndace/%{name}/archive/v%{version}/python-x3dh-%{version}.tar.gz
# https://github.com/Syndace/python-x3dh/commit/7e90648971262d2ce8335052bd046434d5d99580
Patch:          python-dirs.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# For tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)

# for docs
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-autodoc-typehints
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  texinfo

%global _description %{expand:
This python library offers an implementation of the Extended Triple
Diffie-Hellman key agreement protocol (X3DH).

X3DH establishes a shared secret key between two parties who mutually
authenticate each other based on public keys. X3DH provides forward
secrecy and cryptographic deniability.}

%description %_description


%package     -n python3-x3dh
Summary:        Python implementation of the X3DH key agreement protocol

%description -n python3-x3dh
This python library offers an implementation of the Extended Triple
Diffie-Hellman key agreement protocol (X3DH).

X3DH establishes a shared secret key between two parties who mutually
authenticate each other based on public keys. X3DH provides forward
secrecy and cryptographic deniability.

%package docs
Summary: Documentation for python-twomemo
BuildArch: noarch

%description docs %_description


%prep
%autosetup -n %{name}-%{version}

 
%generate_buildrequires
%pyproject_buildrequires -x docs

%build
%pyproject_wheel
pushd docs
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook x3dh.texi
popd # texinfo
popd # docs

%install
%pyproject_install
%pyproject_save_files -l x3dh
# Install docbook docs
install -pDm0644 docs/texinfo/x3dh.xml \
 %{buildroot}%{_datadir}/help/en/python-x3dh/x3dh.xml

%files -n python3-x3dh -f %{pyproject_files}

%files docs
%license LICENSE
%dir  %{_datadir}/help/en/
%lang(en) %{_datadir}/help/en/python-x3dh/


%changelog
* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 1.2.0-2
- Rebuilt for Python 3.14.0rc3 bytecode

* Mon Sep 01 2025 Benson Muite <fed500@fedoraproject.org> - 1.2.0-1
- Update to release 1.2.0
- Use newer packaging macros
- Package documentation

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 1.0.4-5
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 1.0.4-3
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Sep 19 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.0.3-2
- Rebuilt for Python 3.13

* Mon May 20 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3
- Fix typo in %%changelog
- Remove patch and tests suite

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9~beta-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9~beta-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9~beta-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.5.9~beta-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9~beta-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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
