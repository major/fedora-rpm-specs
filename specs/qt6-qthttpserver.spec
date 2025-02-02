#global unstable 0
%global qt_module qthttpserver

%global examples 1

Name:       qt6-qthttpserver
Version:    6.8.2
Release:    1%{?dist}
Summary:    Library to facilitate the creation of an http server with Qt

License:    BSD-3-Clause AND GFDL-1.3-no-invariants-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:        http://qt-project.org/
%global     majmin %(echo %{version} | cut -d. -f1-2)
%global     qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0:    https://download.qt.io/development_releases/qt/%{majmin}/%{qt_version}/submodules/%{qt_module}-everywhere-src-%{qt_version}-%{prerelease}.tar.xz
%else
Source0:    https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

BuildRequires:  qt6-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6BuildInternals) = %{version}
BuildRequires:  cmake(Qt6Core) = %{version}
BuildRequires:  qt6-qtbase-private-devel = %{version}
BuildRequires:  cmake(Qt6Network) = %{version}
BuildRequires:  cmake(Qt6Concurrent) = %{version}
BuildRequires:  cmake(Qt6WebSockets) = %{version}
BuildRequires:  cmake(Qt6Gui) = %{version}
BuildRequires:  libxkbcommon-devel

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if 0%{?examples}
%package        examples
Summary:        Document files for %{name}
Requires:       %{name}-devel = %{version}-%{release}
%description    examples
The %{name}-examples package contains examples that pertain
to the usage of %{name}.
%endif

%prep
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1


%build
%cmake_qt6 \
  -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF} \
  -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF}

%cmake_build


%install
%cmake_install

%files
%license LICENSES/*.txt
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
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

%if 0%{?examples}
%files examples
%{_qt6_libdir}/qt6/examples/
%endif

%changelog
* Fri Jan 31 2025 Jan Grulich <jgrulich@redhat.com> - 6.8.2-1
- 6.8.2

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 05 2024 Jan Grulich <jgrulich@redhat.com> - 6.8.1-2
- Move Software Bill of Materials from -devel

* Thu Nov 28 2024 Jan Grulich <jgrulich@redhat.com> - 6.8.1-1
- 6.8.1

* Fri Oct 11 2024 Jan Grulich <jgrulich@redhat.com> - 6.8.0-1
- 6.8.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Jan Grulich <jgrulich@redhat.com> - 6.7.2-1
- 6.7.2

* Tue May 21 2024 Jan Grulich <jgrulich@redhat.com> - 6.7.1-1
- 6.7.1

* Tue Apr 02 2024 Jan Grulich <jgrulich@redhat.com> - 6.7.0-1
- 6.7.0

* Mon Feb 19 2024 Jan Grulich <jgrulich@redhat.com> - 6.6.2-2
- Examples: also install source files

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
