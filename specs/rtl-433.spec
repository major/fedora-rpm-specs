%global commit_date     20240826
%global commit_long     f0ba1538213a2fcb7487862fa1cfe7a1969a174a
%global commit_short    %(c=%{commit_long}; echo ${c:0:7})

Name: rtl-433
Version: 23.11
Release: 2.%{commit_date}git%{commit_short}%{dist}

Summary: Generic radio data receiver
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
Url: https://github.com/merbanan/rtl_433

Source0: https://github.com/merbanan/rtl_433/archive/%{commit_long}/%{name}-%{commit_long}.tar.gz

BuildRequires: coreutils
BuildRequires: sed
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: rtl-sdr-devel
BuildRequires: SoapySDR-devel
BuildRequires: libusb1-devel

%description
rtl_433 (despite the name) is a generic data receiver, mainly
for the 433.92 MHz, 868 MHz (SRD), 315 MHz, and 915 MHz ISM bands.

For more documentation and related projects see the https://triq.org/ site.

%package devel
Summary:    Development libraries for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries for %{name}

%prep
%autosetup -n rtl_433-%{commit_long}

# Fix python shebang in examples
sed -ri 's\^#!/usr/bin/env python3?$\#!%{python3}\' examples/*.py

%build
%cmake
%cmake_build

%install
%cmake_install

# build the main config file from the example
install -Dm 644 %{buildroot}%{_sysconfdir}/rtl_433/rtl_433.example.conf %{buildroot}%{_sysconfdir}/rtl_433/rtl_433.conf

# Commenting these config options made more sensible defaults on my system
for C in \
    'pulse_detect squelch' \
    'pulse_detect magest' \
    'samples_to_read 0' \
    'analyze_pulses false' \
    'device        0' \
    'pulse_detect autolevel' \
    'report_meta level' \
    'report_meta noise' \
    'report_meta stats' \
    'report_meta time:usec' \
    'report_meta protocol' \
    'signal_grabber none' \
    'output json' \
    'convert si' \
    'stop_after_successful_events false' \
;do
    sed -i 's\^'"$C"'$\'#"$C"'\' %{buildroot}%{_sysconfdir}/rtl_433/rtl_433.conf
done

%check
%ctest

%files
%license COPYING
%doc AUTHORS *.md docs/*.md examples
%dir %{_sysconfdir}/rtl_433
%config(noreplace) %{_sysconfdir}/rtl_433/*.conf
%{_bindir}/rtl_433
%{_mandir}/man*/*

%files devel
%doc AUTHORS
%{_includedir}/rtl_433*.h

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 23.11-2.20240826gitf0ba153
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 09 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 23.11-1.20240826gitf0ba153
- bump to latest git release
- buildrequires libusb1-devel 

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 23.11-7.20240324gitc00aa10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.11-6.20240324gitc00aa10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 09 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 23.11-5.20240324gitc00aa10
- Rebuilt for new rtl-sdr

* Mon Mar 25 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 23.11-4.20240324gitc00aa10
- bump to latest git release
- sample config files are now installed under sysconfdir

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.11-3.20231218git60bdd62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.11-2.20231218git60bdd62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Andrew Bauer <zonexpertconsulting@outlook.com> - 23.11-1.20231218git60bdd62
- bump to latest git release

* Mon Nov 06 2023 Andrew Bauer <zonexpertconsulting@outlook.com> - 22.11-1.20231101git2a7fe21
- bump to latest git release

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2.20230714git37b804c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Andrew Bauer <zonexpertconsulting@outlook.com> - 22.11-1.20230714git37b804c
- bump to latest git release

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 21.12-6.20220401git8228f0d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12-5.20220401git8228f0d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Apr 17 2022 Andrew Bauer <zonexpertconsulting@outlook.com> - 21.12-4.20220401git8228f0d
- Move COPYING to license
- Run test suite

* Sun Apr 10 2022 Andrew Bauer <zonexpertconsulting@outlook.com> - 21.12-3.20220401git8228f0d
- Comment some of the config options makes for more sensible defaults
- Use install instead of cp for config file

* Fri Apr 08 2022 Andrew Bauer <zonexpertconsulting@outlook.com> - 21.12-2.20220401git8228f0d
- libusb obsoleted by libusb-compat-0.1 on f37 and newer

* Thu Apr 07 2022 Andrew Bauer <zonexpertconsulting@outlook.com> - 21.12-1.20220401git8228f0d
- Initial specfile based on altlinux pkg by Sergey Bolshakov <sbolshakov@altlinux.ru>

