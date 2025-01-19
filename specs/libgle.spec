Summary: A Tubing and Extrusion Library for OpenGL
Name: libgle
Version: 3.1.0
Release: 35%{?dist}
# Automatically converted from old format: GPLv2 or (Artistic clarified and MIT) - review is highly recommended.
License: GPL-2.0-only OR (ClArtistic AND LicenseRef-Callaway-MIT)
URL: http://www.linas.org/gle/
Source: http://www.linas.org/gle/pub/gle-%{version}.tar.gz
# Make the examples makefile multilib-compliant
Patch0: libgle-examples-makefile.patch
Patch1: libgle-configure-c99.patch
# https://github.com/linas/glextrusion/pull/13
# https://github.com/linas/glextrusion/commit/2453603748f156a6cde0e810c147dc14a1bbbab8
Patch2: libgle-pr13-function-type-cast.patch

BuildRequires:  gcc
BuildRequires: mesa-libGL-devel 
BuildRequires: freeglut-devel
BuildRequires: libXmu-devel
BuildRequires: libXi-devel 
BuildRequires: make


%description
The GLE Tubing and Extrusion Library consists of a number of "C"
language subroutines for drawing tubing and extrusions. It is a very
fast implementation of these shapes, outperforming all other
implementations, most by orders of magnitude. It uses the
OpenGL programming API to perform the actual drawing of the tubing
and extrusions.

%package devel
Requires: glut-devel
Requires: libGL-devel
Requires: libGLU-devel
Requires: libX11-devel
Requires: libXext-devel
Requires: libXi-devel
Requires: libXmu-devel
Requires: libXmu-devel
Requires: libXt-devel
Summary: GLE includes and development libraries

%description devel
Includes, man pages, and development libraries for the GLE Tubing and
Extrusion Library.

%prep
%setup -q -n gle-%{version}
%patch -P0 -p5
%patch -P1 -p1
%patch -P2 -p1
# Prevent re-running autotools.
touch -r Makefile.am aclocal.m4 configure*

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Clean up a bit
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
mv $RPM_BUILD_ROOT%{_docdir}/gle docs

%ldconfig_scriptlets

%files
%{_libdir}/*.so.*
%doc docs/AUTHORS docs/COPYING docs/README

%files devel
%{_libdir}/*.so
%{_includedir}/*
%{_mandir}/man?/*
%doc docs/examples docs/html


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 08 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-34
- Backport upstream patch to fix FTBFS with -Werror=incompatible-pointer-types

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.0-33
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Florian Weimer <fweimer@redhat.com> - 3.1.0-27
- C99 compatibility fixes for the configure script

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 18 2010 Mary Ellen Foster <mefoster at gmail.com> - 3.1.0-4
- Add the full set of requirements for the -devel package

* Mon Nov 30 2009 Mary Ellen Foster <mefoster at gmail.com> - 3.1.0-3
- Incorporate some more suggestions from Thomas Fitzsimmons

* Wed Sep 30 2009 Mary Ellen Foster <mefoster at gmail.com> - 3.1.0-2
- Incorporating some clean-ups from Ralf Corsépius's spec file

* Tue Sep 29 2009 Mary Ellen Foster <mefoster at gmail.com> - 3.1.0-1
- Initial version, based on upstream .spec file
