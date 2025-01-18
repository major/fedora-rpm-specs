%global use_wayland 1

Name:		enlightenment
Version:	0.26.0
Release:	4%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
Summary:	Enlightenment window manager
Url:		http://enlightenment.org
Source0:	http://download.enlightenment.org/rel/apps/enlightenment/%{name}-%{version}.tar.xz
Patch0:		enlightenment-0.25.0-fix-desktop-files.patch
BuildRequires:	gcc, gcc-c++
BuildRequires:	alsa-lib-devel
BuildRequires:	bluez-libs-devel
BuildRequires:	dbus-devel
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	efl-devel >= 1.26.0
%if %{use_wayland}
BuildRequires:	wayland-protocols-devel
BuildRequires:	wayland-devel
BuildRequires:	xorg-x11-server-Xwayland
%endif
BuildRequires:	libdrm-devel
BuildRequires:	libexif-devel
BuildRequires:	libuuid-devel
BuildRequires:	libXext-devel
BuildRequires:	pam-devel
BuildRequires:	systemd
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	ninja-build, meson
BuildRequires:	xkeyboard-config-devel
Requires:	%{name}-data = %{version}-%{release}
Requires:	efl
Requires:	redhat-menus
Provides:	firstboot(windowmanager) = enlightenment
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd

%description
Enlightenment window manager is a lean, fast, modular and very extensible window
manager for X11 and Linux. It is classed as a "desktop shell" providing the
things you need to operate your desktop (or laptop), but is not a whole '
application suite. This covered launching applications, managing their windows
and doing other system tasks like suspending, reboots, managing files etc.

%package data
Summary:	Enlightenment data files
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description data
Contains data files for Enlightenment

%package devel
Summary:	Enlightenment headers, documentation and test programs
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Headers, test programs and documentation for enlightenment.

%prep
%setup -q
%patch -P0 -p1 -b .fixme

%build
%{meson} \
 -Dpam=true \
 -Dmount-eeze=true \
%if %{use_wayland}
 -Dwl=true \
%endif
 -Dsystemdunitdir=%{_userunitdir}
%{meson_build}

%install
%{meson_install}

find %{buildroot} -name '*.la' -delete

%find_lang %{name}
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

%post
%systemd_post enlightenment.service

%postun
%systemd_postun_with_restart enlightenment.service

%preun
%systemd_preun enlightenment.service

