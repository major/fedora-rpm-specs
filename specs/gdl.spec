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
Release:        7%{?dist}
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
rm -rf src/antlr
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
* Sun Feb 02 2025 Orion Poplawski <orion@nwra.com> - 1.0.6-7
- Rebuild with gsl 2.8

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 23 2024 Orion Poplawski <orion@nwra.com> - 1.0.6-5
- Rebuild with numpy 2.x (rhbz#2333764)

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 1.0.6-4
- Rebuild for hdf5 1.14.5

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 14 2024 Orion Poplawski <orion@nwra.com> - 1.0.6-2
- Rebuilt for Python 3.13

* Thu May 23 2024 Orion Poplawski <orion@nwra.com> - 1.0.6-1
- Update to 1.0.6

* Tue May 21 2024 Orion Poplawski <orion@nwra.com> - 1.0.5-1
- Update to 1.0.5

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.0.4-5
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 24 2023 Sandro Mani <manisandro@gmail.com> - 1.0.4-2
- Rebuild (shapelib)

* Sat Dec 16 2023 Orion Poplawski <orion@nwra.com> - 1.0.4-1
- Update to 1.0.4

* Fri Aug 11 2023 Tom Callaway <spot@fedoraproject.org> - 1.0.2-4
- rebuild against new qhull

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 27 2023 Python Maint <python-maint@redhat.com> - 1.0.2-2
- Rebuilt for Python 3.12

* Sun Jan 22 2023 Orion Poplawski <orion@nwra.com> - 1.0.2-1
- Update to 1.0.2
- Use SPDX License tag

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 15 2022 Scott Talbert <swt@techie.net> - 1.0.1-11
- Rebuild with wxWidgets 3.2

* Sat Nov 05 2022 Orion Poplawski <orion@nwra.com> - 1.0.1-10
- Re-enable LTO on ppc64le

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.1-9
- Rebuild for gsl-2.7.1

% Thu Jul 21 2022 Orion Poplawski <orion@nwra.com> - 1.0.1-8
- Drop i686 completely - no antlr support

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Orion Poplawski <orion@nwra.com> - 1.0.1-7
- Drop java for i686 (bz#2104042)

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.0.1-6
- Rebuilt for Python 3.11

* Thu Mar 10 2022 Sandro Mani <manisandro@gmail.com> - 1.0.1-5
- Rebuild for proj-9.0.0

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.1-4
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 22 2021 Orion Poplawski <orion@nwra.com> - 1.0.1-2
- Rebuild for hdf5 1.12.1

* Mon Oct 18 2021 Orion Poplawski <orion@nwra.com> - 1.0.1-1
- Update to 1.0.1

* Thu Aug 26 2021 Orion Poplawski <orion@nwra.com> - 1.0.0-2
- Re-enable armv7hl; add ppc64le eigen workaround; Cleanup test exclusions

* Sun Aug 22 2021 Orion Poplawski <orion@nwra.com> - 1.0.0-1
- Update to 1.0.0
- Drop EL7 support due to plplot 5.11 requirement

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 1.0.0-0.6.20210123git4892c96
- Rebuild for hdf5 1.10.7/netcdf 4.8.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.5.20210123git4892c96
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.0-0.4.20210123git4892c96
- Rebuilt for Python 3.10

* Sat Mar 13 2021 Orion Poplawski <orion@nwra.com> - 1.0.0-0.3.20210123git4892c96
- Add patch for PROJ 8 support

* Sun Mar 07 2021 Sandro Mani <manisandro@gmail.com> - 1.0.0-0.3.20210123git4892c96
- Rebuild (proj)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.2.20210123git4892c96
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Orion Poplawski <orion@nwra.com> - 1.0.0-0.1.20210123git4892c96
- Update to latest git

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-20.20190915git2870075
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-19.20190915git2870075
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 0.9.9-18.20190915git2870075
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0.9.9-17.20190915git2870075
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jun 26 2020 Orion Poplawski <orion@nwra.com> - 0.9.9-16.20190915git2870075
- Rebuild for hdf5 1.10.6

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.9-15.20190915git2870075
- Rebuilt for Python 3.9

* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 0.9.9-14.20190915git2870075
- Fix string quoting for rpm >= 4.16
- Add BR: expat-devel

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-13.20190915git2870075
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 29 2019 Orion Poplawski <orion@nwra.com> - 0.9.9-12.20190915git2870075
- Rebuild for plplot 5.15

* Tue Sep 17 2019 Orion Poplawski <orion@nwra.com> - 0.9.9-11.20190915git2870075
- Update to latest git

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.9.9-10
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.9-9
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 0.9.9-7
- Rebuild for hdf5 1.10.5

* Fri Feb 22 2019 Orion Poplawski <orion@nwra.com> - 0.9.9-6
- test_bug_635 fails on F28 ppc64

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.9-5
- Rebuild for readline 8.0

* Wed Feb 13 2019 Orion Poplawski <orion@nwra.com> - 0.9.9-4
- Use eccodes where available
- Add patches to fix build
- Use cmake3 for EPEL7 compat

* Wed Feb 13 2019 Orion Poplawski <orion@nwra.com> - 0.9.9-3
- Rebuild for plplot 5.14

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 1 2018 Orion Poplawski <orion@nwra.com> - 0.9.9-1
- Update to 0.9.9

* Wed Oct 31 2018 Orion Poplawski <orion@nwra.com> - 0.9.8-7.20180919gitd892ee5
- Really use eccodes by fixing typo (bug #1644928)

* Thu Sep 20 2018 Orion Poplawski <orion@nwra.com> - 0.9.8-6.20180919gitd892ee5
- Update to latest git
- Port to python 3

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.9.8-5.20180723gitf3b6e01
- Rebuild with fixed binutils

* Mon Jul 23 2018 Orion Poplawski <orion@nwra.com> - 0.9.8-4.20180723gitf3b6e01
- Update to latest git
- Switch to eccodes from grib_api for Fedora 28+

* Sun Jul 22 2018 Scott Talbert <swt@techie.net> - 0.9.8-3
- Rebuild with wxWidgets 3.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 20 2018 Orion Poplawski <orion@cora.nwra.com> - 0.9.8-1
- Update to 0.9.8
- Drop parallel make for now
- Use libtirpc
- Switch to Xorg dummy driver for tests, fail build on test failure
- Add patch to fix ppc64 altivec vector usage
- Add patches to fix various warnings

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.7-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 21 2018 Orion Poplawski <orion@cora.nwra.com> - 0.9.7-10
- Explicitly use python2
- Build with libtirpc

* Tue Feb 20 2018 Orion Poplawski <orion@cora.nwra.com> - 0.9.7-10
- Rebuild for hdf5 1.8.20

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.7-8
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.7-7
- Python 2 binary package renamed to python2-gdl
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Tom Callaway <spot@fedoraproject.org> - 0.9.7-4
- rebuild for plplot 5.12.0

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 1 2017 Orion Poplawski <orion@cora.nwra.com> - 0.9.7-1
- Update to 0.9.7

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9.6-10
- Rebuild for readline 7.x

* Wed Dec 28 2016 Rich Mattes <richmattes@gmail.com> - 0.9.6-9
- Rebuild for eigen3-3.3.1

* Mon Sep 26 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.6-8
- Keep tabs on failing tests

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 29 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.6-6
- Rebuild for hdf5 1.8.17

* Thu Mar 3 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.6-5
- Add patch to build with gcc 6

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.6-4
- Rebuild for gsl 2.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.6-2
- Rebuild for netcdf 4.4.0

* Thu Jan 7 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.6-1
- Update to 0.9.6
- Drop setting -DH5_USE_16_API and -fPIC
- Drop plplot patch applied upstream
- Add patch to fix file_move test
- Run tests with Xvfb and metacity
- Use %%license

* Sun Oct 04 2015 Rex Dieter <rdieter@fedoraproject.org> - 0.9.5-10
- rebuild (GraphicsMagick)

* Wed Jul 15 2015 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-9
- Rebuild for grib_api 1.14.0 soname bump

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-7
- Rebuild for hdf5 1.8.15

* Fri Apr 24 2015 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-6
- Add patch for plplot 5.11.0 support

* Mon Mar 09 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.5-5
- rebuild (GraphicsMagick)

* Wed Jan 07 2015 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-4
- Rebuild for hdf5 1.8.4

* Tue Nov 18 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-3
- Exclude test_zip

* Fri Oct 31 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-2
- No longer need cmake28 on RHEL6

* Wed Oct 8 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-1
- Update to 0.9.5

* Fri Oct 3 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-7
- Re-enable openmp.  Appears to be working now.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 23 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.9.4-5
- Disable tests which fail on aarch64 (#990749)

* Tue Jun 10 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-4
- Fix python find_package usage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 28 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-2
- Rebuild for hdf5 1.8.12

* Tue Oct 8 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-1
- Disable openmp for now due to issues with eigen3 matrix multiply

* Fri Oct 4 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-1
- Add patch to fix use of dynamically sized matrices with Eigen3
- Add patch to fix -Wreorder warnings
- Update gsl patch to match current cvs

* Mon Sep 30 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-1
- Update to 0.9.4
- Update build patch - drop automake components
- New python patch to fix python build
- Add patch to fix gsl usage
- Add patch for test debugging

* Tue Aug 27 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-10.cvs20130804
- Add patch to support new width() method in plplot

* Fri Aug 23 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-10.cvs20130804
- Build with shared grib_api

* Sun Aug 4 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-9.cvs20130804
- Update cvs patch to current cvs
- Drop test_ce patch, enable test_ce

* Wed Jul 31 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-8.cvs20130731
- Update cvs patch to current cvs
- Add patch to fix segfault in test_ce
- Cleanup test excludes, note bugs for failing tests

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-7.cvs20130516
- Update cvs patch to current cvs
- Drop test_ce,tests, netcdf, and python patch applied upstream
- Rebuild for hdf5 1.8.11
- Switch to GraphicsMagick

* Fri Mar 22 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-6.cvs20130321
- Update cvs patch to current cvs
- Add patch to use python 2 with cmake

* Wed Mar 20 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-5
- Add patch to handle netcdf better with cmake
- BR netcdf-devel instead of netcdf-cxx-devel

* Fri Mar 15 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-4
- Change to use cmake
- Update to current cvs via patch
- Add patches to fix tests under cmake
- Build with eigen3

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.9.3-2
- rebuild due to "jpeg8-ABI" feature drop

* Thu Dec 27 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-1
- Update to 0.9.3
- Rebase antlr-auto patch

* Mon Dec 3 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-10.cvs20120717
- Rebuild for hdf5 1.8.10

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-9.cvs20120717
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-8.cvs20120717
- Update to current cvs
- Drop env patch fixed upstream

* Mon Jul 16 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-7.cvs20120716
- Update to current cvs

* Tue May 15 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-6.cvs20120515
- Update to current cvs
- Add patch for testsuite make check to work in build directory
- Add patch to fix pythongdl.c compile
- Run the testsuite properly with make check

* Wed Mar 21 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-5
- Rebuild antlr generated files
- Rebuild for ImageMagick

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-4
- Rebuilt for c++ ABI breakage

* Sat Jan 7 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-3
- Build with pslib

* Wed Nov 16 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-2
- Rebuild for hdf5 1.8.8

* Fri Nov 11 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-1
- Update to 0.9.2
- Drop upstreamed patches
- Drop hdf support from python module, add patch to force building of python
  shared library

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for glibc bug#747377

* Thu Aug 18 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-4
- Rebuild for plplot 5.9.8
- Add upstream patch to fix strsplit and str_sep
- Add patch to fix compile issues with string
- Add patch to change plplot SetOpt to setopt

* Tue May 17 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-3
- Rebuild for hdf5 1.8.7

* Thu Mar 31 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-2
- Rebuild for netcdf 4.1.2

* Tue Mar 29 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-1
- Update to 0.9.1
- Drop numpy and wx patches fixed upstream

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 11 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-5
- Rebuild for plplot 5.9.7

* Wed Sep 29 2010 jkeating - 0.9-4
- Rebuilt for gcc bug 634757

* Wed Sep 15 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-3
- Fix GDL_PATH in profile scripts (bug #634351)

* Wed Sep 15 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-2
- Rebuild for new ImageMagick

* Mon Aug 30 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-1
- Update to 0.9 final

* Thu Aug 26 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.17.rc4
- Add initial patch to build the python module with numpy rather than
  numarray.  Doesn't work yet, but the python module is mostly dead anyway

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.9-0.16.rc4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 0.9-0.15.rc4
- rebuilt against wxGTK-2.8.11-2

* Wed Jul 7 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.14.rc4
- Update to today's cvs
- Drop wx-config patch
- Re-instate wx patch to avoid segfault on test exit

* Thu Jun 3 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.13.rc4
- Update to today's cvs
- Drop GLDLexer and python patches
- BR antlr-C++ on Fedora 14+

* Mon Mar 22 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.12.rc4
- Drop unused BR on proj-devel (bug #572616)

* Mon Mar 8 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.11.rc4
- Rebuild for new ImageMagick

* Wed Feb 17 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.10.rc4
- Update to 0.9rc4
- Enable grib, udunits2, and wxWidgets support
- Build python module and add sub-package for it
- Use %%global instead of %%define

* Tue Dec  8 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9-0.9.rc3
- Explicitly BR hdf-static in accordance with the Packaging
  Guidelines (hdf-devel is still static-only).

* Wed Nov 11 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.8.rc3
- Rebuild for netcdf-4.1.0

* Thu Oct 15 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.7.rc3
- Update to 0.9rc3
- Drop gcc43, ppc64, friend patches fixed upstream
- Add source for makecvstarball
- Rebase antlr patch, add automake source version
- Add conditionals for EPEL builds
- Add %%check section

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.6.rc2.20090312
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.5.rc2.20090312
- Back off building python module until configure macro is updated

* Thu Mar 12 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.4.rc2.20090312
- Update to 0.9rc2 cvs 20090312
- Rebase antlr patch
- Rebuild for new ImageMagick

* Thu Feb 26 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.3.rc2.20090224
- Build python module
- Move common code to noarch common sub-package

* Tue Feb 24 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.2.rc2.20090224
- Update to 0.9rc2 cvs 20090224
- Fix release tag
- Drop ImageMagick patch fixed upstream
- Add patch to compile with gcc 4.4.0 - needs new friend statement
- Don't build included copy of antlr, use system version

* Fri Jan 23 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.rc2.1
- Update to 0.9rc2 based cvs

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9-0.rc1.4.1
- Rebuild for Python 2.6

* Fri Sep  5 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.rc1.4
- Add a requires on plplot to pull in drivers (bug#458277)

* Fri May 16 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.rc1.3
- Update to latest cvs
- Add patch to handle new ImageMagick
- Update netcdf locations

* Mon Apr 28 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.rc1.2
- Rebuild for new ImageMagick

* Sat Apr  5 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.rc1.1
- Update to 0.9rc1

* Mon Mar 17 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre6.2
- Update cvs patch to latest cvs

* Tue Mar 4 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre6.1
- Rebuild for gcc 4.3, and add patch for gcc 4.3 support
- Add patch to build against plplot 5.9.0
- Add cvs patch to update to latest cvs

* Fri Nov  2 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre6
- Update to 0.9pre6

* Tue Aug 21 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre5.2
- Add patch to fix build on ppc64

* Tue Aug 21 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre5.1
- Update license tag to GPLv2+
- Rebuild for BuildID

* Mon Jul  9 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre5
- Update to 0.9pre5

* Tue May 22 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre4.2
- Rebuild for netcdf 3.6.2 with shared libraries

* Tue Jan  9 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre4.1
- Package the library routines and point to them by default

* Fri Jan  5 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre4
- Update to 0.9pre4

* Mon Dec 18 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre3.4
- Add patch for configure to handle python 2.5

* Thu Dec 14 2006 - Jef Spaleta <jspaleta@gmail.com> - 0.9-0.pre3.3
- Bump and build for python 2.5

* Wed Nov 22 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre3.2
- Update to 0.9pre3

* Wed Oct  4 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre3.1
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre3
- Rebuild for FC6
- Add patch for specialization error caught by gcc 4.1.1

* Thu Jun 29 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre2
- Update to 0.9pre2

* Sun Jun 11 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre.1
- Rebuild for ImageMagick so bump

* Mon Apr  3 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre
- Update to 0.9pre

* Fri Feb 24 2006 Orion Poplawski <orion@cora.nwra.com> - 0.8.11-4
- Add --with-fftw to configure

* Thu Feb  2 2006 Orion Poplawski <orion@cora.nwra.com> - 0.8.11-3
- Enable hdf for ppc
- Change fftw3 to fftw

* Tue Jan  3 2006 Orion Poplawski <orion@cora.nwra.com> - 0.8.11-2
- Rebuild

* Mon Nov 21 2005 Orion Poplawski <orion@cora.nwra.com> - 0.8.11-1
- Upstream 0.8.11
- Remove hdf patch fixed upstream
- Remove X11R6 lib path - not needed with modular X

* Wed Nov 16 2005 Orion Poplawski <orion@cora.nwra.com> - 0.8.10-4
- Update for new ImageMagick version

* Thu Sep 22 2005 Orion Poplawski <orion@cora.nwra.com> - 0.8.10-3
- Disable hdf with configure on ppc

* Thu Sep 22 2005 Orion Poplawski <orion@cora.nwra.com> - 0.8.10-2
- Don't include hdf support on ppc

* Fri Aug 19 2005 Orion Poplawski <orion@cora.nwra.com> - 0.8.10-1
- Initial Fedora Extras version
