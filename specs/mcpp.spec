# spec file for mcpp / compiler-independent-library-build on fedora

Summary:    Alternative C/C++ preprocessor
Name:       mcpp
Version:    2.7.2
Release:    38%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
Source:     http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:        http://mcpp.sourceforge.net/

Patch0:     mcpp-manual.html.patch

# Extracted from http://www.zeroc.com/download/Ice/3.4/ThirdParty-Sources-3.4.2.tar.gz
Patch1:     patch.mcpp.2.7.2

# https://bugzilla.redhat.com/show_bug.cgi?id=948860
Patch2:     mcpp-man.patch
Patch3: mcpp-c99.patch


BuildRequires: make
BuildRequires:  gcc
%description
C/C++ preprocessor defines and expands macros and processes '#if',
'#include' and some other directives.

MCPP is an alternative C/C++ preprocessor with the highest conformance.
It supports multiple standards: K&R, ISO C90, ISO C99, and ISO C++98.
MCPP is especially useful for debugging a source program which uses
complicated macros and also useful for checking portability of a source.

Though mcpp could be built as a replacement of GCC's resident
preprocessor or as a stand-alone program without using library build of
mcpp, this package installs only a program named 'mcpp' which links
shared library of mcpp and behaves independent from GCC.

%prep
%setup -q
%patch -P0 -p0 -b -z.euc-jp
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
%configure --enable-mcpplib --disable-static
# Prevent the use of rpath as required by Fedora Packaging Guidelines.
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
mv mcpp-gcc.1 mcpp.1

%install
iconv -f euc-jp -t utf-8 doc-jp/mcpp-manual.html > doc-jp/mcpp-manual-jp.html
rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
rm -f $RPM_BUILD_ROOT%{_libdir}/libmcpp.la

%files
%doc    ChangeLog ChangeLog.old NEWS README
%{_datadir}/man/man1/%{name}.1*
%{_bindir}/%{name}

%package -n libmcpp

Summary:    Alternative C/C++ preprocessor (library build)

%description -n libmcpp
This package provides a library build of mcpp.

%files -n libmcpp
%doc    LICENSE
%{_libdir}/libmcpp.so.*

%ldconfig_scriptlets -n libmcpp

%package -n libmcpp-devel

Summary:    Alternative C/C++ preprocessor (development package for library build)
Requires:   libmcpp = %{version}

%description -n libmcpp-devel
Development package for libmcpp.

%files -n libmcpp-devel
%{_libdir}/libmcpp.so
%{_includedir}/mcpp_lib.h
%{_includedir}/mcpp_out.h

%package doc

Summary:    Alternative C/C++ preprocessor (manual for library build)

%description doc
This package provides an html manual for mcpp.

%files doc
%doc    LICENSE doc/mcpp-manual.html
%lang(ja) %doc  doc-jp/mcpp-manual-jp.html

%changelog
* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.7.2-38
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 07 2023 Florian Weimer <fweimer@redhat.com> - 2.7.2-33
- Fix C99 compatibility issue

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 18 2021 Jeff Makey <jeff@makey.net> - 2.7.2-29
- Prevent the use of rpath as required by Fedora Packaging Guidelines (#1987708).
- Use standard make_build and make_install macros.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
- Add make to BuildRequires.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Owen Taylor <otaylor@redhat.com> - 2.7.2-22
- Handle both compressed and uncompressed manual pages

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 2.7.2-14
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Petr Machata <pmachata@redhat.com> - 2.7.2-10
- Update usage output and man pages to include some omited options.
  (mcpp-man.patch)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 16 2011 Mary Ellen Foster <mefoster at gmail.com> - 2.7.2-6
- Update upstream Ice patch to latest version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 Kiyoshi Matsui <kmatsui@t3.rim.or.jp> 2.7.2-4
- Make subpackages to include LICENSE.

* Tue Oct 13 2009 Mary Ellen Foster <mefoster at gmail.com>
- Incorporate patch from Ice upstream project

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Kiyoshi Matsui <kmatsui@t3.rim.or.jp> 2.7.2-1
- Upstream new release.

* Tue May 20 2008 Kiyoshi Matsui <kmatsui@t3.rim.or.jp> 2.7.1-1
- Upstream new release.
- Change to library build.
- Devide to 4 packages: mcpp, libmcpp, libmcpp-devel and mcpp-doc.
- Thanks to Mary Ellen Foster for correcting this spec file.

* Sun Mar 24 2008 Kiyoshi Matsui <kmatsui@t3.rim.or.jp> 2.7-2
- Upstream new release.

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 2.6.4-2
- Rebuild for selinux ppc32 issue.

* Thu May 19 2007 Kiyoshi Matsui <kmatsui@t3.rim.or.jp> 2.6.4-1
- Upstream new release.

* Fri Apr 27 2007 Kiyoshi Matsui <kmatsui@t3.rim.or.jp> 2.6.3-5
- Apply the new patch (patch1) for mcpp.

* Wed Apr 25 2007 Kiyoshi Matsui <kmatsui@t3.rim.or.jp> 2.6.3-4
- Change installation of doc/mcpp-manual.html and doc-jp/mcpp-manual.html.

* Tue Apr 24 2007 Kiyoshi Matsui <kmatsui@t3.rim.or.jp> 2.6.3-3
- Revise many points to adapt to the guideline of Fedora (thanks to
        the review by Mamoru Tasaka):
    use %%dist, %%configure, %%optflags, %%{_datadir}, %%lang(ja),
    convert encoding of mcpp-manual.html to utf-8,
    and others.

* Sat Apr 21 2007 Kiyoshi Matsui <kmatsui@t3.rim.or.jp> 2.6.3-2
- Replace some variables with macros.
- Rename this spec file.

* Sat Apr 07 2007 Kiyoshi Matsui <kmatsui@t3.rim.or.jp> 2.6.3-1
- First release for V.2.6.3 on sourceforge.
