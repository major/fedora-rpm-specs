%global sover 8

%bcond_without check
%bcond_with all_tests

Name:           qxmpp
Version:        1.14.2
Release:        %autorelease
Summary:        Cross-platform C++ XMPP client and server library

# The library is under LGPL-2.1-or-later license
# the files in doc/ directory are CC0-1.0 license.
# the qxmpp logo is CC-BY-SA-4.0 license.
License:        LGPL-2.1-or-later AND CC0-1.0 AND CC-BY-SA-4.0
URL:            https://invent.kde.org/libraries/qxmpp
Source0:        %{url}/-/archive/v%{version}/qxmpp-v%{version}.tar.gz
# Generate docbook documentation instead of html
# https://invent.kde.org/libraries/qxmpp/-/merge_requests/743
Patch0:         docbook.patch

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

%package        qt6
Summary:        QXmpp library for Qt6
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Core5Compat)
# optional for QXmpp OMEMO module
BuildRequires:  qca-qt6-devel
# calls
BuildRequires:  pkgconfig(gstreamer-1.0)

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
%autosetup -p1 -n qxmpp-v%{version}

%build
OPTIONS=(
    -GNinja \
    -DBUILD_TESTS=ON \
    -DBUILD_DOCUMENTATION=OFF \
    -DBUILD_DOCBOOK_DOCUMENTATION=ON \
    -DBUILD_OMEMO=ON \
    -DWITH_GSTREAMER=ON \
)

%global _vpath_builddir %{_target_platform}-qt6
%cmake \
    ${OPTIONS[@]} \
    -DQT_VERSION_MAJOR=6 \
%cmake_build

%install

%global _vpath_builddir %{_target_platform}-qt6
%cmake_install

%if %{with check}
%check
%global _vpath_builddir %{_target_platform}-qt6
%if %{with all_tests}
%ctest
%else
SKIP_TESTS='tst_qxmppcallmanager'
SKIP_TESTS+='|tst_qxmppdiscoverymanager'
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
%{_libdir}/pkgconfig/QXmppQt6.pc

%files doc
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/qxmpp

%changelog
%autochangelog
