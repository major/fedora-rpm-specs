Name:           virt-backup
Version:        0.2.25
Release:        14%{?dist}
Summary:        Backup script for libvirt managed VM

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://git.fws.fr/fws/virt-backup
Source0:        https://git.fws.fr/fws/%{name}/archive/%{name}-%{version}-1.tar.gz

# Working with upstream to be more packager & distro friendly.
Patch0:         virt-backup-update.patch

BuildArch:      noarch

BuildRequires:  perl-generators

Requires:       bzip2
Requires:       chunkfs
Requires:       gzip
Requires:       lvm2
Requires:       lzop
Requires:       qemu-img
Requires:       util-linux
Requires:       xz


%description
This script allows you to backup Virtual Machines managed by libvirt.
It has only be tested with KVM based VM
This script will dump (or mount as a set of chunks):
 * each block devices
 * optionnally the memory (if --state flag is given)
 * the XML description of the VM


%prep
%autosetup -n %{name}


%build
# Nothing to build


%install
# Install backup script
mkdir -p %{buildroot}%{_bindir}
install -m 0755 virt-backup %{buildroot}%{_bindir}/

# Create backup dir
mkdir -p %{buildroot}%{_sharedstatedir}/libvirt/backup


%files
%doc README
%license COPYING
%{_bindir}/%{name}
%dir %attr(0770, qemu, qemu) %{_sharedstatedir}/libvirt/backup


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.25-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.25-13
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.25-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.25-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.25-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.25-9
* Removed redundant run-require of perl

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.25-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 06 2020 Richard Shaw <hobbes1069@gmail.com> - 0.2.25-3
- Remove requires on libvirt-libs
- Remove upstream spec file changes from the patch.

* Sun Dec 06 2020 Richard Shaw <hobbes1069@gmail.com> - 0.2.25-2
- Update spec per reviewer feedback.

* Thu May 07 2020 Daniel Berteaud <daniel@firewall-services.com> 0.2.25-1
- Wait longer before removing LVM snapshots (daniel@firewall-services.com)

* Tue Apr 14 2020 Daniel Berteaud <daniel@firewall-services.com> 0.2.24-1
- Try to preserve sparse files when dumping with no compression
  (daniel@firewall-services.com)

* Tue Apr 14 2020 Daniel Berteaud <daniel@firewall-services.com> 0.2.23-1
- Remove redundant debug statement (daniel@firewall-services.com)
- Fix $glock scope (daniel@firewall-services.com)
- Fix tito releasers (daniel@firewall-services.com)

* Mon May 27 2019 Daniel Berteaud <daniel@firewall-services.com> 0.2.22-1
- Support pigz compression (daniel@firewall-services.com)
- Don't try to detect backing LVM volume is snapshot is disabled
  (daniel@firewall-services.com)

* Wed Oct 24 2018 Daniel Berteaud <daniel@firewall-services.com> 0.2.21-1
- Various fixes in lock handling (daniel@firewall-services.com)

* Wed Oct 24 2018 Daniel Berteaud <daniel@firewall-services.com> 0.2.20-1
- Timeout for global exclusive lock after 180 sec (instead of 20)
  (daniel@firewall-services.com)

* Mon Oct 22 2018 Daniel Berteaud <daniel@firewall-services.com> 0.2.19-1
- Add an exclusive lock to be sure we correctly count the number of running
  backups This also ensure only one LVM snapshot is created at a time, which is
  a good thing to prevent overloading the system (daniel@firewall-services.com)

* Mon Oct 22 2018 Daniel Berteaud <daniel@firewall-services.com> 0.2.18-1
- Add a max-backups param, to limit the numer of backups running at a time GLPI
  #33827 (daniel@firewall-services.com)

* Thu Jul 26 2018 Daniel Berteaud <daniel@firewall-services.com> 0.2.17-1
- Wait longer after chunkfs umount Or snapshot deletion might fail
  (daniel@firewall-services.com)

* Mon Jul 09 2018 Daniel Berteaud <daniel@firewall-services.com> 0.2.16-1
- Fix typo (opt instead of opts) (daniel@firewall-services.com)

