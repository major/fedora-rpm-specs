# Undefine CMake in-source builds in order to be consistent with f33+
%undefine __cmake_in_source_build

Name:           nexus
Version:        4.4.3
Release:        19%{?dist}
Summary:        Libraries and tools for the NeXus scientific data file format

# The entire source code is GPLv2+ except nxdir which is MIT
# Automatically converted from old format: LGPLv2+ and MIT - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
URL:            http://www.nexusformat.org/
Source0:        https://github.com/nexusformat/code/archive/v%{version}/code-v%{version}.tar.gz
# Fix the version reported by the library
#   (see https://github.com/nexusformat/code/issues/437)
Patch0:         nexus-fix-version.patch
# Remove an additional flag that doesn't work in the EL6 version of gfortran
Patch1:         nexus-el6-fortran-flags.patch
# Back port fix from master branch
Patch2:         nexus-fix-nxtranslate-xml.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++ 
BuildRequires:  hdf5-devel
BuildRequires:  hdf-devel
BuildRequires:  make
BuildRequires:  python-docutils

Requires:       hdf5
Requires:       hdf
Requires:       mxml


%description
NeXus is common data format for neutron, x-ray, and muon science. This
package provides tools and libraries for accessing these files.  The on disk
representation is based upon either HDF4, HDF5 or XML

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hdf5-devel
Requires:       hdf-devel

%description    devel
The %{name}-devel package contains header files for
developing applications that use %{name}


%package        tools
Summary:        Applications for reading and writing NeXus files.
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       readline
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(readline)


%description    tools
%{summary}.


%prep
%setup -q -n code-%{version}
%patch -P0 -p1 -b .fix-version

%if 0%{?el6}
# Fortran flag not supported on EL6
%patch -P1 -p1 -b .el6-flags
%endif

%patch -P2 -p1 -b .nxtranslate

%build
%cmake \
       -DENABLE_HDF5=1 \
       -DENABLE_HDF4=1 \
       -DENABLE_CXX=1 \
       -DENABLE_APPS=1 .
%cmake_build


%install
%cmake_install
# Remove the static libraries 
rm %{buildroot}%{_libdir}/libNeXus.a
rm %{buildroot}%{_libdir}/libNeXusCPP.a

%files
%license COPYING
%doc %{_datadir}/doc/NeXus/README.doc
%{_libdir}/libNeXus.so.1*
%{_libdir}/libNeXusCPP.so.1*

%files devel
%license COPYING
%{_includedir}/nexus/
%{_libdir}/pkgconfig/
%{_libdir}/libNeXus.so
%{_libdir}/libNeXusCPP.so

%files tools
%{_bindir}/nxbrowse
%{_bindir}/nxconvert
%{_bindir}/nxsummary
%{_bindir}/nxtranslate
%{_bindir}/nxtraverse
%{_mandir}/man1/nxbrowse.1.gz
%{_mandir}/man1/nxconvert.1.gz 
%{_mandir}/man1/nxsummary.1.gz
# MIT
%license %{_datadir}/doc/NeXus/programs/nxdir/LICENSE
%doc %{_datadir}/doc/NeXus/programs/nxdir/CHANGES
%doc %{_datadir}/doc/NeXus/programs/nxdir/README
%doc %{_datadir}/doc/NeXus/programs/nxdir/TODO
%{_bindir}/nxdir
%{_mandir}/man1/nxdir.1.gz  



%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 4.4.3-18
- Rebuild for hdf5 1.14.5

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 4.4.3-17
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Orion Poplawski <orion@nwra.com> - 4.4.3-9
- Rebuild for hdf5 1.12.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 3 2020 Stuart Campbell <sic@fedoraproject.org> - 4.4.3-6
- Added COPYING to devel package

* Sun Aug 02 2020 Stuart Campbell <sic@fedoraproject.org> - 4.4.3-5
- Removed static libraries

* Sun Aug 02 2020 Stuart Campbell <sic@fedoraproject.org> - 4.4.3-4
- Added License file, changes from package review

* Sun Aug 02 2020 Stuart Campbell <sic@fedoraproject.org> - 4.4.3-3
- Removed Fortran bindings, added nxtranslate XML fix

* Thu Sep 15 2016 Stuart Campbell <sic@fedoraproject.org> - 4.4.3-2
- Added patch to fix version number

* Mon Sep 12 2016 Stuart Campbell <sic@fedoraproject.org> - 4.4.3-1
- Updated to NeXus 4.4.3

* Thu Apr 28 2016 Stuart Campbell <sic@fedoraproject.org> - 4.4.1-2
- Updated to ship all the tools libraries.

* Mon Dec 21 2015 Stuart Campbell <sic@fedoraproject.org> - 4.4.1-1
- Updated to nexus 4.4.1

* Mon Nov 30 2015 Stuart Campbell <sic@fedoraproject.org> - 4.4.0-1
- Initial package for fedora
