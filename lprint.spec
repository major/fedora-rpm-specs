# the package can work with devices from network, so use hardened build
%global _hardened_build 1

Name: lprint
Version: 1.2.0
Release: 2%{?dist}
Summary: A Label Printer Application

License: ASL 2.0
URL: https://www.msweet.org/lprint
Source0: https://github.com/michaelrsweet/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz


# UPSTREAM PATCHES


# dns-sd support for register/sharing devices
BuildRequires: pkgconfig(avahi-client) >= 0.7
# uses CUPS API for arrays, options, rastering, HTTP, IPP support
BuildRequires: cups-devel >= 2.2.0
# written in C
BuildRequires: gcc
# for autosetup
BuildRequires: git-core
# PNG printing support
BuildRequires: pkgconfig(libpng) >= 1.6.0
# USB printing support
BuildRequires: pkgconfig(libusb-1.0) >= 1.0
# uses Makefile
BuildRequires: make
# the basic printer application related structures are now implemented in PAPPL
BuildRequires: pkgconfig(pappl) >= 1.1
# using pkg-config in configure script
BuildRequires: pkgconf-pkg-config
# for macros in rpm scriptlets
BuildRequires: systemd-rpm-macros

# lprint server now can run as a systemd service
Requires: systemd

%description
LPrint is a label printer application for macOS and Linux. Basically,
LPrint is a print spooler optimized for label printing. It accepts
"raw" print data as well as PNG images (like those used for shipping
labels by most shippers' current web APIs) and has built-in "drivers"
to send the print data to USB and network-connected label printers.


%prep
%autosetup -S git


%build
# use gcc
export CC=%{__cc}

# get system default CFLAGS and LDFLAGS
%set_build_flags

%configure

%make_build


%install
%make_install DESTDIR=''

%post
%systemd_post lprint.service

%preun
%systemd_preun lprint.service

%postun
%systemd_postun_with_restart lprint.service

%files
%doc README.md DOCUMENTATION.md CONTRIBUTING.md CHANGES.md
%license LICENSE NOTICE
%{_bindir}/lprint
%{_mandir}/man1/lprint-add.1*
%{_mandir}/man1/lprint-cancel.1*
%{_mandir}/man1/lprint-default.1*
%{_mandir}/man1/lprint-delete.1*
%{_mandir}/man1/lprint-devices.1*
%{_mandir}/man1/lprint-drivers.1*
%{_mandir}/man1/lprint-jobs.1*
%{_mandir}/man1/lprint-modify.1*
%{_mandir}/man1/lprint-printers.1*
%{_mandir}/man1/lprint-server.1*
%{_mandir}/man1/lprint-shutdown.1*
%{_mandir}/man1/lprint-status.1*
%{_mandir}/man1/lprint-submit.1*
%{_mandir}/man1/lprint.1*
%{_mandir}/man5/lprint.conf.5*
%{_unitdir}/lprint.service


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Zdenek Dohnal <zdohnal@redhat.com> - 1.2.0-1
- 2157610 - lprint-1.2.0 is available

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 06 2022 Zdenek Dohnal <zdohnal@redhat.com> - 1.1.0-3
- path to lprint was hardcoded in service file

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Zdenek Dohnal <zdohnal@redhat.com> - 1.1.0-1
- 2035381 - lprint-1.1.0 is available

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.0-2
- use smaller git-core instead of git

* Mon Aug 17 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.0-1
- Initial import (#1867587)
