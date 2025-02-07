%global gittag 1.7.0
Name:           tlp
Version:        1.7.0
Release:        3%{?dist}
Summary:        Optimize laptop battery life
License:        GPL-2.0-or-later
URL:            https://linrunner.de/tlp
Source0:        https://github.com/linrunner/TLP/archive/%{gittag}.tar.gz#/%{name}-%{gittag}.tar.gz

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  systemd
BuildRequires:  libappstream-glib

#The following requires are not detected:
Requires:       ethtool
Requires:       hdparm
Requires:       iw
Requires:       rfkill
Requires:       systemd
Requires:       udev
Requires:       usbutils
Requires:       pciutils
Recommends:     kernel-tools
Recommends:     smartmontools

#Note: Conflicts with laptop-mode-tools
#Makes sure laptop_mode isn't being used:
Conflicts:      %{_sbindir}/laptop_mode
BuildArch:      noarch

%description
TLP is a feature-rich command-line utility, saving laptop battery power
without the need to delve deeper into technical details.

TLP’s default settings are already optimized for battery life and implement
Powertop’s recommendations out of the box. Moreover TLP is highly
customizable to fulfil specific user requirements.

Settings are organized into two profiles, allowing to adjust between
savings and performance independently for battery (BAT) and AC operation.
In addition TLP can enable or disable Bluetooth, NFC, Wi-Fi and WWAN radio
devices on boot.

For ThinkPads and selected other laptops it provides a unified way
to configure charge thresholds and recalibrate the battery.

%package rdw
Summary:        Radio device wizard for TLP
Requires:       NetworkManager >= 1.20
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description rdw
Radio device wizard is an add-on to TLP. It provides event based
switching of bluetooth, NFC, Wi-Fi and WWAN radio devices on:
 - network connect/disconnect
 - dock/undock

%prep
%autosetup -n TLP-%{gittag}

%build
%make_build

%install
%make_install \
  TLP_SDSL=%{_unitdir}/../system-sleep \
  TLP_NO_INIT=1 \
  TLP_WITH_ELOGIND=0 \
  TLP_SYSD=%{_unitdir} \
  TLP_ULIB=%{_udevrulesdir}/.. \
  TLP_SBIN=%{_bindir}

#Install manpages:
make install-man DESTDIR=%{buildroot}
make install-man-rdw DESTDIR=%{buildroot}

%check
appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/metainfo/*.xml

%files
%config(noreplace) %{_sysconfdir}/tlp.conf
%config(noreplace) %{_sysconfdir}/tlp.d
%license LICENSE
%doc AUTHORS COPYING README.rst changelog
%{_bindir}/*
%exclude %{_bindir}/tlp-rdw
%{_mandir}/man*/*
%exclude %{_mandir}/man*/tlp-rdw*
%{_datadir}/tlp
%{_udevrulesdir}/85-tlp.rules
%{_udevrulesdir}/../tlp-usb-udev
%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/*
%{_datadir}/fish/vendor_completions.d/*
%exclude %{_datadir}/bash-completion/completions/tlp-rdw
%exclude %{_datadir}/zsh/site-functions/_tlp-radio-device
%exclude %{_datadir}/zsh/site-functions/_tlp-rdw
%exclude %{_datadir}/fish/vendor_completions.d/tlp-rdw.fish
%{_unitdir}/*.service
%{_unitdir}/../system-sleep
%{_datadir}/metainfo/*.metainfo.xml
%{_sharedstatedir}/tlp

%files rdw
%doc AUTHORS COPYING README.rst changelog
%{_bindir}/tlp-rdw
%{_mandir}/man*/tlp-rdw*
%{_prefix}/lib/NetworkManager/dispatcher.d/99tlp-rdw-nm
%{_udevrulesdir}/85-tlp-rdw.rules
%{_udevrulesdir}/../tlp-rdw-udev
%{_datadir}/bash-completion/completions/tlp-rdw
%{_datadir}/zsh/site-functions/_tlp-radio-device
%{_datadir}/zsh/site-functions/_tlp-rdw
%{_datadir}/fish/vendor_completions.d/tlp-rdw.fish

%post
%systemd_post tlp.service
if [ $1 -eq 2 ] ; then
    systemctl unmask systemd-rfkill.service
    systemctl unmask power-profiles-daemon.service
fi

%preun
%systemd_preun tlp.service

%postun
%systemd_postun_with_restart tlp.service

%changelog
* Wed Feb 05 2025 Sergi Jimenez <tripledes@fedoraproject.org> - 1.7.0-3
- Fix RHBZ#2341445

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Sep 28 2024 Sergi Jimenez <tripledes@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Sun Aug 11 2024 Sergi Jimenez <tripledes@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.0-4
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 29 2023 Sergi Jimenez <tripledes@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 1.5.0-2
- More fixes for RHBZ#2028701

* Fri Jan 7 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 1.5.0-1
- Update to 1.5.0

* Fri Jan 7 2022 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.4.0-3
- Fix some minor issues based on upstream feedback
- Fix fesco issue 2725, RHBZ#2028701

* Tue Oct 5 2021 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.4.0-2
- Drop lsb-release dependency (not needed)

* Sat Oct 2 2021 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.4.0-1
- Update to 1.4.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.1-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 6 2020 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.3.1-1
- Update to 1.3.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.3.beta.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 1.3.0-0.2.beta.3
- Drop sleep service scriptlets, as they were dropped in 1.3.0

* Fri Jan 17 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 1.3.0-0.1.beta.3
- Update to 1.3.0 beta 3

* Fri Jan 3 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 1.2.2-4
- Fix suspend issue, missing var directory creation

* Thu Aug 22 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.2.2-3
- Move the NetworkManager dispatcher script out of /etc

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Jeremy Newton <alexjnewt at hotmail dot com> - 1.2.2-1
- Update to 1.2.2

* Mon Mar 18 2019 Jeremy Newton <alexjnewt at hotmail dot com> - 1.2.1-1
- Update to 1.2.1
- Modernize SPEC file

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 1.1-1
- Update to 1.1
- Add weak require for kernel-tools

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 03 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0-3
- Remove kernel-tools require, fixes s390x

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0-1
- Update to 1.0

* Mon Mar 20 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 0.9-5
- Cherry-pick upstream fix for mitigate slow shutdown

* Thu Mar 02 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 0.9-4
- Cherry-pick upstream fix for tlp-stat

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 0.9-2
- Fix rfkill service masking

* Sun Aug 28 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 0.9-1
- Update to 0.9

* Wed Feb 24 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 0.8-3
- Fix rpmlint warnings/errors

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 22 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 0.8-1
- Update to 0.8

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 11 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 0.7-4
- Use workaround to avoid conflict with systemd

* Mon May 11 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 0.7-3
- Fix rfkill conflict

* Tue Feb 3 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 0.7-2
- Fix a typo in the spec file

* Sat Jan 31 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 0.7-1
- New Version

* Mon Nov 17 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 0.6-3
- Wireless-tools removed as a dependency

* Tue Nov 04 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 0.6-2
- Missing Dependancy

* Mon Oct 27 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 0.6-1
- New Upstream Version

* Mon Apr 21 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 0.5-2
- Various tweaking
- Move bashcompletion file to silence rpmlint warning

* Sun Apr 20 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 0.5-1
- Initial fedora package
