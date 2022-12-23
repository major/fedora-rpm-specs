Name: ustreamer
Version: 5.34
Release: 1%{?dist}
Summary: Lightweight and fast MJPG-HTTP streamer
License: GPL-3.0-or-later
URL: https://github.com/pikvm/ustreamer
Source: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libevent)
BuildRequires: pkgconfig(libevent_pthreads)
BuildRequires: pkgconfig(libbsd)
BuildRequires: pkgconfig(libgpiod)
BuildRequires: pkgconfig(libsystemd)

%description
ustreamer(µStreamer) is a lightweight and very quick server to stream MJPG video
from any V4L2 device to the net.

All new browsers have native support of this video format,
as well as most video players such as mplayer, VLC etc.

µStreamer is a part of the Pi-KVM project designed to stream VGA and HDMI
screencast hardware data with the highest resolution and FPS possible.


%prep
%autosetup

%build
%set_build_flags
%make_build \
    WITH_GPIO=1 \
    WITH_SYSTEMD=1

%install
%make_install 'PREFIX=%{_prefix}'

%files
%license LICENSE
%doc README.md
%{_bindir}/ustreamer
%{_bindir}/ustreamer-dump
%{_mandir}/man1/ustreamer.1*
%{_mandir}/man1/ustreamer-dump.1*

%changelog
* Wed Dec 14 2022 Tao Jin <tao-j@outlook.com> - 5.34-1
- update to 5.34 and address review comments

* Sun Oct 23 2022 Tao Jin <tao-j@outlook.com> - 5.24-1
- Update to 5.24
- Submit to Fedora for review
