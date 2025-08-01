%global abi 1

Summary:	An OpenGL to PostScript printing library
Summary(pl):	Biblioteka drukowania z OpenGL-a do PostScriptu
Name:		gl2ps
Version:	1.4.2
Release:	15%{?dist}
License:	LGPL-2.0-or-later OR GL2PS
Source0:	http://www.geuz.org/gl2ps/src/%{name}-%{version}.tgz
# bump min cmake version requirement to work with cmake 4.0
Patch0:		gl2ps-cmake4.patch
URL:		http://www.geuz.org/gl2ps/
BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:	libGL-devel
BuildRequires:  libpng-devel

%description
GL2PS is a C library providing high quality vector output for any
OpenGL application. The main difference between GL2PS and other
similar libraries is the use of sorting algorithms capable of handling
intersecting and stretched polygons, as well as non manifold objects.
GL2PS provides advanced smooth shading and text rendering, culling of
invisible primitives, mixed vector/bitmap output, and much more...

GL2PS can currently create PostScript (PS), Encapsulated PostScript
(EPS) and Portable Document Format (PDF) files, as well as LaTeX files
for the text fragments. Adding new vector output formats should be
relatively easy (and amongst the formats we would be interested in
adding, SVG is first in line). Meanwhile, you can use the excellent
pstoedit program to transform the PostScript files generated by GL2PS
into many other vector formats such as xfig, cgm, wmf, etc.

%description -l pl
GL2PS to biblioteka C zapewniająca wysokiej jakości wyjście wektorowe
dla dowolnej aplikacji OpenGL. Główna różnica między GL2PS a innymi
podobnymi bibliotekami polega na użyciu algorytmów sortujących
potrafiących obsłużyć przecinające się i rozciągnięte wielokąty, a
także obiekty nie będące rozmaitościami. GL2PS zapewnia zaawansowane
gładkie cieniowanie i renderowanie tekstu, usuwanie niewidocznych
prymitywów, mieszane wyjście wektorowo-bitmapowe i wiele więcej.

GL2PS aktualnie potrafi tworzyć pliki PostScript (PS), Encapsulated
PostScript (EPS) oraz Portable Document Format (PDF), a także pliki
LaTeXa dla fragmentów tekstowych. Dodanie nowych wyjściowych formatów
wektorowych powinno być względnie łatwe (a spośród formatów, których
dodanie zainteresowani byliby autorzy, pierwszym jest SVG). Tymczasem
można używać świetnego programu pstoedit do przekształcania plików
PostScript generowanych przez GL2PS na wiele innych formatów
wektorowych, takich jak xfig, cgm, wmf itp.

%package devel
Summary:	Header files for GL2PS library
Summary(pl):	Pliki nagłówkowe biblioteki GL2PS
Requires:	%{name}%{_isa} = %{version}-%{release}
Requires:	libGL-devel

%description devel
Header files for GL2PS library.

%description devel -l pl
Pliki nagłówkowe biblioteki GL2PS.

%prep
%autosetup -p1

%build
%cmake -DLIB_SUFFIX=$(echo %{_lib} | sed 's/^lib//')
%cmake_build

%install
%cmake_install

rm -r %{buildroot}%{_docdir}/gl2ps
rm %{buildroot}%{_libdir}/libgl2ps.a

%files
%license COPYING.GL2PS COPYING.LGPL
%doc README.txt
%{_libdir}/libgl2ps.so.%{abi}*

%files devel
%doc gl2ps.pdf gl2psTest*.c
%{_libdir}/libgl2ps.so
%{_includedir}/gl2ps.h

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Mar 12 2025 Dominik Mierzejewski <dominik@greysector.net> - 1.4.2-14
- fix build with cmake 4.0 (resolves rhbz#2349466)

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.2-12
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 20 2020 Dominik Mierzejewski <rpm@greysector.net> 1.4.2-2
- use new cmake macros

* Thu Apr 30 2020 Dominik Mierzejewski <rpm@greysector.net> 1.4.2-1
- updated to 1.4.2
- include ABI version in shared library filename to prevent accidental bumps
- drop obsolete patch

* Mon Apr 6 2020 Dominik Mierzejewski <rpm@greysector.net> 1.4.1-1
- updated to 1.4.1
- retain ABI compatibility

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 17 2017 Dominik Mierzejewski <rpm@greysector.net> 1.4.0-1
- updated to 1.4.0
- libpng-devel requires zlib-devel
- drop obsolete spec file elements
- use modern make build/install macros
- use license macro

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 07 2015 Dominik Mierzejewski <rpm@greysector.net> 1.3.9-1
- updated to 1.3.9

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Orion Poplawski <orion@cora.nwra.com> 1.3.8-1
- Updated to 1.3.8
- Dropped soversion patch applied upstream
- Don't need to move library on 64bit anymore

* Sat Sep 01 2012 Dominik Mierzejewski <rpm@greysector.net> 1.3.6-1
- updated to 1.3.6

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.3.5-3
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 26 2009 Dominik Mierzejewski <rpm@greysector.net> 1.3.5-1
- updated to 1.3.5
- dropped upstreamed patches
- fixed install in libdir
- fixed missing SO version

* Sun Aug 23 2009 Dominik Mierzejewski <rpm@greysector.net> 1.3.3-1
- updated to 1.3.3
- removed calls to exit(3)
- added a simple build system (Makefile)
- dropped libtool dependency
- 1.3.3 added a new symbol, so made it versioned
- added examples to -devel docs

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun 13 2008 Dominik Mierzejewski <rpm@greysector.net> 1.3.2-1
- adapted PLD spec r1.2
- dropped static package
