Name: cmconvert
Summary: CacheMate import file converter 
Version: 1.9.6
Release: 32%{dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.smittyware.com/palm/cachemate/tools.php
Source0: http://www.smittyware.com/download/%{name}-%{version}.tar.gz
BuildRequires: gcc-c++
BuildRequires: expat-devel
BuildRequires: zziplib-devel
BuildRequires: zlib-devel
BuildRequires: make


%description 
This program is used to convert EasyGPS XML file formats (LOC and GPX) to
a format that can be installed onto a Palm OS device and imported into
CacheMate.  Options are also available to list waypoints contained in an
XML file, and selectively convert specified waypoints.

%prep 
%setup -q 

%build 
%configure
make %{?_smp_mflags}

%install 
rm -fr %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"

%files 
%doc ChangeLog README
%license COPYING
%{_bindir}/cmconvert
%{_mandir}/man1/cmconvert.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.9.6-31
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Patrick C. F. Ernzer <cmconvert.spec@pcfe.net> 1.9.6-17
- add BuildRequires: gcc

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.9.6-9
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb 02 2015 Patrick C. F. Ernzer <cmconvert.spec@pcfe.net> 1.9.6-8
- COPYING now listed as a license

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Patrick C. F. Ernzer <cmconvert.spec@pcfe.net> 1.9.6-1
- update to 1.9.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Patrick C. F. Ernzer <cmconvert.spec@pcfe.net> 1.9.5-5
- incorporate feedback from Bug 475000 Comments #11
- also fixed wron date on changelog entries for -3 and -2

* Wed Dec 31 2008 Patrick C. F. Ernzer <cmconvert.spec@pcfe.net> 1.9.5-4
- incorporate feedback from Bug 475000 Comment #5

* Thu Dec 11 2008 Patrick C. F. Ernzer <cmconvert.spec@pcfe.net> 1.9.5-3
- incorporate feedback from Bug 475000 Comments #1 and #2

* Fri Dec 05 2008 Patrick C. F. Ernzer <cmconvert.spec@pcfe.net> 1.9.5-2
- fix rpmlint warnings and errors

* Fri Nov 10 2006 Patrick C. F. Ernzer <cmconvert.spec@pcfe.net> 1.9.5-1
- update to 1.9.5

* Mon Jul 10 2006 Patrick C. F. Ernzer <cmconvert.spec@pcfe.net> 1.9.4-1
- update to 1.9.4

* Sat Apr 22 2006 Patrick C. F. Ernzer <cmconvert.spec@pcfe.net> 1.9.3-1
- update to 1.9.3

* Mon May 09 2005 Patrick C. F. Ernzer <cmconvert.spec@pcfe.net> 1.9.0-1
- first build
