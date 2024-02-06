%global buildid    284
%global octpkg  COPASI

%global with_python  1

# Disabled bindings
%global with_java    0
%global with_octave  0
%global with_perl    0
%global with_r       0
%global with_mono    0
#

# Use QWT6? (Experimental)
%global with_qwt6    0

%if 0%{?with_octave}
# Exclude .oct files from provides
%global __provides_exclude_from ^%{octpkglibdir}/.*\\.oct$
%global octave_ver %(octave-config -p VERSION || echo 0)
%endif

%global _docdir_fmt %{name}

%global blaslib flexiblas
%global lapacklib flexiblas

ExcludeArch:   %{ix86}

Name:  COPASI
Summary: Biochemical network simulator
Version: 4.42.%{buildid}
Release: 6%{?dist}

## Artistic 2.0 is main license
## GPLv2+ is related to a Mixed Source Licensing Scenario
# with 'copasi/randomGenerator/Cmt19937.cpp' file
## GPLv3+ is related to a Mixed Source Licensing Scenario
# with 'copasi/function/CEvaluationParser_yacc.cpp' file
## BSD is related to a Mixed Source Licensing Scenario
# with 'copasi/randomGenerator/Cmt19937.cpp' file
## Any files with different licenses are not involved
License: Artistic-2.0 AND GPL-3.0-or-later AND BSD-3-Clause
URL:   http://copasi.org/
Source0: https://github.com/copasi/COPASI/archive/Build-%{buildid}/%{name}-Build-%{buildid}.tar.gz
Source1: %{name}.appdata.xml

%if 0%{?with_qwt6}
BuildRequires: qwt-devel
BuildRequires: qcustomplot-qt6-devel
%endif
BuildRequires: qwt-qt5-devel
BuildRequires: qwtplot3d-qt5-devel >= 0.3.1a-4
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtwebkit-devel
BuildRequires: qt5-qtdatavis3d-devel
BuildRequires: qcustomplot-qt5-devel
BuildRequires: libmml-qt5-devel
BuildRequires: freeglut-devel
BuildRequires: libsbml-devel
BuildRequires: libsedml-devel >= 2:2.0.19-0.1
BuildRequires: libnuml-devel, libnuml-static
BuildRequires: libCombine-devel
BuildRequires: zipper-devel
BuildRequires: libsbw-devel
BuildRequires: raptor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: cppunit-devel
BuildRequires: libcurl-devel
BuildRequires: libxslt-devel
BuildRequires: pkgconf-pkg-config
BuildRequires: %{blaslib}-devel
BuildRequires: crossguid2-devel >= 0:0.2.2
BuildRequires: desktop-file-utils
BuildRequires: swig
BuildRequires: expat-devel
BuildRequires: f2c
BuildRequires: flex
BuildRequires: cmake, gcc, gcc-c++
BuildRequires: bison
BuildRequires: bzip2-devel
BuildRequires: ImageMagick
BuildRequires: libappstream-glib
BuildRequires: minizip-devel
%ifarch x86_64
BuildRequires: nativejit-devel
%endif
%ifnarch s390x
BuildRequires: google-cpu_features-devel
%endif

Requires: %{name}-data = %{version}-%{release}
Requires: libsedml%{?_isa} >= 1:0.4.3-3

Obsoletes: R-%{octpkg} < 0:4.25.213-1
Obsoletes: perl-%{octpkg} < 0:4.25.213-1
Obsoletes: %{name}-sharp < 0:4.25.213-1

# This patch sets libraries' installation paths
Patch0: %{name}-fix_install_libpaths.patch

# This patch sets paths to find QWT5, QTMML, SBW files on Fedora
Patch1: %{name}-find_QWT5-QTMML-SBW.patch

# This patch sets paths to find QWT6, QTMML, SBW files on Fedora
Patch3: %{name}-find_QWT6-QTMML-SBW.patch

# This patch sets paths to find QTPLOT3D-QT4 files on Fedora
Patch2: %{name}-set_QWTPLOT3D_QT4.patch

# This patch fixes executable permissions of CopasiSE and CopasiUI
Patch4: %{name}-fix_exe_permissions.patch

# This patch sets paths to find QTPLOT3D-QT5 files on Fedora
Patch5: %{name}-set_QWTPLOT3D_QT5.patch

# This patch sets paths to find libCombine files on Fedora
Patch6: %{name}-libCombine_paths.patch

# This patch sets paths to find libcroosguid2 files on Fedora
Patch7: %{name}-find_crossguid2.patch

# This patch forces the use of C++17 standard
Patch8: %{name}-use_c++17.patch

# This patch sets paths to find libsedml files on Fedora
Patch9: %{name}-find_libsedml.patch

# This patch sets paths to find libsbw files on Fedora
Patch10: %{name}-find_sbw.patch

