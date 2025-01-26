%global forgeurl https://github.com/qxmpp-project/qxmpp
Version:        1.9.3
%global sover   5
%forgemeta

%bcond_without check
%bcond_with all_tests

Name:           qxmpp
Release:        %autorelease
Summary:        Cross-platform C++ XMPP client and server library

# The library is under LGPL-2.1-or-later license
# the files in doc/ directory are CC0-1.0 license.
# the qxmpp logo is CC-BY-SA-4.0 license.
License:        LGPL-2.1-or-later AND CC0-1.0 AND CC-BY-SA-4.0
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  doxygen
# optional for QXmpp OMEMO module
BuildRequires:  libomemo-c-devel
BuildRequires:  protobuf-c-devel

%global _description %{expand:
QXmpp is a cross-platform C++ XMPP client and server library. It is written in
C++ and uses Qt framework.

QXmpp strives to be as easy to use as possible, the underlying TCP socket, the
core XMPP RFCs (RFC6120 and RFC6121) and XMPP extensions have been nicely
encapsulated into classes. QXmpp is ready to build XMPP clients complying with
the XMPP Compliance Suites 2022 for IM and Advanced Mobile. It comes with full
API documentation, automatic tests and some examples.}

%description
%{_description}

%package        qt5
Summary:        QXmpp library for Qt5
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Xml)
# optional for QXmpp OMEMO module
BuildRequires:  qca-qt5-devel

%description    qt5
%{_description}

%package        qt5-devel
Summary:        Development Files for %{name}-qt5
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}

%description    qt5-devel
This package contains libraries and header files for developing applications
that use %{name}-qt5.

%package        qt6
Summary:        QXmpp library for Qt6
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Core5Compat)
# optional for QXmpp OMEMO module
BuildRequires:  qca-qt6-devel

%description    qt6
%{_description}

%package        qt6-devel
Summary:        Development Files for %{name}-qt6
Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}

%description    qt6-devel
This package contains libraries and header files for developing applications
that use %{name}-qt6.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains documentation for %{name}.

%prep
%forgeautosetup -p1

%build
OPTIONS=(
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS=ON \
    -DBUILD_DOCUMENTATION=ON \
    -DBUILD_OMEMO=ON \
)
%global _vpath_builddir %{_target_platform}-qt5
%cmake \
    ${OPTIONS[@]} \
    -DQT_VERSION_MAJOR=5 \
%cmake_build

%global _vpath_builddir %{_target_platform}-qt6
%cmake \
    ${OPTIONS[@]} \
    -DQT_VERSION_MAJOR=6 \
%cmake_build

%install
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install

%global _vpath_builddir %{_target_platform}-qt6
%cmake_install

%if %{with check}
%check
%global _vpath_builddir %{_target_platform}-qt5
%if %{with all_tests}
%ctest
%else
SKIP_TESTS=
SKIP_TESTS='tst_qxmppiceconnection'
SKIP_TESTS+='|tst_qxmppfileencryption'
SKIP_TESTS+='|tst_qxmpptransfermanager'
%endif

%global _vpath_builddir %{_target_platform}-qt6
%if %{with all_tests}
%ctest
%else
SKIP_TESTS=
SKIP_TESTS='tst_qxmppdiscoverymanager'
SKIP_TESTS+='|tst_qxmppiceconnection'
SKIP_TESTS+='|tst_qxmpppubsubmanager'
SKIP_TESTS+='|tst_qxmpprostermanager'
SKIP_TESTS+='|tst_qxmppuserlocationmanager'
SKIP_TESTS+='|tst_qxmppusertunemanager'
SKIP_TESTS+='|tst_qxmppfileencryption'
SKIP_TESTS+='|tst_qxmpptransfermanager'
SKIP_TESTS+='|tst_qxmpphttpuploadmanager'
SKIP_TESTS+='|tst_qxmppjinglemessageinitiationmanager'
%ctest -E "$SKIP_TESTS"
%endif

%endif

%files qt5
%license LICENSES/*
%doc README.md
%{_libdir}/libQXmppQt5.so.%{sover}
%{_libdir}/libQXmppQt5.so.%{version}
%{_libdir}/libQXmppOmemoQt5.so.%{sover}
%{_libdir}/libQXmppOmemoQt5.so.%{version}

%files qt5-devel
%{_libdir}/libQXmppQt5.so
%{_libdir}/libQXmppOmemoQt5.so
%dir %{_includedir}/QXmppQt5
%{_includedir}/QXmppQt5/*.h
%{_includedir}/QXmppQt5/*.cpp
%{_includedir}/QXmppQt5/Omemo/
%{_libdir}/cmake/QXmppQt5/
%{_libdir}/cmake/QXmppOmemoQt5/
%{_libdir}/cmake/QXmpp/
%{_libdir}/pkgconfig/QXmppQt5.pc
%{_libdir}/pkgconfig/qxmpp.pc

%files qt6
%license LICENSES/*
%doc README.md
%{_libdir}/libQXmppQt6.so.%{sover}
%{_libdir}/libQXmppQt6.so.%{version}
%{_libdir}/libQXmppOmemoQt6.so.%{sover}
%{_libdir}/libQXmppOmemoQt6.so.%{version}

%files qt6-devel
%{_libdir}/libQXmppQt6.so
%{_libdir}/libQXmppOmemoQt6.so
%dir %{_includedir}/QXmppQt6
%{_includedir}/QXmppQt6/*.h
%{_includedir}/QXmppQt6/*.cpp
%{_includedir}/QXmppQt6/Omemo/
%{_libdir}/cmake/QXmppQt6/
%{_libdir}/cmake/QXmppOmemoQt6/
%{_libdir}/cmake/QXmpp/
%{_libdir}/pkgconfig/QXmppQt6.pc
%{_libdir}/pkgconfig/qxmpp.pc

%files doc
%dir %{_docdir}/qxmpp
%{_docdir}/qxmpp/html/

%changelog
%autochangelog
