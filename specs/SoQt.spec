%global cpack_hash 118ac5a21bcf57f0f90e2b0e681c9dcbf07074c2
%global cpack_short %(c=%{cpack_hash}; echo ${c:0:10})
%global cpack_date 20200419
%global soanydata_hash 3ff6e9203fbb0cc08a2bdf209212b7ef4d78a1f2
%global soanydata_short %(c=%{soanydata_hash}; echo ${c:0:10})
%global soanydata_date 20200419
%global sogui_hash 4b0019d1ecc2b9ad3e77333b9f243b57a15ebc4e
%global sogui_short %(c=%{soanydata_hash}; echo ${c:0:10})
%global sogui_date 20200419

Name:           SoQt
Version:        1.6.0
Release:        18%{?dist}
Summary:        High-level 3D visualization library
# Old version had been licensed GPLv2
License:        BSD-3-Clause

URL:            http://www.coin3d.org
Source0:        https://github.com/coin3d/soqt/archive/%{name}-%{version}.tar.gz

Source1:        https://github.com/coin3d/cpack.d/archive/%{cpack_hash}/coin3d-cpack-%{cpack_date}git%{cpack_short}.tar.gz
Source2:        https://github.com/coin3d/soanydata/archive/%{soanydata_hash}/coin3d-soanydata-%{soanydata_date}git%{soanydata_short}.tar.gz
Source3:        https://github.com/coin3d/sogui/archive/%{sogui_hash}/coin3d-sogui-%{sogui_date}git%{sogui_short}.tar.gz

Patch1:         SoQt-1.6.0-cmake.patch

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  /usr/bin/iconv
BuildRequires:  /usr/bin/perl
BuildRequires:  Coin4-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  libXi-devel

Provides:       Coin4-SoQt = %{version}-%{release}

%description
SoQt is a Qt GUI component toolkit library for Coin.  It is also compatible
with SGI and TGS Open Inventor, and the API is based on the API of the
InventorXt GUI component toolkit.


%package devel
Summary: Development files for SoQt
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: Coin4-devel
Requires: qt5-qtbase-devel
Requires: libXi-devel

Provides: Coin4-SoQt-devel = %{version}-%{release}

%description devel
Development package for SoQt.


%prep
%autosetup -p1 -n soqt-%{name}-%{version}

mkdir cpack.d data src/Inventor/Qt/common
tar --strip-components=1 -C cpack.d -xf %{SOURCE1}
tar --strip-components=1 -C data -xf %{SOURCE2}
tar --strip-components=1 -C src/Inventor/Qt/common -xf %{SOURCE3}

# Some sources are ISO-8859-1 encoded
# We want doxygen to generate utf-8 encoded docs from them
for nonUTF8 in \
  src/Inventor/Qt/common/SoGuiRenderArea.cpp.in \
  src/Inventor/Qt/common/viewers/SoGuiExaminerViewer.cpp.in \
  src/Inventor/Qt/common/viewers/SoGuiFullViewer.h.in \
  src/Inventor/Qt/common/viewers/SoGuiViewer.cpp.in \
; do \
  %{_bindir}/iconv -f ISO-8859-1 -t utf-8 $nonUTF8 > $nonUTF8.conv
  mv -f $nonUTF8.conv $nonUTF8
done

# No timestamps in doxygen generated docs!
sed -i -e 's,HTML_TIMESTAMP.*= YES,HTML_TIMESTAMP = NO,' \
  src/Inventor/Qt/common/sogui.doxygen.cmake.in

%build
mkdir build-%{_build_arch} && cd build-%{_build_arch}
%cmake -DSOQT_BUILD_DOCUMENTATION=TRUE \
       -DSOQT_BUILD_DOC_MAN=TRUE \
       -S .. -B .

%make_build


%install
cd build-%{_build_arch}
%make_install

# Move the headers to the same directory as Coin4.
mkdir -p %{buildroot}%{_includedir}/Coin4
mv %{buildroot}%{_includedir}/Inventor %{buildroot}%{_includedir}/Coin4/

# Remove stray files
rm -rf %{buildroot}/usr/share/info/SoQt1


%files
%doc AUTHORS ChangeLog* README
%license COPYING
%{_libdir}/libSoQt.so.*

