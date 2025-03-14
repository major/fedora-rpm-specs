%global use_qt4 0
%global use_qt5 1

%global wrpname q%{name}
%global qt4_build_dir release-qt4
%global qt5_build_dir release-qt5

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

%if 0%{?use_qt4}
BuildRequires: pkgconfig(QtCore)
BuildRequires: pkgconfig(QtNetwork)
%endif

%if 0%{?use_qt5}
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Network)
%endif

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

%if 0%{?use_qt4}
%package -n %{wrpname}-qt4
Summary: Qt4-wrapper for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{wrpname} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{wrpname} < %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{wrpname}-qt4
For Qt4 users there is a wrapper available called QJDns and a very
high-level wrapper called QJDnsShared (under its original name
JDnsShared).

%package -n %{wrpname}-qt4-devel
Summary: Development files for %{wrpname}-qt4
Requires: %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{wrpname}-qt4%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{wrpname}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{wrpname}-devel < %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{wrpname}-qt4-devel
This package contains libraries and header files for developing applications
that use %{wrpname}-qt4.
%endif

%if 0%{?use_qt5}
%package -n %{wrpname}-qt5
Summary: Qt5-wrapper for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{wrpname}-qt5
For Qt5 users there is a wrapper available called QJDns and a very
high-level wrapper called QJDnsShared (under its original name
JDnsShared).

%package -n %{wrpname}-qt5-devel
Summary: Development files for %{wrpname}-qt5
Requires: %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{wrpname}-qt5%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{wrpname}-qt5-devel
This package contains libraries and header files for developing applications
that use %{wrpname}-qt5.

%package -n %{wrpname}-qt5-tools
Summary: Qt-based command-line tool %{name}

%description -n %{wrpname}-qt5-tools
This package contains Qt-based command-line tool called %{name} that can
be used to test functionality.
%endif

%prep
%autosetup -p1

%build
%if 0%{?use_qt4}
mkdir %{qt4_build_dir} && pushd %{qt4_build_dir}
%cmake -G Ninja \
    -S'..' \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_JDNS_TOOL:BOOL=OFF \
%if 0%{?fedora} && 0%{?fedora} >= 43
%if "%{?_lib}" == "lib64"
    -DLIB_SUFFIX:STRING=64 \
%endif
    -DLIB_INSTALL_DIR:PATH="%{_libdir}" \
%endif
    -DQT4_BUILD:BOOL=ON
%cmake_build
popd
%endif

%if 0%{?use_qt5}
mkdir %{qt5_build_dir} && pushd %{qt5_build_dir}
%cmake -G Ninja \
    -S'..' \
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
popd
%endif

%install
%if 0%{?use_qt4}
pushd %{qt4_build_dir}
%cmake_install
popd
%endif

%if 0%{?use_qt5}
pushd %{qt5_build_dir}
%cmake_install
popd
%endif

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

%if 0%{?use_qt4}
%files -n %{wrpname}-qt4
%{_libdir}/lib%{wrpname}-qt4.so.2*

%files -n %{wrpname}-qt4-devel
%{_includedir}/%{name}/%{wrpname}.h
%{_includedir}/%{name}/%{wrpname}shared.h
%{_libdir}/lib%{wrpname}-qt4.so
%{_libdir}/cmake/%{wrpname}/
%{_libdir}/cmake/%{wrpname}-qt4/
%{_libdir}/pkgconfig/%{wrpname}-qt4.pc
%endif

%if 0%{?use_qt5}
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
%endif

%changelog
%autochangelog
