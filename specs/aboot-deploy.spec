Name:           aboot-deploy
Version:        0.9.14
Release:        3%{?dist}
Summary:        Deploy aboot

License:        GPL-2.0-or-later
URL:            https://gitlab.com/CentOS/automotive/src/aboot-deploy
ExclusiveArch:  x86_64 aarch64
Source0:        %{url}/-/releases/%{version}/downloads/aboot-deploy-%{version}.tar.xz

BuildRequires:  gcc meson libselinux-devel libfdisk-devel systemd file-devel
%description
Aboot-deploy is a tool that given a aboot (Android) image, writes it to the
relevant bootloader partition.


# --- SUBPACKAGE: Aboot-update ---
%package -n aboot-update
Summary:        Update aboot from kernel/initrd

Recommends:     android-tools
Recommends:     kernel-tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       unzboot

%description -n aboot-update
Aboot-update is a tool that given a kernel version creates an android
boot image (aboot) file called /boot/aboot-VERSION.img based on the
options specified in /boot/aboot.cfg.

There is also a kernel-install script (90-aboot.install) that automatically
runs this on each new kernel install if the kernel install layout is set
to aboot.

%prep
%autosetup

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%post
%systemd_post aboot-gptctl-set-success.service

%preun
%systemd_preun aboot-gptctl-set-success.service

%postun
%systemd_postun aboot-gptctl-set-success.service

%files
%license LICENSE
%doc README.md
%{_bindir}/aboot-deploy
%{_bindir}/aboot-gptctl
%{_unitdir}/aboot-gptctl-set-success.service

# 2. Aboot-update Subpackage Files
%files -n aboot-update
%license LICENSE
%doc README.md
%{_bindir}/aboot-update
%{_prefix}/lib/kernel/install.d/90-aboot.install


%changelog
* Mon Oct 05 2026 Ian Mullins <imullins@redhat.com> - 0.9.14-3
- Restrict build architectures to x86_64 and aarch64

* Thu Oct 01 2026 Ian Mullins <imullins@redhat.com> - 0.9.14-2
- Address some rpmlint warnings prior to request to get
  aboot-deploy into fedora.

* Tue Sep 22 2026 Alexander Larsson  <alex@mac-studio> - 0.9.14-1
- Update to 0.9.14

* Wed Sep 16 2026 Alexander Larsson  <alex@mac-studio> - 0.9.13-1
- Update to 0.9.13

* Thu Aug 20 2026 Michael Engel <mengel@redhat.com> - 0.9.12-1
- Update to 0.9.12

* Fri Apr 24 2026 Alexander Larsson  <alexl@redhat.com> - 0.9.11-1
- Update to 0.9.11

* Thu Apr 16 2026 Alexander Larsson  <alexl@redhat.com> - 0.9.10-1
- Update to 0.9.10

* Mon Mar 16 2026 Alexander Larsson  <alexl@redhat.com> - 0.9.9-1
- Update to 0.9.9

* Fri Feb 13 2026 Alexander Larsson  <alexl@redhat.com> - 0.9.8-1
- Update to 0.9.8

* Thu Feb 12 2026 Alexander Larsson  <alexl@redhat.com> - 0.9.7-1
- Update to 0.9.7

* Tue Feb 10 2026 Alexander Larsson  <alexl@redhat.com> - 0.9.6-1
- Update to 0.9.6

* Thu Jan 15 2026 Ian Mullins <imullins@redhat.com> - 0.9.5-1
- gptctl: switch UFS boot LUN when required

* Wed Jan 07 2026 Ian Mullins <imullins@redhat.com> - 0.9.4-1
- Fix path used for aboot.cfg and kernel config.

* Fri Dec 05 2025 Ian Mullins <imullins@redhat.com> - 0.9.3-1
- Update to 0.9.3
- Add aboot-update as a subpackage
- Replace legacy aboot-update Bash script with C implementation

* Thu Dec 04 2025 Alexander Larsson  <alexl@redhat.com> - 0.9.2-1
- Update to 0.9.2
- Add aboot-gptctl-set-success.service and systemd build-dep

* Thu Dec 04 2025 Alexander Larsson  <alexl@redhat.com> - 0.9.1-1
- Update to 0.9.1
- Added aboot-gptctl

* Fri Nov 21 2025 Ian Mullins <imullins@redhat.com> - 0.9.0-1
- Rewrite aboot-deploy in C

* Fri Oct 31 2025 Alexander Larsson  <alexl@redhat.com> - 0.7.2-1
- Fix default config file reading

* Wed May 7 2025 Ian Mullins <imullins@redhat.com> - 0.7.1-1
- Make the repo a dist-git repo only

* Tue Apr 29 2025 Alexander Larsson  <alexl@redhat.com> - 0.7-1
- Add support for ukiboot

* Tue Feb 25 2025 Ian Mullins <imullins@redhat.com>
- Properly handle the case where VBMETA_PARTITION_A/B is not configured.

* Tue Apr 23 2024 Eric Curtin <ecurtin@redhat.com>
- Deploy vbmeta partition also.

* Mon Apr 15 2024 Eric Curtin <ecurtin@redhat.com>
- Remove pipefail, pipes fail deliberately in some parts of this
  script.

* Mon Apr 8 2024 Eric Curtin <ecurtin@redhat.com>
- Add aboot-deploy -l option for flashing Android Boot Images to the
  correct slot

* Sun Jul 16 2023 Eric Curtin <ecurtin@redhat.com>
- In the presence of no AB switching tool, allow single slot upgrades
- selinux fix, change of label

* Mon Jun 26 2023 Eric Curtin <ecurtin@redhat.com>
- Integrate abctl/qbootctl

* Wed Jan 11 2023 Eric Curtin <ecurtin@redhat.com>
- Changed to take ab partitioning into account

* Wed Jan 11 2023 Eric Curtin <ecurtin@redhat.com>
- Added noarch, it's a shell script

* Wed Oct 12 2022 Eric Curtin <ecurtin@redhat.com>
- Initial version
