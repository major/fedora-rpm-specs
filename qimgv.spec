%bcond_with kde
%bcond_with mpv

Name:           qimgv
Version:        1.0.3
Release:        5.alpha%{?dist}
Summary:        Image viewer. Fast, easy to use. Optional video support

License:        GPLv3+
URL:            https://github.com/easymodo/qimgv
Source0:        %{url}/archive/v%{version}-alpha/%{name}-%{version}-alpha.tar.gz

# Add AppData installation via Cmake and update manifest
# https://github.com/easymodo/qimgv/pull/408
Patch0:         https://github.com/easymodo/qimgv/pull/408.patch

BuildRequires:  cmake >= 3.13
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++ >= 9
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  opencv-devel

BuildRequires:  cmake(exiv2)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core) >= 5.12
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
%if %{with kde}
BuildRequires:  cmake(KF5WindowSystem)
%endif
%if %{with mpv}
BuildRequires:  pkgconfig(mpv)
%endif

Requires:       hicolor-icon-theme

%description
Image viewer. Fast, easy to use. Optional video support.

Key features:

  * Simple UI
  * Fast
  * Easy to use
  * Fully configurable, including themes, shortcuts
  * High quality scaling
  * Basic image editing: Crop, Rotate and Resize
  * Ability to quickly copy / move images to different folders
  * Experimental video playback via libmpv
  * Folder view mode
  * Ability to run shell scripts


%if %{with mpv}
%package        freeworld
Summary:        Video support for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    freeworld
Video support for %{name}.
%endif


%prep
%autosetup -n %{name}-%{version}-alpha -p1

# Remove bundled translations because it doesn't work anyway with current Qt ver
sed -e '/translations/d' -i qimgv/resources.qrc

# Use default for Fedora build flags
sed -e 's/ -O3//g' -i CMakeLists.txt


%build
%cmake \
    -G Ninja \
    -DVIDEO_SUPPORT:BOOL=%{?with_mpv:ON}%{!?with_mpv:OFF} \
    -DKDE_SUPPORT:BOOL=%{?with_kde:ON}%{!?with_kde:OFF} \
    -DOPENCV_SUPPORT=ON \
%ninja_build -C %{_vpath_builddir}


%install
%ninja_install -C %{_vpath_builddir}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_metainfodir}/*.xml

%if %{with mpv}
%files freeworld
%{_libdir}/lib%{name}_player_mpv.so*
%endif


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Sérgio Basto <sergio@serjux.com> - 1.0.3-4.alpha
- Rebuilt for opencv 4.6.0

* Mon May 02 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.3-3.alpha
- build: Use upstream suggested patch with AppData

* Mon May 02 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.3-2.alpha
- build: Update description

* Mon May 02 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.3-1.alpha
- chore(update): 1.0.3-alpha

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 29 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.2-1
- build(update): 1.0.2

* Mon Sep 27 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.1-1
- build(update): 1.0.1

* Wed Sep 22 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.0-1
- build(update): 1.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 10:54:15 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.1-6
- build(rebuild): 'opencv' soname bump | rh#1892895

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.1-4
- Rebuild with out-of-source builds new CMake macros

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.9.1-2
- Rebuilt for OpenCV 4.3.0

* Mon May 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.1-1
- Update to 0.9.1

* Fri May 01 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9-1
- Update to 0.9

* Tue Mar 31 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8.9-1
- Update to 0.8.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8.8-1
- Update to 0.8.8

* Tue Nov 12 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8.7-1
- Update to 0.8.7

* Wed Oct 16 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8.6-7
- Spec file fixes

* Tue Oct 15 2019 gasinvein <gasinvein@gmail.com>
- Initial package
