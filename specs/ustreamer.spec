Name: ustreamer
Version: 6.12
Release: 3%{?dist}
Summary: Lightweight and fast MJPG-HTTP streamer
License: GPL-3.0-or-later
URL: https://github.com/pikvm/ustreamer
Source: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: libatomic
BuildRequires: pkgconfig(libbsd)
BuildRequires: pkgconfig(libevent)
BuildRequires: pkgconfig(libevent_pthreads)
BuildRequires: pkgconfig(libgpiod)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(python)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(build)
BuildRequires: python3dist(wheel)
BuildRequires: python3dist(pip)

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
    WITH_SYSTEMD=1 \
    WITH_GPIO=1 \
    WITH_PYTHON=1

%install
%make_install 'PREFIX=%{_prefix}'\
    WITH_PYTHON=1

%files
%license LICENSE
%doc README.md
%{_bindir}/ustreamer
%{_bindir}/ustreamer-dump
%{_mandir}/man1/ustreamer.1*
%{_mandir}/man1/ustreamer-dump.1*

%package -n python3-%{name}
Summary: Python 3 bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Python 3 bindings for %{name}.

%files -n python3-%{name}
%{python3_sitearch}/%{name}*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 1 2024 Tao Jin <tao-j@outlook.com> - 6.12-1
- Update to 6.12
- Add libgpiod interface since upstream has refactored to support 2.0 API

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 5.41-3
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 27 2023 Tao Jin <tao-j@outlook.com> - 5.41-1
- Update to 5.41
- Remove libgpiod interface due to incompatiable 2.0 API

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 5.37-2
- Rebuilt for Python 3.12

* Thu Feb 16 2023 Tao Jin <tao-j@outlook.com> - 5.37-1
- Update to 5.37

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 07 2023 Tao Jin <tao-j@outlook.com> - 5.36-1
- Update to 5.36
- Add python package build

* Wed Dec 14 2022 Tao Jin <tao-j@outlook.com> - 5.34-1
- Update to 5.34 and address review comments

* Sun Oct 23 2022 Tao Jin <tao-j@outlook.com> - 5.24-1
- Update to 5.24
- Submit to Fedora for review
