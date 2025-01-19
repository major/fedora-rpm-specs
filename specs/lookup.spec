Summary: A graphical tool to search DNS for answers
Name: lookup
Version: 2.2.3
Release: 16%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: http://www.dnssec-tools.org/
Source0: https://www.dnssec-tools.org/download/%{name}-%{version}.tar.gz
Source1: COPYING-from-dnssec-tools.txt
Source2: lookup.desktop
Patch0:  lookup-1.11.p2-dont-double-install.patch

BuildRequires: qt-devel
BuildRequires: dnssec-tools-libs-devel >= 2.2
BuildRequires: openssl-devel
BuildRequires: desktop-file-utils
BuildRequires: glibc
BuildRequires: glibc-devel
BuildRequires: libnsl2
BuildRequires: libnsl2-devel
BuildRequires: make

%description
The lookup utility allows you to query the DNS for answers.  It
displays the results in a graphical tree structure, and checks the
answers for validity and conformance with DNSSEC.  The results are
color coded based on their DNSSEC status.

%prep
%setup -q 
%patch -P0 -p1

%build
%{qmake_qt4} PREFIX=/usr
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

rm -f %{buildroot}%{_datadir}/pixmap/lookup.xpm
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/
install -p -m 644 data/64x64/lookup.png %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/

rm -f %{buildroot}%{_datadir}/applications/hildon/lookup.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

mkdir -p %{buildroot}/%{_mandir}/man1
install -p -D -m 644 man/lookup.1 %{buildroot}/%{_mandir}/man1/lookup.1

%files
%doc COPYING
%doc %{_mandir}/man1/*
%{_bindir}/lookup
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/applications/lookup.desktop

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.3-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 29 2018 Wes Hardaker <wjhns174@hardakers.net> - 2.2.3-1
- match upstream version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1-9
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.1-4
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Sep 08 2014 Wes Hardaker <wjhns174@hardakers.net> - 2.1-1
- 2.1 release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 17 2013 Peter Robinson <pbrobinson@fedoraproject.org> 2.0-2
- Cleanup spec, fix build

* Thu Aug 08 2013 Wes Hardaker <wjhns174@hardakers.net> - 2.0-1
- 2.0 release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 15 2012 Wes Hardaker <wjhns174@hardakers.net> - 1.14-2
- new upstream 1.14 (no real changes though)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Wes Hardaker <wjhns174@hardakers.net> - 1.13-1
- upgrade to 1.13

* Tue Jan 31 2012 Wes Hardaker <wjhns174@hardakers.net> - 1.12-1
- Upgraded to version 1.12

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.p2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.11.p2-2
- don't double-install the binary

* Thu Oct 27 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.11.p2-1
- updated to upstream version with man page and COPYING file

* Fri Oct 21 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.11-3
- don't require dnssec-tools-libs; it's auto-required

* Fri Oct 21 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.11-2
- added a patch to fix the validator-config.h file path

* Fri Oct 21 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.11-1
- Initial version for approval


