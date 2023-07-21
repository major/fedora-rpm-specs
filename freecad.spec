# Setup python target for shiboken so the right cmake file is imported.
%global py_suffix %(%{__python3} -c "import sysconfig; print(sysconfig.get_config_var('SOABI'))")

# Maintainers:  keep this list of plugins up to date
# List plugins in %%{_libdir}/freecad/lib, less '.so' and 'Gui.so', here
%global plugins Complete DraftUtils Drawing Fem FreeCAD Image Import Inspection Mesh MeshPart Part PartDesign Path Points QtUnit Raytracing ReverseEngineering Robot Sketcher Spreadsheet Start Web PartDesignGui _PartDesign Spreadsheet SpreadsheetGui area

# Some configuration options for other environments
# rpmbuild --with=bundled_zipios:  use bundled version of zipios++
%global bundled_zipios %{?_with_bundled_zipios: 1} %{?!_with_bundled_zipios: 0}
# rpmbuild --without=bundled_pycxx:  don't use bundled version of pycxx
%global bundled_pycxx %{?_with_bundled_pycxx: 1} %{?!_with_bundled_pycxx: 0}
# rpmbuild --without=bundled_smesh:  don't use bundled version of Salome's Mesh
%global bundled_smesh %{?_with_bundled_smesh: 0} %{?!_with_bundled_smesh: 1}

#global commit 110860fa4700dabf263918f80afcc75982b7dc37
#global short %(c=%{commit}; echo ${c:0:10})
#global date 20210221


Name:           freecad
Epoch:          1
Version:        0.20.2
Release:        5%{?dist}
Summary:        A general purpose 3D CAD modeler

License:        GPLv2+
URL:            http://freecadweb.org/
Source0:        https://github.com/FreeCAD/FreeCAD/archive/%{version}%{?pre:_pre}/FreeCAD-%{version}%{?pre:_pre}.tar.gz
Source102:      freecad.1

Patch0:         freecad-unbundled-pycxx.patch
Patch1:         freecad-cstdint.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} > 36
ExcludeArch:    i686
%endif

# Utilities
BuildRequires:  cmake gcc-c++ gettext dos2unix
BuildRequires:  doxygen swig graphviz
BuildRequires:  gcc-gfortran
BuildRequires:  desktop-file-utils
%ifnarch ppc64
BuildRequires:  tbb-devel
%endif
# Development Libraries
BuildRequires:  freeimage-devel
BuildRequires:  libXmu-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  libglvnd-devel
BuildRequires:  opencascade-devel
BuildRequires:  Coin4-devel
BuildRequires:  python3-devel
BuildRequires:  python3-matplotlib
BuildRequires:  python3-pivy
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
# Qt5 dependencies
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5UiTools)
%ifarch x86_64 aarch64
BuildRequires:  cmake(Qt5WebEngine)
%else
BuildRequires:  cmake(Qt5WebKit)
%endif
BuildRequires:  cmake(Qt5XmlPatterns)
#BuildRequires:  SoQt-devel
BuildRequires:  xerces-c xerces-c-devel
BuildRequires:  libspnav-devel
BuildRequires:  python3-shiboken2-devel
BuildRequires:  python3-pyside2-devel pyside2-tools
%if ! %{bundled_smesh}
BuildRequires:  smesh-devel
%endif
# Does not build with current versions of OCCT.
#BuildRequires:  netgen-mesher-devel
%if ! %{bundled_zipios}
BuildRequires:  zipios++-devel
%endif
%if ! %{bundled_pycxx}
BuildRequires:  python3-pycxx-devel
%endif
BuildRequires:  libicu-devel
BuildRequires:  vtk-devel
#BuildRequires:  openmpi-devel
BuildRequires:  med-devel
BuildRequires:  libkdtree++-devel

# For appdata
%if 0%{?fedora}
BuildRequires:  libappstream-glib
%endif

Requires:       python3-pivy
Requires:       python3-matplotlib
Requires:       python3-collada
Requires:       python3-pyside2
Requires:       qt5-assistant

Requires:       %{name}-data = %{epoch}:%{version}-%{release}

Provides:       bundled(smesh) = 5.1.2.2


%description
FreeCAD is a general purpose Open Source 3D CAD/MCAD/CAx/CAE/PLM modeler, aimed
directly at mechanical engineering and product design but also fits a wider
range of uses in engineering, such as architecture or other engineering
specialties. It is a feature-based parametric modeler with a modular software
architecture which makes it easy to provide additional functionality without
modifying the core system.


