Name:           libannodex
Version:        0.7.3
Release:        36%{?dist}
Summary:        Library for annotating and indexing networked media

License:        BSD
URL:		http://www.annodex.net/
Source:		http://www.annodex.net/software/libannodex/download/%{name}-%{version}.tar.gz
Patch:          libannodex.man.patch
Patch1:         libannodex-0.7.3-macropen.patch

BuildRequires:	doxygen
BuildRequires:	docbook-utils
BuildRequires:	libogg-devel >= 1.0
BuildRequires:	liboggz-devel >= 0.9.1
BuildRequires:	libcmml-devel >= 0.8
BuildRequires:	libsndfile-devel

# because of patch
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake

# libtool
BuildRequires:	gcc-c++
BuildRequires: make

%description
libannodex is a library to provide reading and writing of Annodex
files and streams.

%package devel
Summary:	Files needed for development using libannodex
Requires:       libannodex = %{version}
Requires:       liboggz-devel >= 0.9.1
Requires:       pkgconfig

%description devel
libannodex is a library to provide reading and writing of Annodex
files and streams.

This package contains the header files and documentation needed for
development using libannodex.

%prep
%setup -q -n %{name}-%{version}
%patch
%patch1 -p1 -b .macropen

aclocal -I m4
libtoolize
autoconf
automake --add-missing

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall docdir=`pwd`/doxygen

# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/annodex/importers/*.la

# remove doxygen build stamp; fixed in upstream CVS
rm -f $RPM_BUILD_ROOT%{_datadir}/doc/libannodex/doxygen-build.stamp

%files
%doc AUTHORS ChangeLog COPYING README
# NEWS is empty in 0.6.2
# %doc NEWS
%{_libdir}/libannodex.so.*
%{_bindir}/anx*
%dir %{_libdir}/annodex
%dir %{_libdir}/annodex/importers
%{_libdir}/annodex/importers/libanx*.so*
%{_mandir}/man1/*

%files devel
%doc doxygen/html
%{_libdir}/libannodex.so
%{_libdir}/pkgconfig/annodex.pc
%{_includedir}/annodex

%ldconfig_scriptlets

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Adam Jackson <ajax@redhat.com> 0.7.3-19
- Fix build with new automake

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 02 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 0.7.3-14
- Bump for new liboggz

* Thu Feb 04 2010 Adam Jackson <ajax@redhat.com> - 0.7.3-13
- drop static libs
- drop the chcon from %%post, not needed.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.7.3-10
- Autorebuild for GCC 4.3

* Tue Oct 16 2007 Joe Orton <jorton@redhat.com> 0.7.3-9
- rebuild for expat 2.x

* Wed Aug  8 2007 Joe Orton <jorton@redhat.com> 0.7.3-8
- fix build with new glibc

* Mon Apr 23 2007 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.3-7
- Own another directory.  Fixes #233859.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.7.3-5
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Wed Sep 20 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.3-4
- rebuilt

* Sun Mar 05 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.3-3
- added docbook-utils, needed for man page build

* Sun Mar 05 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.3-2
- added patch for man pages

* Sun Mar 05 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.3-1
- new upstream release

* Sun Nov 13 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.2-1: new upstream release

* Mon Jun 13 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.6.2-2: add dist tag

* Fri Jun 03 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.6.2-1: initial package
