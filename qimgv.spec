%bcond_with kde
%bcond_with mpv

Name:           qimgv
Version:        1.0.3
Release:        %autorelease
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
%autochangelog