%package data
Summary:        Data files for FreeCAD
BuildArch:      noarch
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description data
Data files for FreeCAD


%prep
%autosetup -p1 -n FreeCAD-%{version}
# Remove bundled pycxx if we're not using it
%if ! %{bundled_pycxx}
rm -rf src/CXX
%endif

%if ! %{bundled_zipios}
rm -rf src/zipios++
%endif

# Fix encodings
dos2unix -k src/Mod/Test/unittestgui.py \
            ChangeLog.txt \
            data/License.txt


%build
%cmake -DCMAKE_CXX_STANDARD=17 \
       -DCMAKE_INSTALL_PREFIX=%{_libdir}/%{name} \
       -DCMAKE_INSTALL_DATADIR=%{_datadir}/%{name} \
       -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
       -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir} \
       -DRESOURCEDIR=%{_datadir}/%{name} \
       -DPYTHON_EXECUTABLE=%{__python3} \
       -DPYSIDE_INCLUDE_DIR=/usr/include/PySide2 \
       -DPYSIDE_LIBRARY=%{_libdir}/libpyside2.%{py_suffix}.so \
       -DSHIBOKEN_INCLUDE_DIR=%{_includedir}/shiboken2 \
       -DSHIBOKEN_LIBRARY=%{_libdir}/libshiboken2.%{py_suffix}.so \
       -DBUILD_QT5=ON \
       -DOpenGL_GL_PREFERENCE=LEGACY \
       -DCOIN3D_INCLUDE_DIR=%{_includedir}/Coin4 \
       -DCOIN3D_DOC_PATH=%{_datadir}/Coin4/Coin \
       -DUSE_OCC=TRUE \
%if ! %{bundled_smesh}
       -DFREECAD_USE_EXTERNAL_SMESH=TRUE \
       -DSMESH_INCLUDE_DIR=%{_includedir}/smesh \
%endif
%if ! %{bundled_zipios}
       -DFREECAD_USE_EXTERNAL_ZIPIOS=TRUE \
%endif
%if ! %{bundled_pycxx}
       -DPYCXX_INCLUDE_DIR=$(pkg-config --variable=includedir PyCXX) \
       -DPYCXX_SOURCE_DIR=$(pkg-config --variable=srcdir PyCXX) \
%endif
       -DMEDFILE_INCLUDE_DIRS=%{_includedir}/med

%cmake_build


%install
%cmake_install

# Symlink binaries to /usr/bin
mkdir -p %{buildroot}%{_bindir}
ln -rs %{buildroot}%{_libdir}/freecad/bin/FreeCAD %{buildroot}%{_bindir}
ln -rs %{buildroot}%{_libdir}/freecad/bin/FreeCADCmd %{buildroot}%{_bindir}

