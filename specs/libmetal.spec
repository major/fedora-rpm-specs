Name:		libmetal
Version:	2025.10.0
Release:	%autorelease
Summary:	An abstraction layer across user-space Linux, baremetal, and RTOS environments 
License:	BSD-3-Clause OR Apache-2.0 OR GPL-2.0-only
URL:		https://github.com/OpenAMP/libmetal/
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		libmetal-add-additional-arches.patch

BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	gcc
BuildRequires:	glibc-devel
BuildRequires:	libsysfs-devel

%description
An abstraction layer across user-space Linux, baremetal, and RTOS environments.

%package devel
Summary: 	Development files for libmetal
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Development file for libmetal: An abstraction layer across user-space Linux,
baremetal, and RTOS environments.

%package doc
Summary:	Documentation files for libmetal
BuildArch:	noarch
%description doc
Documentation file for libmetal: An abstraction layer across user-space Linux,
baremetal, and RTOS environments.


%prep
%autosetup -p1


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} -DWITH_STATIC_LIB=OFF
%cmake_build


%install
%cmake_install


%files
%license LICENSE.md
%doc README.md
%{_bindir}/test-metal-shared
%{_libdir}/libmetal.so.1
%{_libdir}/libmetal.so.1.*

%files devel
%{_libdir}/libmetal.so
%{_includedir}/metal/

%files doc
%license LICENSE.md
%doc README.md
%doc %{_datarootdir}/doc/metal/


%changelog
%autochangelog
