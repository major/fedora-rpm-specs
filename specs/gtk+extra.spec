Name:		gtk+extra
Version:	2.1.2
Release:	41%{?dist}
Summary:	A library of gtk+ widgets
Summary(fr):	Une bibliothèque de widgets gtk+

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		http://gtkextra.sourceforge.net/
Source:		http://downloads.sourceforge.net/gtkextra/gtk+extra-%{version}.tar.gz
Patch0:		%{name}-%{version}-gtk2.21.patch
Patch1:		%{name}-%{version}-make.patch
Patch2:		%{name}-%{version}-marshal.patch
Patch3:		%{name}-%{version}-gtkitementry.patch
Patch4:		%{name}-%{version}-gtkcharsel.patch
Patch5:		%{name}-%{version}-gtkcolorcombo.patch
Patch6:		%{name}-%{version}-format.patch
Patch7:		%{name}-%{version}-roundint.patch

BuildRequires:	gtk2-devel libtool gtk-doc
BuildRequires: make

%description
A library of dynamically linked gtk+ widgets including:
GtkSheet, GtkPlot, and GtkIconList

%description -l fr
Une bibliothèque de widgets gtk+ liés dynamiquement incluant :
GtkSheet, GtkPlot et GtkIconList

%package devel
Summary:	A library of gtk+ widgets
Summary(fr):	Une bibliothèque de widgets gtk+
Requires:	%{name} = %{version}-%{release}
Requires:	gtk2-devel

%description devel
The %{name}-devel package includes the static libraries, header files,
and documentation for compiling programs that use gtk+extra widgets.

%description -l fr devel
Le paquetage %{name}-devel contient les bibliothèques statiques, les fichiers
d'en-têtes et la documentation nécessaires à la compilation des programmes
qui utilisent les widgets gtk+extra.

%prep
%setup -q
%{__chmod} a-x ChangeLog
%{__sed} -i 's/\r//' docs/{gtk*.ChangeLog,HELP,README,TODO,VERSION}
%{__sed} -i 's/\r//' docs/reference/*.html
%{__sed} -i 's/\r//' docs/tutorial/{*.html,gtksheet/*.{c,html}}

%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p1
%patch -P3 -p0
%patch -P4 -p0
%patch -P5 -p0
%patch -P6 -p0
%patch -P7 -p0
libtoolize --force
aclocal
autoheader

autoreconf -i
automake 

%build
%configure
make  %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libgtkextra*.so.*

%files devel
%doc docs/{gtk*.ChangeLog,COPYING,HELP,README,TODO,VERSION}
%doc docs/reference/ docs/tutorial/
%dir %{_datadir}/gtk-doc/html/gtkextra/
%{_datadir}/gtk-doc/html/gtkextra/*
%{_libdir}/*.a
%exclude %{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.2-40
- convert license to SPDX

* Fri Jul 26 2024 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> - 2.1.2-39
- Correct fatal specfile error

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 17 2018 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> - 2.1.2-23
- fix build issue concerning gtkmarshal

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> - 2.1.2-17
- fix build issue

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 15 2014 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> - 2.1.2-14
- fix build issue

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 07 2011 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> - 2.1.2-8
- patch for glib change, patch buffer overflow

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.1.2-7
- Rebuild for new libpng

* Mon Feb 21 2011 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> - 2.1.2-6
- patch for sigsegv when using gtksheet

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 2.1.2-4
- Rebuilt for gcc bug 634757

* Tue Sep 14 2010 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> - 2.1.2-3
- Patches to configuration, Makefile and marshall

* Sat Jun 12 2010 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> - 2.1.2-2
- Patch to compile with gtk2-2.21

* Tue Mar 23 2010 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> - 2.1.2-1
- Upstream bugfix release 2.1.2 

* Fri Feb 12 2010 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> - 2.1.1-15
- Patch for implicit DSO linking

* Sat Jan 30 2010 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> - 2.1.1-14
- Exclude *.a files BZ 556054
  License in specfile wrong BZ 559985

* Sun Dec 20 2009 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> - 2.1.1-13
- Fix crash issue with gtk2-2.18 BZ 546648

* Sat Aug 01 2009 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> - 2.1.1-12
- Patch to compile with gtk2-2.17.5

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec  6 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.1.1-9
  - Rebuild for pkgconfig

* Mon Apr 07 2008 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2.1.1-8
  - Patch to fix BZ #431150

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.1.1-7
  - Autorebuild for GCC 4.3

* Fri Oct 19 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2.1.1-6
  - Update patch to fix BZ #339611

* Tue Aug 21 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2.1.1-5
  - Licence tag clarification

* Thu May  3 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2.1.1-4
  - Add patch to fix SF #1504169

* Fri Sep  1 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2.1.1-3
  - FE6 rebuild

* Mon Mar 13 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2.1.1-2
  - Rebuild for FE5

* Wed Oct 5 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2.1.1-1
  - New version
  - Revert to the official package.

* Thu Sep 15 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 1.1.0-3
  - BuildRequires is gtk2-devel, not gtk+-devel
  - Add Requires gtk2-devel for package devel
  - Exclude .la files
  - Add a lot of documentation
  - Move gtk*.ChangeLog in devel package
  - Convert DOS format end-of-line to Unix-like format
  - Contributions of Jose Pedro Oliveira <jpo[AT]di[DOT]uminho[DOT]pt>
    Thanks to him.

* Tue Sep 13 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 1.1.0-2
  - Add french summary and description

* Mon Sep 12 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 1.1.0-1
  - New version

* Fri Oct 29 2004 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0:0.99.17-0.fdr.2
  - Add BuildRequires gtk+-devel

* Wed Oct 27 2004 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0:0.99.17-0.fdr.1
  - Initial Fedora RPM
