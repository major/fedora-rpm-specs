%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%global oname  gle-graphics

Summary:       Graphics Layout Engine
Name:          gle
Version:       4.2.5
Release:       28%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://www.gle-graphics.org/
Source0:       http://downloads.sourceforge.net/glx/gle-graphics-%{version}f-src.tar.gz
Source1:       http://downloads.sourceforge.net/glx/GLEusersguide.pdf
# https://sourceforge.net/p/glx/mailman/glx-devel/?viewmonth=201708
Patch0:        gle-4.2.5-gcc7.patch

BuildRequires: gcc-c++
BuildRequires: cairo-devel
BuildRequires: libstdc++-devel >= 3.0
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libjpeg-devel
BuildRequires: ncurses-devel
BuildRequires: poppler-glib-devel
BuildRequires: zlib-devel
BuildRequires: xorg-x11-proto-devel
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: qt-devel >= 4.1.1
BuildRequires: dos2unix
BuildRequires: tex(latex)
BuildRequires: tex(rotating.sty)
BuildRequires: tex(supertabular.sty)
BuildRequires: ghostscript
BuildRequires: make
Requires:      ghostscript
Requires:      tex(latex)
Requires:      tex(rotating.sty)
Requires:      tex(supertabular.sty)

%description
GLE (Graphics Layout Engine) is a high-quality graphics package for
scientists, combining a user-friendly scripting language with a full
range of facilities for producing publication-quality graphs,
diagrams, posters and slides. GLE provides LaTeX quality fonts
together with a flexible graphics module which allows the user to
specify any feature of a graph. Complex pictures can be drawn with
user-defined subroutines and simple looping structures. Current output
formats include EPS, PS, PDF, JPEG, and PNG.

%package -n    qgle
Summary:       QT frontend to GLE
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description -n qgle
GLE (Graphics Layout Engine) is a high-quality graphics package for
scientists, combining a user-friendly scripting language with a full
range of facilities for producing publication-quality graphs,
diagrams, posters and slides. GLE provides LaTeX quality fonts
together with a flexible graphics module which allows the user to
specify any feature of a graph. Complex pictures can be drawn with
user-defined subroutines and simple looping structures. Current output
formats include EPS, PS, PDF, JPEG, and PNG.

This package contains the QT frontend.

%package       doc
Summary:       User documentation for GLE
BuildArch:     noarch

%description doc
GLE (Graphics Layout Engine) is a high-quality graphics package for
scientists, combining a user-friendly scripting language with a full
range of facilities for producing publication-quality graphs,
diagrams, posters and slides. GLE provides LaTeX quality fonts
together with a flexible graphics module which allows the user to
specify any feature of a graph. Complex pictures can be drawn with
user-defined subroutines and simple looping structures. Current output
formats include EPS, PS, PDF, JPEG, and PNG.

This package contains the user documentation.

%prep
%autosetup -p1 -n %{oname}-%{version}
install -p -m 0644 %{SOURCE1} .
touch -r README.txt configure.ac

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure --with-qt=%{_libdir}/qt4 \
           --with-jpeg              \
           --with-png               \
           --with-tiff              \
           --with-z                 \
           --with-x                 \
           --with-rpath=no          \
           --with-debug=yes         \
           --with-libgle=yes        \
           --with-extrafonts=yes    \
           --docdir=%{_pkgdocdir}   \
           CPPFLAGS="%{optflags} -std=c++14" \
           CXXFLAGS="%{optflags}"
make
# %{?_smp_mflags} build fails

# docs
make doc

%install
%make_install
mv %{buildroot}/%{_pkgdocdir}/gle-manual.pdf .
rm -rf %{buildroot}/%{_pkgdocdir}

# Some fixes
dos2unix LICENSE.txt
rm -f %{buildroot}%{_libdir}/pkgconfig/gle-graphics.pc