# rhbz#1896407
Patch11: %{name}-porting_to_python310.patch

Patch12: %{name}-find_raptor.patch

# qwt-6.2 compatibility
Patch13: %{name}-qwt62.patch

# This patch fixes a missing header request
Patch14: %{name}-4.41.283-fix_missing_header.patch

# This patch sets path to find qcustomplot-qt5 libraries on Fedora
Patch15: %{name}-find_qcp_libs.patch

# This patch fixes compatibility with swig-4.2.0
Patch16: %{name}-fix_swig_4.2.0_compatibility.patch

%description
COPASI is a software application for simulation and analysis of biochemical
networks and their dynamics.
COPASI is a stand-alone program that supports models in the SBML standard
and can simulate their behavior using ODEs or Gillespie's stochastic
simulation algorithm; arbitrary discrete events can be included in such
simulations.

COPASI carries out several analyses of the network and its dynamics and 
has extensive support for parameter estimation and optimization. 
COPASI provides means to visualize data in customizable plots, histograms and 
animations of network diagrams.


%package gui
Summary: The COPASI graphical user interface
Requires: %{name}-data = %{version}-%{release}
Requires: %{name}-doc = %{version}-%{release}

%description gui
COPASI is a software application for simulation and analysis of biochemical
networks and their dynamics.
COPASI is a stand-alone program that supports models in the SBML standard
and can simulate their behavior using ODEs or Gillespie's stochastic
simulation algorithm; arbitrary discrete events can be included in such
simulations.

COPASI carries out several analyses of the network and its dynamics and 
has extensive support for parameter estimation and optimization. 
COPASI provides means to visualize data in customizable plots, histograms and 
animations of network diagrams.
This package provides the COPASI graphical user interface.


%package data
Summary: COPASI data files 
BuildArch: noarch
%description data
This package provides the COPASI data, example and license files.

%if 0%{?with_python}
%package -n python3-%{name}
Summary: %{name} Python3 Bindings
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Obsoletes: python2-%{name} < 0:4.25.213-1
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-%{octpkg}
This package provides the libraries to 
develop applications with COPASI Python3 bindings.
%endif

%if 0%{?with_java}
%package -n java-%{octpkg}
Summary: %{name} Java Bindings
BuildRequires:  java-1.8.0-openjdk-devel
Requires: java-headless >= 1:minimal_required_version
Requires: javapackages-tools 
%description -n java-%{octpkg}
This package provides the libraries to 
develop applications with COPASI Java bindings.
%endif

%if 0%{?with_octave}
%package -n octave-%{octpkg}
Summary: %{name} Octave Bindings
BuildRequires:  octave-devel
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
%description -n octave-%{octpkg}
This package provides the libraries to 
develop applications with COPASI Octave bindings.
%endif

%if 0%{?with_perl}
%package -n perl-%{octpkg}
Summary: %{name} Perl Bindings
BuildRequires: perl-interpreter
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
%description -n perl-%{octpkg}
This package provides the libraries to 
develop applications with COPASI Perl bindings.
%endif

%if 0%{?with_r}
%package -n R-%{octpkg}
Summary: %{name} R Bindings
BuildRequires: R-devel, R-core-devel, tex(latex)
Requires:      R-core%{?_isa}
%description -n R-%{octpkg}
This package provides the libraries to 
develop applications with COPASI R bindings.
%endif

%if 0%{?with_mono}
%package sharp
Summary: %{name} Mono Bindings
BuildRequires: xerces-c-devel, libxml2-devel, expat-devel
BuildRequires: mono-core
BuildRequires: make

%description sharp
This package provides the libraries to 
develop applications with COPASI C# bindings.
%endif

%package doc
Summary: COPASI HTML documentation and examples
BuildArch: noarch
%description doc
COPASI HTML documentation and examples.

%prep
%autosetup -n %{name}-Build-%{buildid} -N

# This an old and obsolete license file
rm -f license.txt

# Convert to utf-8
for file in `find copasi -type f \( -name "*.cpp" \)`; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%patch -P 0 -p0 -b .fix_install_libpaths
%patch -P 4 -p0 -b .fix_exe_permissions
%patch -P 6 -p0 -b .libCombine_paths
%patch -P 7 -p0 -b .find_crossguid2
%patch -P 8 -p1 -b .use_c++17
%patch -P 9 -p0 -b .find_libsedml
%patch -P 10 -p0 -b .find_sbw
%patch -P 12 -p1 -b .find_raptor
%patch -P 13 -p1 -b .qwt
%patch -P 14 -p1 -b .backup
%patch -P 15 -p1 -b .backup
%patch -P 16 -p1 -b .backup

%if 0%{?with_python}
%if 0%{?python3_version_nodots} > 39
%patch -P 11 -p1 -b .porting_to_python310
%endif
%endif

