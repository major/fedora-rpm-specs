Name:          initoverlayfs
Version:       0.995
Release:       4%{?dist}
Summary:       An initial scalable filesystem for Linux operating systems
License:       GPL-2.0-only
URL:           https://github.com/containers/initoverlayfs
Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: libblkid-devel
Recommends: lz4
Recommends: gzip
Requires: erofs-utils
Requires: dracut

%global debug_package %{nil}

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build
RPM_OPT_FLAGS="${RPM_OPT_FLAGS/-flto=auto /}"
gcc ${RPM_OPT_FLAGS} -lblkid initoverlayfs.c -o initoverlayfs

%install
install -D -m755 bin/initoverlayfs-install ${RPM_BUILD_ROOT}/%{_bindir}/initoverlayfs-install
install -D -m755 initoverlayfs ${RPM_BUILD_ROOT}/%{_sbindir}/initoverlayfs
install -D -m755 lib/dracut/modules.d/81initoverlayfs/module-setup.sh ${RPM_BUILD_ROOT}/%{_prefix}/lib/dracut/modules.d/81initoverlayfs/module-setup.sh
install -D -m644 lib/systemd/system/pre-initoverlayfs.target ${RPM_BUILD_ROOT}/%{_prefix}/lib/systemd/system/pre-initoverlayfs.target
install -D -m644 lib/systemd/system/pre-initoverlayfs.service ${RPM_BUILD_ROOT}/%{_prefix}/lib/systemd/system/pre-initoverlayfs.service
install -D -m644 lib/systemd/system/pre-initoverlayfs-switch-root.service ${RPM_BUILD_ROOT}/%{_prefix}/lib/systemd/system/pre-initoverlayfs-switch-root.service
install -D -m755 lib/kernel/install.d/94-initoverlayfs.install ${RPM_BUILD_ROOT}/%{_prefix}/lib/kernel/install.d/94-initoverlayfs.install

%files
%license LICENSE
%doc README.md
%attr(0755,root,root)
%{_bindir}/initoverlayfs-install
%{_sbindir}/initoverlayfs
%{_prefix}/lib/dracut/modules.d/81initoverlayfs/
%{_prefix}/lib/systemd/system/pre-initoverlayfs.target
%{_prefix}/lib/systemd/system/pre-initoverlayfs.service
%{_prefix}/lib/systemd/system/pre-initoverlayfs-switch-root.service
%{_prefix}/lib/kernel/install.d/94-initoverlayfs.install

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.995-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.995-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.995-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 20 2024 Stephen Smoogen <ssmoogen@redhat.com> - 0.995-1
- Create tag for new RPM release.
- Sync spec file with version from tar file.

* Tue Mar 12 2024 Eric Curtin <ecurtin@redhat.com> - 0.994-1
- Automatically rebuild initoverlayfs on kernel update.

* Mon Mar 11 2024 Eric Curtin <ecurtin@redhat.com> - 0.993-1
- Add option to use initoverlayfs as an init system and mount
  storage immediately.
- Used in Automotive, requires storage drivers to be built
  directly in the kernel.

* Mon Feb 12 2024 Eric Curtin <ecurtin@redhat.com> - 0.992-1
- Update to 0.992 release.
- Automatically rebuild kernel on upgrade (ecurtin)
- Build initrd in no-hostonly mode for generic initrd (ecurtin)

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Stephen Smoogen <ssmoogen@redhat.com> - 0.991-1
- Update to 0.991 release.
- fork storage-init as a systemd unit (ecurtin)
- shell-less initrd work (ecurtin)

* Thu Dec 14 2023 Stephen Smoogen <ssmoogen@redhat.com> - 0.99-1
- Update to 0.99 release.
- shellcheck corrections (Yariv)
- install: detect where the initramfs exists (Douglas)
- fix bootfs wait (Eric)
- Add code for packit
- Add autotools items for building.

* Thu Dec  7 2023 Stephen Smoogen <ssmoogen@redhat.com> - 0.98-1
- Release 0.98
- Improve documentation (PR31 and ecurtin)
- Only wait for bootfs storage device if it is configured (PR32)

* Fri Nov 17 2023 Eric Curtin <ecurtin@redhat.com> - 0.97-1
- Raspberry Pi 4 enablement.

* Wed Nov  8 2023 Stephen Smoogen <ssmoogen@redhat.com> - 0.96-2
- Make changes to pass fedora-review tests on permissions and other items

* Tue Oct 24 2023 Eric Curtin <ecurtin@redhat.com> - 0.96-1
- Leave initoverlayfs dracut module out of initoverlayfs.
* Tue Oct 24 2023 Eric Curtin <ecurtin@redhat.com> - 0.95-1
- Install script changes.
* Wed Oct 18 2023 Eric Curtin <ecurtin@redhat.com> - 0.94-1
- Add partlabel support.
* Mon Oct 16 2023 Eric Curtin <ecurtin@redhat.com> - 0.93-1
- More optimization, can now install initoverlayfs files for kernels that
  aren't currently running.
* Fri Oct 13 2023 Eric Curtin <ecurtin@redhat.com> - 0.92-1
- Add default fs and fstype.
* Fri Oct 13 2023 Eric Curtin <ecurtin@redhat.com> - 0.91-1
- Rm custom tokenizer, replace with strtok.
* Thu Oct 12 2023 Eric Curtin <ecurtin@redhat.com> - 0.9-1
- Change to bls_parser, split into separate files. Remove grub dependancy.
* Thu Oct 5 2023 Eric Curtin <ecurtin@redhat.com> - 0.8-1
- Change to initoverlayfs.bootfs and initoverlay.bootfstype
* Wed Oct 4 2023 Eric Curtin <ecurtin@redhat.com> - 0.7-1
- Some bugfixes, leading / in fs=, asprintf check incorrect
* Tue Oct 3 2023 Eric Curtin <ecurtin@redhat.com> - 0.6-1
- initoverlayfs-install generates /etc/initoverlayfs.conf
* Mon Oct 2 2023 Eric Curtin <ecurtin@redhat.com> - 0.5-1
- Add dracut files to initramfs
* Wed Sep 27 2023 Eric Curtin <ecurtin@redhat.com> - 0.4-1
- Package initoverlayfs

