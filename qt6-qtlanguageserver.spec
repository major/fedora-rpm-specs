
%global qt_module qtlanguageserver

#global unstable 1
%if 0%{?unstable}
%global prerelease rc2
%endif

Summary: Qt6 - LanguageServer component
Name:    qt6-%{qt_module}
Version: 6.5.1
Release: 1%{?dist}

License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0: https://download.qt.io/development_releases/qt/%{majmin}/%{qt_version}/submodules/%{qt_module}-everywhere-src-%{qt_version}-%{prerelease}.tar.xz
%else
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

## upstreamable patches

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

%description
The Qt Language Server component provides an implementation of the Language
Server protocol.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.


%prep
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1


%build
%cmake_qt6

%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%{_qt6_libdir}/libQt6JsonRpc.so.6*
%{_qt6_libdir}/libQt6LanguageServer.so.6*

%files devel
%{_qt6_headerdir}/QtJsonRpc/
%{_qt6_headerdir}/QtLanguageServer/
%{_qt6_libdir}/libQt6JsonRpc.prl
%{_qt6_libdir}/libQt6JsonRpc.so
%{_qt6_libdir}/libQt6LanguageServer.prl
%{_qt6_libdir}/libQt6LanguageServer.so
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtLanguageServer*
%{_qt6_libdir}/cmake/Qt6JsonRpcPrivate/
%{_qt6_libdir}/cmake/Qt6LanguageServerPrivate/
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_jsonrpc*.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_languageserver*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/JsonRpcPrivate.json
%{_qt6_libdir}/qt6/modules/LanguageServerPrivate.json
#{_qt6_libdir}/pkgconfig/*.pc


%changelog
* Wed May 24 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.1-1
- 6.5.1

* Thu May 04 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 6.5.0-1
- 6.5.0

* Thu May 04 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 6.4.3-1
- 6.4.3