%if 0%{?with_qwt6}
%patch -P 3 -p0
%else
%patch -P 1 -p0
%endif

# Set Qwt libdir
sed -e 's|@@libdir@@|%{_libdir}|g' -i CMakeModules/FindQWT.cmake

%patch -P 5 -p0 -b .QWTPLOT3D_QT5
# Set QTPLOT3D-QT5 paths
sed -e 's|@@qtplot3d_includedir@@|%{_qt5_headerdir}/qwtplot3d-qt5|g' -i CMakeModules/FindQWTPLOT3D.cmake
sed -e 's|@@qtplot3d_libdir@@|%{_qt5_libdir}|g' -i CMakeModules/FindQWTPLOT3D.cmake

# Set QtMmlQt5 paths
sed -e 's|@@_libmml_includedir@@|%{_qt5_headerdir}/libmml-qt5|g' -i CMakeModules/FindMML.cmake
sed -e 's|@@_libmml_libdir@@|%{_qt5_libdir}|g' -i CMakeModules/FindMML.cmake

# Exclude obsolete functions
# http://tracker.copasi.org/show_bug.cgi?id=2810#c1
sed -i.bak '/double sqrt(doublereal);/d' copasi/optimization/CNL2SOL.cpp
sed -i.bak '/double pow_dd(doublereal *, doublereal *);/d' copasi/optimization/CNL2SOL.cpp
sed -i.bak '/int s_copy(char *, char *, ftnlen, ftnlen);/d' copasi/optimization/CNL2SOL.cpp
sed -i.bak '/double sqrt(doublereal);/d' copasi/odepack++/dc_decsol.cpp
sed -i.bak '/double sqrt(doublereal),/d' copasi/odepack++/CRadau5.cpp
sed -i.bak '/double pow_dd(doublereal *,/d' copasi/odepack++/CRadau5.cpp
sed -i.bak '/C_FLOAT64 d_lg10(C_FLOAT64 *);/d' copasi/optimization/CPraxis.cpp

%build
export CXXFLAGS="%{build_cxxflags} -I$PWD/copasi/lapack -I$PWD/copasi/CopasiSBW -I%{_includedir}/%{blaslib} %{__global_ldflags}"
export LDFLAGS="%{__global_ldflags} -lbz2"
%global __cmake_in_source_build copasi
%cmake \
 -Wno-dev -DCOPASI_OVERRIDE_VERSION:STRING=%{version} \
%if 0%{?with_python}
 -DENABLE_PYTHON:BOOL=ON \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DPYTHON_INCLUDE_DIR:PATH=%{_includedir}/python%{python3_version}%(python3-config --abiflags) \
 -DPYTHON_LIBRARY:FILEPATH=%{_libdir}/libpython%{python3_version}%(python3-config --abiflags).so \
%else
 -DENABLE_PYTHON:BOOL=OFF \
%endif
%if 0%{?with_java}
 -DENABLE_JAVA:BOOL=ON \
 -DBUILD_JAVA_EXAMPLES:BOOL=OFF \
%endif
%if 0%{?with_octave}
 -DENABLE_OCTAVE:BOOL=ON \
 -DOCTAVE_INCLUDE_DIR:PATH=%{_includedir}/octave-%{octave_ver} \
 -DOCTAVE_OCTINTERP_LIBRARY:FILEPATH=%{_libdir}/octave/%{octave_ver}/liboctinterp.so \
 -DOCTAVE_OCTAVE_LIBRARY:FILEPATH=%{_libdir}/octave/%{octave_ver}/liboctave.so \
%endif
%if 0%{?with_perl}
 -DENABLE_PERL:BOOL=ON \
%endif
%if 0%{?with_r}
 -DENABLE_R:BOOL=ON \
 -DR_INCLUDE_DIRS:PATH=%{_includedir}/R \
%endif
%if 0%{?with_mono}
 -DENABLE_CSHARP:BOOL=ON \
 -DBUILD_CS_EXAMPLES:BOOL=OFF \
%endif
 -DCSHARP_COMPILER:FILEPATH=%{_bindir}/mcs \
%if 0%{?with_qwt6}
 -DQWT_VERSION_STRING:STRING="%(pkg-config --modversion qwt)" \