%files devel
%{_docdir}/%{name}/html/
%{_datadir}/%{name}/
%{_includedir}/Coin4/Inventor/
%{_libdir}/libSoQt.so
%{_libdir}/pkgconfig/SoQt.pc
%{_libdir}/cmake/%{name}-%{version}/
%{_mandir}/man?/*.?.gz


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 15 2024 Richard Shaw <hobbes1069@gmail.com> - 1.6.0-17
- Update cmake patch to add SoQt library to pkgconf file, fixes #2260745.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 20 2023 Richard Shaw <hobbes1069@gmail.com> - 1.6.0-13
- Rebuild for Coin4.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 15 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.6.0-11
- Switch off HTML_TIMESTAMPs.

* Thu Dec 15 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.6.0-10
- Convert license to SPDX.
- Remove bogusly installed /usr/share/info/SoQt1.
- Fix broken handling of non-utf8 sources.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.6.0-5
- Work around cmake madness (F33FTBS, RHBZ#1863123).

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 05 2019 Richard Shaw <hobbes1069@gmail.com> - 1.6.0-1
- Update to 1.6.0.
- Move from autotools to CMake based build.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 02 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.5.0-20
- Add BR: /usr/bin/perl.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.5.0-18
- Remove stray COPYING from %%doc.

* Sun Jan 03 2016 Corsépius <corsepiu@fedoraproject.org> - 1.5.0-17
- Elimiate %%define.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.5.0-15
- Rebuilt for GCC 5 C++11 ABI change

* Fri Feb 27 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.5.0-14
- Fix bogus %%changelog entry.
- Let SoQt-devel require SoQt%%{?_isa}.

* Thu Feb 26 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.5.0-13
- Rebuild against Coin3.
- Modernise spec.
- Remove %%optflags and %%__global_ld_flags from *.cfg.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 24 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.5.0-9
- Update config.{guess,sub} to allow building for aarch64*
  (Add SoQt-1.5.0-config.patch; RHBZ #926552).

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 23 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.5.0-7
- Fix typo in spec.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 11 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.5.0-5
- Prevent empty LDFLAGS from choking sed.

* Sun Mar 11 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.5.0-4
- Modernize spec.
- Filter CFLAGS/LDFLAGS clutter in *.pc, *.cfg.
- Pass x_includes=" " x_libraries=" " to %%configure to work-around RHBZ #801369.
- Don't add build-time to doxygen generated docs (Add SoQt-1.5.0-doxgen.diff).

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 03 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.5.0-1
- Upstream update.
- Spec file overhaul.
- Remove qt4-fixes.patch.

* Mon Feb 15 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.4.1-15
- Pass CONFIG_QTLIBS to configure to work around (BZ 564918).

* Mon Nov 23 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.4.1-14
- Let soqt-config search in %%{_libdir}/Coin2.

* Sun Nov 22 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.4.1-13
- Eliminate stray /usr/share/Coin directory.

* Wed Jul 29 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.4.1-12
- Switch to qt4.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar 25 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.4.1-9
- s/qt-devel/qt3-devel/

* Sun Feb 10 2008 Ralf Corsépius <rc040203@freenet.de> - 1.4.1-8
- Rebuild for gcc43.

* Thu Nov 29 2007 Ralf Corsépius <rc040203@freenet.de> - 1.4.1-7
- Rebuild against Coin-2.5.0.
- Rebuild with doxygen-1.5.3-1 (BZ 343211).

* Wed Aug 22 2007 Ralf Corsépius <rc040203@freenet.de> - 1.4.1-6
- Mass rebuild.
- Update license tag.

* Tue Feb 20 2007 Ralf Corsépius <rc040203@freenet.de> - 1.4.1-5
- Install soqt-default.cfg into %%{_prefix}/%%{_lib}

* Mon Feb 19 2007 Ralf Corsépius <rc040203@freenet.de> - 1.4.1-4
- Filter errant -L%%_libdir from soqt-config.cfg.
- Remove *.la.

* Fri Jan 19 2007 Ralf Corsépius <rc040203@freenet.de> - 1.4.1-3
- BR: libXi-devel, R: libXi-devel 
  (Work-around to XInput.h/libXi packaging issues).

* Sat Nov 04 2006 Ralf Corsépius <rc040203@freenet.de> - 1.4.1-2
- Inc Release due to buildsys bug.

* Sat Nov 04 2006 Ralf Corsépius <rc040203@freenet.de> - 1.4.1-1
- Upstream update.

* Fri Sep 08 2006 Ralf Corsépius <rc040203@freenet.de> - 1.4.0-1
- Upstream update.
- Add utf-8/doxygen hack.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.3.0-4
- Mass rebuild.

* Wed May 31 2006 Ralf Corsépius <rc040203@freenet.de> - 0:1.3.0-3
- Rebuild against Coin-2.4.5.
- Spec file cleanup.

* Mon Feb 20 2006 Ralf Corsépius <rc040203@freenet.de> - 0:1.3.0-2
- Rebuild for FC5.

* Fri Sep 23 2005 Ralf Corsepius <rc040203@freenet.de> - 0:1.3.0-1
- Update to 1.3.0
- Build w/o simacros.
