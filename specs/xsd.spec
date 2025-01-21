Name: xsd
Version: 4.1.0
Release: 0.17.a11%{?dist}
Summary: W3C XML schema to C++ data binding compiler
# Exceptions permit otherwise GPLv2 incompatible combination with ASL 2.0
# Automatically converted from old format: GPLv2 with exceptions and ASL 2.0 - review is highly recommended.
License: LicenseRef-Callaway-GPLv2-with-exceptions AND Apache-2.0  
URL: https://www.codesynthesis.com/products/xsd/
Source0: https://codesynthesis.com/~boris/tmp/xsd/%{version}.a11/xsd-%{version}.a11+dep.tar.bz2

# Sent suggestion to upstream via e-mail 20090707
# http://anonscm.debian.org/cgit/collab-maint/xsd.git/tree/debian/patches/0001-xsd_xsdcxx-rename.patch
Patch0: %{name}-%{version}-xsdcxx-rename.patch

# Remove tests for character reference values unsupported by Xerces-C++ 3.2
# https://anonscm.debian.org/cgit/collab-maint/xsd.git/diff/debian/patches/0110-xerces-c3.2.patch?id=442e98604d4158dae11056c4f94aaa655cb480fa
Patch1: %{name}-xerces_3-2.patch

BuildRequires: make
BuildRequires: m4, xerces-c-devel, libcutl-devel, gcc-c++

%if 0%{?rhel} >= 8 || 0%{?fedora}
BuildRequires: boost-devel
%else
BuildRequires: boost148-devel
Requires: boost148%{?_isa}
%endif

%description
CodeSynthesis XSD is an open-source, cross-platform W3C XML Schema to
C++ data binding compiler. Provided with an XML instance specification
(XML Schema), it generates C++ classes that represent the given
vocabulary as well as parsing and serialization code.
You can then access the data stored in XML using types and functions
that semantically correspond to your application domain rather than
dealing with intricacies of reading and writing XML.

%package   doc
BuildArch: noarch
BuildRequires: ghostscript
Summary:   API documentation files for %{name}

%description    doc
This package contains API documentation for %{name}.

%prep
%autosetup -p0 -n xsd-%{version}.a11+dep

##Unbundle libcutl
rm -rf libcutl

%build
%make_build verbose=1 CXX=g++ CC=gcc CXXFLAGS="$RPM_OPT_FLAGS -std=c++14 -fPIC -pie -Wl,-z,now" LDFLAGS="%{__global_ldflags} -fPIC -pie -Wl,-z,now" BOOST_LINK_SYSTEM=y EXTERNAL_LIBCUTL=y

%install
rm -rf apidocdir

%make_install LDFLAGS="%{__global_ldflags}" install_prefix=$RPM_BUILD_ROOT%{_prefix} \
 install_bin_dir=$RPM_BUILD_ROOT%{_bindir} install_man_dir=$RPM_BUILD_ROOT%{_mandir} EXTERNAL_LIBCUTL=y BOOST_LINK_SYSTEM=y

