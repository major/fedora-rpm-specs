Name:       callaudiod
Version:    0.1.5
Release:    1%{?dist}
Summary:    Daemon for dealing with audio routing during phone calls

License:        GPLv3+
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
* Thu Dec 08 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3

* Wed Jan 05 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Thu Sep 16 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.0-1
- Upgrade to 0.1.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.0.5-1
- Update to 0.0.5

* Thu Dec 17 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.0.4-2
- Enabling debug

* Wed Nov 04 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.0.4-1
- Initial packaging