%files
%license LICENSE.txt
%doc README.txt src/gui/readme.txt
%{_bindir}/gle
%{_bindir}/glebtool
%{_bindir}/manip
%{_datadir}/gle-graphics
%{_mandir}/man1/gle.1*
%{_libdir}/libgle-graphics-%{version}.so

%files -n qgle
%license LICENSE.txt
%{_bindir}/qgle

%files doc
%license LICENSE.txt
%doc gle-manual.pdf GLEusersguide.pdf

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 4.2.5-27
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Terje Rosten <terje.rosten@ntnu.no> - 4.2.5-25
- Use autosetup macro

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 4.2.5-16
- Use C++14 as this code is not C++17 ready

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Tom Stellard <tstellar@redhat.com> - 4.2.5-14
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Sun Jul 12 2020 Terje Rosten <terje.rosten@ntnu.no> - 4.2.5-13
- Rebuilt for Fedora 33

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 4.2.5-11
- Rebuild for poppler-0.84.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.2.5-7
- Added gcc-c++ buildrequires.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 24 2017 Terje Rosten <terje.rosten@ntnu.no> - 4.2.5-5
- Add patch to build with GCC7

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 14 2016 Terje Rosten <terje.rosten@ntnu.no> - 4.2.5-1
- 4.2.5

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4c-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 15 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.2.4c-16
- Add gle-graphics-4.2.4c-string-gledir-filemenu.patch,
  gle-graphics-4.2.4c-string-gledir.patch from openSUSE
  (Fix F23FTBFS, RHBZ#1239532).
- Add gle-graphics-4.2.4c-outofbounds.patch
  (Avoid array out of bounds).
- Remove redundant CPPFLAGS, CXXFLAGS from %%build.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4c-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4c-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.2.4c-13
- Add in some explicit buildrequires and --with switches the need for
  which was revealed in EPEL.
- Add in requires on the BR'd latex packages that are necessary for a
  properly functioning package.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4c-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 15 2013 Terje Rosten <terje.rosten@ntnu.no> - 4.2.4c-11
- Remove outdated obsoletes, spec file cleanup

* Mon Aug 05 2013 Terje Rosten <terje.rosten@ntnu.no> - 4.2.4c-10
- New doc location

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4c-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4c-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 4.2.4c-7
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Terje Rosten <terje.rosten@ntnu.no> - 4.2.4c-6
- Build with newer tex (with help from Jussi)
- Fix changelog

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 4.2.4c-5
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 Marek Kasik <mkasik@redhat.com> - 4.2.4c-3
- Rebuild (poppler-0.20.0)

* Mon May 07 2012 Terje Rosten <terje.rosten@ntnu.no> - 4.2.4c-2
- Rebuilt for new libtiff

* Mon Mar 19 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.2.4c-1
- Update to 4.2.4c

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4b-3
- Rebuilt for c++ ABI breakage

* Tue Jan 17 2012 Terje Rosten <terje.rosten@ntnu.no> - 4.2.4b-2
- Add patches from upstream to fix gcc-4.7 build

* Tue Jan 17 2012 Terje Rosten <terje.rosten@ntnu.no> - 4.2.4b-1
- 4.2.4b
- docs
- include pdf support

* Mon Jan 02 2012 Terje Rosten <terje.rosten@ntnu.no> - 4.2.4-1
- 4.2.4
- Update patches

* Mon Nov 07 2011 Terje Rosten <terje.rosten@ntnu.no> - 4.2.3b-4
- Rebuilt for new libpng

* Sat Oct 1 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.2.3b-3
- Enable extra fonts
- Fix FTBFS on rawhide
- Branch QT frontend into separate package

* Fri Sep 30 2011 Terje Rosten <terje.rosten@ntnu.no> - 4.2.3b-2
- Fix src url
- qt4 is qt

* Fri Sep 30 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.2.3b-1
- Update to 4.2.3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct  1 2010 Dan Horák <dan[at]danny.cz> - 4.2.2-6
- 64-bit fixes

* Tue Sep 07 2010 Terje Rosten <terje.rosten@ntnu.no> - 4.2.2-3
* Be more explicit about qt devel buildreq
 
* Thu Feb 11 2010 Terje Rosten <terjeros@phys.ntnu.no> - 4.2.2-2
- Fix typo

* Thu Feb 11 2010 Terje Rosten <terjeros@phys.ntnu.no> - 4.2.2-1
- 4.2.2

* Sun Dec 06 2009 Terje Rosten <terjeros@phys.ntnu.no> - 4.2.1-1
- 4.2.1

* Fri Jul 31 2009 Terje Rosten <terjeros@phys.ntnu.no> - 4.2.0-4
- Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 19 2009 Terje Rosten <terjeros@phys.ntnu.no> - 4.2.0-2
- Build with cairo support 
- Use correct optflags

* Tue May 19 2009 Terje Rosten <terjeros@phys.ntnu.no> - 4.2.0-1
- 4.2.0
- Drop gcc43 patch now upstream
- Add more documentation

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb  7 2009 Terje Rosten <terjeros@phys.ntnu.no> - 4.1.2-2
- Add patch to compile with gcc-4.4

* Sun Mar  2 2008 Terje Rosten <terjeros@phys.ntnu.no> - 4.1.2-1
- 4.1.2
- Update pdf documentation
- Drop patch now upstream

* Sun Feb 10 2008 Terje Rosten <terjeros@phys.ntnu.no> - 4.1.1-4
- Add patch to build with gcc-4.3

* Sat Feb  9 2008 Terje Rosten <terjeros@phys.ntnu.no> - 4.1.1-3
- rebuild

* Sat Jan  5 2008 Terje Rosten <terjeros@phys.ntnu.no> - 4.1.1-2
- Drop libs and devel packages
- Don't ship pc file

* Sat Jan  5 2008 Terje Rosten <terjeros@phys.ntnu.no> - 4.1.1-1
- 4.1.1 proper

* Thu Jan  3 2008 Terje Rosten <terjeros@phys.ntnu.no> - 4.1.1-0.1.S010308
- Update to 4.1.1-S010308 (4.1.0 + some gcc 4.3 and 64 bits fixes)
- Random spec clean ups
- Add man page, lib and pc file
- Create libs and devel subpackage
- Add rpath flag to configure

* Sun Aug 19 2007 Terje Rosten <terjeros@phys.ntnu.no> - 4.0.12a-2
- Fix license tag

* Tue Mar 13 2007 Terje Rosten <terjeros@phys.ntnu.no> - 4.0.12a-1
- New src upstream, lots of fixes
- Dropped subpackage: see updated LICENSE.txt
- Add ghostscript to req
- Add PDF doc

* Mon Mar 12 2007 Terje Rosten <terjeros@phys.ntnu.no> - 4.0.12-4
- Try to fix X11 preview support
- Drop preserve timestamps patch

* Mon Mar 12 2007 Terje Rosten <terjeros@phys.ntnu.no> - 4.0.12-3
- Subpackage: gui (different license on gui)
- Fix perms on src files (for debug pkg)
- Fix src url
- Fix LICENSE.txt
- Preserve timestamps
- More info: bz #229676

* Thu Feb 22 2007 Terje Rosten <terjeros@phys.ntnu.no> - 4.0.12-2
- Spec cleanup
- Build and ship qgle
- Add patch to avoid stripping

* Sun Oct 15 2006 Jonas Frantz <jonas.frantz@welho.com> - 4.0.12-1
- Updated to release 4.0.12

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 4.0.11-2.2
- Rebuild for Fedora Core 5

* Sat Dec 17 2005 Dries Verachtert <dries@ulyssis.org> - 4.0.11-1
- Updated to release 4.0.11

* Sat Nov 19 2005 Jonas Frantz <jonas.frantz@welho.com> - 4.0.10-2
- Fix problem with making inittex.ini

* Tue Nov 08 2005 Dries Verachtert <dries@ulyssis.org> - 4.0.10-1
- Initial package
