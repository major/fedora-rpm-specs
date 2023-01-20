Summary: DNS Visualization Tool
Name: dnssec-nodes
Version: 2.1
Release: 19%{?dist}
License: BSD
URL: http://www.dnssec-tools.org/
Source0: https://www.dnssec-tools.org/download/%{name}-%{version}.tar.gz
Source1: dnssec-nodes.desktop

BuildRequires: gcc-c++
BuildRequires: qt-devel
BuildRequires: dnssec-tools-libs-devel >= 2.2
BuildRequires: openssl-devel
BuildRequires: desktop-file-utils
BuildRequires: libpcap-devel
BuildRequires: libnsl2-devel
BuildRequires: make
Requires: dnssec-tools-libs >= 2.2

%description
A graphical DNS visualization application, specializing in DNSSEC.
The DNSSEC-Nodes application is a graphical debugging utility that
allows administrators to watch the data being logged into a libval or
bind logging file.

%prep
%setup -q

%build
%{qmake_qt4} PREFIX=/usr
make %{?_smp_mflags} V=1

%install
make install INSTALL_ROOT=%{buildroot}

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -p -m 644 icons/dnssec-nodes.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}/%{_mandir}/man1
install -p -D -m 644 man/dnssec-nodes.1 %{buildroot}/%{_mandir}/man1/dnssec-nodes.1

%files
%license COPYING
%{_bindir}/dnssec-nodes
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/applications/dnssec-nodes.desktop
%doc %{_mandir}/man1/*

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Tom Callaway <spot@fedoraproject.org> - 2.1-12
- none of the "2.2.3" builds ever succeeded. no evidence of 2.2.3 sources.
  so... we go back to 2.1.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1-9
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.1-4
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Sep 08 2014 Wes Hardaker <wjhns174@hardakers.net> - 2.1-1
- 2.1 release

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 17 2013 Peter Robinson <pbrobinson@fedoraproject.org> 2.0-3
- Actually upload the 2.0 source, cleanup spec

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 20 2013 Wes Hardaker <wjhns174@hardakers.net> - 2.0-1
- 2.0 release

* Fri Oct 12 2012 Wes Hardaker <wjhns174@hardakers.net> - 1.14-1
- new upstream release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Wes Hardaker <wjhns174@hardakers.net> - 1.13-1
- upgrade to 1.13

* Sat May 19 2012 Wes Hardaker <wjhns174@hardakers.net> - 1.12-2
- require dnssec-tools 1.12.1

* Tue Jan 31 2012 Wes Hardaker <wjhns174@hardakers.net> - 1.12-1
- Upgraded to version 1.12

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.p2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 27 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.11.p2-1
- Update to better upstream version with a man page and COPYING file

* Mon Oct 17 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.11.p1-2
- Update to reflect needed changes for review

* Thu Oct 13 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.11.p1-1
- Initial version
