%global gittag v2.0.0

Name:		ancient
Version:	2.0.0
Release:	2%{?dist}
Summary:	Modern decompressor for old data compression formats

# All files are BSD-2-Clause except src/BZIP2Table.hpp which is bzip2-1.0.6
License:	BSD-2-Clause AND bzip2-1.0.6
URL:		https://github.com/temisu/ancient
Source0:	https://github.com/temisu/ancient/archive/%{gittag}/%{name}-%{version}.tar.gz

BuildRequires:	autoconf
BuildRequires:	autoconf-archive
BuildRequires:	automake
BuildRequires:	gcc-c++
BuildRequires:	gzip
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	pkg-config

%description
This is a collection of decompression routines for old formats popular
in the Amiga, Atari computers and some other systems from 80's and
90's as well as some that are currently used which were used in a some
specific way in these old systems.


%package devel
Summary: Library and header files for building applications to use libancient
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Header files and a library of bzip2 functions, for developing apps
which will use the library.


%package libs
Summary: Library files for libancient decompressor for old formats

%description libs
Library files for applications needing to decompress ancient
compression formats.


%prep
%autosetup


%build
./autogen.sh
%configure
%make_build


%install
%make_install


%check
gzip -dc %{SOURCE0} > %{_tmppath}/%{name}-%{version}.tar
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/ancient verify %{SOURCE0} %{_tmppath}/%{name}-%{version}.tar


%files
%license LICENSE
%doc %{_pkgdocdir}
%exclude %{_pkgdocdir}/LICENSE
%{_bindir}/ancient

%files libs
%license LICENSE
%{_libdir}/libancient.so.2
%{_libdir}/libancient.so.2.0.0

%files devel
%{_includedir}/%{name}
%{_libdir}/libancient.so
%exclude %{_libdir}/libancient.a
%{_libdir}/pkgconfig/libancient.pc


%changelog
* Mon Feb 27 2023 Charles R. Anderson <cra@alum.wpi.edu> - 2.0.0-2
- Specify binary file explicitly rather than with a glob
- Devel subpackage doesn't need license file
- Add check section using ancient to verify Source0 gzip file

* Mon Jan 23 2023 Charles R. Anderson <cra@alum.wpi.edu> - 2.0.0-1
- Initial package
