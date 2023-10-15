%global qt_module qtwebview

%global examples 1

Summary: Qt6 - WebView component
Name:    qt6-%{qt_module}
Version: 6.6.0
Release: 1%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz

# FIXME use/update qt6_qtwebengine_arches
# 32-bit arches not supported (https://bugreports.qt.io/browse/QTBUG-102143)
ExclusiveArch: aarch64 x86_64

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel >= %{version}
BuildRequires: qt6-qtwebengine-devel
BuildRequires: pkgconfig(xkbcommon) >= 0.4.1

%description
Qt WebView provides a way to display web content in a QML application
without necessarily including a full web browser stack by using native
APIs where it makes sense.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
%description devel
%{summary}.

%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.
%endif

%prep
%autosetup -n %{qt_module}-everywhere-src-%{version}%{?unstable:-%{prerelease}} -p1


%build
%cmake_qt6 -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF}

%cmake_build


%install
%cmake_install


%files
%license LICENSES/GPL* LICENSES/LGPL*
%{_qt6_libdir}/libQt6WebView.so.6{,.*}
%{_qt6_libdir}/libQt6WebViewQuick.so.6{,.*}
%{_qt6_qmldir}/QtWebView/
%dir %{_qt6_plugindir}/webview/
%{_qt6_plugindir}/webview/libqtwebview_webengine.so

%files devel
%dir %{_qt6_headerdir}/QtWebView
%{_qt6_headerdir}/QtWebView/*
%dir %{_qt6_headerdir}/QtWebViewQuick
%{_qt6_headerdir}/QtWebViewQuick/*
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtWebViewTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6WebView
%{_qt6_libdir}/cmake/Qt6WebView/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6WebViewQuick
%{_qt6_libdir}/cmake/Qt6WebViewQuick/*.cmake
%{_qt6_libdir}/libQt6WebView.so
%{_qt6_libdir}/libQt6WebView.prl
%{_qt6_libdir}/libQt6WebViewQuick.so
%{_qt6_libdir}/libQt6WebViewQuick.prl
%{_qt6_libdir}/pkgconfig/Qt6WebView.pc
%{_qt6_libdir}/pkgconfig/Qt6WebViewQuick.pc
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/*.json
%{_qt6_libdir}/qt6/modules/*.json

%if 0%{?examples}
%files examples
%dir %{_qt6_examplesdir}/webview/minibrowser
%{_qt6_examplesdir}/webview/minibrowser/minibrowser
%endif


%changelog
* Fri Oct 13 2023 Jan Grulich <jgrulich@redhat.com> - 6.6.0-1
- 6.6.0

* Sun Oct 01 2023 Justin Zobel <justin.zobel@gmail.com> - 6.5.3-1
- new version

* Mon Jul 24 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.2-1
- 6.5.2

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 František Zatloukal <fzatlouk@redhat.com> - 6.5.1-3
- Rebuilt for ICU 73.2

* Thu Jul 13 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.1-2
- Bump build for private API version change

* Mon May 22 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.1-1
- 6.5.1

* Wed Apr 05 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.0-1
- 6.5.0

* Mon Mar 27 2023 Jan Grulich <jgrulich@redhat.com> - 6.4.3-1
- 6.4.3

* Wed Jan 25 2023 Jan Grulich <jgrulich@redhat.com> - 6.4.2-1
- 6.4.2