* Sat Jan 27 2018 Daniel Berteaud <daniel@firewall-services.com> 0.2.15-1
- Don't use double bracket for variable substitution, but double underscores
  (daniel@firewall-services.com)

* Mon Jan 08 2018 Daniel Berteaud <daniel@firewall-services.com> 0.2.14-1
- Add support for dumpcmd With this new option, suggested and coded by Jan
  Schulz-Hofen <hi@jan.sh>, you can pipe the output of dd to a custom command
  which will consume the data through stdin. This new option is only valid with
  the dumpo action, and remove the need for a temporary file (daniel@firewall-
  services.com)

* Tue Nov 14 2017 Daniel Berteaud <daniel@firewall-services.com> 0.2.13-1
- Remove now unused CHANGELOG.git (daniel@firewall-services.com)

* Tue Nov 14 2017 Daniel Berteaud <daniel@firewall-services.com>
- Remove now unused CHANGELOG.git (daniel@firewall-services.com)

* Tue Nov 14 2017 Daniel Berteaud <daniel@firewall-services.com> 0.2.12-1
- new package built with tito

* Tue Nov 24 2015 Daniel B. <daniel@firewall-services.com> - 0.2.11-1
- Detect thin volumes
- Code/comment cleanup

* Tue Feb 17 2015 Daniel B. <daniel@firewall-services.com> - 0.2.10-1
- Correctly handle disks list when several VM are backed up in one run
  Patch by Diego Rondini <diego.rondini@kynetics.it>

* Tue Feb 10 2015 Daniel B. <daniel@firewall-services.com> - 0.2.9-1
- Fix when using a relative path for backupdir
- Fix image based disk support when they are stored on the / filesystem

* Thu Nov 6 2014 Daniel B. <daniel@firewall-services.com> - 0.2.8-1
- Support thin volumes
- Possibility to specify an alternate lock directory

* Tue Oct 21 2014 Daniel B. <daniel@firewall-services.com> - 0.2.7-1
- Do not explicitly require pbzip2

* Mon Jun 23 2014 Daniel B. <daniel@firewall-services.com> - 0.2.6-1
- Add a --no-offline option
- Revert 10 tries max to take snapshot
- Cleanup snapshot and temp files for image based disks

* Wed Jun 4 2014 Daniel B. <daniel@firewall-services.com> - 0.2.5-1
- Fix breaking the loop while taking snapshots

* Tue Jun 3 2014 Daniel B. <daniel@firewall-services.com> - 0.2.4-1
- Try up to 30 times to take a snapshot before giving up

* Fri May 2 2014 Daniel B. <daniel@firewall-services.com> - 0.2.3-1
- Better handle snapshot failure when there's no lock

* Tue Apr 22 2014 Daniel B. <daniel@firewall-services.com> - 0.2.2-1
- Lock LVM before snapshot

* Thu Jan 30 2014 Daniel B. <daniel@firewall-services.com> - 0.2.1-1
- Gracefuly handle snapshot failure for file based disks
- Improve comments

* Fri Aug 9 2013 Daniel B. <daniel@firewall-services.com> - 0.2.0-1
- Support snapshot for file based images (if FS is backed by LVM)
- Support a dual nodes cluster situation
- Add a convert action, which uses qemu-img to convert into qcow2
  instead of dumping with dd
- Cleanup the spec file

* Tue Mar 5 2013 Daniel B. <daniel@firewall-services.com> - 0.1.3-1
- Send /dev/null to lvm commands stdin

* Tue Nov 20 2012 Daniel B. <daniel@firewall-services.com> - 0.1.2-1
- Fix some spacing issue
- re-add full path to lvcreate and lvremove
- sleep to prevent race conditions

* Thu Jun 28 2012 Daniel B. <daniel@firewall-services.com> - 0.1.1-1
- Don't use absolute path for lvcreate and lvremove

* Sun Jun 17 2012 Daniel B. <daniel@firewall-services.com> - 0.1.0-1
- Move virt-backup to it's own RPM (and GIT repo)

