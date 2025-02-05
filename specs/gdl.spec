%global commit f29c1fa51cfe3771ad156a05cc3962d4ffbbe102
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global __cmake_in_source_build 1

#TODO - Build with mpi support

# No more antlr-C++ or Java on i686
ExcludeArch: %{ix86}

# No eccodes or grib_api on EL9 s390x
%if 0%{?rhel} >= 9 && "%{_arch}" == "s390x"
%bcond_with grib
%else
%bcond_without grib
%endif

%bcond_without java

%if 0%{?rhel} == 9 && "%{_arch}" == "ppc64le"
# lto seems to have a problem with latest eigen3
# https://bugzilla.redhat.com/show_bug.cgi?id=1996330
%global _lto_cflags %nil
%endif

%if 0%{?el8}
# libqhullcpp.a(PointCoordinates.cpp.o): relocation R_X86_64_PC32 against symbol `_ZTVN8orgQhull10QhullErrorE' can not be used when making a shared object; recompile with -fPIC
%bcond_with qhull
%else
%bcond_without qhull
%endif

Name:           gdl
Version:        1.0.6
Release:        %autorelease
Summary:        GNU Data Language

License:        GPL-2.0-or-later
URL:            http://gnudatalanguage.sourceforge.net/
Source0:        https://github.com/gnudatalanguage/gdl/releases/download/v%{version}/gdl-v%{version}.tar.gz
#Source0:        https://github.com/gnudatalanguage/gdl/releases/download/weekly-release/gdl-unstable-f29c1fa.tar.gz
Source1:        gdl.csh
Source2:        gdl.sh
Source4:        xorg.conf
# Build with system antlr library.  Request for upstream change here:
# https://sourceforge.net/tracker/index.php?func=detail&aid=2685215&group_id=97659&atid=618686
Patch1:         gdl-antlr.patch

BuildRequires:  gcc-c++
BuildRequires:  antlr-C++
BuildRequires:  antlr-tool
%if %{with java}
BuildRequires:  java-devel
%endif
BuildRequires:  eigen3-static
BuildRequires:  expat-devel
BuildRequires:  fftw-devel
BuildRequires:  glpk-devel
BuildRequires:  GraphicsMagick-c++-devel
BuildRequires:  gsl-devel
BuildRequires:  hdf-static
BuildRequires:  hdf5-devel
BuildRequires:  libdivide-devel
BuildRequires:  libgeotiff-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtirpc-devel
BuildRequires:  ncurses-devel
BuildRequires:  netcdf-devel
BuildRequires:  plplot-wxGTK-devel >= 5.11
BuildRequires:  proj-devel
BuildRequires:  pslib-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-matplotlib
BuildRequires:  readline-devel
# Not yet possible to build with external dSFMT
#BuildRequires:  dSFMT-devel
Provides:       bundled(dSFMT)
BuildRequires:  shapelib-devel
%if %{with grib}
# eccodes not available on these arches
%ifnarch i686 s390x
BuildRequires:  eccodes-devel
%else
BuildRequires:  grib_api-devel
%endif
%endif
%if %{with qhull}
BuildRequires:  qhull-devel
%endif
BuildRequires:  udunits2-devel
BuildRequires:  wxGTK%{?el8:3}-devel
BuildRequires:  cmake3
# For tests
# EL8 s390x missing xorg-x11-drv-dummy
%if ! ( 0%{?rhel} >= 8 && "%{_arch}" == "s390x" )
BuildRequires:  xorg-x11-drv-dummy
BuildRequires:  metacity
%endif
BuildRequires: make
# Needed to pull in drivers
Requires:       plplot
# Widgets use wx
Recommends:     plplot-wxGTK
Requires:       %{name}-common = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
# Need to match hdf5 compile time version
Requires:       hdf5 = %{_hdf5_version}


%description
A free IDL (Interactive Data Language) compatible incremental compiler
(i.e. runs IDL programs). IDL is a registered trademark of Research
Systems Inc.


%package        common
Summary:        Common files for GDL
Requires:       %{name}-runtime = %{version}-%{release}
BuildArch:      noarch

%description    common
Common files for GDL


%package        -n python%{python3_pkgversion}-gdl
%{?python_provide:%python_provide python%{python3_pkgversion}-gdl}
# Remove before F30
Provides: %{name}-python = %{version}-%{release}
Provides: %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}
Summary:        GDL python module
# Needed to pull in drivers
Requires:       plplot
Requires:       %{name}-common = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description    -n python%{python3_pkgversion}-gdl
%{summary}.


%prep
%setup -q -n %{name}-v%{version}
rm -rf src/antlr src/libdivide.h
# Not yet possible to build with external dSFMT
#rm -r src/dSFMT
%patch -P1 -p1 -b .antlr

