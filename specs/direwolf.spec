Name:           direwolf
Version:        1.7
Release:        6%{?dist}
Summary:        Sound Card-based AX.25 TNC

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/wb2osz/direwolf/
# This is the actual source
Source0:        https://github.com/wb2osz/direwolf/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        direwolf.service
Source2:        direwolf.sysconfig
Source3:        direwolf.logrotate

ExcludeArch:    i686

BuildRequires:  gcc gcc-c++
BuildRequires:  cmake
BuildRequires:  glibc-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  gpsd-devel
BuildRequires:  hamlib-devel
BuildRequires:  systemd systemd-devel

Requires:       ax25-tools ax25-apps
Requires(pre):  shadow-utils


%description
Dire Wolf is a modern software replacement for the old 1980's style
TNC built with special hardware.  Without any additional software, it
can perform as an APRS GPS Tracker, Digipeater, Internet Gateway
(IGate), APRStt gateway. It can also be used as a virtual TNC for
other applications such as APRSIS32, UI-View32, Xastir, APRS-TW, YAAC,
UISS, Linux AX25, SARTrack, Winlink Express, BPQ32, Outpost PM, and many
others.


%prep
%autosetup -p 1


%build
%cmake -DUNITTEST=1 -DENABLE_GENERIC=1
%cmake_build

%check
%ctest


%install
%cmake_install

# Install service file
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
cp %{SOURCE1} ${RPM_BUILD_ROOT}%{_unitdir}/%{name}.service

# Install service config file
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
cp %{SOURCE2} ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{name}

# Install logrotate config file
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
cp %{SOURCE3} ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}

# copy config file
cp ${RPM_BUILD_ROOT}%{_pkgdocdir}/conf/%{name}.conf ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}.conf

# Make log directory
mkdir -m 0755 -p ${RPM_BUILD_ROOT}/var/log/%{name}

# Move udev rules to system dir
mkdir -p ${RPM_BUILD_ROOT}%{_udevrulesdir}
mv ${RPM_BUILD_ROOT}%{_sysconfdir}/udev/rules.d/99-direwolf-cmedia.rules ${RPM_BUILD_ROOT}%{_udevrulesdir}/99-direwolf-cmedia.rules

# Copy doc pngs
cp direwolf-block-diagram.png ${RPM_BUILD_ROOT}%{_pkgdocdir}/direwolf-block-diagram.png
cp tnc-test-cd-results.png    ${RPM_BUILD_ROOT}%{_pkgdocdir}/tnc-test-cd-results.png

# remove extraneous files
# This is not a desktop application, per the guidelines.  Running it in a terminal
# does not make it a desktop application.
rm ${RPM_BUILD_ROOT}/usr/share/applications/direwolf.desktop
rm ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/direwolf_icon.png
rm ${RPM_BUILD_ROOT}%{_pkgdocdir}/CHANGES.md
rm ${RPM_BUILD_ROOT}%{_pkgdocdir}/LICENSE
rm ${RPM_BUILD_ROOT}%{_pkgdocdir}/README.md

# remove Windows external library directories
rm -r ${RPM_BUILD_ROOT}%{_pkgdocdir}/external