%endif
 -DENABLE_JIT:BOOL=OFF \
 -DSELECT_QT=Qt5 \
 -DSITE:STRING=fedora -DF2C_INTEGER=int -DF2C_LOGICAL=long \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{build_cxxflags} -I$PWD/copasi/lapack -I$PWD/copasi/CopasiSBW -I%{_includedir}/%{blaslib} %{__global_ldflags} -DNDEBUG" \
 -DCOPASI_INSTALL_C_API=OFF -DCombine_DIR:PATH=%{_libdir}/cmake \
 -DCMAKE_SHARED_LINKER_FLAGS:STRING="%{__global_ldflags} -pthread" \
 -DCMAKE_EXE_LINKER_FLAGS:STRING="%{__global_ldflags} -pthread" \
 -DQT_QMAKE_EXECUTABLE:FILEPATH=%{_bindir}/qmake-qt5 \
 -DQWT_VERSION_STRING:STRING="%(pkg-config --modversion Qt5Qwt6)" \
 -DQWT_LIBRARY:FILEPATH=%{_qt5_libdir}/libqwt-qt5.so \
 -DQWT_INCLUDE_DIR:PATH=%{_qt5_headerdir}/qwt \
 -DBUILD_GUI:BOOL=ON -DBUILD_COPASISBW:BOOL=ON -DENABLE_MML:BOOL=ON -DENABLE_USE_SBMLUNIT=ON \
 -DMML_INCLUDE_DIR:PATH=%{_qt5_headerdir}/libmml-qt5 -DMML_LIBRARY:FILEPATH=%{_qt5_libdir}/libmml.so \
 -DENABLE_SBW_INTEGRATION=ON -DBUILD_CXX_EXAMPLES=OFF \
 -DENABLE_COPASI_BANDED_GRAPH:BOOL=ON -DENABLE_COPASI_SEDML:BOOL=ON \
 -DENABLE_COPASI_NONLIN_DYN_OSCILLATION:BOOL=ON -DENABLE_COPASI_EXTUNIT:BOOL=ON \
 -DCOPASI_OVERWRITE_USE_LAPACK:BOOL=ON -DNO_BLAS_WRAP:BOOL=ON -DBLA_VENDOR=Generic \
 -DBLAS_blas_LIBRARY:FILEPATH=%{_libdir}/lib%{blaslib}.so \
 -DLAPACK_lapack_LIBRARY:FILEPATH=%{_libdir}/lib%{lapacklib}.so \
 -DCROSSGUID_INCLUDE_DIR:PATH=%{_includedir}/crossguid2 \
 -DENABLE_COPASI_PARAMETERFITTING_RESIDUAL_SCALING:BOOL=ON \
 -DENABLE_WITH_MERGEMODEL:BOOL=ON -DENABLE_USE_MATH_CONTAINER:BOOL=ON \
 -DLIBSBML_INCLUDE_DIR:PATH=%{_includedir}/sbml -DLIBSBML_SHARED:BOOL=ON -DLIBSBML_LIBRARY:FILEPATH=%{_libdir}/libsbml.so \
 -DLIBNUML_LIBRARY:FILEPATH=%{_libdir}/libnuml.so -DEXTRA_INCLUDE_DIRS:STRING=-I%{_includedir}/numl \
 -DEXPAT_LIBRARY:FILEPATH=%{_libdir}/libexpat.so -DEXPAT_INCLUDE_DIR:PATH=%{_includedir} \
 -DF2C_INCLUDE_DIR:PATH=%{_includedir} \
 -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DENABLE_GPROF:BOOL=OFF \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DENABLE_FLEX_BISON:BOOL=ON -DBISON_EXECUTABLE:FILEPATH=%{_bindir}/bison \
 -DPREFER_STATIC:BOOL=OFF -DCMAKE_SKIP_RPATH:BOOL=YES -DCOPASI_USE_QCUSTOMPLOT:BOOL=ON

%cmake_build

%install
%cmake_install

# Remove directory of examples
%if 0%{?with_python}
rm -rf  $RPM_BUILD_ROOT%{python3_sitearch}/copasi/examples
%endif

# For R library only
%if 0%{?with_r}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library build/copasi/bindings/R/%{name}_*.tar.gz
test -d %{octpkg}/src && (cd %{octpkg}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/%{octpkg}/R.css
chmod a+x $RPM_BUILD_ROOT%{_libdir}/R/library/%{octpkg}/libs/COPASI.so
%endif

%if 0%{?with_octave}
mkdir -p $RPM_BUILD_ROOT%{octpkgdir}/packinfo
install -pm 644 copasi/ArtisticLicense.txt $RPM_BUILD_ROOT%{octpkgdir}/packinfo
%endif

# Install .xpm icon files
install -pm 644 copasi/UI/icons/Copasi48-Alpha.xpm $RPM_BUILD_ROOT%{_datadir}/icons/copasi/icons

# Make a .desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=CopasiUI
Comment=Use COPASI by a Graphical User Interface
Exec=CopasiUI --copasidir %{_prefix}
Icon=%{_datadir}/icons/copasi/icons/Copasi48-Alpha.xpm
Terminal=false
Type=Application
Categories=Science;
EOF

# Install appdata file
mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_metainfodir}/

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.appdata.xml

%files
%{_bindir}/CopasiSE

