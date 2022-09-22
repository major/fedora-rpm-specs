Name:		chmlib
Summary:	Library for dealing with ITSS/CHM format files
Version:	0.40
Release:	27%{?dist}
License:	LGPLv2+
Url:		http://www.jedrea.com/chmlib/
%if 0%{?el7}%{?fedora}
VCS:		https://github.com/jedwing/CHMLib.git
%endif
Source0:	http://www.jedrea.com/chmlib/%{name}-%{version}.tar.bz2
# backported from upstream
Patch1:		chmlib-0001-Patch-to-fix-integer-types-problem-by-Goswin-von-Bre.patch
# backported from upstream
Patch2:		chmlib-0002-Fix-for-extract_chmLib-confusing-empty-files-with-di.patch
# Submitted upstream https://github.com/jedwing/CHMLib/pull/10
Patch3:		chm_http-port-shortopt.patch
# Submitted upstream https://github.com/jedwing/CHMLib/pull/11
Patch4:		chm_http-bind-localhost.patch
# Submitted upstream https://github.com/jedwing/CHMLib/pull/12
Patch5:		chm_http-output-server-address.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires: make


%description
CHMLIB is a library for dealing with ITSS/CHM format files. Right now, it is
a very simple library, but sufficient for dealing with all of the .chm files
I've come across. Due to the fairly well-designed indexing built into this
particular file format, even a small library is able to gain reasonably good
performance indexing into ITSS archives.


%package devel
Summary:	Library for dealing with ITSS/CHM format files - development files
Requires:	%{name}%{?_isa} = %{version}-%{release}


%description devel
Files needed for developing apps using chmlib.


%prep
%setup -q
%patch1 -p1 -b .types
%patch2 -p1 -b .files_dirs
%patch3 -p1 -b .shortopt
%patch4 -p1 -b .localhost
%patch5 -p1 -b .printaddr
rm -f libtool
mv configure.in configure.ac
autoreconf -ivf


%build
%configure --enable-examples --disable-static
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}/%{_libdir}/*.la


%ldconfig_scriptlets


%files
%{_bindir}/chm_http
%{_bindir}/enum_chmLib
%{_bindir}/enumdir_chmLib
%{_bindir}/extract_chmLib
%{_bindir}/test_chmLib
%{_libdir}/libchm.so.*
%doc README AUTHORS COPYING NEWS


%files devel
%{_includedir}/*
%{_libdir}/libchm.so


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.40-20
- Patch chm_http to fix -p (port) short opt, bind to 127.0.0.1, display URL

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 31 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.40-9
- Spec-file cleanup
- Remove pre-EL6/FC6 stuff (no longer builds on EL5)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 26 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.40-3
- Removed rpath (see rhbz #569128)
- Patches rebased

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 28 2009 Peter Lemenkov <lemenkov@gmail.com> - 0.40-1
- Ver. 0.40

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Mar 29 2008 Peter Lemenkov <lemenkov@gmail.com> - 0.39-7
- Enable utilities (close BZ#437151)

* Sat Feb  9 2008 Peter Lemenkov <lemenkov@gmail.com> - 0.39-6
- Rebuild for GCC 4.3

* Sun Sep 30 2007 Peter Lemenkov <lemenkov@gmail.com> - 0.39-5
- Changel license tag from LGPL to LGPLv2+

* Sun Aug  5 2007 Peter Lemenkov <lemenkov@gmail.com> - 0.39-4
- Better fix for multi-arch issues

* Sat Aug  4 2007 Peter Lemenkov <lemenkov@gmail.com> - 0.39-3
- Upstream URL changed

* Thu Aug 02 2007 Oliver Falk <oliver@linux-kernel.at> - 0.39-2
- Add alpha fix

* Thu Feb  1 2007 Peter Lemenkov <lemenkov@gmail.com> - 0.39-1
- Ver. 0.39

* Tue Sep 12 2006 Peter Lemenkov <lemenkov@gmail.com> - 0.38-2
- rebuild for FC6

* Wed Jun 28 2006 Peter Lemenkov <lemenkov@newmail.ru> - 0.38-1
- Version 0.38

* Thu Mar 30 2006 Peter Lemenkov <lemenkov@newmail.ru> - 0.37.4-6
- rebuild

* Mon Mar 27 2006 Peter Lemenkov <lemenkov@newmail.ru> - 0.37.4-5
- rebuild

* Tue Jan 10 2006 Peter Lemenkov <lemenkov@newmail.ru> - 0.37.4-4
- Next try to fix powerpc-arch

* Mon Jan 09 2006 Peter Lemenkov <lemenkov@newmail.ru> - 0.37.4-3
- Typo fix

* Mon Jan 09 2006 Peter Lemenkov <lemenkov@newmail.ru> - 0.37.4-2
- Fix for PPC-arch

* Sat Nov 12 2005 Peter Lemenkov <lemenkov@newmail.ru> - 0.37.4-1
- Initial build for FC-Extras

