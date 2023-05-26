# FIXME: qt6-qtdeclarative doesn't build on S390x
# BUG: https://bugreports.qt.io/browse/QTBUG-93101
ExcludeArch: s390x

%global qt_module qtlocation

#global unstable 1
%if 0%{?unstable}
%global prerelease rc2
%endif

Summary: Qt6 - Location component
Name:    qt6-%{qt_module}
Version: 6.2.2
Release: 1%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPLv2 with exceptions or GPLv3 with exceptions
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0: https://download.qt.io/development_releases/qt/%{majmin}/%{qt_version}/submodules/%{qt_module}-everywhere-src-%{qt_version}-%{prerelease}.tar.xz
%else
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

# build failure with gcc10
# various C++ runtime headers indirectly included <string> which in turn
# included <local> and <cerrno>.  Those indirect inclusions have been
# eliminated which in turn forces packages to include the C++ headers they
# actually need.
Patch0: qtlocation-gcc10.patch

# filter plugin/qml provides
%global __provides_exclude_from ^(%{_qt6_archdatadir}/qml/.*\\.so|%{_qt6_plugindir}/.*\\.so)$

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-rpm-macros
BuildRequires: qt6-qtbase-devel >= %{version}
# QtPositioning core-private
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel >= %{version}
BuildRequires: qt6-qtserialport-devel >= %{version}

BuildRequires: pkgconfig(dconf)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(xkbcommon) >= 0.5.0

%description
The Qt Location and Qt Positioning APIs gives developers the ability to
determine a position by using a variety of possible sources, including
satellite, or wifi, or text file, and so on.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1


%build
# QT is known not to work properly with LTO at this point.  Some of the issues
# are being worked on upstream and disabling LTO should be re-evaluated as
# we update this change.  Until such time...
# Disable LTO
%define _lto_cflags %{nil}

%cmake_qt6

%cmake_build


%install
%cmake_install

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd


%ldconfig_scriptlets

%files
%license LICENSE.GPL* LICENSE.LGPL*
%{_qt6_libdir}/libQt6Positioning.so.6*
%dir %{_qt6_archdatadir}/qml/QtPositioning
%{_qt6_archdatadir}/qml/QtPositioning/*
%{_qt6_plugindir}/position/
%{_qt6_libdir}/libQt6PositioningQuick.so.6*

%files devel
%{_qt6_headerdir}/QtPositioning/
%{_qt6_libdir}/libQt6Positioning.so
%{_qt6_libdir}/libQt6Positioning.prl
%{_qt6_headerdir}/QtPositioningQuick/
%{_qt6_libdir}/libQt6PositioningQuick.so
%{_qt6_libdir}/libQt6PositioningQuick.prl
%dir %{_qt6_libdir}/cmake/Qt6Positioning
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtLocationTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Bundled_Clip2Tri/Qt6Bundled_Clip2TriDependencies.cmake
%{_qt6_libdir}/cmake/Qt6Positioning/*.cmake
%{_qt6_libdir}/cmake/Qt6PositioningQuick/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_positioning*.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_positioning*.pri
%{_qt6_libdir}/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json

%files examples
%{_qt6_examplesdir}/


%changelog
* Tue Dec 14 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.2-1
- 6.2.2

* Fri Oct 29 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.1-1
- 6.2.1

* Thu Sep 30 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0-1
- 6.2.0

* Mon Sep 27 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0~rc2-1
- 6.2.0 - rc2

* Thu Sep 16 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0~rc-1
- 6.2.0 - rc
