Summary: Tells the Hebrew date, Torah readings, and generates calendars
Summary(he): תוכנות להדפסת התאריך העברי, פרשות השבוע, ולוחות שנה.
Name: taarich
Version: 1.20051120
Release: 34%{?dist}
URL: ftp://ftp.math.technion.ac.il/calendar/gauss/
Source0: gauss-%{version}.tar.gz
License: BSD

BuildRequires: make
BuildRequires:  gcc
%description
Taarich displays the current Hebrew date (in English or in Hebrew).
When run with -h command line option, it prints the date in UTF8 Hebrew.
Luach renders a calendar of the current Gregorian month, with Hebrew dates.
Both use Gauss's algorithm to find the Gregorian date of Passover.

%description -l he
Taarich מציג את התאריך העברי הנוכחי (באנגלית או בעברית).
עם האופציה -h, מדפיס את התאריך בעברית בקידוד UTF8.
Luach מדפיס לוח-שנה של החודש הגרגוריאני הנוכחי, עם תאריכים עבריים.
שניהם משתמשים באלגוריתם גאוס למציאת התאריך הגרגוריאני של חג הפסח.

%prep
%setup -q -n gauss-%{version}

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_bindir}
install -d -m755 %{buildroot}%{_mandir}/man1
install luach taarich %{buildroot}%{_bindir}
install -m644 {luach.man,taarich.man} %{buildroot}%{_mandir}/man1

%files
%doc gauss.txt reading.txt COPYING
%{_bindir}/taarich
%{_bindir}/luach
%{_mandir}/man1/*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20051120-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20051120-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.20051120-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.20051120-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20051120-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20051120-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20051120-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20051120-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20051120-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20051120-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20051120-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20051120-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20051120-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.20051120-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20051120-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20051120-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20051120-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20051120-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20051120-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20051120-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20051120-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20051120-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20051120-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20051120-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.20051120-10
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.20051120-9
- Autorebuild for GCC 4.3

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.20051120-8
- Rebuild for selinux ppc32 issue.

* Sat Jul  3 2007 Dan Kenigsberg <danken@cs.technion.ac.il> 1.20051120-7
- change spec encoding to UTF8 (bug 246580)
* Sat Sep 16 2006 Dan Kenigsberg <danken@cs.technion.ac.il> 1.20051120-6
- Rebuild for Fedora Extras 6
* Tue Feb 28 2006 Dan Kenigsberg <danken@cs.technion.ac.il> 1.20051120-5
- A cvs missunderstanding. My bad.
* Tue Feb 28 2006 Dan Kenigsberg <danken@cs.technion.ac.il> 1.20051120-4
- Rebuild for Fedora Extras 5
* Mon Nov 21 2005 Dan Kenigsberg <danken@cs.technion.ac.il> 1.20051120-3
- Hebrew summary added, -s removed from CFLAGS, mention that -h output is UTF8.
* Mon Nov 21 2005 Dan Kenigsberg <danken@cs.technion.ac.il> 1.20051120-2
- Clean things according to the review of mpeters AT mac.com
* Sun Nov 20 2005 Dan Kenigsberg <danken@cs.technion.ac.il> 1.20051120-1
- Beautification for Fedora Extras: create a tarball from the ftp directory, add
  a COPYING file according to Zvi Har'El's request
* Sun Feb 23 2003 Dan Kenigsberg <danken@cs.technion.ac.il> 1-1
- created
