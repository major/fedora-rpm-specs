Name:          neard
Version:       0.19
Release:       6%{?dist}
Summary:       Near Field Communication (NFC) manager
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:       GPL-2.0-only
URL:           https://01.org/linux-nfc/
Source0:       https://git.kernel.org/pub/scm/network/nfc/neard.git/snapshot/%{name}-%{version}.tar.gz

BuildRequires: automake autoconf libtool autoconf-archive
BuildRequires: dbus-devel
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: libnl3-devel
BuildRequires: make
BuildRequires: systemd

%description
neard is an NFC (Near Field Communication) daemon for managing NFC operations 
on devices running the Linux operating system. It relies on the Linux kernel NFC 
socket and generic netlink families, and is a fully modular system that can be 
extended through plug-ins.

It supports all 4 NFC tag types reading and writing, along with NFC LLCP 
(peer to peer mode) in both target and initiator modes.

%package tools
Summary: Tools for use with neard

%description tools
These are tools to use neard.

%package devel
Summary: Development package for neard
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with neard.

%prep
%autosetup -p1

%build
autoreconf -vif
%configure --enable-tools
%{make_build}

%install
%{make_install}

rm -f %{buildroot}/usr/include/version.h

%check
make check %{?_smp_mflags}

%ldconfig_scriptlets

%files
%license COPYING
%{_sysconfdir}/dbus-1/system.d/org.neard.conf
%{_unitdir}/neard.service
%{_libexecdir}/nfc/neard
%{_mandir}/man5/neard.conf.5*
%{_mandir}/man8/neard.8*

%files tools
%{_bindir}/nciattach
%{_bindir}/nfctool
%{_mandir}/man1/nfctool.1*

%files devel
%doc doc/*txt
%{_includedir}/near/
%{_libdir}/pkgconfig/neard.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.19-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Aug 27 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.19-1
- Update to 0.19

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 09 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 0.18-1
- Update to 0.18

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 22 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.17-1
- Update to 0.17

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec  3 2020 Dave Olsthoorn <daveo@fedoraproject.org> - 0.16-10
- Enable tools

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.16-1
- Initial package