%files gui
%{_bindir}/CopasiUI
%{_bindir}/CopasiSBW
%{_datadir}/icons/copasi/
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/*.appdata.xml

%files data
%license copasi/ArtisticLicense.txt
%{_datadir}/copasi/
%exclude %{_datadir}/copasi/doc/

%if 0%{?with_python}
%files -n python3-%{octpkg}
%license copasi/ArtisticLicense.txt
%{python3_sitearch}/copasi/
%{python3_sitearch}/*.pth
%endif

%if 0%{?with_java}
%files -n java-%{octpkg}
%license copasi/ArtisticLicense.txt
%{_javadir}/*.jar
%{_javadir}/copasi/
%{_libdir}/copasi/
%endif

%if 0%{?with_octave}
%files -n octave-%{octpkg}
%dir %{octpkgdir}
%{octpkgdir}/packinfo/ArtisticLicense.txt
%{octpkglibdir}/
%endif

%if 0%{?with_perl}
%files -n perl-%{octpkg}
%license copasi/ArtisticLicense.txt
%{perl_vendorarch}/auto/COPASI/
%endif

%if 0%{?with_r}
%files -n R-%{octpkg}
%license copasi/ArtisticLicense.txt
%{_libdir}/R/library/%{octpkg}/
%endif

%if 0%{?with_mono}
%files sharp
%license copasi/ArtisticLicense.txt
%{_prefix}/lib/mono/copasicsP/
%endif

%files doc
%license copasi/ArtisticLicense.txt
%{_datadir}/copasi/doc/

%changelog
* Sun Feb 04 2024 Antonio Trande <sagitter@fedoraproject.org> - 4.42.284-6
- Exclude ix86 architectures

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.42.284-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Antonio Trande <sagitter@fedoraproject.org> - 4.42.284-4
- Patched for swig-4.2.0 (rhbz#2259156)

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.42.284-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.42.284-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 02 2023 Antonio Trande <sagitter@fedoraproject.org> - 4.42.284-1
- Release 4.42 build-284

* Thu Nov 30 2023 Antonio Trande <sagitter@fedoraproject.org> - 4.41.283-1
- Release 4.41 build-283
- Add COPASI_USE_QCUSTOMPLOT cmake option (upstream bug #3202)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.40.278-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.40.278-2
- Rebuilt for Python 3.12

* Thu Jun 01 2023 Antonio Trande <sagitter@fedoraproject.org> - 4.40.278-1
- Release 4.40 build-278

* Fri Feb 03 2023 Antonio Trande <sagitter@fedoraproject.org> - 4.39.272-1
- Release 4.39 build-272

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.38.268-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Sandro Mani <manisandro@gmail.com> - 4.38.268-2
- Rebuild (qwt)

* Sat Dec 03 2022 Antonio Trande <sagitter@fedoraproject.org> - 4.38.268-1
- Release 4.38 build-268

* Thu Oct 06 2022 Antonio Trande <sagitter@fedoraproject.org> - 4.37.264-1
- Release 4.37 build-264

* Tue Oct 04 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.36.260-3
- Applied the patch for rhbz#2128029

* Fri Sep 23 2022 Antonio Trande <sagitter@fedoraproject.org> - 4.36.260-2
- Patched for rhbz#2128029

* Tue Sep 13 2022 Antonio Trande <sagitter@fedoraproject.org> - 4.36.260-1
- Release 4.36 build-260

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.35.258-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.35.258-3
- Rebuilt for Python 3.11

* Wed May 11 2022 Antonio Trande <sagitter@fedoraproject.org> - 4.35.258-2
- Rebuild for libCombine-0.2.17

* Sat Mar 19 2022 Antonio Trande <sagitter@fedoraproject.org> - 4.35.258-1
- Release 4.35 build-258

* Sat Mar 05 2022 Antonio Trande <sagitter@fedoraproject.org> - 4.34.251-4
- Fix rhbz#2060860

* Wed Feb 09 2022 Antonio Trande <sagitter@fedoraproject.org> - 4.34.251-3
- JIT disabled in Fedora 36 (rhbz#2052707)

* Sun Jan 30 2022 Antonio Trande <sagitter@fedoraproject.org> - 4.34.251-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
- Patched for GCC-12

* Fri Aug 13 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.34.251-1
- Release 4.34 build-251

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.33.246-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.33.246-2
- Rebuild for qwtplot3d-qt5

* Sun Jun 20 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.33.246-1
- Release 4.33 build-246

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.31.243-2
- Rebuilt for Python 3.10

* Thu May 13 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.31.243-1
- Release 4.31 build-243

* Thu Mar 18 2021 Antonio Trande <sagitter@fedoraproject.org> - 4.30.240-1
- Release 4.30 build-240

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.29.228-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 12 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.29.228-3
- Porting to Python-3.10

* Wed Aug 12 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.29.228-2
- Use flexiblas on Fedora 33+

* Wed Aug 12 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.29.228-1
- Release 4.29 build-228

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.28.226-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Iñaki Úcar <iucar@fedoraproject.org> - 4.28.226-3
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Wed Jun 24 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.28.226-2
- BuildRequires python-setuptools explicitly

* Mon Jun 15 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.28.226-1
- Release 4.28 build-226

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.27.217-5
- Rebuilt for Python 3.9

* Fri May 15 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.27.217-4
- Rebuild for zipper-1.0.1/libCombine-0.2.7

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.27.217-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Richard Shaw <hobbes1069@gmail.com> - 4.27.217-2
- Rebuilt for qt5-qtdatavis3d 5.13.2.

* Sat Sep 14 2019 Antonio Trande <sagitter@fedoraproject.org> - 4.27.217-1
- Release 4.27 build-217

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.25.213-2
- Rebuilt for Python 3.8

* Wed Jul 31 2019 Antonio Trande <sagitter@fedoraproject.org> - 4.25.213-1
- Release 4.25 build-213
- Use standard c++17
- Disable R package
- Disable perl package

* Wed Jun 19 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 4.25.207-6
- Do not list Git-tracked COPASI.rpmlintrc as source

* Tue Jun 18 2019 Orion Poplawski <orion@nwra.com> - 4.25.207-5
- Rebuild for octave 5.1

* Sat Jun 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.25.207-4
- Perl 5.30 rebuild

* Tue May 21 2019 Antonio Trande <sagitter@fedoraproject.org> - 4.25.207-3
- Use Python3 abiflags

* Sun May 05 2019 Antonio Trande <sagitter@fedoraproject.org> - 4.25.207-2
- Rebuild for libsbml-5.18.0

* Sat Mar 16 2019 Antonio Trande <sagitter@fedoraproject.org> - 4.25.207-1
- Release 4.25 build-207
- Use openblas always
- Add crossguid dependency

* Fri Mar 08 2019 Antonio Trande <sagitter@fedoraproject.org> - 4.24.197-8
- Obsolete COPASI-sharp on fedora 30+/pp64* (rhbz#1588734,#1686738)

* Fri Mar 08 2019 Antonio Trande <sagitter@fedoraproject.org> - 4.24.197-7
- Exclude mono builds on fedora 30+/pp64* (rhbz#1588734,#1686738)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.24.197-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Orion Poplawski <orion@cora.nwra.com> - 4.24.197-5
- Rebuild for octave 4.4

* Mon Sep 24 2018 Antonio Trande <sagitter@fedoraproject.org> - 4.24.197-4
- Bundle minizip on fedora 30+ (rhbz#1632172) (upstream bug #466)

* Tue Aug 28 2018 Patrik Novotný <panovotn@redhat.com - 4.24.197-3
- change requires to minizip-compat(-devel), rhbz#1609830, rhbz#1615381

* Sun Aug 05 2018 Antonio Trande <sagitter@fedoraproject.org> - 4.24.197-2
- Rebuild for libsbw-2.12.2

* Tue Jul 31 2018 Antonio Trande <sagitter@fedoraproject.org> - 4.24.197-1
- Release 4.24 build-197
- Erase obsolete patches
- Drop Python2 binding
- Disable BUILD_CXX_EXAMPLES

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.23.184-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 4.23.184-14
- Perl 5.28 rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.23.184-13
- Perl 5.28 rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.23.184-12
- Rebuilt for Python 3.7

* Wed Jun 06 2018 Antonio Trande <sagitter@fedoraproject.org> - 4.23.184-11
- Rebuild for libsbml-5.17.0

* Mon Jun 04 2018 Antonio Trande <sagitter@fedoraproject.org> - 4.23.184-10
- Patched for Qt-5.11.0 (upstream bugs #2625 #2629)

* Fri Jun 01 2018 Antonio Trande <sagitter@fedoraproject.org> - 4.23.184-9
- Remove directory of examples

* Fri Jun 01 2018 Antonio Trande <sagitter@fedoraproject.org> - 4.23.184-8
- Fix Python interpreter again
- Add COPASI.rpmlintrc

* Thu May 31 2018 Antonio Trande <sagitter@fedoraproject.org> - 4.23.184-7
- Use always Qt5

* Fri May 18 2018 Antonio Trande <sagitter@fedoraproject.org> - 4.23.184-6
- Fix Python interpreter

* Thu May 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 4.23.184-5
- Rebuild with Qt5

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 4.23.184-4
- rebuild for R 3.5.0

* Sat May 05 2018 Antonio Trande <sagitter@fedoraproject.org> - 4.23.184-3
- Now built with Qt5
- Built against libmml

* Sun Apr 29 2018 Antonio Trande <sagitter@fedoraproject.org> - 4.23.184-2
- Now built with Qt4
- Disable java/octave bindings

* Sun Apr 29 2018 Antonio Trande <sagitter@fedoraproject.org> - 4.23.184-1
- Update to version 4.23 -build 184
- Add libCombine, zipper, minizip dependencies
- Build with Qt5

* Thu Feb 15 2018 Antonio Trande <sagitter@fedoraproject.org> - 4.22.170-7
- Rebuild for libsbml-5.16.0
- Disable Octave binding on ARM ('virtual memory exhausted' issue)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.22.170-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.22.170-5
- Appdata file moved into metainfo data directory

* Sun Dec 10 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.22.170-4
- Rebuild for libsbml-5.16.0

* Fri Nov 24 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.22.170-3
- Additional screeshots (bz#1517299)

* Fri Nov 24 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.22.170-2
- Appdata file edited (bz#1517299)

* Sat Nov 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.22.170-1
- Update to version 4.22 -build 170
- Use OpenBlas

* Thu Oct 12 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.21.166-2
- Remove old Obsoletes

* Tue Oct 10 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.21.166-1
- Update to version 4.21 -build 166

* Fri Sep 22 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.20.165-1
- Update to version 4.20 -build 165

* Tue Sep 05 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.20.159-1
- Update to version 4.20 -build 159

* Wed Aug 16 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.20.158-4
- Fix Python interpreter

* Mon Aug 07 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.20.158-3
- Reintroduce command to disable generation of the debuginfo package on s390x (bz#1478284)

* Tue Aug 01 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.20.158-2
- Make a new conditional macro to control stripping of symbols from object files

* Mon Jul 31 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.20.158-1
- Update to version 4.20 -build 158
- Debuginfo packages built

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.19.156-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.19.156-1
- Update to version 4.19 -build 156

* Sun Jul 02 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.19.155-1
- Update to version 4.19 -build 155 (fix upstream bug #2428)

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.19.150-2
- Perl 5.26 rebuild

* Fri Jun 02 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.19.150-1
- Update to version 4.19 -build 150 (fix upstream bug #2415)

* Sat Apr 15 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.19.148-1
- Update to version 4.19 -build 148 (fix upstream bug #2403)

* Fri Apr 14 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.19.147-3
- Rebuild for libsbml-5.15.0

* Thu Apr 06 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.19.147-2
- Override version from headers
- Fix installation of examples and docs
- Fix copasidir option
- Strip executable binary/library files

* Sun Mar 26 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.19.147-1
- Update to version 4.19 -build 147
- Fix Octave binding (upstream bug #2342)

* Sat Mar 04 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.19.146-1
- Update to version 4.19 -build 146

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.19.143-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.19.143-1
- Update to version 4.19 -build 143

* Wed Jan 18 2017 Antonio Trande <sagitter@fedoraproject.org> - 4.19.141-1
- Update to version 4.19 -build 141

* Thu Dec 22 2016 Antonio Trande <sagitter@fedoraproject.org> - 4.18.138-1
- Update to build 138 (bug fixes from upstream)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.18.136-4
- Rebuild for Python 3.6

* Tue Dec 13 2016 Antonio Trande <sagitter@fedoraproject.org> - 4.18.136-3
- Exclude Octave-4.2 binding (upstream bug #2342)

* Wed Dec 07 2016 Orion Poplawski <orion@cora.nwra.com> - 4.18.136-2
- Rebuild for octave 4.2

* Tue Nov 29 2016 Antonio Trande <sagitter@fedoraproject.org> - 4.18.136-1
- Update to build-136 (stable release)

* Tue Nov 22 2016 Antonio Trande <sagitter@fedoraproject.org> - 4.17-0.15.20161122gita15717
- Update to build-135 (stable release)

* Thu Nov 17 2016 Antonio Trande <sagitter@fedoraproject.org> - 4.17-0.14.20161115git6c93c0
- Update to build-134 (fix bugs 2324 2327)

* Sun Nov 06 2016 Antonio Trande <sagitter@fedoraproject.org> - 4.17-0.13.20161102gitbdf5cd
- Fix memory issue on s390

* Fri Nov 04 2016 Antonio Trande <sagitter@fedoraproject.org> - 4.17-0.12.20161102gitbdf5cd
- Disable generation of debuginfo package on s390

* Wed Nov 02 2016 Antonio Trande <sagitter@fedoraproject.org> - 4.17-0.11.20161102gitbdf5cd
- Update to build-131
- Drop old patch

* Mon Oct 17 2016 Antonio Trande <sagitter@fedoraproject.org> - 4.17-0.10.20161013gitde9275
- Update to build-128

* Thu Oct 13 2016 Antonio Trande <sagitter@fedoraproject.org> - 4.17-0.9.20161011git00c753
- Update to build-127 (bz#1384081)

* Sun Sep 11 2016 Antonio Trande <sagitter@fedoraproject.org> - 4.17-0.8.20160909git7c2623
- Update to build-123

* Wed Aug 17 2016 Antonio Trande <sagitter@fedoraproject.org> - 4.17-0.7.20160720git31a978
- Rebuild for Python 3.5.2

* Wed Jul 27 2016 Antonio Trande <sagitter@fedoraproject.org> - 4.17-0.6.20160720git31a978
- Update to build-119

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.17-0.5.20160203git7b0f05
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.17-0.4.20160203git7b0f05
- Perl 5.24 rebuild

* Tue Apr 19 2016 Antonio Trande <sagitter@fedoraproject.org> - 4.17-0.3.20160203git7b0f05
- Rebuild for libSBML 5.13.0

* Sun Feb 07 2016 Antonio Trande <sagitter@fedoraproject.org> - 4.17-0.2.20160203git7b0f05
- Exclude Octave binding on s390

* Wed Feb 03 2016 Antonio Trande <sagitter@fedoraproject.org> - 4.17-0.1.20160203git7b0f05
- Rebuild with GCC-6.0
- Update to commit #7b0f05
- License for octave sub-package relocated
- Debugging re-enabled

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.16-0.22.20150817git3bc4e9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Antonio Trande <sagitter@fedoraproject.org> - 4.16-0.21.20150817git3bc4e9
- Renamed Python2 package

* Sun Dec 13 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16-0.20.20150817git3bc4e9
- Rebuild with GCC-5.3

* Sat Nov 14 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16-0.19.20150817git3bc4e9
- Rebuilt for libsbml-5.12.0 and Python3.5

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.16-0.18.20150817git3bc4e9
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Nov 06 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16-0.17.20150817git3bc4e9
- Hardened rebuild on Fedora <23

* Fri Nov 06 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16-0.16.20150817git3bc4e9
- Rebuild with -pie on Fedora >22

* Sat Sep 19 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16-0.15.20150817git3bc4e9
- Fixed COPASI-gui icon

* Fri Sep 18 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16-0.14.20150817git3bc4e9
- Rebuild for libsedml update

* Tue Aug 25 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16-0.13.20150817git3bc4e9
- Removed obsolete license file

* Thu Aug 20 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16-0.12.20150817git3bc4e9
- Bump to commit #3bc4e9
- Disabled debug package
- Version tag changed to 4.16 (now it's built a pre-release)
- CXX examples built

* Mon Jul 27 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16.101-11.20150725git435d61
- Bump to commit #435d61
- Disabled debug package

* Tue Jul 21 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16.101-10.20150707git192df4
- Patched CCopasiMethod.cpp (debuginfo issue caused by //)
- Enabled debug package

* Fri Jul 17 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16.101-9.20150707git192df4
- Fixed License
- Fixed executable permissions

* Mon Jul 13 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16.101-8.20150707git192df4
- Enabled COPASI-sharp build
- Disabled debug packages

* Sat Jul 11 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16.101-7.20150707git192df4
- Disabled COPASI-sharp build

* Thu Jul 09 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16.101-6.20150707git192df4
- QWT5/6 lib paths set separately

* Wed Jul 08 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16.101-5.20150707git192df4
- Removed unused Qt macros

* Tue Jul 07 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16.101-4.20150707git192df4
- Update to post-release #192df4
- With QWT6
- Octave binding disabled

* Tue Jun 30 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16.101-3.20150626git678de9
- Update to post-release #678de9 (ARM fixing)
- Without QWT6
- Packaged an appdata file for COPASI-gui

* Wed Jun 17 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16.101-2.20150617git865113
- Update to post-release #865113
- Built with clang on F23 64bit

* Wed Jun 10 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.16.101-1
- Update to the release 4.16.101

* Mon Feb 02 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.14.90-6.20150126git4848fe
- Defined F2C_INTEGER/F2C_LOGICAL variables based on arch

* Mon Jan 26 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.14.90-5.20150126git4848fe
- New commit (4848fe)
- Defined new F2C_INTEGER/F2C_LOGICAL variables (fix bug(copasi)#2119)

* Mon Jan 12 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.14.90-4.20150109git8f2d99
- New commit (8f2d99)

* Wed Jan 07 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.14.90-3.20150109gite316ac
- New commit (fix bug(copasi)#2121#2123)

* Mon Jan 05 2015 Antonio Trande <sagitter@fedoraproject.org> - 4.14.90-2.20150105git9b6683
- New commit (fix bug(copasi)#2119)

* Tue Dec 30 2014 Antonio Trande <sagitter@fedoraproject.org> - 4.14.90-1.20141208git3431bd
- First package

