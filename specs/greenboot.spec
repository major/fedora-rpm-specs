%global debug_package %{nil}

Name:               greenboot
Version:            0.15.7
Release:            2%{?dist}
Summary:            Generic Health Check Framework for systemd
License:            LGPL-2.1-or-later

%global repo_owner  fedora-iot
%global repo_name   %{name}
%global repo_tag    v%{version}

URL:                https://github.com/%{repo_owner}/%{repo_name}
Source0:            https://github.com/%{repo_owner}/%{repo_name}/archive/%{repo_tag}.tar.gz

ExcludeArch: s390x
BuildRequires:      systemd-rpm-macros
%{?systemd_requires}
Requires:           systemd >= 240
Requires:           grub2-tools-minimal
Requires:           rpm-ostree
# PAM is required to programatically read motd messages from /etc/motd.d/*
# This causes issues with RHEL-8 as the fix isn't there an el8 is on pam-1.3.x
Requires:           pam >= 1.4.0
# While not strictly necessary to generate the motd, the main use-case of this package is to display it on SSH login
Recommends:         openssh
Provides:           greenboot-auto-update-fallback
Obsoletes:          greenboot-auto-update-fallback <= 0.12.0
Provides:           greenboot-grub2
Obsoletes:          greenboot-grub2 <= 0.12.0
Provides:           greenboot-reboot
Obsoletes:          greenboot-reboot <= 0.12.0
Provides:           greenboot-status
Obsoletes:          greenboot-status <= 0.12.0
Provides:           greenboot-rpm-ostree-grub2
Obsoletes:          greenboot-rpm-ostree-grub2 <= 0.12.0

%description
%{summary}.

%package default-health-checks
Summary:            Series of optional and curated health checks
Requires:           %{name} = %{version}-%{release}
Requires:           util-linux
Requires:           jq
Provides:           greenboot-update-platforms-check
Obsoletes:          greenboot-update-platforms-check <= 0.12.0