# Find grib_api on architectures where needed
sed -i -e '/find_library(GRIB_LIBRARIES/s/eccodes/eccodes grib_api/' CMakeModules/FindGrib.cmake

pushd src
for f in *.g
do
  antlr $f
done
popd

%global __python %{__python3}
%global python_sitearch %{python3_sitearch}
%global cmake_opts \\\
   -DGDL_LIB_DIR:PATH=%{_libdir}/gnudatalanguage \\\
   -DGEOTIFF_INCLUDE_DIR=%{_includedir}/libgeotiff \\\
   -DGRIB=ON \\\
   -DOPENMP=ON \\\
   -DPYTHON_EXECUTABLE=%{__python} \\\
   -DWXWIDGETS=ON \\\
   %{!?with_grib:-DGRIB=OFF} \\\
   %{!?with_qhull:-DQHULL=OFF} \\\
%{nil}
# TODO - build an mpi version
#           INCLUDES="-I/usr/include/mpich2" \
#           --with-mpich=%{_libdir}/mpich2 \

%build
export CXXFLAGS="%optflags -fcommon"
mkdir build build-python
#Build the standalone executable
pushd build
%cmake3 %{cmake_opts} ..
make #{?_smp_mflags}
popd
#Build the python module
pushd build-python
%cmake3 %{cmake_opts} -DPYTHON_MODULE=ON ..
make #{?_smp_mflags}
popd


%install
pushd build
%make_install
popd
pushd build-python
%make_install
# Install the python module in the right location
install -d -m 0755 $RPM_BUILD_ROOT%{python_sitearch}
%if "%{_lib}" != "lib"
mv $RPM_BUILD_ROOT%{_prefix}/lib/python*/site-packages/GDL.so \
  $RPM_BUILD_ROOT%{python_sitearch}/GDL.so
%endif
popd

# Install the profile file to set GDL_PATH
install -d -m 0755 $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -m 0644 %SOURCE1 $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -m 0644 %SOURCE2 $RPM_BUILD_ROOT%{_sysconfdir}/profile.d


# EL8 s390x missing xorg-x11-drv-dummy
%if ! ( 0%{?rhel} >= 8 && "%{_arch}" == "s390x" )
%check
export GDL_DRV_DIR=$RPM_BUILD_ROOT%{_libdir}/gnudatalanguage
cd build
cp %SOURCE4 .
if [ -x /usr/libexec/Xorg ]; then
   Xorg=/usr/libexec/Xorg
elif [ -x /usr/libexec/Xorg.bin ]; then
   Xorg=/usr/libexec/Xorg.bin
else
   # Strip suid root
   cp /usr/bin/Xorg .
   Xorg=./Xorg
fi
$Xorg -noreset +extension GLX +extension RANDR +extension RENDER -logfile ./xorg.log -config ./xorg.conf -configdir . :99 &
export DISPLAY=:99

metacity &
sleep 2
# byte_conversion/bytscl - https://github.com/gnudatalanguage/gdl/issues/1079
# test_l64 - https://github.com/gnudatalanguage/gdl/issues/1075
# test_elmhes/formats - https://github.com/gnudatalanguage/gdl/issues/1833
%ifarch aarch64
failing_tests="test_(byte_conversion|bytscl|elmhes|formats)"
%endif
%ifarch ppc64le
# gaussfit - https://github.com/gnudatalanguage/gdl/issues/1695
failing_tests="test_(byte_conversion|bytscl|elmhes|formats|finite|gaussfit|matrix_multiply)"
%endif
%ifarch riscv64
failing_tests="test_(byte_conversion|bytscl|elmhes|formats|finite|tic_toc)"
%endif
%ifarch s390x
# test_hdf5 - https://github.com/gnudatalanguage/gdl/issues/1488
# save_restore - https://github.com/gnudatalanguage/gdl/issues/1655
failing_tests="test_(byte_conversion|bytsc|elmhes|formats|hdf5|tic_toc|save_restore)"
%endif
make test VERBOSE=1 ARGS="-V -E '$failing_tests'"
make test VERBOSE=1 ARGS="-V -R '$failing_tests' --timeout 600" || :
kill %1 || :
cat xorg.log
%endif


%files
%license COPYING
%doc AUTHORS HACKING NEWS README
%config(noreplace) %{_sysconfdir}/profile.d/gdl.*sh
%{_bindir}/gdl
%{_libdir}/gnudatalanguage/
%{_mandir}/man1/gdl.1*

%files common
%{_datadir}/gnudatalanguage/

%files -n python%{python3_pkgversion}-gdl
%{python_sitearch}/GDL.so


%changelog
%autochangelog
