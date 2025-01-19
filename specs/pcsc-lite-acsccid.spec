%global dropdir %(pkg-config libpcsclite --variable usbdropdir 2>/dev/null)

Name:		pcsc-lite-acsccid
Version:	1.1.11
Release:	4%{?dist}
Summary:	ACS CCID PC/SC Driver for Linux/Mac OS X

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		https://acsccid.sourceforge.io/
Source0:	https://downloads.sourceforge.net/acsccid/acsccid-%{version}.tar.bz2

BuildRequires:	make
BuildRequires:	gettext-devel
BuildRequires:	autoconf automake libtool
BuildRequires:	autoconf-archive
BuildRequires:	gcc
BuildRequires:	pcsc-lite-devel
BuildRequires:	libusb-compat-0.1-devel
BuildRequires:	flex
BuildRequires:	perl
BuildRequires:	pkg-config
BuildRequires:	systemd-rpm-macros

Requires:	pcsc-lite

# This is bundled from pcsc-lite-ccid and pcsc-lite upstreams
Provides: bundled(simclist) = 1.6
# There are parts of openct project, last import to CCID on 2004
Provides: bundled(openct) = 0.6.0

%description
acsccid is a PC/SC driver for Linux/Mac OS X and it supports ACS CCID smart card
readers. This library provides a PC/SC IFD handler implementation and
communicates with the readers through the PC/SC Lite resource manager (pcscd).

acsccid is based on ccid. See CCID free software driver [1] for more
information.


%prep
%setup -q -n acsccid-%{version}


%build
./bootstrap
%configure --disable-silent-rules
%make_build


%install
%make_install
install -p -m 644 src/openct/LICENSE LICENSE.openct
install -p -m 644 src/towitoko/README README.towitoko


%post
%systemd_postun_with_restart pcscd.service


%preun
%systemd_preun pcscsd.service


%postun
%systemd_postun_with_restart pcscd.service


%files
%doc AUTHORS README README.towitoko
%license COPYING LICENSE.openct
%dir %{dropdir}/ifd-acsccid.bundle/
%dir %{dropdir}/ifd-acsccid.bundle/Contents/
%{dropdir}/ifd-acsccid.bundle/Contents/Info.plist
%dir %{dropdir}/ifd-acsccid.bundle/Contents/Linux/
%{dropdir}/ifd-acsccid.bundle/Contents/Linux/libacsccid.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.11-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 28 2024 Jakub Jelen <jjelen@redhat.com> - 1.1.11-1
- New upstream release

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 07 2023 Jakub Jelen <jjelen@redhat.com> - 1.1.10-1
- New upstream release

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 27 2023 Jakub Jelen <jjelen@redhat.com> - 1.1.9-1
- New upstream release (#2181481)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 02 2022 Jakub Jelen <jjelen@redhat.com> - 1.1.8-8
- Use compat libusb to build this package (#2113573)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Jakub Jelen <jjelen@redhat.com> - 1.1.8-1
- New upstream release (#1788719)

* Mon Aug 19 2019 Jakub Jelen <jjelen@redhat.com> - 1.1.7-1
- New upstream release (#1742307)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Jakub Jelen <jjelen@redhat.com> - 1.1.6-1
- Initial release in Fedora
