Name:           cppmyth
Version:        2.20.4
Release:        %autorelease
Summary:        Client interface for the MythTV backend

License:        GPL-2.0-or-later
URL:            https://github.com/janbar/%{name}/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:          0001-mythintrinsic.h-was-removed-in-2024.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(zlib)

%description
This project is intended to create a easy client interface for the MythTV
backend. Its development started from January 2014 and today the API supports
the protocol version of MythTV 0.26 to 0.29.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%prep
%autosetup -p1


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build


%install
%cmake_install


%files
%doc README
%{_libdir}/*.so.2*


%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
%autochangelog
