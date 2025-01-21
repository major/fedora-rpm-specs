%undefine __cmake_in_source_build
# compression tests take up 3GB of disk space and a lot of time
%global compression_tests 0
%global desc \
TRAJNG (Trajectory next generation) is a program library for handling\
molecular dynamics (MD) trajectories. It can store coordinates, and\
optionally velocities and the H-matrix. Coordinates and velocities are\
stored with user-specified precision. In addition, program specific\
information (text strings) can optionally be stored in the beginning\
of each file. Atomic labels can also optionally be stored once in the\
beginning of the file.


Name:          tng
Version:       1.8.2
Release:       18%{?dist}
Summary:       Trajectory Next Generation binary format manipulation library

# Automatically converted from old format: BSD and zlib - review is highly recommended.
License:       LicenseRef-Callaway-BSD AND Zlib
Source0:       https://github.com/gromacs/tng/archive/v%{version}/%{name}-%{version}.tar.gz
# fix build with gfortran 12, see https://www.gnu.org/software/gcc//gcc-12/changes.html
Patch0:        tng-gf12.patch
URL:           http://www.gromacs.org/Developer_Zone/Programming_Guide/File_formats

BuildRequires:  cmake3 >= 3.1
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: gcc-gfortran
BuildRequires: zlib-devel
Provides:      bundled(md5-deutsch)

%description
%{desc}

%package devel
Summary:       Trajectory Next Generation binary format manipulation library development files
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
%{desc}

This package contains the development files.

%package doc
Summary:       Trajectory Next Generation binary format manipulation library documentation
BuildArch:     noarch

%description doc
%{desc}

This package contains the documentation.

%prep
%setup -q
%patch -P0 -p1 -b .gf12

%build
%{cmake3} \
    -DTNG_BUILD_DOCUMENTATION=ON \
    -DTNG_BUILD_FORTRAN=ON \
%if 0%{?compression_tests} > 0
    -DTNG_BUILD_COMPRESSION_TESTS=ON \
%endif
    -DTNG_BUILD_WITH_ZLIB=ON \
    %{nil}

%cmake3_build

%install
%cmake3_install

# build/Documentation/html
rm -r %{buildroot}%{_datadir}/tng/doc/latex
mkdir -p %{buildroot}%{_defaultdocdir}
mv %{buildroot}{%{_datadir}/tng/doc/html,%{_defaultdocdir}/tng}

%check
pushd %{_vpath_builddir}/bin/tests
./tng_testing
popd
%if 0%{?compression_tests}
pushd %{_vpath_builddir}/bin/compression_tests
./test_tng_compress_write.sh
./test_tng_compress_read.sh
popd
%endif

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS Trajectoryformatspecification.mk
%{_libdir}/libtng_io.so.*

%files devel
%{_includedir}/tng
%{_libdir}/cmake/tng_io
%{_libdir}/libtng_io.so

%files doc
%{_docdir}/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.2-17
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 01 2022 Dominik Mierzejewski <dominik@greysector.net> 1.8.2-11
- fix FTBFS with gfortran 12 (#2047039)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 01 2019 Dominik Mierzejewski <dominik@greysector.net> 1.8.2-5
- drop unnecessary ifdef
- simplify github source URL
- use make_build macro

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Christoph Junghans <junghans@votca.org> 1.8.2-1
- update to 1.8.2 (bug #1569468)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 15 2017 Christoph Junghans <junghans@votca.org> 1.8.0-4
- fix version in tng_io-configVersion.cmake (needed for gromacs-2016.4)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 09 2017 Dominik Mierzejewski <dominik@greysector.net> 1.8.0-1
- update to 1.8.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 16 2016 Dominik Mierzejewski <dominik@greysector.net> 1.7.8-3
- add zlib to license list

* Tue Mar 15 2016 Dominik Mierzejewski <dominik@greysector.net> 1.7.8-2
- make devel subpackage depend on arched main package
- move docs to -doc subpackage

* Sat Dec 26 2015 Dominik Mierzejewski <dominik@greysector.net> 1.7.8-1
- update to 1.7.8
- drop upstream'd patch

* Tue Dec 15 2015 Dominik Mierzejewski <dominik@greysector.net> 1.7.7-1
- initial build
