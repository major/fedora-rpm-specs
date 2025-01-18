Name:       callaudiod
Version:    0.1.10
Release:    3%{?dist}
Summary:    Daemon for dealing with audio routing during phone calls

License:        GPL-3.0-or-later
URL:            https://gitlab.com/mobian1/callaudiod
Source0:        https://gitlab.com/mobian1/callaudiod/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)


%description
callaudiod is a daemon for dealing with audio routing during phone calls.
It provides a D-Bus interface allowing other programs to:

switch audio profiles
output audio to the speaker or back to its original port
mute the microphone


%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install


%files
%{_bindir}/%{name}
%{_bindir}/callaudiocli
%dir %{_includedir}/libcallaudio-0.1
%{_libdir}/libcallaudio-0.1.so.0
%{_datadir}/dbus-1/interfaces/org.mobian_project.CallAudio.xml
%{_datadir}/dbus-1/services/org.mobian_project.CallAudio.service

%files devel
%{_includedir}/libcallaudio-0.1/libcallaudio.h
%{_includedir}/libcallaudio-0.1/libcallaudio-enums.h
%{_libdir}/libcallaudio-0.1.so
%{_libdir}/pkgconfig/libcallaudio-0.1.pc

%doc README.md
%license COPYING

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

%autochangelog
