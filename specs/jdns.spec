%global wrpname q%{name}

Name: jdns
Version: 2.0.6
Release: %autorelease

License: MIT
Summary: A simple DNS queries library
URL: https://github.com/psi-im/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: ninja-build

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Network)

%description
JDNS is a simple DNS implementation that can perform normal DNS
queries of any record type (notably SRV), as well as Multicast DNS
queries and advertising. Multicast support is based on Jeremie
Miller's "mdnsd" implementation.

For maximum flexibility, JDNS is written in C with no direct
dependencies, and is licensed under the MIT license. Your application
must supply functionality to JDNS, such as UDP sending/receiving, via
callbacks.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary: %{name} API documentation
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch: noarch

%description doc
This package includes %{name} API documentation in HTML format.

%package -n %{wrpname}-qt5
Summary: Qt5-wrapper for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{wrpname}-qt4 < 2.0.6-23

%description -n %{wrpname}-qt5
For Qt5 users there is a wrapper available called QJDns and a very
high-level wrapper called QJDnsShared (under its original name
JDnsShared).

%package -n %{wrpname}-qt5-devel
Summary: Development files for %{wrpname}-qt5
Requires: %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{wrpname}-qt5%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{wrpname}-qt4-devel < 2.0.6-23

%description -n %{wrpname}-qt5-devel
This package contains libraries and header files for developing applications
that use %{wrpname}-qt5.

%package -n %{wrpname}-qt5-tools
Summary: Qt-based command-line tool %{name}
Requires: %{wrpname}-qt5%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{wrpname}-qt5-tools
This package contains Qt-based command-line tool called %{name} that can
be used to test functionality.

%prep
%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_JDNS_TOOL:BOOL=ON \
%if 0%{?fedora} && 0%{?fedora} >= 43
%if "%{?_lib}" == "lib64"
    -DLIB_SUFFIX:STRING=64 \
%endif
    -DLIB_INSTALL_DIR:PATH="%{_libdir}" \
%endif
    -DQT4_BUILD:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md
%{_libdir}/lib%{name}.so.2*

%files devel
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/%{name}.h
%{_includedir}/%{name}/%{name}_export.h
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%{_docdir}/%{name}/html/

%files -n %{wrpname}-qt5
%{_libdir}/lib%{wrpname}-qt5.so.2*

%files -n %{wrpname}-qt5-devel
%{_includedir}/%{name}/%{wrpname}.h
%{_includedir}/%{name}/%{wrpname}shared.h
%{_libdir}/lib%{wrpname}-qt5.so
%{_libdir}/cmake/%{wrpname}/
%{_libdir}/cmake/%{wrpname}-qt5/
%{_libdir}/pkgconfig/%{wrpname}-qt5.pc

%files -n %{wrpname}-qt5-tools
%{_bindir}/%{name}

%changelog
%autochangelog
