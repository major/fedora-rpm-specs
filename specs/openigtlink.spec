%global srcname OpenIGTLink
%global _docdir_fmt %{name}

Name:		openigtlink
Version:	2.1
Release:	%autorelease
Summary:	Implementation of the OpenIGTLink network communication protocol

License:	BSD-3-Clause
URL:		http://openigtlink.org
Source0:	https://github.com/openigtlink/OpenIGTLink/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

# RHBZ1509365
Patch2:		openigtlink-install_cmake.patch

# RHBZ1509407
Patch3:		openigtlink-install_headers.patch

BuildRequires:	gcc-c++
BuildRequires:	cmake


%description
OpenIGTLink is a network communication protocol specifically designed and
developed for research on image-guided and computer-assisted interventions. It
provides a standardized mechanism for communications among computers and
devices in operating rooms (OR) for a wide variety of image-guided therapy
(IGT) applications. Examples of such applications include:

- Stereotactic surgical guidance using optical position sensor and medical
  image visualization software
- Intraoperative image guidance using real-time MRI and medical image
  visualization software
- Robot-assisted interventions using robotic devices and surgical planning
  software

OpenIGTLink is a set of messaging formats and rules (protocol) used for data
exchange on a local area network (LAN). The specification of OpenIGTLink and
its reference implementation, the OpenIGTLink Library, are available free of
charge for any purpose including commercial use.


%package devel
Summary:	OpenIGTLink development files
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	cmake%{?_isa}

%description devel
Development files for the OpenIGTLink library.

%prep
%autosetup -n %{srcname}-%{version} -p1
find . -type f -executable -a \( -name '*.h' -o -name '*.cxx' \) -exec chmod a-x {} +


%build
# disable gtest due to upstream bug #122
%cmake \
    -DUSE_GTEST=OFF \
    -D%{srcname}_INSTALL_LIB_DIR=%{_lib} \
    -D%{srcname}_INSTALL_PACKAGE_DIR=%{_lib}/cmake/%{srcname} \
    -D%{srcname}_LEGACY_REMOVE=ON \
%cmake_build


%install
%cmake_install

%check
%global _smp_mflags -j1
%ctest

%files
%license LICENSE.txt
%{_libdir}/lib%{srcname}.so.2
%{_libdir}/lib%{srcname}.so.2.1.0

%files devel
%doc README.md
%{_libdir}/lib%{srcname}.so
%{_libdir}/cmake/%{srcname}/
%{_includedir}/igtl/


%changelog
%autochangelog