# Move Telemetry Toolkit sample scripts into docs
mkdir -p ${RPM_BUILD_ROOT}%{_pkgdocdir}/telem/
mv ${RPM_BUILD_ROOT}%{_bindir}/telem* ${RPM_BUILD_ROOT}%{_pkgdocdir}/telem/
chmod 0644 ${RPM_BUILD_ROOT}%{_pkgdocdir}/telem/*


%package -n %{name}-doc
Summary:        Documentation for Dire Wolf
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description -n %{name}-doc
Dire Wolf is a modern software replacement for the old 1980's style
TNC built with special hardware.  Without any additional software, it
can perform as an APRS GPS Tracker, Digipeater, Internet Gateway
(IGate), APRStt gateway. It can also be used as a virtual TNC for
other applications such as APRSIS32, UI-View32, Xastir, APRS-TW, YAAC,
UISS, Linux AX25, SARTrack, RMS Express, BPQ32, Outpost PM, and many
others.


%files
%license LICENSE
%{_udevrulesdir}/99-direwolf-cmedia.rules
%{_bindir}/* 
%{_mandir}/man1/*
%{_datadir}/%{name}/*
%dir %{_pkgdocdir}
%{_pkgdocdir}/conf/*
%{_pkgdocdir}/scripts/*
%{_pkgdocdir}/telem/*
%{_unitdir}/%{name}.service
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/%{name}.conf
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/logrotate.d/%{name}
%dir %attr(0755, %{name}, %{name}) /var/log/%{name}

%files -n %{name}-doc
%{_pkgdocdir}/*.pdf
%{_pkgdocdir}/*.png

# At install, create a user in group audio (so can open sound card device files)
# and in group dialout (so can open serial device files)
%pre
getent group direwolf >/dev/null || groupadd -r direwolf
getent passwd direwolf >/dev/null || \
    useradd -r -g audio -G audio,dialout -d %{_datadir}/%{name} -s /sbin/nologin \
	    -c "Direwolf Sound Card-based AX.25 TNC" direwolf
exit 0


%changelog
* Tue Dec 31 2024 Richard Shaw <hobbes1069@gmail.com> - 1.7-6
- Rebuild for Hamlib 4.6.

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 31 2023 Richard Shaw <hobbes1069@gmail.com> - 1.7-1
- Update to 1.7, for details see:
  https://github.com/wb2osz/direwolf/releases/tag/1.7

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 24 2023 Adam Williamson <awilliam@redhat.com> - 1.6.0-18
- rebuild for new libgps

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 07 2022 Richard Shaw <hobbes1069@gmail.com> - 1.6.0-16
- Rebuild for updated hamlib 4.5.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Richard Shaw <hobbes1069@gmail.com> - 1.6.0-14
- Rebuild for gpsd 3.24.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 1.6.0-12
- Rebuild for hamlib 4.4.

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 1.6.0-10
- Rebuild for hamlib 4.4.

* Tue Oct 12 2021 Richard Shaw <hobbes1069@gmail.com> - 1.6.0-9
- Rebuild for hamlib 4.3.1.

* Wed Aug 11 2021 Björn Esser <besser82@fedoraproject.org> - 1.6.0-8
- Rebuild (gpsd)
- Add patch for gpsapi12

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 30 2021 Richard Shaw <hobbes1069@gmail.com> - 1.6.0-6
- Rebuild for hamlib 4.2.

* Tue Feb 02 2021 Richard Shaw <hobbes1069@gmail.com> - 1.6.0-5
- Rebuild for hamlib 4.1.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Matt Domsch <matt@domsch.com> - 1.6.0-3
- rebuild for gpsd-3.22 soname bump

* Tue Nov  3 2020 Matt Domsch <matt@domsch.com> - 1.6.0-2
- Add upstream patch for https://github.com/wb2osz/direwolf/issues/296

* Thu Oct 29 2020 Matt Domsch <matt@domsch.com> - 1.6.0-1
- Upstream 1.6.0 release
- use cmake macros

* Fri Jul 3 2020 Matt Domsch <matt@domsch.com> - 1.6-0.5
- AIS decoding, FX.25 error checking bits set automatically
- GPSD API 10 support

* Thu Apr 30 2020 Matt Domsch <matt@domsch.com> - 1.6-0.4
- copr rebuild for F32 hamlib 4.0

* Mon Apr 20 2020 Matt Domsch <matt@domsch.com> - 1.6-0.3
- drop unneeded BR libax25-devel

* Mon Apr 20 2020 Matt Domsch <matt@domsch.com> - 1.6-0.2
- write stdout/err to /var/log/direwolf, logrotate 30 days.
- run ctest
- remove CPU instruction tests, leave architecture choice up to the distro

* Sun Apr 19 2020 Matt Domsch <matt@domsch.com> - 1.6-0.1
- upstream 1.6 prerelease
- drop obsolete patches, use cmake
- add systemd startup, direwolf user

* Tue Mar 31 2020 Richard Shaw <hobbes1069@gmail.com> - 1.5-6
- Rebuild for hamlib 4.

* Thu Feb 20 2020 Matt Domsch <matt@domcsh.com> - 1.5-5
- Remove unneeded dependency on python2-devel (#1805225)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Björn Esser <besser82@fedoraproject.org> - 1.5-2
- Rebuild (gpsd)

* Sun Feb 17 2019 Matt Domsch <matt@domsch.com> - 1.5-1
- Upgrade to released version 1.5
- Apply upstream patch for newer gpsd API

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.2.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 27 2018 Matt Domsch <matt@domsch.com> - 1.5-0.1.beta4
- Fedora Packaging Guidelines, based on spec by David Ranch
  Moved Telemetry Toolkit examples into examples/ docs.
