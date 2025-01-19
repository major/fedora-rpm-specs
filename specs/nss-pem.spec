%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build

Name:       nss-pem
Version:    1.1.0
Release:    8%{?dist}
Summary:    PEM file reader for Network Security Services (NSS)

# See README for details
# list.h - GPL-2.0-only
# *      - MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later
License:    GPL-2.0-only AND (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later)
URL:        https://github.com/kdudka/nss-pem
Source0:    https://github.com/kdudka/nss-pem/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz
Source1:    https://github.com/kdudka/nss-pem/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz.asc

# gpg --keyserver pgp.mit.edu --recv-key 992A96E075056E79CD8214F9873DB37572A37B36
# gpg --output kdudka.pgp --armor --export kdudka@redhat.com
Source2:    kdudka.pgp

BuildRequires: cmake3
BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: make
BuildRequires: nss-pkcs11-devel

# require at least the version of nss that nss-pem was built against (#1428965)
Requires: nss%{?_isa} >= %(nss-config --version 2>/dev/null || echo 0)

%description
PEM file reader for Network Security Services (NSS), implemented as a PKCS#11
module.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build
%cmake3 -S src
%cmake3_build

%install
%cmake3_install

%check
%ctest3

%files
%{_libdir}/libnsspem.so
%license COPYING.{GPL,MPL}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 04 2024 Lukáš Zaoral <lzaoral@redhat.com> - 1.1.0-6
- fix typo in the license expression

* Thu Jul 04 2024 Lukáš Zaoral <lzaoral@redhat.com> - 1.1.0-5
- migrate to SPDX license format

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb 17 2023 Kamil Dudka <kdudka@redhat.com> 1.1.0-1
- update to latest upstream release

* Fri Feb 03 2023 Kamil Dudka <kdudka@redhat.com> 1.0.9-1
- update to latest upstream bugfix release (#2121064)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 15 2022 Kamil Dudka <kdudka@redhat.com> 1.0.8-4
- verify GPG signature of upstream tarball when building the package

* Thu Mar 03 2022 Kamil Dudka <kdudka@redhat.com> 1.0.8-3
- make the package build in up2date Fedora rawhide buildroot

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 17 2021 Kamil Dudka <kdudka@redhat.com> 1.0.8-1
- update to latest upstream bugfix release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Kamil Dudka <kdudka@redhat.com> 1.0.7-1
- update to latest upstream bugfix release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jul 30 2020 Kamil Dudka <kdudka@redhat.com> 1.0.6-3
- fix build failure on Fedora rawhide

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 13 2020 Kamil Dudka <kdudka@redhat.com> 1.0.6-1
- update to latest upstream bugfix release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 07 2019 Kamil Dudka <kdudka@redhat.com> 1.0.5-1
- update to latest upstream bugfix release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 09 2018 Kamil Dudka <kdudka@redhat.com> 1.0.4-1
- update to latest upstream bugfix release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 09 2018 Kamil Dudka <kdudka@redhat.com>> - 1.0.3-9
- nss-pem is no longer a multilib package, ease the f27->f28 upgrade (#1553646)

* Mon Feb 19 2018 Kamil Dudka <kdudka@redhat.com>> - 1.0.3-8
- add explicit BR for the gcc compiler

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Kamil Dudka <kdudka@redhat.com> 1.0.3-6
- release bump needed to fix #1500655

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 13 2017 Kamil Dudka <kdudka@redhat.com> 1.0.3-3
- release bump

* Mon Mar 06 2017 Kamil Dudka <kdudka@redhat.com> 1.0.3-2
- require at least the version of nss that nss-pem was built against (#1428965)

* Wed Mar 01 2017 Kamil Dudka <kdudka@redhat.com> 1.0.3-1
- update to latest upstream bugfix release

* Wed Feb 22 2017 Kamil Dudka <kdudka@redhat.com> 1.0.2-4
- rebuild against nss-3.29.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 22 2016 Kamil Dudka <kdudka@redhat.com> 1.0.2-2
- explicitly conflict with all nss builds with bundled nss-pem (#1347336)

* Thu Jun 16 2016 Kamil Dudka <kdudka@redhat.com> 1.0.2-1
- packaged for Fedora
