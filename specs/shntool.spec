Name:           shntool
Version:        3.0.10
Release:        35%{?dist}
Summary:        A multi-purpose WAVE data processing and reporting utility

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://etree.org/shnutils/shntool
Source0:        http://etree.org/shnutils/shntool/dist/src/%{name}-%{version}.tar.gz
# Patches are from Debian
# https://sources.debian.org/patches/shntool/3.0.10-1/
Patch0:         large-size.patch
Patch1:         large-times.patch
Patch2:         no-cdquality-check.patch
Patch3:         https://github.com/max619/shntool/commit/cfd06e4edecdca2013e0fe04db135fd110a68203.patch
Patch4:         0001-fix-valid-wavepack-header-versions.patch

BuildRequires: make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc

%description
A multi-purpose WAVE data processing and reporting utility. File
formats are abstracted from its core, so it can process any file that contains
WAVE data, compressed or not - provided there exists a format module to handle
that particular file type. 

%prep
%autosetup -p1
autoreconf -fiv

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog NEWS README
%doc doc/*
%license COPYING
%{_bindir}/shn*
%{_mandir}/man1/%{name}.1.*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.10-34
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 08 2021 Felix Kaechele <felix@kaechele.ca> - 3.0.10-27
- add patch to support newer wavepack header versions (rhbz#1940701)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 07 2020 Felix Kaechele <felix@kaechele.ca> - 3.0.10-23
- Fix for rhbz#1833083 (shntool: cannot split 24-bit flac files)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Felix Kaechele <heffer@fedoraproject.org> - 3.0.10-19
- Add gcc BuildRequires

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0.10-17
- Fix splitting large files at high bitrate
- Clean spec file

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 01 2013 Felix Kaechele <heffer@fedoraproject.org> - 3.0.10-8
- run autoreconf during setup for aarch64 support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 09 2009 Felix Kaechele <felix at fetzig dot org> - 3.0.10-1
- 3.0.10

* Sun Mar 29 2009 Felix Kaechele <felix at fetzig dot org> - 3.0.9-1
- 3.0.9

* Tue Mar 03 2009 Felix Kaechele <felix at fetzig dot org> - 3.0.8-1
- initial build
