Name: btrfsmaintenance
Version: 0.5
Release: 9%{?dist}
Summary: Scripts for btrfs maintenance tasks
BuildArch: noarch

License: GPLv2+
URL: https://github.com/kdave/btrfsmaintenance
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: systemd-rpm-macros

Requires: btrfs-progs

Enhances: btrfs-progs

%description
Scripts for btrfs maintenance tasks like periodic scrub, balance, trim or
defrag on selected mountpoints or directories. 

This is a set of scripts supplementing the btrfs filesystem and aims to
automate a few maintenance tasks. This means the scrub, balance, trim or
defragmentation.

Each of the tasks can be turned on/off and configured independently. The
default config values were selected to fit the default installation profile
with btrfs on the root filesystem.

Overall tuning of the default values should give a good balance between
effects of the tasks and low impact of other work on the system. If this does
not fit your needs, please adjust the settings.


%prep
%autosetup -p1


%install
# Scripts
install -Dpm755 btrfs-defrag.sh -t %{buildroot}%{_datadir}/%{name}
install -Dpm755 btrfs-balance.sh -t %{buildroot}%{_datadir}/%{name}
install -Dpm755 btrfs-scrub.sh -t %{buildroot}%{_datadir}/%{name}
install -Dpm755 btrfs-trim.sh -t %{buildroot}%{_datadir}/%{name}
install -Dpm755 %{name}-refresh-cron.sh -t %{buildroot}%{_datadir}/%{name}
install -Dpm755 %{name}-functions -t %{buildroot}%{_datadir}/%{name}

# Systemd services and timers
install -Dpm644 %{name}-refresh.service -t %{buildroot}%{_unitdir}
install -Dpm644 %{name}-refresh.path -t %{buildroot}%{_unitdir}
install -Dpm644 btrfs-balance.service -t %{buildroot}%{_unitdir}
install -Dpm644 btrfs-defrag.service -t %{buildroot}%{_unitdir}
install -Dpm644 btrfs-scrub.service -t %{buildroot}%{_unitdir}
install -Dpm644 btrfs-trim.service -t %{buildroot}%{_unitdir}
install -Dpm644 btrfs-balance.timer -t %{buildroot}%{_unitdir}
install -Dpm644 btrfs-defrag.timer -t %{buildroot}%{_unitdir}
install -Dpm644 btrfs-scrub.timer -t %{buildroot}%{_unitdir}
install -Dpm644 btrfs-trim.timer -t %{buildroot}%{_unitdir}

# Config
install -Dpm644 sysconfig.%{name} %{buildroot}%{_sysconfdir}/sysconfig/%{name}


%post
%systemd_post %{name}-refresh.service %{name}-refresh.path btrfs-balance.service btrfs-balance.timer btrfs-defrag.service btrfs-defrag.timer btrfs-scrub.service btrfs-scrub.timer btrfs-trim.service btrfs-trim.timer

%preun
%systemd_preun %{name}-refresh.service %{name}-refresh.path btrfs-balance.service btrfs-balance.timer btrfs-defrag.service btrfs-defrag.timer btrfs-scrub.service btrfs-scrub.timer btrfs-trim.service btrfs-trim.timer

%postun
%systemd_postun_with_restart %{name}-refresh.service %{name}-refresh.path btrfs-balance.service btrfs-balance.timer btrfs-defrag.service btrfs-defrag.timer btrfs-scrub.service btrfs-scrub.timer btrfs-trim.service btrfs-trim.timer


%files
%license COPYING
%doc README.md
%{_datadir}/%{name}/
%{_unitdir}/%{name}-refresh.path
%{_unitdir}/%{name}-refresh.service
%{_unitdir}/btrfs-balance.service
%{_unitdir}/btrfs-balance.timer
%{_unitdir}/btrfs-defrag.service
%{_unitdir}/btrfs-defrag.timer
%{_unitdir}/btrfs-scrub.service
%{_unitdir}/btrfs-scrub.timer
%{_unitdir}/btrfs-trim.service
%{_unitdir}/btrfs-trim.timer
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 29 12:46:07 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5-1
- Initial package