# Move mis-installed files to the right location
# Need to figure out if FreeCAD can install correctly at some point.
mkdir -p %{buildroot}%{_datadir}
mv %{buildroot}%{_libdir}/%{name}/share/* \
   %{buildroot}%{_datadir}

# Install man page
install -pD -m 0644 %{SOURCE102} \
    %{buildroot}%{_mandir}/man1/%{name}.1

# Symlink manpage to other binary names
pushd %{buildroot}%{_mandir}/man1
ln -sf %{name}.1.gz FreeCAD.1.gz 
ln -sf %{name}.1.gz FreeCADCmd.1.gz
popd

# Remove obsolete Start_Page.html
rm -f %{buildroot}%{_docdir}/%{name}/Start_Page.html

# Belongs in %%license not %%doc
rm -f %{buildroot}%{_docdir}/freecad/ThirdPartyLibraries.html

# Remove header from external library that's erroneously installed
rm -f %{buildroot}%{_libdir}/%{name}/include/E57Format/E57Export.h

# Remove redundant HTML version of the license
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE.html

# Bytecompile Python modules
%py_byte_compile %{__python3} %{buildroot}%{_libdir}/%{name}


%check
desktop-file-validate \
    %{buildroot}%{_datadir}/applications/org.freecadweb.FreeCAD.desktop
%{?fedora:appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/*.appdata.xml}


%files
%license data/License.txt src/Doc/ThirdPartyLibraries.html LICENSE
%doc ChangeLog.txt README.md
%{_bindir}/*
%{_metainfodir}/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/freecad.svg
%{_datadir}/icons/hicolor/scalable/apps/org.freecadweb.FreeCAD.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-extension-fcstd.svg
%{_datadir}/pixmaps/freecad.xpm
%{_datadir}/mime/packages/*.xml
%{_datadir}/thumbnailers/FreeCAD.thumbnailer
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/bin/
%{_libdir}/%{name}/%{_lib}/
%{_libdir}/%{name}/Ext/
%{_libdir}/%{name}/Mod/
%{_mandir}/man1/*.1.gz

%files data
%{_datadir}/%{name}/


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.20.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1:0.20.2-4
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.20.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 15 2023 Orion Poplawski <orion@nwra.com> - 1:0.20.2-2
- Rebuild for vtk 9.2.5

* Fri Jan 13 2023 Richard Shaw <hobbes1069@gmail.com> - 1:0.20.2-1
- Update to 0.20.2.

* Tue Aug 30 2022 Richard Shaw <hobbes1069@gmail.com> - 1:0.20.1-1.1
- Rebuild for retagged upstream source, fixes rhbz#2121671.
- Readd Python 3.11 patches that did not make it into the current release.

* Tue Aug 09 2022 Richard Shaw <hobbes1069@gmail.com> - 1:0.20.1-1
- Update to 0.20.1.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Richard Shaw <hobbes1069@gmail.com> - 1:0.20-1
- Update to 0.20.

* Fri Jun 24 2022 Jonathan Wakely <jwakely@redhat.com> -1:0.19.4-4
- Remove obsolete boost-python3-devel build dependency (#2100748)

* Wed May 11 2022 Richard Shaw <hobbes1069@gmail.com> - 1:0.19.4-3
- Add patch to provide std::unique_ptr, fixes #2084307.

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1:0.19.4-2
- Rebuilt for Boost 1.78

* Tue Mar 01 2022 Richard Shaw <hobbes1069@gmail.com> - 1:0.19.4-1
- Update to 0.19.4.

* Sat Jan 29 2022 Richard Shaw <hobbes1069@gmail.com> - 1:0.19.3-1
- Update to 0.19.3.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.19.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 25 2021 Orion Poplawski <orion@nwra.com> - 1:0.19.2-6
- Rebuild for vtk 9.1.0

* Thu Aug 19 2021 Richard Shaw <hobbes1069@gmail.com> - 1:0.19.2-5
- Add patch from upstream for better vtk9 compatibility.

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 1:0.19.2-4
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.19.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1:0.19.2-2
- Rebuilt for Python 3.10

* Wed May 05 2021 Richard Shaw <hobbes1069@gmail.com> - 1:0.19.2-1
- Update to 0.19.2.

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 1:0.19-0.8.20210130git4db83a41ca
- Rebuilt for removed libstdc++ symbol (#1937698)

* Sun Feb 21 2021 Richard Shaw <hobbes1069@gmail.com> - 1:0.19-0.8.20210221git110860fa47
- Update to 110860fa4700dabf263918f80afcc75982b7dc37.

* Sun Jan 31 2021 Orion Poplawski <orion@nwra.com> - 1:0.19-0.7.20210130git4db83a41ca
- Rebuild for VTK 9

* Sat Jan 30 2021 Richard Shaw <hobbes1069@gmail.com> - 1:0.19-0.6.20210130git4db83a41ca
- Update to 0.19pre, git 4db83a41ca5800a0238a3030c81e33950c3070a3.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.19-0.5.20201125gita50ae33557
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1:0.19-0.4.20201125gita50ae33557
- Rebuilt for Boost 1.75

* Wed Nov 25 2020 Richard Shaw <hobbes1069@gmail.com> - 1:0.19-0.3.20201125gita50ae33557
- Rebuild with OCC 7.5.0.

* Wed Nov 25 2020 Richard Shaw <hobbes1069@gmail.com> - 1:0.19-0.2.20201125gita50ae33557
- Update to latest git checkout, properly fixes ambiguous reference in
  Part/Sketcher.

* Wed Nov 25 2020 Richard Shaw <hobbes1069@gmail.com> - 1:0.19-0.1.20201124git6bd39e8a90
- Update to 0.19 pre-release.

* Mon Nov 23 2020 Richard Shaw <hobbes1069@gmail.com> - 1:0.18.4-13
- Rebuild for OpenCascade 7.5.0.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Miro Hrončok <mhroncok@redhat.com> - 1:0.18.4-10
- Bytecompile Python modules

* Wed Jun 03 2020 Scott Talbert <swt@techie.net> - 1:0.18.4-9
- Fix build with unbundled pycxx

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:0.18.4-8
- Rebuilt for Python 3.9

* Tue May 05 2020 Richard Shaw <hobbes1069@gmail.com> - 1:0.18.4-7
- Rebuild for Pyside2 5.14.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Richard Shaw <hobbes1069@gmail.com> - 1:0.18.4-5
- Move < f32 back to Coin3.

* Thu Jan 09 2020 Richard Shaw <hobbes1069@gmail.com> - 1:0.18.4-2
- Rebuild for Qt/PySide 5.13.2.

* Tue Nov 05 2019 Richard Shaw <hobbes1069@gmail.com> - 1:0.18.4-1
- Update to 0.18.4.

* Mon Nov 04 2019 Richard Shaw <hobbes1069@gmail.com> - 1:0.18.3-7
- Fix python3-pyside2 requires and other specfile cleanup.

* Mon Oct 28 2019 Richard Shaw <hobbes1069@gmail.com> - 1:0.18.3-6
- Rebuild for downgraded PySide2 so the version matches with Qt5.

* Thu Oct 10 2019 Richard Shaw <hobbes1069@gmail.com> - 1:0.18.3-5.1
- Rebuild for Coin4 and python-pyside2 on rawhide (f32).
- Rebuild for python-pyside2 only for others.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:0.18.3-4
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Ivan Mironov <mironov.ivan@gmail.com> - 1:0.18.3-3
- Build C++ code with usual CXXFLAGS (including -O2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.18.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Richard Shaw <hobbes1069@gmail.com> - 1:0.18.3-1
- Update to 0.18.3.

* Mon May 20 2019 Richard Shaw <hobbes1069@gmail.com> - 1:0.18.2-3
- Bump release so NVER is higher on f31 than f30 & f29.

* Sun May 19 2019 Richard Shaw <hobbes1069@gmail.com> - 1:0.18.2-2
- Remove more python2 dependencies and fix shiboken building with python2.

* Sun May 12 2019 Richard Shaw <hobbes1069@gmail.com> - 1:0.18.2-1
- Update to 0.18.2.
- Hopefully fix python3 issues.

* Sun Mar 24 2019 Richard Shaw <hobbes1069@gmail.com> - 1:0.18-2
- Rebuild to require python3 pivy and collada.

* Wed Mar 13 2019 Richard Shaw <hobbes1069@gmail.com> - 1:0.18-1
- Update to 0.18.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Richard Shaw <hobbes1069@gmail.com> - 1:0.17-1
- Update to 0.17 release.

* Sat Mar 31 2018 Richard Shaw <hobbes1069@gmail.com> - 1:0.17-0.1
- Update to 0.17 prerelease.

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 1:0.16-12
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 23 2017 Richard Shaw <hobbes1069@gmail.com> - 1:0.16-10
- Add qt-assistant so that help works properly.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 1:0.16-7
- Rebuilt for Boost 1.64

* Thu May 11 2017 Richard Shaw <hobbes1069@gmail.com> - 1:0.16-6
- Rebuild for OCE 0.18.1.

* Tue Feb 07 2017 Kalev Lember <klember@redhat.com> - 1:0.16-5
- Rebuilt for Boost 1.63

* Wed Dec 28 2016 Rich Mattes <richmattes@gmail.com> - 1:0.16-4
- Rebuild for eigen3-3.3.1

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 1:0.16-3
- rebuilt for matplotlib-2.0.0

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 1:0.16-2
- Rebuilt for linker errors in boost (#1331983)

* Wed Apr 13 2016 Richard Shaw <hobbes1069@gmail.com> - 1:0.16-1
- Update to latest upstream release.

* Wed Apr  6 2016 Richard Shaw <hobbes1069@gmail.com> - 1:0.16-0.1
- Update to 0.16 prerelease.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Jonathan Wakely <jwakely@redhat.com> 0.15-11
- Patched and rebuilt for Boost 1.60

* Mon Jan  4 2016 Richard Shaw <hobbes1069@gmail.com> - 1:0.15-10
- Fix appdata license, fixes BZ#1294623.

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1:0.15-9
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1:0.15-7
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Richard Shaw <hobbes1069@gmail.com> - 1:0.15-5
- Fix version reporting in the About dialog (BZ#1192841).

* Tue May 19 2015 Richard Shaw <hobbes1069@gmail.com> - 1:0.15-4
- Bump Epoch to downgrade to 0.14 for Fedora 21 and below due to Coin2/Coin3
  library mismatch between Freecad & python-pivy (BZ#1221713).

* Fri Apr 10 2015 Richard Shaw <hobbes1069@gmail.com> - 0.15-1
- Update to latest upstream release.

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.14-6
- Rebuild for boost 1.57.0

* Tue Jan  6 2015 Richard Shaw <hobbes1069@gmail.com> - 0.14-5
- Fix bug introduced by PythonSnap patch, fixes BZ#1178672.

* Thu Sep 18 2014 Richard Shaw <hobbes1069@gmail.com> - 0.14-4
- Patch PythonSnap, fixes BZ#1143814.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug  4 2014 Richard Shaw <hobbes1069@gmail.com> - 0.14-2
- Add python-pyside as requirement as it is not currently being pulled in as a
  automatic dependency by rpmbuild.

* Wed Jul 16 2014 Richard Shaw <hobbes1069@gmail.com> - 0.14-1
- Update to latest upstream release.

* Mon Jun 23 2014 John Morris <john@zultron.com> - 0.13-10
- Add Requires: qt-assistant for bz #1112045

* Thu Jun 19 2014 Richard Shaw <hobbes1069@gmail.com> - 0.13-9
- Fix obsoletes of old documentation subpackage.
- Add conditional so EPEL 6 ppc64 does not require python-pivy which does not
  build on that platform.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Richard Shaw <hobbes1069@gmail.com> - 0.13-7
- Update OCE patch with bad conditional which caused undefined symbols.

* Fri May 23 2014 Richard Shaw <hobbes1069@gmail.com> - 0.13-6
- Fix duplicate documentation.
- Correct license tag to GPLv2+.

* Mon May 19 2014 Richard Shaw <hobbes1069@gmail.com> - 0.13-5
- Move noarch data into it's own subpackage.
- Fix cmake conditionals to work for epel7.

* Thu Oct 10 2013 Richard Shaw <hobbes1069@gmail.com> - 0.13-4
- Rebuild for OCE 0.13.

* Mon Jul 15 2013 Richard Shaw <hobbes1069@gmail.com> - 0.13-3
- Rebuild for updated OCE.

* Mon Apr 29 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.13-2
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Feb 18 2013 Richard Shaw <hobbes1069@gmail.com> - 0.13-1
- Update to latest upstream release.

* Sat Oct 20 2012 John Morris <john@zultron.com> - 0.12-9
- Use cmake28 package on el6
- Remove COIN3D_DOC_PATH cmake def (one less warning during build)
- Add PyQt as requirement.
- Add libicu-devel as build requirement.

* Wed Sep 26 2012 Richard Shaw <hobbes1069@gmail.com> - 0.12-8
- Rebuild for boost 1.50.

* Thu Jul 05 2012 Richard Shaw <hobbes1069@gmail.com> - 0.12-7
- Remove BuildRequires: tbb-devel and gts-devel
- Add missing license files to %%doc.
- Add missing requirement for hicolor-icon-theme.
- Fix excessive linking issue.
- Other minor spec updates.

* Mon Jun 25 2012  <john@zultron.com> - 0.12-6
- Filter out automatically generated Provides/Requires of private libraries
- freecad.desktop not passing 'desktop-file-validate'; fixed
- Remove BuildRequires: tbb-devel and gts-devel
- Update license tag to GPLv3+ only.
- Add missing license files to %%doc.
- Add missing build requirement for hicolor-icon-theme.
- Fix excessive linking issue.
- Other minor spec updates.

* Mon Jun 25 2012  <john@zultron.com> - 0.12-5
- New patch to unbundle PyCXX
- Add conditional build options for OpenCASCADE, bundled Zipios++,
  bundled PyCXX, bundled smesh

* Tue Jun 19 2012 Richard Shaw <hobbes1069@gmail.com> - 0.12-4
- Add linker flag to stop excessive linking.

* Thu May 31 2012 Richard Shaw <hobbes1069@gmail.com> - 0.12-3
- Add patch for GCC 4.7 on Fedora 17.

* Thu Nov 10 2011 Richard Shaw <hobbes1069@gmail.com> - 0.12-2
- Initial release.
