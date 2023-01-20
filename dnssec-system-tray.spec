Summary: System Tray for monitoring log files for DNSSEC errors
Name: dnssec-system-tray
Version: 2.1
Release: 20%{?dist}
License: BSD
URL: http://www.dnssec-tools.org/
Source0: https://www.dnssec-tools.org/download/%{name}-%{version}.tar.gz
Source1: dnssec-system-tray.desktop
# generated from a larger PNG inside the source code
Source2: dnssec-system-tray-64x64.png


BuildRequires: qt-devel
BuildRequires: desktop-file-utils
BuildRequires: make

%description
A simply system-tray application that monitors log files (eg libval,
or bind/named logfiles) for DNSSEC error messages that should be
displayed to the user.

%prep
%setup -q 

%build
%{qmake_qt4} PREFIX=/usr
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make install INSTALL_ROOT=%{buildroot}

%{__mkdir_p} %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/
%{__install} -p -m 644 %{SOURCE2} %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%{__mkdir_p} %{buildroot}/%{_mandir}/man1
%{__install} -p -D -m 644 man/dnssec-system-tray.1 %{buildroot}/%{_mandir}/man1/dnssec-system-tray.1

%files
%doc COPYING
%doc %{_mandir}/man1/*
%{_bindir}/dnssec-system-tray
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/applications/dnssec-system-tray.desktop

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-12
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

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 15 2012 Wes Hardaker <wjhns174@hardakers.net> - 1.14-1
- update to upstream 1.14 release with no real major changes

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Wes Hardaker <wjhns174@hardakers.net> - 1.13-1
- update to new upstream

* Tue Jan 31 2012 Wes Hardaker <wjhns174@hardakers.net> - 1.12-1
- Upgraded to version 1.12

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.p2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 27 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.11.p2-1
- updated to upstream version with man page and COPYING file

* Mon Oct 17 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.11-2
- initial version for approval

