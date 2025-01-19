%global pkgrel    1.0.0
%global extver    pre12

Name:           imwheel
Version:        %{pkgrel}
Release:        0.17.%{extver}%{?dist}
Summary:        Mouse Event to Key Event Mapper Daemon
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Url:            http://imwheel.sourceforge.net
Source0:        http://prdownloads.sourceforge.net/%{name}/%{name}-%{pkgrel}%{extver}.tar.gz
Source1:        http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
# PATCH-FIX-UPSTREAM to prevent compiler warnings
# "cast from pointer to integer of different size"
Patch1:         imwheel-intptr_t.patch
# PATCH-FIX-UPSTREAM to fix uninitialized variable hsi.
Patch2:         imwheel-fix_uninitialized_var.patch
# PATCH-FIX-OPENSUSE not to install to root only.
Patch3:         imwheel-fix_destdir.patch
# PATCH-FEATURE-OPENSUSE to put configs to /etc/ instead of /etc/X11.
Patch4:         imwheel-config_file_path.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRequires: make
# https://bugzilla.redhat.com/show_bug.cgi?id=1823983
Requires:       xorg-x11-fonts-75dpi

%description
A daemon for X11, which watches for mouse wheel actions and outputs them as
key presses. It can be configured separately for different windows. It also
allows input from it's own (included) gpm, or from jamd, or from XFree86 ZAxis
mouse wheel conversion.

%prep
%autosetup -p0 -n %{name}-%{pkgrel}%{extver}
iconv -f iso88591 -t utf8 ChangeLog > ChangeLog
sed -i 's|AM_CONFIG_HEADER|AC_CONFIG_HEADERS|' configure.in
mv %{S:1} COPYING

%build
autoreconf -fiv
%configure --with-x
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog EMACS
%doc FREEBSD NEWS README
%license COPYING
%config(noreplace) %{_sysconfdir}/imwheelrc
%{_bindir}/imwheel
%{_mandir}/man1/imwheel.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.17.pre12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.0-0.16.pre12
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.15.pre12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.14.pre12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.13.pre12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.12.pre12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.11.pre12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.10.pre12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.9.pre12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.8.pre12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.7.pre12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.6.pre12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 14 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.0.0-0.5.pre12
- Requires xorg-x11-fonts-75dpi (RHBZ#1823983)
- BR only gcc instead of gcc-c++

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.4.pre12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.3.pre12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.2.pre12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 mosquito <sensor.wen@gmail.com> - 1.0.0-0.1.pre12
- Package for fedora

* Tue Aug 29 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.0-0.1.pre12
- Correct spec for fedora
