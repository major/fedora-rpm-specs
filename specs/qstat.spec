%global commit fab391255297c437fb84676104508a8b489fa8bf
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary: Real-time Game Server Status for FPS game servers
Name: qstat
Version: 2.17
Release: 10%{?dist}
License: Artistic-2.0
URL: https://github.com/multiplay/qstat
Source0: https://github.com/multiplay/qstat/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildRequires: make
BuildRequires: autoconf, automake, libtool

%description
QStat is a command-line program that gathers real-time statistics
from Internet game servers. Most supported games are of the first
person shooter variety (Quake, Half-Life, etc)

%prep
%setup -q -n %{name}-%{commit}
sed -i 's/m4_esyscmd\(.*\),/%{version},/g' configure.ac
autoreconf -ifv

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

# Rename binary as discussed in https://bugzilla.redhat.com/show_bug.cgi?id=472750
mv %{buildroot}%{_bindir}/qstat %{buildroot}%{_bindir}/quakestat

# prepare for including to documentation
find template -name "Makefile*" -type f | xargs rm -f

%files
%doc CHANGES.txt
%license LICENSE.txt
%doc contrib.cfg info/*.txt qstatdoc.html template/
%config(noreplace) %{_sysconfdir}/qstat.cfg
%{_bindir}/quakestat

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 2.17-8
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Tom Callaway <spot@fedoraproject.org> 2.17-1
- update to 2.17

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-14.20200131gitd1469ab
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-13.20200131gitd1469ab
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-12.20200131gitd1469ab
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Tom Callaway <spot@fedoraproject.org> - 2.15-11.20200131gitd1469ab
- update to latest git to fix FTBFS

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-10.20150619gita60436
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-9.20150619gita60436
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-8.20150619gita60436
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-7.20150619gita60436
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-6.20150619gita60436
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-5.20150619gita60436
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-4.20150619gita60436
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-3.20150619gita60436
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-2.20150619gita60436
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Tom Callaway <spot@fedoraproject.org> - 2.15-1.20150619gita60436
- upstream bumped to 2.15 in git, new upstream home

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-19.20131212svn382
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-18.20131212svn382
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-17.20131212svn382
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 12 2013 Tom Callaway <spot@fedoraproject.org> - 2.11-16.20131212svn382
- update to svn 382

* Thu Dec 12 2013 Tom Callaway <spot@fedoraproject.org> - 2.11-15.20080912svn311
- apply fixes for format-security issues

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-14.20080912svn311
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-13.20080912svn311
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-12.20080912svn311
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-11.20080912svn311
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-10.20080912svn311
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 08 2009 Andy Shevchenko <andy@smile.org.ua> - 2.11-9.20080912svn311
- rename /usr/bin/qstat to /usr/bin/quakestat (#472750)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-8.20080912svn311
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-7.20080912svn311
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.11-6.20080912svn311
- update to latest svn
- upstream relicensed to Artistic 2.0

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.11-5
- Autorebuild for GCC 4.3

* Wed Jan 23 2008 Andy Shevchenko <andy@smile.org.ua> 2.11-4
- fix Source0 URL

* Tue Aug 21 2007 Andy Shevchenko <andy@smile.org.ua> 2.11-3
- Mass rebuild

* Tue Jul 24 2007 Andy Shevchenko <andy@smile.org.ua> 2.11-2.1
- Do not use -delete for find

* Wed May 23 2007 Andy Shevchenko <andy@smile.org.ua> 2.11-2
- Fix URL tag

* Fri Dec 01 2006 Andy Shevchenko <andy@smile.org.ua> 2.11-1
- update to version 2.11
- do not use __make and makeinstall macros

* Tue Aug 29 2006 Andy Shevchenko <andriy@asplinux.com.ua> 2.10-6
- http://fedoraproject.org/wiki/Extras/Schedule/FC6MassRebuild

* Thu Aug 10 2006 Andy Shevchenko <andriy@asplinux.com.ua> 2.10-5
- add Conflicts with torque-client (#201279)

* Mon Jul 31 2006 Andy Shevchenko <andriy@asplinux.com.ua> 2.10-4
- do not pack COMPILE.txt
- no need Makefile* in the documentation

* Fri Jul 28 2006 Andy Shevchenko <andriy@asplinux.com.ua> 2.10-3
- drop check for "/" in install and clean sections
- drop -n for setup macro
- do not use attr macro in files section
- qstat can be used not only for Quake, so change Summary

* Thu Jul 27 2006 Andy Shevchenko <andriy@asplinux.com.ua> 2.10-2
- preparing for Fedora Extras
- correct BuildRoot tag

* Mon Nov 07 2005 Andy Shevchenko <andriy@asplinux.ru>
- update to 2.10
- use full URL for source

* Fri Oct 15 2004 Evgeniy Bolshakov <ben@asplinux.ru>
- update to 2.6

* Fri Jul 09 2004 Alexandr D. Kanevskiy <kad@asplinux.ru>
- cvs patches from XQF project

* Wed Oct 22 2003 Alexandr D. Kanevskiy <kad@asplinux.ru>
- rebuild 

* Thu Jul 10 2003 Alexandr D. Kanevskiy <kad@asplinux.ru>
- build for ASPLinux
