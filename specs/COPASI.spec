%global buildid    298
%global octpkg  COPASI

%global with_python  1

# Disabled bindings
%global with_java    0
%global with_octave  0
%global with_perl    0
%global with_r       0
%global with_mono    0
#

%global with_raptor  0

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
Version: 4.45.%{buildid}
Release: %autorelease

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
%if 0%{?with_raptor}
BuildRequires: raptor2-devel
%endif
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

# qwt-6.2 compatibility
Patch13: %{name}-qwt62.patch

# This patch fixes a missing header request
Patch14: %{name}-4.41.283-fix_missing_header.patch

# This patch sets path to find qcustomplot-qt5 libraries on Fedora
Patch15: %{name}-find_qcp_libs.patch

# Allow CMake 4.0 builds
# https://github.com/copasi/COPASI/pull/11
Patch20: %{name}-cmake4.patch
Patch21: %{name}-bug3304.patch

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
%patch -P 6 -p0 -b .libCombine_paths
%patch -P 7 -p0 -b .find_crossguid2
%patch -P 8 -p1 -b .use_c++17
%patch -P 9 -p0 -b .find_libsedml
%patch -P 10 -p0 -b .find_sbw
%patch -P 13 -p1 -b .qwt
%patch -P 14 -p1 -b .backup
%patch -P 15 -p1 -b .backup
%patch -P 20 -p1 -b .cmake4
%patch -P 21 -p1 -b .backup

%if 0%{?with_python}
%patch -P 11 -p1 -b .porting_to_python310
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
%if 0%{?with_raptor}
 -DCOPASI_USE_RAPTOR:BOOL=ON -DRAPTOR_INCLUDE_DIR:PATH=%{_includedir}/raptor2 -DRAPTOR_LIBRARY:FILEPATH=%{_libdir}/libraptor2.so \
%else
 -DCOPASI_USE_RAPTOR:BOOL=OFF \
%endif
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
 -DLIBSBML_SHARED:BOOL=ON -DLIBSBML_LIBRARY:FILEPATH=%{_libdir}/libsbml.so \
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
%autochangelog
