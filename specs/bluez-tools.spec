# No proper release-tags, yet.  :(
%global commit 7cb788c9c43facfd2d14ff50e16d6a19f033a6a7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20170912
%global git_ver -git%{gitdate}.%{shortcommit}
%global git_rel .git%{gitdate}.%{shortcommit}


Name:		bluez-tools
Version:	0.2.0
Release:	0.27%{?git_rel}%{?dist}
Summary:	A set of tools to manage Bluetooth devices for Linux

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/khvzak/%{name}
Source0:	%{url}/archive/%{commit}/%{name}-%{version}%{?git_ver}.tar.gz
Patch0:		%{url}/pull/34.patch#/fix_gcc-10_compile.patch
Patch1:		%{name}-exit-if-no-adapter.patch

BuildRequires:	gcc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	readline-devel
BuildRequires: make

Requires:	bluez%{?_isa}

%description
This was a GSoC'10 project to implement a new command line tools for
bluez (Bluetooth stack for Linux).  It is currently an active open
source project.

The project is implemented in C and uses the D-Bus interface of bluez.

The project is still a work in progress, and not all APIs from Bluez
have been implemented as a part of bluez-tools.  The APIs which have
been implemented in bluez-tools are adapter, agent, device, network
and obex.  Other APIs, such as interfaces for medical devices,
pedometers and other specific APIs have not been ported to bluez-tools.


%prep
%autosetup -n %{name}-%{commit} -p 1
%{_bindir}/autoreconf -fiv


%build
%configure
%make_build


%install
%make_install


%files
%license AUTHORS COPYING
%doc ChangeLog README
%{_bindir}/bt-*
%{_mandir}/man1/bt-*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.27.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 09 2025 Dominik Mierzejewski <dominik@greysector.net> - 0.2.0-0.26.git20170912.7cb788c
- fix crash if no adapter found (resolves rhbz#2321335)

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.0-0.25.git20170912.7cb788c
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.24.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.23.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.22.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.21.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.20.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.19.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.18.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.17.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.16.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.15.git20170912.7cb788c
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.14.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Leigh Scott <leigh123linux@googlemail.com> - 0.2.0-0.13.git20170912.7cb788c
- Fix gcc-10 compile

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.12.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.11.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-0.10.git20170912.7cb788c
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.9.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.8.git20170912.7cb788c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Björn Esser <besser82@fedoraproject.org> - 0.2.0-0.7.git20170912.7cb788c
- New snapshot

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.6.git20161212.97efd29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.5.git20161212.97efd29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.4.git20161212.97efd29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 01 2017 Björn Esser <besser82@fedoraproject.org> - 0.2.0-0.3.git20161212.97efd29
- Append %%{?git_rel} to Release-tag

* Sun Feb 19 2017 Björn Esser <besser82@fedoraproject.org> - 0.2.0-0.2
- Initial import (rhbz#1424772)

* Sun Feb 19 2017 Björn Esser <besser82@fedoraproject.org> - 0.2.0-0.1
- Initial rpm-release (rhbz#1424772)
