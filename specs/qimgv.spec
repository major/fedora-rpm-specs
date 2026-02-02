%bcond_with kde

%global gitdate       20260119
%global commit        3127a2d211b124ad4fcf853d01e6df9323bdfdc3
%global short_commit  %(c="%{commit}"; echo ${c:0:7})

Name:           qimgv
Version:        1.0.3^%{gitdate}git%{short_commit}
Release:        %autorelease
Summary:        Image viewer. Fast, easy to use. Optional video support

License:        GPL-3.0-or-later
URL:            https://github.com/easymodo/qimgv
Source0:        %{url}/archive/%{commit}/%{name}-%{short_commit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  opencv-devel

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6LinguistTools)

%if %{with kde}
BuildRequires:  cmake(KF6WindowSystem)
%endif
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(mpv)

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

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

%prep
%autosetup -p1 -C

%build
%cmake \
    -G Ninja \
    -DEXIV2=ON \
    -DVIDEO_SUPPORT=ON \
    -DOPENCV_SUPPORT=ON \
    -DKDE_SUPPORT:BOOL=%{?with_kde:ON}%{!?with_kde:OFF} \
    -DUSE_QT5=OFF
%cmake_build

%install
%cmake_install

%find_lang qimgv --with-qt --all-name

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f qimgv.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_metainfodir}/*.xml
%{_libdir}/%{name}/player_mpv.so

%changelog
%autochangelog
