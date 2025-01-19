Name:       mbpfan
Version:    2.4.0
Release:    7%{?dist}
Summary:    A simple daemon to control fan speed on all MacBook/MacBook Pros
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:    GPL-3.0-only
URL:        https://github.com/linux-on-mac/mbpfan
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros

ExclusiveArch:  x86_64

%description
This is an enhanced version of Allan McRae mbpfan

mbpfan is a daemon that uses input from coretemp module and sets the
fan speed using the applesmc module. This enhanced version assumes any
number of processors and fans (max. 10).

* It only uses the temperatures from the processors as input.
* It requires coretemp and applesmc kernel modules to be loaded.
* It requires root use
* It daemonizes or stays in foreground
* Verbose mode for both syslog and stdout
* Users can configure it using the file /etc/mbpfan.conf

%prep
%setup -q

%build
%set_build_flags
%make_build

%install
# Installing the binaries
install -Dpm 0755 -t %{buildroot}%{_sbindir}/ bin/%{name}
install -Dpm 0755 -t %{buildroot}%{_sbindir}/ bin/%{name}-tests

# Installing the systemd service
install -Dpm 0644 -t %{buildroot}%{_unitdir}/ %{name}.service

# Installing the configuration file
install -Dpm 0644 -t %{buildroot}/etc/ %{name}.conf

# Installing the manual
install -Dpm 0644 -t %{buildroot}%{_mandir}/man8/ %{name}.8.gz

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%{_sbindir}/%{name}
%{_sbindir}/%{name}-tests
%{_unitdir}/%{name}.service
%{_mandir}/man8/mbpfan.8.*
%config(noreplace) /etc/%{name}.conf
%doc README.md AUTHORS
%license COPYING

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.0-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 07 2023 Lyes Saadi <fedora@lyes.eu> - 2.4.0-1
- Updating to 2.4.0 (fix #2183803)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Mar 06 2022 Lyes Saadi <fedora@lyes.eu> - 2.3.0-1
- Updating to 2.3.0 (fix #2061113)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.1-6
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Lyes Saadi <fedora@lyes.eu> - 2.2.1-2
- Improving the spec file, thanks to Robert-André Mauchin:
  - Adding Systemd scriptlets to automatically enable the mbpfan service.
  - Adding Fedora's build flags.
  - Ensuring that installed files are not executables.


* Sun Nov 24 2019 Lyes Saadi <fedora@lyes.eu> - 2.2.1-1
- Updating to 2.2.1.
- For additional information, see https://github.com/linux-on-mac/mbpfan/releases/tag/v2.2.1

* Sat Nov 09 2019 Lyes Saadi <fedora@lyes.eu> - 2.2.0-3
- Improving the spec file, thanks to Dominik 'Rathann' Mierzejewski.

* Fri Nov 01 2019 Lyes Saadi <fedora@lyes.eu> - 2.2.0-2
- Making the spec file compliant to Fedora Packaging Guidelines.
- Adding manpages.

* Fri Nov 01 2019 Lyes Saadi <fedora@lyes.eu> - 2.2.0-1
- Updating to 2.2.0.
- For additional information, see https://github.com/linux-on-mac/mbpfan/releases/tag/v2.2.0

* Fri Oct 04 2019 Lyes Saadi <fedora@lyes.eu> - 2.1.1-2
- Adding path for systemd.

* Thu Oct 03 2019 Lyes Saadi <fedora@lyes.eu> - 2.1.1-1
- Creating the spec file.