%description default-health-checks
%{summary}.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_exec_prefix}/lib/motd.d/
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/check/required.d
mkdir    %{buildroot}%{_sysconfdir}/%{name}/check/wanted.d
mkdir    %{buildroot}%{_sysconfdir}/%{name}/green.d
mkdir    %{buildroot}%{_sysconfdir}/%{name}/red.d
mkdir -p %{buildroot}%{_prefix}/lib/%{name}/check/required.d
mkdir    %{buildroot}%{_prefix}/lib/%{name}/check/wanted.d
mkdir    %{buildroot}%{_prefix}/lib/%{name}/green.d
mkdir    %{buildroot}%{_prefix}/lib/%{name}/red.d
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_unitdir}/greenboot-healthcheck.service.d
mkdir -p %{buildroot}%{_tmpfilesdir}
install -DpZm 0755 usr/libexec/greenboot/* %{buildroot}%{_libexecdir}/%{name}
install -DpZm 0644 usr/lib/motd.d/boot-status %{buildroot}%{_exec_prefix}/lib/motd.d/boot-status
install -DpZm 0644 usr/lib/systemd/system/greenboot-healthcheck.service.d/10-network-online.conf %{buildroot}%{_unitdir}/greenboot-healthcheck.service.d/10-network-online.conf
install -DpZm 0644 usr/lib/systemd/system/*.target %{buildroot}%{_unitdir}
install -DpZm 0644 usr/lib/systemd/system/*.service %{buildroot}%{_unitdir}
install -DpZm 0644 usr/lib/tmpfiles.d/greenboot-status-motd.conf %{buildroot}%{_tmpfilesdir}/greenboot-status-motd.conf
install -DpZm 0755 usr/lib/greenboot/check/required.d/* %{buildroot}%{_prefix}/lib/%{name}/check/required.d
install -DpZm 0755 usr/lib/greenboot/check/wanted.d/* %{buildroot}%{_prefix}/lib/%{name}/check/wanted.d
install -DpZm 0644 etc/greenboot/greenboot.conf %{buildroot}%{_sysconfdir}/%{name}/greenboot.conf
install -DpZm 0644 etc/grub.d/greenboot.cfg %{buildroot}%{_sysconfdir}/grub.d/greenboot.cfg

%post
%systemd_post greenboot-healthcheck.service
%systemd_post greenboot-loading-message.service
%systemd_post greenboot-task-runner.service
%systemd_post redboot-task-runner.service
%systemd_post redboot.target
%systemd_post greenboot-status.service
%systemd_post greenboot-grub2-set-counter.service
%systemd_post greenboot-grub2-set-success.service
%systemd_post greenboot-rpm-ostree-grub2-check-fallback.service
%systemd_post redboot-auto-reboot.service
if [ -d /usr/lib/bootupd/grub2-static/configs.d ]; then
cp /etc/grub.d/greenboot.cfg /usr/lib/bootupd/grub2-static/configs.d
fi

%post default-health-checks
%systemd_post greenboot-loading-message.service

%preun
%systemd_preun greenboot-healthcheck.service
%systemd_preun greenboot-loading-message.service
%systemd_preun greenboot-task-runner.service
%systemd_preun redboot-task-runner.service
%systemd_preun redboot.target
%systemd_preun greenboot-status.service
%systemd_preun greenboot-grub2-set-counter.service
%systemd_preun greenboot-grub2-set-success.service
%systemd_preun greenboot-rpm-ostree-grub2-check-fallback.service

%preun default-health-checks
%systemd_preun greenboot-loading-message.service

%postun
%systemd_postun greenboot-healthcheck.service
%systemd_postun greenboot-loading-message.service
%systemd_postun greenboot-task-runner.service
%systemd_postun redboot-task-runner.service
%systemd_postun redboot.target
%systemd_postun greenboot-status.service
%systemd_postun greenboot-grub2-set-counter.service
%systemd_postun greenboot-grub2-set-success.service
%systemd_postun greenboot-rpm-ostree-grub2-check-fallback.service
if [ -f /usr/lib/bootupd/grub2-static/configs.d/greenboot.cfg ]; then
rm -f /usr/lib/bootupd/grub2-static/configs.d/greenboot.cfg
fi

%postun default-health-checks
%systemd_postun greenboot-loading-message.service

%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/check
%dir %{_sysconfdir}/%{name}/check/required.d
%dir %{_sysconfdir}/%{name}/check/wanted.d
%dir %{_sysconfdir}/%{name}/green.d
%dir %{_sysconfdir}/%{name}/red.d
%config(noreplace) %{_sysconfdir}/%{name}/greenboot.conf
%dir %{_prefix}/lib/%{name}
%dir %{_prefix}/lib/%{name}/check
%dir %{_prefix}/lib/%{name}/check/required.d
%{_prefix}/lib/%{name}/check/required.d/00_required_scripts_start.sh
%dir %{_prefix}/lib/%{name}/check/wanted.d
%{_prefix}/lib/%{name}/check/wanted.d/00_wanted_scripts_start.sh
%dir %{_prefix}/lib/%{name}/green.d
%dir %{_prefix}/lib/%{name}/red.d
%{_exec_prefix}/lib/motd.d/boot-status
%{_tmpfilesdir}/greenboot-status-motd.conf
%{_sysconfdir}/grub.d/*.cfg
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{name}
%{_libexecdir}/%{name}/greenboot-grub2-set-success
%{_libexecdir}/%{name}/greenboot-boot-remount
%{_libexecdir}/%{name}/greenboot-grub2-set-counter
%{_libexecdir}/%{name}/greenboot-loading-message
%{_libexecdir}/%{name}/greenboot-status
%{_libexecdir}/%{name}/greenboot-rpm-ostree-grub2-check-fallback
%{_libexecdir}/%{name}/redboot-auto-reboot
%{_unitdir}/greenboot-grub2-set-counter.service
%{_unitdir}/greenboot-grub2-set-success.service
%{_unitdir}/greenboot-healthcheck.service
%{_unitdir}/greenboot-loading-message.service
%{_unitdir}/greenboot-status.service
%{_unitdir}/greenboot-task-runner.service
%{_unitdir}/greenboot-rpm-ostree-grub2-check-fallback.service
%{_unitdir}/redboot.target
%{_unitdir}/redboot-auto-reboot.service
%{_unitdir}/redboot-task-runner.service

%files default-health-checks
%{_prefix}/lib/%{name}/check/required.d/01_repository_dns_check.sh
%{_prefix}/lib/%{name}/check/wanted.d/01_update_platforms_check.sh
%{_unitdir}/greenboot-healthcheck.service.d/10-network-online.conf
%{_prefix}/lib/%{name}/check/required.d/02_watchdog.sh

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 11 2024 Packit <hello@packit.dev> - 0.15.7-1
## What's Changed
 * packit: only use IoT relevant branches by @miabbott in https://github.com/fedora-iot/greenboot/pull/156
 * Fixed the issue that boot_counter cannot be unset and some scripts do… by @ssk-wh in https://github.com/fedora-iot/greenboot/pull/151
 * fix: reword warning message for disabled checks by @runcom in https://github.com/fedora-iot/greenboot/pull/160
 * update to v0.15.7 by @say-paul in https://github.com/fedora-iot/greenboot/pull/162

## New Contributors
 * @ssk-wh made their first contribution in https://github.com/fedora-iot/greenboot/pull/151

 **Full Changelog**: https://github.com/fedora-iot/greenboot/compare/v0.15.6...v0.15.7

* Tue Sep 17 2024 Aashish Radhakrishnan <aaradhak@redhat.com> - 0.15.6-2
- Exclude ix86

* Wed Sep 11 2024 Packit <hello@packit.dev> - 0.15.6-1
## What's Changed
 * packit.yaml: add copy_upstream_release_description true by @pcdubs in https://github.com/fedora-iot/greenboot/pull/150
 * fix: remove bootupd by @say-paul in https://github.com/fedora-iot/greenboot/pull/152
 * Release v0.15.5-3 by @pcdubs in https://github.com/fedora-iot/greenboot/pull/153
 * Release v0.15.6 by @pcdubs in https://github.com/fedora-iot/greenboot/pull/155

* Thu Aug 22 2024 Packit <hello@packit.dev> - 0.15.5-2
- Update to version 0.15.5 (say-paul)
- Auto-detect image type and use correct rollback (say-paul)
- Support for read-only/boot mount (say-paul)
- Warn users of missing disabled healthchecks (djach7)
- Add feature to disable healthchecks (djach7)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 0.15.4-6
- Reorder files, don't overwrite configs on update

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 27 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.15.4-3
- migrated to SPDX license

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Packit <hello@packit.dev> - 0.15.4-1
- Release v0.15.4 (Paul Whalen)
- checks: update assignment of platform URLs var (Micah Abbott)
- Revert "update_platforms_check: quote array for ShellCheck fix" (Micah Abbott)
- Update README.md (alcir)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Packit <hello@packit.dev> - 0.15.3-1
- Release 0.15.3 (Paul Whalen)
- packit: add koji, bodhi jobs, upstream url (Paul Whalen)
- packit.yaml: Fix deprecated and renamed keys. (Paul Whalen)
- greenboot: fix exit status with unknown argument (Paul Whalen)
- greenboot-grub2-set-counter.service: ensure /boot is mounted (Adam Williamson)
- check-fallbback: ShellCheck fix (Micah Abbott)
- greenboot-grub2-set-counter: ShellCheck fix (Micah Abbott)
- greenboot-status: fix or statements to default to true (Micah Abbott)
- update_platforms_check: quote array for ShellCheck fix (Micah Abbott)
- watchdog.sh: ShellCheck fixes (Micah Abbott)
- add shellcheck GH action (Micah Abbott)
- Revert "disable DefaultDependencies to fix cycle error" (Antonio Murdaca)
- Revert "Add greenboot-service-monitor.service for service health checking" (Antonio Murdaca)

* Fri Sep 23 2022 Adam Williamson <awilliam@redhat.com> - 0.15.2-2
- Backport PR #84 to fix RHBZ #2121944

* Thu Sep 08 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 0.15.2-1
- Update to 0.15.2

* Wed Aug 31 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 0.15.1-2
- disable DefaultDependencies to fix cycle error

* Tue Aug 09 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 0.15.1-1
- Add conf during installation

* Thu Jul 21 2022 Sayan Paul <saypaul@fedoraproject.org> - 0.15.0-1
- The 0.15.0 release
- Add service-monitor

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 18 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.14.0-1
- The 0.14.0 release
- Add watchdog-triggered boot check
- Ensure all required health checks are run

* Wed Nov 10 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.13.1-1
- Update to 0.13.1

* Mon Jul 26 2021 Jose Noguera <jnoguera@redhat.com> - 0.12.0-1
- Update to 0.12.0
- Add ability to configure maximum number of boot attempts via env var and config file.
- Add How does it work section to README.
- Add CI via GitHub Actions and unit testing with BATS.
- Add update platforms DNS resolution and connection checker as health checks out of the box

* Sat Jan 16 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.11.0-2
- Make arch specific due to grub availability on s390x
- Resolves: rhbz#1915241

* Thu Aug 13 2020 Christian Glombek <lorbus@fedoraproject.org> - 0.11.0-1
- Update to 0.11.0

* Thu Jun 11 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.10.3-2
- Update changelog

* Fri Jun 05 2020 Christian Glombek <lorbus@fedoraproject.org> - 0.10.3-1
- Update to 0.10.3

* Wed Jun 03 2020 Christian Glombek <lorbus@fedoraproject.org> - 0.10.2-1
- Update to 0.10.2

* Wed May 27 2020 Christian Glombek <lorbus@fedoraproject.org> - 0.10-1
- Update to 0.10

* Mon May 04 2020 Christian Glombek <lorbus@fedoraproject.org> - 0.9-2
- Added missing requires to grub2 and rpm-ostree-grub2 packages
- Run %%setup quietly

* Fri Apr 03 2020 Christian Glombek <lorbus@fedoraproject.org> - 0.9-1
- Update to v0.9
- Update repo_owner

* Wed Feb 05 2020 Christian Glombek <lorbus@fedoraproject.org> - 0.8-1
- Update to v0.8
- Add guard against bootlooping in redboot-auto-reboot.service

* Mon Apr 01 2019 Christian Glombek <lorbus@fedoraproject.org> - 0.7-1
- Update to v0.7
- Rename ostree-grub2 subpackage to  rpm-ostree-grub2 to be more explicit
- Add auto-update-fallback meta subpackage

* Wed Feb 13 2019 Christian Glombek <lorbus@fedoraproject.org> - 0.6-1
- Update to v0.6
- Integrate with systemd's boot-complete.target
- Rewrite motd sub-package and rename to status

* Fri Oct 19 2018 Christian Glombek <lorbus@fedoraproject.org> - 0.5-1
- Update to v0.5

* Tue Oct 02 2018 Christian Glombek <lorbus@fedoraproject.org> - 0.4-2
- Spec Review

* Thu Jun 14 2018 Christian Glombek <lorbus@fedoraproject.org> - 0.4-1
- Initial Package
