%global _hardened_build 1

Summary:       Network traffic recorder
Name:          tcpflow
Version:       1.6.1
Release:       12%{?dist}
License:       GPL-1.0-or-later
URL:           https://github.com/simsong/tcpflow
Source0:       http://digitalcorpora.org/downloads/tcpflow/tcpflow-%{version}.tar.gz
Patch0:        tcpflow-1.6.1-format.patch
Patch1:        tcpflow-1.6.1-uint.patch
BuildRequires: make
BuildRequires: boost-devel
#BuildRequires: bzip2-devel
BuildRequires: cairo-devel
BuildRequires: gcc-c++
BuildRequires: libpcap-devel
BuildRequires: openssl-devel
BuildRequires: zlib-devel
%description
tcpflow is a program that captures data transmitted as part of TCP
connections (flows), and stores the data in a way that is convenient
for protocol analysis or debugging. A program like 'tcpdump' shows a
summary of packets seen on the wire, but usually doesn't store the
data that's actually being transmitted. In contrast, tcpflow
reconstructs the actual data streams and stores each flow in a
separate file for later analysis.

%prep
%autosetup -p1

%build
export CPPFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} INSTALL='install -p' install

%check
make check || :

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS
%{_bindir}/tcpflow
%{_mandir}/man1/tcpflow.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.1-10
- convert license to SPDX

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 02 2023 Terje Rosten <terje.rosten@ntnu.no> - 1.6.1-7
- Add patch to fix FTBFS

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.6.1-3
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb 20 2021 Terje Rosten <terje.rosten@ntnu.no> - 1.6.1-1
- 1.6.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.5.0-4
- Get 1.5.2 diff from github

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 27 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.5.0-2
- Still issue with check

* Mon Aug 27 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.5.0-1
- 1.5.0 (includes fix for rhbz#1614046

* Mon Jul 16 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.4.5-9
- Add C++ compiler

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Jonathan Wakely <jwakely@redhat.com> - 1.4.5-2
- Rebuilt for Boost 1.63
- Use compat-openssl10 (#1417755)

* Thu Aug 25 2016 Jason Taylor <jtfas90@gmail.com> - 1.4.5-1
- updated to latest upstream release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 1.4.4-11
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.4.4-10
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.4.4-8
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4.4-6
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.4.4-5
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.4.4-2
- Rebuild for boost 1.55.0

* Sat Jan 11 2014 Terje Rosten <terje.rosten@ntnu.no> - 1.4.4-1
- 1.4.4

* Tue Nov 05 2013 Terje Rosten <terje.rosten@ntnu.no> - 1.4.0-2
- Add patches to build on arm

* Mon Oct 21 2013 Terje Rosten <terje.rosten@ntnu.no> - 1.4.0-1
- 1.4.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 Terje Rosten <terje.rosten@ntnu.no> - 1.3.0-1
- 1.3.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 11 2012 Terje Rosten <terje.rosten@ntnu.no> - 1.2.4-1
- 1.2.4
- New home

* Sat Mar 31 2012 Terje Rosten <terje.rosten@ntnu.no> - 1.2.3-1
- 1.2.3

* Sun Mar 25 2012 Terje Rosten <terje.rosten@ntnu.no> - 1.2.2-1
- 1.2.2

* Sun Mar 25 2012 Terje Rosten <terje.rosten@ntnu.no> - 1.2.1-1
- 1.2.1

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for c++ ABI breakage

* Thu Feb 16 2012 Dan Horák <dan[at]danny.cz> - 1.1.0-2
- fix build on arches without cpuid instruction

* Mon Jan 30 2012 Terje Rosten <terje.rosten@ntnu.no> - 1.1.0-1
- 1.1.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.0.4-1
- Fix issue with expressions

* Fri Oct 21 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.0.1-1
- New major version
- Project has moved to new site and maintainer

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 14 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.21-8
- add patch from bz #556683

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-7
- rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-6
- rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.21-5
- fix source url

* Fri May  2 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.21-4
- fix color patch (bz #444833)

* Sat Feb  9 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.21-3
- rebuild

* Tue Nov 27 2007 Terje Rosten <terje.rosten@ntnu.no> - 0.21-2
- fix license

* Tue Nov 27 2007 Terje Rosten <terje.rosten@ntnu.no> - 0.21-1
- initial package

