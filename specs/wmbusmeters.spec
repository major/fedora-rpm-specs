%global with_tag 1

Name:                  wmbusmeters
%global forgeurl       https://github.com/weetmuts/%{name}

%if %{with_tag}
%global tag            1.18.0
Version:               %{tag}
%else
%global date           20210813
%global commit         8dd3e87c44ecb2e3fc46f7bc6df9ea6195c8b988
Version:               1.4.0
%endif

%forgemeta

Release:               3%{?dist}
Summary:               Read the wireless mbus protocol to acquire utility meter readings
License:               GPL-3.0-or-later
Url:                   %{forgeurl}
Source0:               %{forgesource}
# Default configuration file
# Stores all logs in journald
Source1:               file://%{name}.conf
# Systemd service file
Source2:               file://%{name}.service

BuildRequires:         /usr/bin/git
BuildRequires:         /usr/bin/make
BuildRequires:         gcc-c++
BuildRequires:         systemd-rpm-macros
BuildRequires:         pkgconfig(ncurses)
BuildRequires:         pkgconfig(librtlsdr)
BuildRequires:         pkgconfig(libusb-1.0)
BuildRequires:         pkgconfig(libxml-2.0)

Requires:              rtl-wmbus >= 0-18


%description
The program receives and decodes C1,T1 or S1 telegrams
(using the wireless mbus protocol) to acquire utility meter readings.
The readings can then be published using MQTT, curled to a REST api,
inserted into a database or stored in a log file.


%prep
%forgeautosetup -S git
# For https://fedoraproject.org/wiki/Changes/Unify_bin_and_sbin
# Unfortunately other distros does not have similar plan so we cannot
# upstream the change for now.
sed -i 's#/sbin#/bin#g' scripts/install_binaries.sh


%build
%set_build_flags
%{make_build} STRIP=true COMMIT_HASH="" TAG=%{version} COMMIT=%{version} \
    TAG_COMMIT=%{version}%{distprefix} CHANGES=""


%install
%set_build_flags
%{make_install} STRIP=true COMMIT_HASH="" TAG=%{version} COMMIT=%{version} \
    TAG_COMMIT=%{version} CHANGES="" \
    DESTDIR=%{buildroot} EXTRA_INSTALL_OPTIONS="--no-adduser"

# We are using journald
rm -rf %{buildroot}%{_sysconfdir}/logrotate.d/

# Create directory for storing pid files.
install -m 0755 -d %{buildroot}/%{_rundir}/%{name}/

# Fix systemd unit dir location
mv %{buildroot}/lib %{buildroot}/%{_prefix}

# We are installing template version
rm -f %{buildroot}%{_unitdir}/%{name}.service

# Install default configuration file
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}.conf

# Install systemd service file
install -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service


%files
%license LICENSE
%doc README.md CHANGES HowToAddaNewMeter.txt
%dir %{_sysconfdir}/%{name}.d/
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/wmbusmetersd
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_mandir}/man1/%{name}*
%ghost %{_rundir}/%{name}/


%post
%systemd_post %{name}.service
 
%preun
%systemd_preun %{name}.service
 
%postun
%systemd_postun_with_restart %{name}.service


%changelog
* Tue Jan 21 2025 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.18.0-3
- Fix FTBFS on F42.

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 05 2024 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.18.0-1
- Update to 1.18.0 (rhbz#2329228)

* Mon Oct 07 2024 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.17.1-2
- Rebuilt for updated license tag

* Thu Sep 12 2024 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.17.1-1
- Update to 1.17.1 (rhbz#2307772)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 05 2024 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.16.1-2
- Rebuild for rtl-sdr-2.0 (rhbz#2273601)

* Fri Feb 23 2024 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.16.1-1
- Update to 1.16.1 (rhbz#2264357)
- Switch to use pkgconfig for BuildRequires
- Specify Require for rtl-wmbus which supports needed -f option

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 07 2023 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.14.0-1
- Update to 1.14.0 (rhbz#2219146)

* Mon May 08 2023 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.13.0-1
- Update to 1.13.0 (rhbz#2196040)

* Mon Mar 13 2023 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.12.0-1
- Update to 1.12.0 (rhbz#2177567)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.11.0-1
- Update to 1.11.0 (rhbz#2156910)

* Fri Dec 09 2022 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.10.1-1
- Update to 1.10.1 (rhbz#2151407)

* Wed Sep 14 2022 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.9.0-1
- Update to 1.9.0 (rhbz#2124324)
- Drop patch merged upstream

* Tue Jul 26 2022 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.8.0-4
- Fix FTBFS on F37

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.8.0-2
- Update to 1.8.0 (rhbz#2101195)
- Update change log

* Mon Jun 27 2022 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.8.0-1
- Update to 1.7.0 (rhbz#2101195)

* Wed Apr 06 2022 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.7.0-1
- Update to 1.7.0 (rhbz#2069461)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.6.0-1
- Update to 1.6.0 (rhbz#2020903)

* Tue Nov 09 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.5.0-1
- Update to 1.5.0 (rhbz#2020903)

* Tue Aug 31 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.4.1-1
- Update to 1.4.1

* Fri Aug 13 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.4.0-2
- Update to the latest snapshot (fixes compilation errors)

* Thu Aug 12 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.4.0-1
- Update to 1.4.0 (#1991762)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 31 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.3.0-1
- Update to 1.3.0 (#1936290)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.0-6
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Feb 22 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.1.0-5
- Update to 1.1.0 (#1922583),
- Remove duplicate BR for make.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.4-2
- Switch (as per upstream) to non template unit file

* Mon Dec 07 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.4-1
- Update to the latest available version

* Sat Oct 31 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.36-2
- Allows to build non-released versions

* Tue Sep 08 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.36-1
- Update to the latest available version

* Mon Aug 31 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.35-1
- Update to the latest available version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.32-1
- Update to the latest available version

* Mon May 25 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.31-2
- Add missing ncurses-devel BR

* Mon May 25 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.31-1
- Update to the latest available version

* Thu Apr 23 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.30-1
- Update to the latest available version

* Fri Apr 03 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.29-1
- Update to the latest available version

* Tue Mar 24 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.28-1
- Update to the latest available version
- Drop patches upstream merged

* Mon Mar 23 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.27-6
- Remove -v from the forgemeta
- Remove instead of exclude logrotate.d directory
- Use %%{_prefix} instead of /usr
- Add %%systemd_{*} scriplets

* Wed Mar 04 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.27-5
- Add creation of /run/wmbusmeters dir. to the service file.

* Tue Mar 03 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.27-4
- Use %%set_build_flags

* Tue Mar 03 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.27-3
- Fix wmbusmeters.d accessability
- Store all logs in journald

* Mon Mar 02 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.27-2
- Add upstream reference to pathces.

* Fri Feb 28 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.27-1
- Initial RPM release.
