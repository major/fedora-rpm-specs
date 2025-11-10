Name:           obs-studio-plugin-droidcam
Version:        2.4.1
Release:        %autorelease
Summary:        Use your phone as a camera in OBS Studio

# Public Domain File
# src/mdns.h
License:        GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:            https://droidcam.app/obs
Source0:        https://github.com/dev47apps/droidcam-obs-plugin/archive/%{version}/droidcam-obs-plugin-%{version}.tar.gz
# This should be fixed in the next release: 
# https://github.com/dev47apps/droidcam-obs-plugin/blob/161cb95b8dc5fe77185e52a9783dc45c6d137165/src/ffmpeg_decode.cc#L122-L127
Patch0: ffmpeg8.patch

BuildRequires:  make
BuildRequires:  gcc-c++

BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(libusbmuxd-2.0)
BuildRequires:  pkgconfig(libimobiledevice-1.0)
BuildRequires:  pkgconfig(libobs)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)

Requires:       obs-studio%{?_isa}
Supplements:    obs-studio%{?_isa}


%description
Use your phone as a camera directly in OBS.
You can add as many devices as you want,
either using WiFi or USB.


%prep
%autosetup -n droidcam-obs-plugin-%{version} -p1


%build
mkdir -p build

%make_build \
    LIBUSBMUXD=libusbmuxd-2.0 \
    LIBIMOBILEDEV=libimobiledevice-1.0 \
    ALLOW_STATIC=no \
    ENABLE_GUI=yes

%install
mkdir -p %{buildroot}%{_libdir}/obs-plugins
install -pm 0755 build/droidcam-obs.so %{buildroot}%{_libdir}/obs-plugins

mkdir -p %{buildroot}%{_datadir}/obs/obs-plugins/droidcam-obs
cp -r data/* %{buildroot}%{_datadir}/obs/obs-plugins/droidcam-obs


%files
%license LICENSE
%doc README.md
%{_libdir}/obs-plugins/droidcam-obs.so
%{_datadir}/obs/obs-plugins/droidcam-obs/


%changelog
%autochangelog
