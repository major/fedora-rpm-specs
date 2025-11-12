Name:		libad9361-iio
URL:		https://github.com/analogdevicesinc/libad9361-iio
Version:	0.3
Release:	%autorelease
License:	LGPL-2.1-or-later
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	libiio-devel
BuildRequires:	doxygen
Summary:	IIO AD9361 library for filter design and handling, multi-chip sync and more
Source:		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

%description
IIO AD9361 library which manages multi-chip sync (on platforms (FMCOMMS5)
where multiple AD9361 devices are used) and can create AD9361 specific FIR
filters on the fly.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Development files for %{name}.

%package doc
Summary:	Documentation files for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation files for %{name}.

%prep
%autosetup -p1

%build
%cmake -DINSTALL_LIB_DIR=%{_libdir}
%cmake_build

%install
%cmake_install

# Fix doc dir
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_docdir}/ad93610-doc __docs

%check
cd %{_vpath_builddir}
%make_build test

%files
%doc README.md
%license LICENSE
%{_libdir}/*.so.0*

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/ad9361.h
%{_libdir}/*.so

%files doc
%doc __docs/html

%changelog
%autochangelog
