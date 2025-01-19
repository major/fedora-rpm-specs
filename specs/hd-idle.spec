Name:           hd-idle
Version:        1.05
Release:        23%{?dist}
Summary:        Spin down idle [USB] hard disks

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://hd-idle.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
Source1:        %{name}.service
Source2:        %{name}.default

Patch0:         %{name}-systemd-nodaemon.diff

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd

%description
hd-idle is a utility program for spinning-down external disks after a period
of idle time. Since most external IDE disk enclosures don't support setting
the IDE idle timer, a program like hd-idle is required to spin down idle disks
automatically.

A word of caution: hard disks don't like spinning up too often. Laptop disks
are more robust in this respect than desktop disks but if you set your disks
to spin down after a few seconds you may damage the disk over time due to the
stress the spin-up causes on the spindle motor and bearings. It seems that
manufacturers recommend a minimum idle time of 3-5 minutes, the default in
hd-idle is 10 minutes.

One more word of caution: hd-idle will spin down any disk accessible via the
SCSI layer (USB, IEEE1394, ...) but it will not work with real SCSI disks
because they don't spin up automatically. Thus it's not called scsi-idle and
I don't recommend using it on a real SCSI system unless you have a kernel
patch that automatically starts the SCSI disks after receiving a sense buffer
indicating the disk has been stopped. Without such a patch, real SCSI disks
won't start again and you can as well pull the plug.


%prep
%autosetup -n %{name} -p1
sed -i 's/install -D -g root -o root/install -D/' Makefile


%build
%set_build_flags
%make_build


%install
%make_install

# Remove executable bit from manual page
find "%{buildroot}%{_mandir}" -executable -type f -exec chmod -x {} \;

install -dpm 0755 %{buildroot}%{_unitdir}
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_unitdir}
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%license LICENSE
%doc README
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_unitdir}/*.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.05-22
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 08 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.05-13
- feat: Add hd-idle-systemd-nodaemon patch which allow to writes logs into
  journald instead of plain text file

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.05-12
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Samuel Rakitničan <samuel.rakitnican@gmail.com> 1.05-4
- Add requirement on logrotate and systemd
- Remove executable bit from manual page
- Use macro for systemd with correct post/preun/postun Requires tags

* Wed Aug 02 2017 Samuel Rakitničan <samuel.rakitnican@gmail.com> 1.05-3
- Use %%{optflags} macro

* Wed Aug 02 2017 Samuel Rakitničan <samuel.rakitnican@gmail.com> 1.05-2
- Use macros for building and installing
- Add gcc build requirement

* Sun Feb 26 2017 Samuel Rakitničan <samuel.rakitnican@gmail.com> 1.05-1
- Initialize
