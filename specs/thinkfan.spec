Name:          thinkfan
Version:       1.3.1
Release:       9%{?dist}
Summary:       A simple fan control program

License:       GPL-3.0-or-later
URL:           https://github.com/vmatare/thinkfan
Source0:       https://github.com/vmatare/thinkfan/archive/%{version}/%{name}-%{version}.tar.gz
Source1:       thinkfan.modprobe
Source2:       thinkfan.sysconfig

# Fix systemd service install directory
Patch0:        thinkfan_systemd.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: systemd-units
BuildRequires: libatasmart-devel
BuildRequires: yaml-cpp-devel
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
A simple fan control program. Works with any Linux hwmon driver, especially
with thinkpad_acpi. It is designed to eat as little CPU power as possible.


%prep
%autosetup -p1


%build
%cmake -DUSE_ATASMART:BOOL=ON
%cmake_build

%install
%cmake_install

# Install configuration file
install -Dpm 0644 examples/thinkfan.yaml %{buildroot}%{_sysconfdir}/thinkfan.conf

# Install modprobe configuration file
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/modprobe.d/thinkfan.conf

# Install sysconfig
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/thinkfan

# Installed through %%license
rm -f %{buildroot}/%{_pkgdocdir}/COPYING


%post
%systemd_post thinkfan.service

%preun
%systemd_preun thinkfan.service

%postun
%systemd_postun_with_restart thinkfan.service


%files
%license COPYING
%doc README.md
%doc %{_pkgdocdir}/thinkfan.yaml
%{_sbindir}/thinkfan
%{_unitdir}/thinkfan.service
%{_unitdir}/thinkfan-wakeup.service
%{_unitdir}/thinkfan-sleep.service
%config(noreplace) %{_sysconfdir}/sysconfig/thinkfan
%config(noreplace) %{_sysconfdir}/thinkfan.conf
%config(noreplace) %{_sysconfdir}/modprobe.d/thinkfan.conf
%{_mandir}/man1/thinkfan.1.*
%{_mandir}/man5/thinkfan.conf.5.*
%{_mandir}/man5/thinkfan.conf.legacy.5.*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 1.3.1-8
- Rebuild for yaml-cpp 0.8

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 08 2022 Richard Shaw <hobbes1069@gmail.com> - 1.3.1-3
- Rebuild for yaml-cpp 0.7.0.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb 07 2022 Sandro Mani <manisandro@gmail.com> - 1.3.1-1
- Update to 1.3.1

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 01 2021 Sandro Mani <manisandro@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Sandro Mani <manisandro@gmail.com> - 1.2.2-1
- Update to 1.2.2

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.1-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Sandro Mani <manisandro@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Sat Jun 06 2020 Sandro Mani <manisandro@gmail.com> - 1.2-1
- Update to 1.2

* Sat Apr 04 2020 Sandro Mani <manisandro@gmail.com> - 1.1-1
- Update to 1.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Sandro Mani <manisandro@gmail.com> - 1.0.2-6
- Also patch the thinkfan.service cmake template in thinkfan_systemd.patch

* Sun Nov 17 2019 Sandro Mani <manisandro@gmail.com> - 1.0.2-5
- Bump F31/F30 for yaml-cpp rebuild

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 1.0.2-4
- Adapt service file to use an EnvironmentFile instead of overrides.conf (#1763148)
- Pass -n in ExecStart and drop Type=forking

* Fri Oct 18 2019 Richard Shaw <hobbes1069@gmail.com> - 1.0.2-3
- Rebuild for yaml-cpp 0.6.3.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Sandro Mani <manisandro@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Mon Feb 04 2019 Sandro Mani <manisandro@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri May 06 2016 Sandro Mani <manisandro@gmail.com> - 0.9.3-1
- Update to 0.9.3

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 08 2015 Sandro Mani <manisandro@gmail.com> - 0.9.2-6
- Add patch for #1247034: setfan_ibm: Error writing to /proc/acpi/ibm/fan: Invalid argument

* Mon Oct 26 2015 Sandro Mani <manisandro@gmail.com> - 0.9.2-5
- Fix incorrectly installed sysconfig file

* Wed Oct 21 2015 Sandro Mani <manisandro@gmail.com> - 0.9.2-4
- Install sysconfig file (#1189976)
- Modernize spec

* Fri Oct 09 2015 Matt Spaulding <mspaulding06@gmail.com> - 0.9.2-3
- Add libatasmart support (RHBZ#1243367)
- Add config files to docs

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Dec 07 2014 Matt Spaulding <mspaulding06@gmail.com> - 0.9.2-1
- Update to latest upstream version

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 17 2013 Matt Spaulding <mspaulding06@gmail.com> - 0.8.1-5
- Fixed empty man pages
- Fixed config in wrong location (RHBZ#998110)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 01 2012 Matt Spaulding <mspaulding06@gmail.com> - 0.8.1-2
- Fixed license type
- Fixed manpages entry in files section

* Sat Sep 29 2012 Matt Spaulding <mspaulding06@gmail.com> - 0.8.1-1
- Initial packaging

