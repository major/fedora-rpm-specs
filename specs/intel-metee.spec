%global upstream_name metee

Name:		intel-metee
Version:	5.0.0
Release:	%autorelease
Summary:	Cross-platform access library for Intel CSME HECI interface

# Most of the source code is Apache-2.0, with the following exceptions:
# src/linux/include/linux/mei.h: (GPL-2.0 WITH Linux-syscall-note) OR BSD-3-Clause
# src/linux/libmei.h: BSD-3-Clause
# src/linux/mei.c: BSD-3-Clause
License:	Apache-2.0 AND BSD-3-Clause AND ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-3-Clause)
URL:		https://github.com/intel/metee
Source0:	%url/archive/%{version}/%{upstream_name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc gcc-c++
BuildRequires:  doxygen

# Upstream only supports x86_64
ExclusiveArch:	x86_64

%description
Cross-platform access library for Intel CSME HECI interface.
ME TEE Library is a C library to access CSE/CSME/GSC firmware via an mei
interface.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.
ME TEE Library is a C library to access CSE/CSME/GSC firmware via a mei
interface.

%package	doc
Summary:	Documentation files for %{name}
BuildArch:	noarch
%description	doc
The %{name}-doc package contains documentation files for %{name}.
ME TEE Library is a C library to access CSE/CSME/GSC firmware via a mei
interface.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
%cmake \
   -DCMAKE_BUILD_TYPE=Release \
   -DBUILD_SHARED_LIBS=ON \
   -DBUILD_DOCS=YES
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc CHANGELOG.md README.md
%{_libdir}/lib%{upstream_name}.so.%{version}

%files devel
%{_includedir}/%{upstream_name}.h
%{_libdir}/lib%{upstream_name}.so
%{_mandir}/man3/*

%files doc
%license COPYING
%{_docdir}/%{upstream_name}


%changelog
%autochangelog
