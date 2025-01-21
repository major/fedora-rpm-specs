Name:           xsecurelock
Version:        1.8.0
Release:        8%{?dist}
Summary:        X11 screen lock utility with security in mind
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/google/xsecurelock

Source0:        https://github.com/google/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

Requires: libXft
BuildRequires: make
BuildRequires: gcc
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pam-devel
BuildRequires: pamtester
BuildRequires: pkgconfig(libbsd)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(xrandr)
BuildRequires: httpd-tools
BuildRequires: pandoc
BuildRequires: doxygen
BuildRequires: libXft-devel
BuildRequires: xscreensaver
BuildRequires: mpv


%description
XSecureLock is an X11 screen lock utility designed with the primary goal of
security.

%prep
%autosetup

%build
%configure --with-pam-service-name=system-auth --with-xft --with-xscreensaver=/usr/bin/xscreensaver --with-mpv=/usr/bin/mpv --with-htpasswd=/usr/bin/htpasswd
%make_build

%install
%make_install
rm %{buildroot}%{_pkgdocdir}/LICENSE

%files
%license LICENSE
%doc README.md
%doc CONTRIBUTING
%doc /usr/share/doc/xsecurelock/examples/saver_livestreams
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_libexecdir}/%{name}/auth_x11
%{_libexecdir}/%{name}/authproto_pam
%{_libexecdir}/%{name}/authproto_pamtester
%{_libexecdir}/%{name}/authproto_htpasswd
%{_libexecdir}/%{name}/dimmer
%{_libexecdir}/%{name}/pgrp_placeholder
%{_libexecdir}/%{name}/saver_blank
%{_libexecdir}/%{name}/saver_multiplex
%{_libexecdir}/%{name}/until_nonidle
%{_libexecdir}/%{name}/saver_xscreensaver
%{_libexecdir}/%{name}/saver_mpv

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.0-7
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 19 2022 Sam P <survient@fedoraproject.org> - 1.8.0-2
- Added mpv build flag.

* Wed Oct 19 2022 Sam P <survient@fedoraproject.org> - 1.8.0-1
- Latest upstream release.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Sam P <survient@fedoraproject.org> - 1.7.0-7
- Added path to xscreensaver binary to build saver_xscreensaver

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 14 2020 Sam P <survient@fedoraproject.org> - 1.7.0-3
- Added --with-xft build flag

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 21 2020 Sam P <survient@fedoraproject.org> - 1.7.0-1
- Initial Build
