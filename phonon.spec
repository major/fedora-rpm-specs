
Summary: Multimedia framework api
Name:    phonon
Version: 4.11.1
Release: 12%{?dist}
License: LGPLv2+
URL:     https://community.kde.org/Phonon

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/phonon/%{version}/phonon-%{version}.tar.xz

## upstream patches

## upstreamable patches

# filter plugins
%global __provides_exclude_from ^(^%{_qt5_plugindir}/.*\\.so)$

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: pkgconfig
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libpulse-mainloop-glib) > 0.9.15
BuildRequires: pkgconfig(libxml-2.0)
# Qt5
BuildRequires: pkgconfig(Qt5DBus) pkgconfig(Qt5Designer) pkgconfig(Qt5OpenGL) pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(xcb)

## optional features


%description
%{summary}.

%package qt5
Summary: Multimedia framework api for Qt5
%{?_qt5:Requires: %{_qt5}%{?_isa} >= %{_qt5_version}}
Recommends: phonon-qt5-backend-gstreamer%{?_isa}
%description qt5
%{summary}.

%package qt5-devel
Summary: Developer files for %{name}-qt5
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-devel
%{summary}.


%prep
%autosetup -n phonon-%{version} -p1


%build
%cmake_kf5 \
  -DCMAKE_BUILD_TYPE:STRING="Release" \
  -DPHONON_BUILD_DECLARATIVE_PLUGIN:BOOL=%{?declarative:ON}%{!?declarative:OFF} \
  -DPHONON_BUILD_PHONON4QT5:BOOL=ON \
  -DPHONON_QT_IMPORTS_INSTALL_DIR=%{_qt5_importdir} \
  -DPHONON_QT_MKSPECS_INSTALL_DIR=%{_qt5_archdatadir}/mkspecs/modules \
  -DPHONON_QT_PLUGIN_INSTALL_DIR=%{_qt5_plugindir}/designer

%cmake_build


%install
%cmake_install

%find_lang %{name} --with-qt --all-name

# own these dirs
mkdir -p %{buildroot}%{_qt5_plugindir}/phonon4qt5_backend


%check
export PKG_CONFIG_PATH="%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig${PKG_CONFIG_PATH:+:}${PKG_CONFIG_PATH}"
test "$(pkg-config --modversion phonon4qt5)" = "%{version}"


%files qt5 -f %{name}.lang
%license COPYING.LIB
%{_bindir}/phononsettings
%{_libdir}/libphonon4qt5.so.4*
%{_libdir}/libphonon4qt5experimental.so.4*
# own backends dir
%dir %{_qt5_plugindir}/phonon4qt5_backend/
# designer plugin
%{_qt5_plugindir}/designer/phononwidgets.so

%files qt5-devel
%dir %{_datadir}/phonon4qt5
%{_datadir}/phonon4qt5/buildsystem/
%{_libdir}/cmake/phonon4qt5/
%{_includedir}/phonon4qt5/
%{_libdir}/libphonon4qt5.so
%{_libdir}/libphonon4qt5experimental.so
%{_libdir}/pkgconfig/phonon4qt5.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_phonon4qt5.pri


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 4.11.1-6
- use new cmake macros 

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Rex Dieter <rdieter@fedoraproject.org> - 4.11.1-3
- -devel: fix dep on main pkg
- simplify, drop need for bootstrap (rely on Recommends only)

* Wed Jan 29 2020 Rex Dieter <rdieter@fedoraproject.org> - 4.11.1-2
- enable boostrap

* Wed Jan 29 2020 Rex Dieter <rdieter@fedoraproject.org> - 4.11.1-1
- 4.11.1
- phonon-qt4 now packaged separately
- .spec cleanup

* Wed Jul 31 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.10.3-1
- 4.10.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-3
- rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-1
- 4.10.2

* Mon Sep 24 2018 Owen Taylor <otaylor@redhat.com> - 4.10.1-3
- Pass Qt paths we'll use in the file list to CMake
- In %%check, augment PKG_CONFIG_PATH, not replace it

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.10.1-1
- 4.10.1

* Wed Feb 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-4
- Recommends: phonon-backend-gstreamer
- drop versioned pulseaudio

* Wed Feb 28 2018 Adam Williamson <awilliam@redhat.com> - 4.10.0-3
- Back to a non-bootstrap build

* Wed Feb 28 2018 Adam Williamson <awilliam@redhat.com> - 4.10.0-2
- Bootstrapping build (to fix bogus dependency error in gstreamer backend)

* Fri Feb 23 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-1
- 4.10.0
- .spec cleanup/cosmetics

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.9.1-3
- rebuild (cmake.prov)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.9.1-1
- phonon-4.9.1
- better handle optional (default off) features: declarative, zeitgeist

* Mon Jan 02 2017 Rex Dieter <rdieter@math.unl.edu> - 4.9.0-4
- filter plugin provides

* Thu May 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.9.0-3
- drop revert, fix in other components instead (knotifications, knotifyconfig)

* Fri Apr 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.9.0-2
- revert upstream commit causing regression (kde#337276)

* Thu Apr 21 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.9.0-1
- phonon-4.9.0, disable qzeitgeist support
