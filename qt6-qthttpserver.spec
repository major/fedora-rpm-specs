#global unstable 0
%global		qt_module qthttpserver
Name:		qt6-qthttpserver
Version:	6.6.2
Release:	1%{?dist}
Summary:	Library to facilitate the creation of an http server with Qt

License:	BSD-3-Clause AND GFDL-1.3-no-invariants-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:		http://qt-project.org/
%global		majmin %(echo %{version} | cut -d. -f1-2)
%global		qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0:	https://download.qt.io/development_releases/qt/%{majmin}/%{qt_version}/submodules/%{qt_module}-everywhere-src-%{qt_version}-%{prerelease}.tar.xz
%else
Source0:	https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

BuildRequires:	qt6-rpm-macros
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	ninja-build
BuildRequires:	cmake(Qt6BuildInternals) = %{version}
BuildRequires:	cmake(Qt6Core) = %{version}
BuildRequires:	qt6-qtbase-private-devel = %{version}
BuildRequires:	cmake(Qt6Network) = %{version}
BuildRequires:	cmake(Qt6Concurrent) = %{version}
BuildRequires:	cmake(Qt6WebSockets) = %{version}
BuildRequires:	cmake(Qt6Gui) = %{version}
BuildRequires:	libxkbcommon-devel

%description
%{summary}.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	examples
Summary:	Document files for %{name}
Requires:	%{name}-devel = %{version}-%{release}
%description	examples
The %{name}-examples package contains examples that pertain
to the usage of %{name}.

%prep
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1


%build
%cmake_qt6
%cmake_build


%install
%cmake_install

%files
%license LICENSES/*.txt
%{_qt6_libdir}/libQt6HttpServer.so.6{,.*}

%files devel
%dir %{_qt6_headerdir}/QtHttpServer
%{_qt6_headerdir}/QtHttpServer/*
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtHttpServerTestsConfig.cmake
%dir %{_qt6_libdir}/cmake/Qt6HttpServer
%{_qt6_libdir}/cmake/Qt6HttpServer/*
%{_qt6_libdir}/libQt6HttpServer.prl
%{_qt6_libdir}/libQt6HttpServer.so
%{_qt6_libdir}/pkgconfig/Qt6HttpServer.pc
%{_qt6_libdir}/qt6/metatypes/qt6httpserver_relwithdebinfo_metatypes.json
%{_qt6_libdir}/qt6/mkspecs/modules/qt_lib_httpserver.pri
%{_qt6_libdir}/qt6/mkspecs/modules/qt_lib_httpserver_private.pri
%{_qt6_libdir}/qt6/modules/HttpServer.json

%files examples
%{_qt6_libdir}/qt6/examples/

%changelog
* Thu Feb 15 2024 Jan Grulich <jgrulich@redhat.com> - 6.6.2-1
- 6.6.2

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 27 2023 Jan Grulich <jgrulich@redhat.com> - 6.6.1-1
- 6.6.1

* Tue Oct 10 2023 Jan Grulich <jgrulich@redhat.com> - 6.6.0-1
- 6.6.0

* Mon Oct 02 2023 Justin Zobel <justin.zobel@gmail.com> - 6.5.3-1
- Update to 6.5.3

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 6.5.2-1
- Initial release
