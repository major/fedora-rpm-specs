
Summary: Gstreamer phonon backend
Name:    phonon-backend-gstreamer
Epoch:   2
Version: 4.10.0
Release: 15%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://community.kde.org/Phonon

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/phonon/phonon-backend-gstreamer/%{version}/phonon-backend-gstreamer-%{version}.tar.xz

## upstream patches

## upstreamable patches

BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-app-1.0) pkgconfig(gstreamer-audio-1.0) pkgconfig(gstreamer-video-1.0)

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(Phonon4Qt5) >= 4.11
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: pkgconfig
BuildRequires: pkgconfig(Qt5OpenGL)
BuildRequires: pkgconfig(Qt5X11Extras)

%global phonon_version %(pkg-config --modversion phonon 2>/dev/null || echo 4.11)

%description
%{summary}.

%package -n phonon-qt5-backend-gstreamer
Summary:  Gstreamer phonon-qt5 backend
Provides: phonon-qt5-backend%{?_isa} = %{phonon_version}
Requires: gstreamer1-plugins-good%{?_isa}
%description -n phonon-qt5-backend-gstreamer
%{summary}.


%prep
%autosetup -n phonon-backend-gstreamer-%{version} -p1


%build
%cmake_kf5 \
  -DCMAKE_BUILD_TYPE:STRING="Release" \
  -DUSE_INSTALL_PLUGIN:BOOL=ON \
  -DPHONON_BUILD_PHONON4QT5:BOOL=ON

%cmake_build


%install
%cmake_install

%find_lang phonon_gstreamer --with-qt


%files -n phonon-qt5-backend-gstreamer -f phonon_gstreamer.lang
%license COPYING.LIB
%{_qt5_plugindir}/phonon4qt5_backend/phonon_gstreamer.so
%{_kf5_datadir}/icons/hicolor/*/apps/phonon-gstreamer.*


%changelog
* Wed Jan 08 2025 Alessandro Astone <ales.astone@gmail.com> - 2:4.10.0-15
- Add build dependency on Qt5LinguistTools

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2:4.10.0-14
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:4.10.0-4
- use new cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.10.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jan 20 2020 Rex Dieter <rdieter@fedoraproject.org> - 2:4.10.0-1
- 4.10.0
- qt4 support now packaged separately (phonon-qt4-backend-gstreamer)
- .spec cleanup

* Wed Jul 31 2019 Rex Dieter <rdieter@fedoraproject.org> - 2:4.9.1-1
- 4.9.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Rex Dieter <rdieter@fedoraproject.org> - 2:4.9.0-11
- rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Adam Williamson <awilliam@redhat.com> - 2:4.9.0-8
- Fix a gstreamer dep from -7 (good, not good5)

* Tue Feb 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 2:4.9.0-7
- tighten gstreamer plugin dep
- use %%license, %%make_build 
- BR: gcc-c++

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2:4.9.0-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:4.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 21 2016 Rex Dieter <rdieter@fedoraproject.org> - 2:4.9.0-1
- phonon-backend-4.9.0

