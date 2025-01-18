Name:		dm-zoned-tools
Version:	2.2.2
Release:	7%{?dist}
Summary:	Provides utilities to format, check and repair Linux dm-zoned devices

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://github.com/westerndigitalcorporation/%{name}
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(devmapper)
BuildRequires:	pkgconfig(libkmod)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(blkid)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	gcc

%description
This package provides the dmzadm utility which can be used to format,
check and repair zoned block devices used with Linux dm-zoned device
mapper target driver.

%prep
%autosetup

%build
sh autogen.sh
%configure
%make_build

%install
%make_install

%files
%{_sbindir}/dmzadm
%{_mandir}/man8/dmzadm.*

%license COPYING.GPL
%doc README.md CONTRIBUTING

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.2-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 31 2023 Damien Le Moal <damien.lemoal@wdc.com> 2.2.2-1
- Version 2.2.2 package

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Damien Le Moal <damien.lemoal@wdc.com> 2.2.1-1
- Version 2.2.1 package

* Wed Sep 01 2021 Damien Le Moal <damien.lemoal@wdc.com> 2.2.0-1
- Add "systemd-devel" as a build dependency
- Version 2.2.0 package

* Thu Jul 01 2021 Damien Le Moal <damien.lemoal@wdc.com> 2.1.3-1
- Add "make" as a build dependency 
- Version 2.1.3 package

* Mon Jun 14 2021 Damien Le Moal <damien.lemoal@wdc.com> 2.1.2-1
- Version 2.1.2 initial package
