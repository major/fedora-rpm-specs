Name:           libcmml
Version:        0.9.1
Release:        30%{?dist}
Summary:        Library for handling Continuous Media Markup Language

License:        BSD
URL:		http://www.annodex.net/
Source:		http://www.annodex.net/software/libcmml/download/%{name}-%{version}.tar.gz

BuildRequires:	doxygen
BuildRequires:	expat-devel

# libtool
BuildRequires:	gcc-c++
BuildRequires: make

%description
Libcmml is a library which enables the handling of documents
written in CMML (Continuous Media Markup Language) for the
Continuous Media Web (CMWeb).

It provides a very simple API for reading files marked up with the
Continuous Media Markup Language (CMML), and returns C structures
containing this information in a format which can be used by an
Annodexer for creating ANNODEX(tm) format documents (ANX).

%package devel
Summary:	Files needed for development using libcmml
Requires:       libcmml = %{version}
Requires:       pkgconfig
Requires:	expat-devel

%description devel
Libcmml is a library which enables the handling of documents
written in CMML (Continuous Media Markup Language) for the
Continuous Media Web (CMWeb).

It provides a very simple API for reading files marked up with the
Continuous Media Markup Language (CMML), and returns C structures
containing this information in a format which can be used by an
Annodexer for creating ANNODEX(tm) format documents (ANX).

This package contains the header files and documentation needed for
development using libcmml.

%prep
%setup -q -n %{name}-%{version}

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make docdir=/doxygen DESTDIR=$RPM_BUILD_ROOT install
mv $RPM_BUILD_ROOT/doxygen .

# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# remove doxygen build stamp; fixed in upstream CVS
rm -f $RPM_BUILD_ROOT%{_datadir}/doc/libcmml/doxygen-build.stamp

%files
%doc AUTHORS ChangeLog COPYING NEWS README
# zero length NEWS file
# %doc NEWS
%{_libdir}/libcmml.so.*
%{_bindir}/cmml*

%files devel
%doc doxygen/html
%{_libdir}/libcmml.so
%{_libdir}/pkgconfig/cmml.pc
%{_includedir}/cmml.h

%ldconfig_scriptlets

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May 21 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.1-8
- disable static libs
- don't use %%makeinstall
- fix rpath

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.1-5
- Autorebuild for GCC 4.3

* Tue Oct 16 2007 Joe Orton <jorton@redhat.com> 0.9.1-4
- rebuild for expat 2.x (#296301)

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.9.1-3
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Wed Sep 20 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.1-2
- rebuilt

* Sun Mar 05 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.1-1
- new upstream release

* Thu Jun 16 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.0-2: suggestions from Ville

* Sat Jun 04 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.0-1: initial package
