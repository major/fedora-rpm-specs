%bcond_without doc

%global srcname the_Foundation

Name:           the_foundation
Version:        1.4.0
Release:        %autorelease
Summary:        Opinionated C11 library for low-level functionality

# SPDX-3.0-License-Identifier: BSD-2-Clause
License:        BSD
URL:            https://codeberg.org/skyjake/the_Foundation
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libunistring-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
%if %{with doc}
BuildRequires:  doxygen
%endif

%global abi_ver %%(echo %%{version}} | cut -d. -f1)

%global _description %{expand:
An object-oriented C library whose API is designed for a particular coding
style, taking cues from C++ STL and Qt.}

%description    %{_description}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem
Requires:       pkgconfig

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{srcname}.


%if %{with doc}
%package        doc
Summary:        Documentation for %{srcname}
BuildArch:      noarch

%description    doc %{_description}

The %{name}-doc package contains the documentation for %{srcname}.
%endif


%prep
%autosetup -n %{name} -p1


%build
%cmake
%cmake_build
%if %{with doc}
doxygen %{srcname}.doxygen
%endif


%install
%cmake_install


%check
# math and threading has non-zero retvals
for t in \
  archive \
  network \
  string \
  test \
  udptest \
; do
  %{__cmake_builddir}/${t}_Foundation
done


%files
%license LICENSE
%doc CHANGES.md README.md
%{_libdir}/*.so.%{abi_ver}{,.*}

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/%{srcname}
%{_libdir}/pkgconfig/%{srcname}.pc

%if %{with doc}
%files doc
%license LICENSE
%doc doc/html/*
%endif


%changelog
%autochangelog