# Split API documentation to -doc subpackage.
mkdir -p apidocdir
mv $RPM_BUILD_ROOT%{_datadir}/doc/xsd/*.{xhtml,css} apidocdir/
mv $RPM_BUILD_ROOT%{_datadir}/doc/xsd/cxx/ apidocdir/
mv $RPM_BUILD_ROOT%{_datadir}/doc/xsd/ docdir/

# Convert to utf-8.
for file in docdir/NEWS; do
    mv $file timestamp
    iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
    touch -r timestamp $file
done

# Rename binary to xsdcxx to avoid conflicting with mono-web package.
# Sent suggestion to upstream via e-mail 20090707
# they will consider renaming in 4.0.0
mv $RPM_BUILD_ROOT%{_bindir}/xsd $RPM_BUILD_ROOT%{_bindir}/xsdcxx
mv $RPM_BUILD_ROOT%{_mandir}/man1/xsd.1 $RPM_BUILD_ROOT%{_mandir}/man1/xsdcxx.1

# Remove duplicate docs.
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libxsd

# Remove Microsoft Visual C++ compiler helper files.
rm -rf $RPM_BUILD_ROOT%{_includedir}/xsd/cxx/compilers

# Remove redundant PostScript files that rpmlint grunts about not being UTF8
# See: https://bugzilla.redhat.com/show_bug.cgi?id=502024#c27
# for Boris Kolpackov's explanation about those
find apidocdir -name "*.ps" | xargs rm -f
# Remove other unwanted crap
find apidocdir -name "*.doxygen" \
            -o -name "makefile" \
            -o -name "*.html2ps" | xargs rm -f

##Test failed on EPEL6 due to "bad" xerces-c
##http://codesynthesis.com/pipermail/xsd-users/2015-October/004696.html
##https://bugzilla.redhat.com/show_bug.cgi?id=1270978
%if 0%{?fedora} || 0%{?rhel} >= 7
%check
make -j 1 test EXTERNAL_LIBCUTL=y BOOST_LINK_SYSTEM=y
%endif

%files
%doc docdir/README docdir/NEWS docdir/FLOSSE
%license docdir/GPLv2 docdir/LICENSE
%{_bindir}/xsdcxx
%{_mandir}/man1/xsdcxx.1*
%{_includedir}/xsd/

%files doc
%doc docdir/README docdir/NEWS docdir/FLOSSE
%license docdir/GPLv2 docdir/LICENSE
%doc apidocdir/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-0.17.a11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 18 2024 Pete Walter <pwalter@fedoraproject.org> - 4.1.0-0.16.a11
- Rebuild for xerces-c 3.3

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 4.1.0-0.15.a11
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-0.14.a11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-0.13.a11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-0.12.a11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-0.11.a11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-0.10.a11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-0.9.a11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Antonio Trande <sagitter@fedoraproject.org> - 4.1.0-0.8.a11
- Rebuild for EPEL9

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-0.7.a11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-0.6.a11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Jeff Law <law@redhat.com> - 4.1.0-0.5.a11
- Force C++14 as this code is not C++17 ready

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-0.4.a11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-0.3.a11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-0.2.a11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 15 2019 Antonio Trande <sagitter@fedoraproject.org> - 4.1.0-0.1.a11
- Pre-release 4.1.0.a11

* Thu Feb 07 2019 Antonio Trande <sagitter@fedoraproject.org> - 4.0.0-27
- Fix BR required for rhel8

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 4.0.0-25
- Some minor changes

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 4.0.0-23
- Add gcc-c++ BR

* Fri Feb 16 2018 Antonio Trande <sagitterATfedoraproject.org> - 4.0.0-22
- Patched for xerces-c-3.2 (patch from Debian)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 4.0.0-18
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jun 26 2016 Antonio Trande <sagitterATfedoraproject.org> - 4.0.0-15
- Remove conditional macro for the Patch1 (bz#1350231)

* Fri Feb 05 2016 Antonio Trande <sagitterATfedoraproject.org> - 4.0.0-14
- Set flags for hardened builds

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 4.0.0-12
- Rebuilt for Boost 1.60

* Wed Nov 25 2015 Antonio Trande <sagitterATfedoraproject.org> - 4.0.0-11
- Rebuild for libcutl

* Fri Nov 06 2015 Antonio Trande <sagitterATfedoraproject.org> - 4.0.0-10
- Add patch to fix bug in C++/Parser Expat Support in EPEL builds

* Mon Oct 12 2015 Antonio Trande <sagitterATfedoraproject.org> - 4.0.0-9
- Header files included again in main package

* Mon Oct 12 2015 Antonio Trande <sagitterATfedoraproject.org> - 4.0.0-8
- Requires explicitely Boost148 in EPEL
- Tests not performed in EPEL6

* Thu Oct 08 2015 Antonio Trande <sagitterATfedoraproject.org> - 4.0.0-7
- Used %%license tag
- libcutl libraries unbundled
- Header files packaged apart
- Made tests

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 4.0.0-6
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 4.0.0-4
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.0.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar 28 2015 Kalev Lember <kalevlember@gmail.com> - 4.0.0-1
- Update to 4.0.0

* Wed Feb 25 2015 Rex Dieter <rdieter@fedoraproject.org> 3.3.0-23
- rebuild (gcc5)

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 3.3.0-22
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun  5 2014 Peter Robinson <pbrobinson@fedoraproject.org> 3.3.0-19
- Update config.* to fix FTBFS on aarch64/ppc64le

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 3.3.0-18
- Rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 3.3.0-16
- Rebuild for boost 1.54.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 3.3.0-15
- Rebuild for Boost-1.53.0

* Sun Aug 12 2012 Rex Dieter <rdieter@fedoraproject.org> 3.3.0-14
- xsd-3.3.0-2+dep 

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 18 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.0-12
- Update to xsd-3.3.0-1+dep upstream tarball, which includes the gcc 4.7 patch

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-11
- Rebuilt for c++ ABI breakage

* Thu Jan 19 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.3.0-10
- Add xsd-3.3.0-gcc47.patch (Fix mass rebuild FTBFS).

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Thomas Spura <tomspur@fedoraproject.org> - 3.3.0-8
- rebuild for https://fedoraproject.org/wiki/Features/F17Boost148

* Fri Jul 22 2011 Antti Andreimann <Antti.Andreimann@mail.ee> - 3.3.0-7
- Rebuilt for boost 1.47.0

* Wed Apr 06 2011 Kalev Lember <kalev@smartlink.ee> - 3.3.0-6
- Rebuilt for boost 1.46.1 soname bump

* Thu Mar 10 2011 Kalev Lember <kalev@smartlink.ee> - 3.3.0-5
- Rebuilt with xerces-c 3.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Thomas Spura <tomspur@fedoraproject.org> - 3.3.0-3
- rebuild for new boost (thanks Petr Machata for the fix)

* Mon Aug 02 2010 Antti Andreimann <Antti.Andreimann@mail.ee> 3.3.0-2
- Rebuild for new boost

* Sun Jun 20 2010 Antti Andreimann <Antti.Andreimann@mail.ee> 3.3.0-1
- Updated to version 3.3.0
- Implemented a workaround for gcc segfault on el5

* Sun Feb 07 2010 Caolán McNamara <caolanm@redhat.com> - 3.2.0-7
- Rebuild for xerces soname bump

* Fri Jan 22 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 3.2.0-6
- Rebuild for Boost soname bump

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 07 2009 Antti Andreimann <Antti.Andreimann@mail.ee> 3.2.0-4
- Removed redundant PostScript files from the doc package

* Mon Jul 06 2009 Antti Andreimann <Antti.Andreimann@mail.ee> 3.2.0-3
- Added ACE homepage to SPEC file comments
- Added verbose=1 to MAKEFLAGS so compiler flags could be
  verified from build logs.

* Sat Jul 04 2009 Antti Andreimann <Antti.Andreimann@mail.ee> 3.2.0-2
- Changed License tag to clarify which exceptions we are talking about

* Wed May 20 2009 Antti Andreimann <Antti.Andreimann@mail.ee> 3.2.0-1
- Initial RPM release.