%files
%doc AUTHORS COPYING README.md TODO.md
%dir %{_sysconfdir}/enlightenment
%config %{_sysconfdir}/enlightenment/system.conf
%{_sysconfdir}/xdg/menus/e-applications.menu
%{_sysconfdir}/enlightenment/sysactions.conf
%{_bindir}/emixer
%{_bindir}/enlightenment
%{_bindir}/enlightenment_askpass
%{_bindir}/enlightenment_filemanager
%{_bindir}/enlightenment_fprint
%{_bindir}/enlightenment_imc
%{_bindir}/enlightenment_open
%{_bindir}/enlightenment_paledit
%{_bindir}/enlightenment_remote
%{_bindir}/enlightenment_start
%{_libdir}/enlightenment
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/places/*
%{_datadir}/pixmaps/enlightenment-askpass.png
%{_userunitdir}/enlightenment.service

%files data -f %{name}.lang
%if %{use_wayland}
%{_datadir}/wayland-sessions/enlightenment.desktop
%endif
%{_datadir}/xsessions/enlightenment.desktop
%{_datadir}/enlightenment
%{_datadir}/applications/*.desktop

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/enlightenment

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.26.0-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 02 2024 Ding-Yi Chen <dingyichen@gmail.com> - 0.26.0-1
- Upstream update to 0.26.0
- Upstream remove NEWS, thus remove from doc
- Upstream rename README to README.md
- Upstream has TODO.md now, thus add to doc

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 24 2022 Tom Callaway <spot@fedoraproject.org> - 0.25.4-1
- update to 0.25.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan  3 2022 Tom Callaway <spot@fedoraproject.org> - 0.25.1-1
- update to 0.25.1

* Wed Dec 29 2021 Tom Callaway <spot@fedoraproject.org> - 0.25.0-1
- update to 0.25.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Tom Callaway <spot@fedoraproject.org> - 0.24.2-1
- update to 0.24.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun  2 2020 Tom Callaway <spot@fedoraproject.org> - 0.24.1-1
- update to 0.24.1

* Mon May 18 2020 Tom Callaway <spot@fedoraproject.org> - 0.24.0-1
- update to 0.24.0
- turn wayland support on

* Fri Jan 31 2020 Tom Callaway <spot@fedoraproject.org> - 0.23.1-3
- fix FTBFS

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 2019 Tom Callaway <spot@fedoraproject.org> - 0.23.1-1
- update to 0.23.1

* Thu Aug 29 2019 Tom Callaway <spot@fedoraproject.org> - 0.23.0-1
- update to 0.23.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct  4 2018 Tom Callaway <spot@fedoraproject.org> - 0.22.4-1
- update to 0.22.4

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 25 2018 Tom Callaway <spot@fedoraproject.org> - 0.22.3-1
- update to 0.22.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Tom Callaway <spot@fedoraproject.org> - 0.22.1-1
- update to 0.22.1

* Fri Nov 17 2017 Tom Callaway <spot@fedoraproject.org> - 0.22.0-1
- update to 0.22.0

* Thu Oct 12 2017 Tom Callaway <spot@fedoraproject.org> - 0.21.10-1
- update to 0.21.10

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 Tom Callaway <spot@fedoraproject.org> - 0.21.8-1
- update to 0.21.8

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec  9 2016 Tom Callaway <spot@fedoraproject.org> - 0.21.5-1
- update to 0.21.5

* Thu Dec  1 2016 Tom Callaway <spot@fedoraproject.org> - 0.21.4-1
- update to 0.21.4

* Mon Nov 28 2016 Tom Callaway <spot@fedoraproject.org> - 0.21.3-1
- update to 0.21.3
- add pulseaudio-libs-devel as BR

* Tue Sep  6 2016 Tom Callaway <spot@fedoraproject.org> - 0.21.2-1
- update to 0.21.2

* Mon Jul 25 2016 Tom Callaway <spot@fedoraproject.org> - 0.21.1-1
- update to 0.21.1

* Tue Jun 14 2016 Tom Callaway <spot@fedoraproject.org> - 0.20.9-1
- update to 0.20.9

* Tue May 17 2016 Tom Callaway <spot@fedoraproject.org> - 0.20.8-1
- update to 0.20.8

* Fri May 13 2016 Tom Callaway <spot@fedoraproject.org> - 0.20.7-2
- ensure that the startup apps cache handler has run before trying to start apps
- thanks to Mike Blumenkrantz

* Tue Apr 26 2016 Tom Callaway <spot@fedoraproject.org> - 0.20.7-1
- update to 0.20.7

* Wed Feb  3 2016 Tom Callaway <spot@fedoraproject.org> - 0.20.4-1
- update to 0.20.4

* Thu Jan 21 2016 Ding-Yi Chen <dchen@redhat.com> - 0.20.3-1
- update to 0.20.3

* Tue Dec 15 2015 Tom Callaway <spot@fedoraproject.org> - 0.20.1-1
- update to 0.20.1

* Wed Dec  2 2015 Tom Callaway <spot@fedoraproject.org> - 0.20.0-1
- update to 0.20.0

* Fri Nov 13 2015 Tom Callaway <spot@fedoraproject.org> - 0.19.13-1
- update to 0.19.13

* Tue Nov 10 2015 Tom Callaway <spot@fedoraproject.org> - 0.19.12-1
- update to 0.19.12

* Fri Sep 25 2015 Tom Callaway <spot@fedoraproject.org> - 0.19.11-1
- update to 0.19.11

* Mon Sep 14 2015 Tom Callaway <spot@fedoraproject.org> - 0.19.10-1
- update to 0.19.10

* Mon Aug 31 2015 Tom Callaway <spot@fedoraproject.org> - 0.19.9-1
- update to 0.19.9

* Thu Aug 13 2015 Tom Callaway <spot@fedoraproject.org> - 0.19.8-1
- update to 0.19.8

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Tom Callaway <spot@fedoraproject.org> - 0.19.5-2
- conditionalize wayland (default to off)

* Tue May  5 2015 Tom Callaway <spot@fedoraproject.org> - 0.19.5-1
- update to 0.19.5

* Thu Apr  2 2015 Tom Callaway <spot@fedoraproject.org> - 0.19.4-1
- update to 0.19.4

* Fri Dec 12 2014 Tom Callaway <spot@fedoraproject.org> - 0.17.6-2
- use systemctl calls to suspend/hibernate

* Thu Oct 23 2014 Tom Callaway <spot@fedoraproject.org> - 0.17.6-1
- update to 0.17.6

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 12 2013 Dan Mashal <dan.mashal@fedoraproject.org> 0.17.5-2
- Add emotion-devel to BRs

* Thu Nov 07 2013 Dan Mashal <dan.mashal@fedoraproject.org> 0.17.5-1
- Update to 0.17.5

* Mon Oct 07 2013 Dan Mashal <dan.mashal@fedoraproject.org> 0.17.4-4
- Add hard runtime requirements so one package can install the entire stack.

* Sun Oct 06 2013 Dan Mashal <dan.mashal@fedoraproejct.org> 0.17.4-3
- Add versioned build deps.

* Sun Oct 06 2013 Dan Mashal <dan.mashal@fedoraproejct.org> 0.17.4-2
- Update spec as per package review #1014619

* Tue Sep 24 2013 Dan Mashal <dan.mashal@fedoraproject.org> 0.17.4-1
- Update to 0.17.4
- Clean up spec file
- Update license from MIT to BSD

* Wed Jan 02 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.17.0-1
- initial spec
