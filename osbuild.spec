%global         forgeurl https://github.com/osbuild/osbuild
%global         selinuxtype targeted

Version:        75

%forgemeta

%global         pypi_name osbuild
%global         pkgdir %{_prefix}/lib/%{pypi_name}

Name:           %{pypi_name}
Release:        1%{?dist}
License:        ASL 2.0

URL:            %{forgeurl}

Source0:        %{forgesource}
BuildArch:      noarch
Summary:        A build system for OS images

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  systemd

Requires:       bash
Requires:       bubblewrap
Requires:       coreutils
Requires:       curl
Requires:       dnf
Requires:       e2fsprogs
Requires:       glibc
Requires:       policycoreutils
Requires:       qemu-img
Requires:       systemd
Requires:       tar
Requires:       util-linux
Requires:       python3-%{pypi_name} = %{version}-%{release}
Requires:       (%{name}-selinux if selinux-policy-%{selinuxtype})

# Turn off dependency generators for runners. The reason is that runners are
# tailored to the platform, e.g. on RHEL they are using platform-python. We
# don't want to pick up those dependencies on other platform.
%global __requires_exclude_from ^%{pkgdir}/(runners)/.*$

# Turn off shebang mangling on RHEL. brp-mangle-shebangs (from package
# redhat-rpm-config) is run on all executables in a package after the `install`
# section runs. The below macro turns this behavior off for:
#   - runners, because they already have the correct shebang for the platform
#     they're meant for, and
#   - stages and assemblers, because they are run within osbuild build roots,
#     which are not required to contain the same OS as the host and might thus
#     have a different notion of "platform-python".
# RHEL NB: Since assemblers and stages are not excluded from the dependency
# generator, this also means that an additional dependency on /usr/bin/python3
# will be added. This is intended and needed, so that in the host build root
# /usr/bin/python3 is present so stages and assemblers can be run.
%global __brp_mangle_shebangs_exclude_from ^%{pkgdir}/(assemblers|runners|stages)/.*$

%{?python_enable_dependency_generator}

%description
A build system for OS images

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A build system for OS images

%package        lvm2
Summary:        LVM2 support
Requires:       %{name} = %{version}-%{release}
Requires:       lvm2

%description lvm2
Contains the necessary stages and device host
services to build LVM2 based images.

%package        luks2
Summary:        LUKS2 support
Requires:       %{name} = %{version}-%{release}
Requires:       cryptsetup

%description luks2
Contains the necessary stages and device host
services to build LUKS2 encrypted images.

%package        ostree
Summary:        OSTree support
Requires:       %{name} = %{version}-%{release}
Requires:       ostree
Requires:       rpm-ostree

%description ostree
Contains the necessary stages, assembler and source
to build OSTree based images.

%package        selinux
Summary:        SELinux policies
Requires:       %{name} = %{version}-%{release}
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel
%{?selinux_requires}

%description    selinux
Contains the necessary SELinux policies that allows
osbuild to use labels unknown to the host inside the
containers it uses to build OS artifacts.

%package        tools
Summary:        Extra tools and utilities
Requires:       %{name} = %{version}-%{release}
Requires:       python3-pyyaml

%description    tools
Contains additional tools and utilities for development of
manifests and osbuild.

%prep
%forgesetup

%build
%py3_build
make man

# SELinux
make -f /usr/share/selinux/devel/Makefile osbuild.pp
bzip2 -9 osbuild.pp

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%install
%py3_install

mkdir -p %{buildroot}%{pkgdir}/stages
install -p -m 0755 $(find stages -type f) %{buildroot}%{pkgdir}/stages/

mkdir -p %{buildroot}%{pkgdir}/assemblers
install -p -m 0755 $(find assemblers -type f) %{buildroot}%{pkgdir}/assemblers/

mkdir -p %{buildroot}%{pkgdir}/runners
install -p -m 0755 $(find runners -type f -or -type l) %{buildroot}%{pkgdir}/runners

mkdir -p %{buildroot}%{pkgdir}/sources
install -p -m 0755 $(find sources -type f) %{buildroot}%{pkgdir}/sources

mkdir -p %{buildroot}%{pkgdir}/devices
install -p -m 0755 $(find devices -type f) %{buildroot}%{pkgdir}/devices

mkdir -p %{buildroot}%{pkgdir}/inputs
install -p -m 0755 $(find inputs -type f) %{buildroot}%{pkgdir}/inputs

mkdir -p %{buildroot}%{pkgdir}/mounts
install -p -m 0755 $(find mounts -type f) %{buildroot}%{pkgdir}/mounts

# mount point for bind mounting the osbuild library
mkdir -p %{buildroot}%{pkgdir}/osbuild

# schemata
mkdir -p %{buildroot}%{_datadir}/osbuild/schemas
install -p -m 0644 $(find schemas/*.json) %{buildroot}%{_datadir}/osbuild/schemas
ln -s %{_datadir}/osbuild/schemas %{buildroot}%{pkgdir}/schemas

# documentation
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man5
install -p -m 0644 -t %{buildroot}%{_mandir}/man1/ docs/*.1
install -p -m 0644 -t %{buildroot}%{_mandir}/man5/ docs/*.5

# SELinux
install -D -m 0644 -t %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype} %{name}.pp.bz2
install -D -m 0644 -t %{buildroot}%{_mandir}/man8 selinux/%{name}_selinux.8
install -D -p -m 0644 selinux/osbuild.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{name}.if

# Udev rules
mkdir -p %{buildroot}%{_udevrulesdir}
install -p -m 0755 data/10-osbuild-inhibitor.rules %{buildroot}%{_udevrulesdir}

%check
exit 0
# We have some integration tests, but those require running a VM, so that would
# be an overkill for RPM check script.

%files
%license LICENSE
%{_bindir}/osbuild
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}-manifest.5*
%{_datadir}/osbuild/schemas
%{pkgdir}
%{_udevrulesdir}/*.rules
# the following files are in the lvm2 sub-package
%exclude %{pkgdir}/devices/org.osbuild.lvm2*
%exclude %{pkgdir}/stages/org.osbuild.lvm2*
# the following files are in the luks2 sub-package
%exclude %{pkgdir}/devices/org.osbuild.luks2*
%exclude %{pkgdir}/stages/org.osbuild.crypttab
%exclude %{pkgdir}/stages/org.osbuild.luks2*
# the following files are in the ostree sub-package
%exclude %{pkgdir}/assemblers/org.osbuild.ostree*
%exclude %{pkgdir}/inputs/org.osbuild.ostree*
%exclude %{pkgdir}/sources/org.osbuild.ostree*
%exclude %{pkgdir}/stages/org.osbuild.ostree*
%exclude %{pkgdir}/stages/org.osbuild.rpm-ostree

%files -n       python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%{python3_sitelib}/%{pypi_name}/

%files lvm2
%{pkgdir}/devices/org.osbuild.lvm2*
%{pkgdir}/stages/org.osbuild.lvm2*

%files luks2
%{pkgdir}/devices/org.osbuild.luks2*
%{pkgdir}/stages/org.osbuild.crypttab
%{pkgdir}/stages/org.osbuild.luks2*

%files ostree
%{pkgdir}/assemblers/org.osbuild.ostree*
%{pkgdir}/inputs/org.osbuild.ostree*
%{pkgdir}/sources/org.osbuild.ostree*
%{pkgdir}/stages/org.osbuild.ostree*
%{pkgdir}/stages/org.osbuild.rpm-ostree

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%{_mandir}/man8/%{name}_selinux.8.*
%{_datadir}/selinux/devel/include/distributed/%{name}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{name}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%files tools
%{_bindir}/osbuild-mpp


%changelog
* Wed Jan 04 2023 Packit <hello@packit.dev> - 75-1
Changes with 75
----------------
  * runners: add Fedora Asahi runner (#1216)
  * stages/rhsm.facts: create facts file in /etc (#1220)
  * test/objectstore: use os.stat instead Path.stat (#1217)

Contributions from: Achilleas Koutsou, Christian Kellner, Eric Curtin

— Somewhere on the Internet, 2023-01-04



* Wed Dec 21 2022 Packit <hello@packit.dev> - 74-1
Changes with 74
----------------
  * Clamp mtime to `source-epoch` if specified (#1207)
  * New `ostree.encapsulate` for "native ostree containers" (#1091)
  * [v2] util/fscache: introduce versioning (#1198)
  * fscache: post-merge improvements (#1211)
  * ostree.config: add aboot (Android) bootloader config option (#1204)
  * runners: add AutoSD runner (#1210)
  * schutzbot: set the cache size for the correct store (#1199)
  * stages/users: accept identical uid for existing users (#1188)
  * test/fscache: drop PathLike annotation (#1196)
  * test/stages/users: ignore non-deterministic files (#1197)
  * test: convert objectstore test to pytest (#1201)
  * util/fscache: add cachedir-tag support (#1212)
  * util: fix typo in get_consumer_secrets (#1200)
  * 🗄Write and read metadata from the store and integrate `FsCache` into `ObjectStore` (#1187)

Contributions from: Christian Kellner, David Rheinsberg, Eric Curtin, Sanne Raymaekers

— Somewhere on the Internet, 2022-12-21



* Wed Dec 07 2022 Packit <hello@packit.dev> - 73-1
Changes with 73
----------------
  * cache: provide FsCache utility for concurrent caches (#1130)
  * ci: use the latest terraform to fix missing images (#1185)
  * mounts: use the options object for mountopts (#1182)
  * schutzfile: update manifest-db ref 2022-12-05 (#1194)

Contributions from: David Rheinsberg, SchutzBot, Thomas Lavocat

— Somewhere on the Internet, 2022-12-07



* Wed Nov 23 2022 Packit <hello@packit.dev> - 72-1
Changes with 72
----------------
  * UKI: Add support for building unified kernel images (#1167)
  * Update snapshots to 20221115 (#1177)
  * `objectstore`: use direct path input/output for `Object` (#1179)
  * `stages/containers.storage.conf`: ability to specify a base file  (#1173)
  * devices: tolerate existing device nodes (#1181)
  * grub2.iso: add timeout option (#1175)
  * ignition: fix ignition_network_kcmdline (#1172)
  * test/data: persist the journal for ostree images (#1178)
  * ❌ 🐮 Remove copy-on-write support for `Object` (no-cow) (#1169)

Contributions from: Antonio Murdaca, Christian Kellner, Thomas Lavocat, schutzbot

— Somewhere on the Internet, 2022-11-23



* Wed Nov 09 2022 Packit <hello@packit.dev> - 71-1
Changes with 71
----------------
  * Extend firewall stage to add sources (continues from PR #1137) (#1157)
  * Update snapshots to 20221025 (#1159)
  * Update snapshots to 20221028 (#1161)
  * ci(lint): add shell linter - Differential ShellCheck (#1147)
  * ci: update to containers/privdocker@552e30c (#1166)
  * ci: upgrade to actions/checkout@v3 (#1165)
  * osbuild-dev: a new tool to help with manifests (#1152)
  * osbuild-mpp: recognize manifest without mediaType and with manifests fields as a list (#1168)
  * stages/ostree.preptree: link to rpm-ostree code (#1151)
  * stages: add new cpio.out stage (#1164)
Contributions from: Antonio Murdaca, Christian Kellner, Colin Walters, David Rheinsberg, Irene Diez, Jan Macku, Simon de Vlieger, Ygal Blum, schutzbot
— Somewhere on the Internet, 2022-11-09





* Wed Oct 26 2022 Packit <hello@packit.dev> - 70-1
Changes with 70
----------------
  * Build rpms on RHEL 8.8 and 9.2 (#1141)
  * packit: Replace deprecated config options (#1145)
  * schutzbot/mockbuild: stop running mock as root (#1148)
  * schutzfile: update manifest-db ref 2022-10-20 (#1155)
  * sources/ostree: set contenturl when pulling from remote (#1140)
  * stages/keymap: add font option (#1158)
  * stages/logind-systemd: add `ReserveVT` option (#1156)
  * stages/rpm: make the fake machine-id newline-terminated (#1150)
  * stages: add systemd-journald stage (#1143)
  * test: add README.md on how to make tests for stages (#1149)
Contributions from: Christian Kellner, Irene Diez, Jakub Rusz, Jan Macku, Ondřej Budai, Sanne Raymaekers, SchutzBot
— Somewhere on the Internet, 2022-10-26





* Wed Oct 12 2022 Packit <hello@packit.dev> - 69-1
Changes with 69
----------------
  * runners: auto detection based on best matching distro+version (#996)
  * sources/ostree: pull from remote using rhsm mTLS certs (#1138)
  * stages: fix ostree config stage (#1129)
Contributions from: Antonio Murdaca, Christian Kellner, Sanne Raymaekers
— Somewhere on the Internet, 2022-10-12





* Wed Sep 28 2022 Packit <hello@packit.dev> - 68-1
Changes with 68
----------------
  * manifest-db: propage the osbuild SHA on manifest-db (#1124)
  * packit: Enable Bodhi updates for unstable Fedoras (#1128)
  * packit: add epel-9 to copr_build (#1118)
  * selinux: Update based on latest packaging guide (#1127)
  * stages/greenboot: avoid new pylint suppressions (#1114)
  * test/src: improve file enumeration (#1106)
Contributions from: David Rheinsberg, Ondřej Budai, Simon Steinbeiss, Thomas Lavocat, Vit Mojzis
— Somewhere on the Internet, 2022-09-28





* Wed Sep 14 2022 Packit <hello@packit.dev> - 67-1
Changes with 67
----------------
  * Quote URL paths before downloading in curl source (#1100)
  * Use isort to sort all imports (#1087)
  * ci: remove the composer image test (#1110)
  * org.osbuild.oci-archive: Support setting Entrypoint (#1103)
  * osbuild-mpp: Add url option to mpp-embed (#1104)
  * osbuild-mpp: fix minor issues and coding-style (#1112)
  * osbuild: explicit encodings for `open()` (#1108)
  * osbuild: pylint version fixes (#1094)
  * osbuild: share terminal formats between files (#1072)
  * packit: Enable Bodhi updates workflow (#1102)
  * rpmbuild: add fedora-37 (#1101)
  * test: run mypy in test-src not in GH actions (#1093)
  * tree: fix newer pylint warnings (#1107)
Contributions from: Achilleas Koutsou, Alexander Larsson, David Rheinsberg, Simon Steinbeiss, Simon de Vlieger, Thomas Lavocat, Ygal Blum
— Somewhere on the Internet, 2022-09-14





* Wed Aug 31 2022 Packit <hello@packit.dev> - 66-1
Changes with 66
----------------
  * test: manifests testing on each PR (#1052)
Contributions from: Thomas Lavocat
— Somewhere on the Internet, 2022-08-31





* Fri Aug 26 2022 Packit <hello@packit.dev> - 65-1
Changes with 65
----------------
  * Add greenboot configuration management via osbuild (#1086)
  * Add new properties to ostree.remotes stage: gpgkeypath and contenturl (#1097)
  * pipeline: include mounts in stage checksum (#1098)
  * runners: add fedora38 (#1092)
Contributions from: Achilleas Koutsou, Christian Kellner, Ondřej Budai, Sayan Paul
— Somewhere on the Internet, 2022-08-26





* Wed Aug 17 2022 Packit <hello@packit.dev> - 64-1
Changes with 64
----------------
  * Ability to mark installation as `ostree-booted` (#1085)
  * Add org.osbuild.gcp.guest-agent.conf stage (#1080)
  * Check source via `autopep8` (#1083)
  * `stages/gcp.guest-agent.conf`: various small fixes (#1081)
  * osbuild-mpp: Allow use of mpp-* operations for stages (#1084)
  * stages/rpm: allow setting the dbpath (#666)
Contributions from: Alexander Larsson, Christian Kellner, fkolwa
— Somewhere on the Internet, 2022-08-17





* Wed Aug 03 2022 Packit <hello@packit.dev> - 63-1
Changes with 63
----------------
  * stage: add an rhsm.facts stage (#1060)
Contributions from: Simon de Vlieger
— Somewhere on the Internet, 2022-08-03





* Wed Jul 27 2022 Packit <hello@packit.dev> - 62-1
Changes with 62
----------------
  * COMPOSER-1622: Enable Fedora 36 testing (#1061)
  * `stages/container.storage.conf`: fix `filename` property lookup (#1077)
  * mounts: minor fixes with no functional changes (#1076)
  * schema: assorted fixes for schema formatting and handling (#1079)
  * stages/containers.storage.conf: support pytoml (#1078)
  * stages/users: support a dot inside a username (#1075)
Contributions from: Alexander Todorov, Christian Kellner, David Rheinsberg, Ondřej Budai
— Somewhere on the Internet, 2022-07-27





* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Packit <hello@packit.dev> - 61-1
Changes with 61
----------------
  * Add new `containers.storage.conf` stage to edit `containers-storage.conf(5)` files (#1069)
  * docs: update osbuild(1) (#1068)
  * osbuild: fix current partial type annotations (#1067)
  * source/skopeo: use subprocess.check_output (#1071)
  * stages/skopeo: use extra intermediate download dir (#1074)
  * tests: Run tests on RHEL 9.1 and 8.7 nightly (#1051)
Contributions from: Christian Kellner, David Rheinsberg, Jakub Rusz, Simon de Vlieger
— Somewhere on the Internet, 2022-07-20





* Wed Jul 06 2022 Packit <hello@packit.dev> - 60-1
Changes with 60
----------------
  * Add `_install langs` support (#1064)
  * Add a Vagrant libvirt stage (#947)
  * `stages/dnf.config`: ability to configure rpm transaction flags (#1063)
  * `stages/oci-archive`: small cleanups (#1062)
  * ci: push tags to gitlab (#1058)
  * git: ignore common virtual env locations (#1066)
  * main: add a --version argument (#1039)
  * osbuild-mpp: small python cleanups (#1056)
  * rpmbuild: add fedora-36 (#1053)
  * stages: OpenSCAP remediation at build time (#1059)
  * stages: add new org.osbuild.rpmkeys.import stage (#1057)
Contributions from: Christian Kellner, Gianluca Zuccarelli, Jakub Rusz, Jelle van der Waa, Simon de Vlieger
— Somewhere on the Internet, 2022-07-06





* Wed Jun 22 2022 Packit <hello@packit.dev> - 59-1
Changes with 59
----------------
  * Remove `options` from the v1 result (#1044)
  * Run rpmbuild on new nightlies. (#1049)
  * Support calling curl with --insecure (#1047)
  * ci: Adjust release schedule timer (#1045)
  * stages/mkfs.fat: pass `-I` command line option (#1050)
  * stages/qemu: expose vpc options (#1046)
  * store: various code cleanups (#1032)
Contributions from: Achilleas Koutsou, Christian Kellner, Jakub Rusz, Simon Steinbeiss
— Somewhere on the Internet, 2022-06-22





* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 58-2
- Rebuilt for Python 3.11

* Wed Jun 08 2022 Packit <hello@packit.dev> - 58-1
Changes with 58
----------------
  * COMPOSER-1576: rpmbuild on 8.6 and 9.0 ga (#1043)
  * `grub2.legacy`: stricter schema, replace `architecture` with `bios.platform`  (#1035)
  * `stages/grub2.legacy`: small schema fixes (#1034)
  * stages: add OpenSCAP first boot remediation (#1033)
  * tests: handle `-` in the sfdisk version test (#1037)
Contributions from: Alexander Todorov, Christian Kellner, Gianluca Zuccarelli, Simon de Vlieger
— Somewhere on the Internet, 2022-06-08





* Wed May 25 2022 Packit <hello@packit.dev> - 57-1
Changes with 57
----------------
  * meta: show stage name when schema is missing (#1022)
  * sources: curl max_workers 2 * num_cpus (#1024)
  * stages/ostree.passwd: fix subid source path (#1027)
  * stages/udev.rules: use correct separator (#1026)
  * stages: add new sgdisk stage (#1029)
Contributions from: Christian Kellner, Simon de Vlieger
— Somewhere on the Internet, 2022-05-25





* Wed May 11 2022 Packit <hello@packit.dev> - 56-1
Changes with 56
----------------
  * Re-enable pylint warning W0201 (attribute-defined-outside-init) (#1019)
  * Restrict capabilities is stages (#1010)
  * org.osbuild.luks2.format: Support dm-integrity (#1015)
  * packit: Enable Koji build integration (#1021)
  * sources: refactor the SourceService class (#998)
  * stage/ostree.passwd: also merge /etc/sub{u,g}id (#1013)
  * stages: add new org.osbuild.udev.rules stage (#1018)
  * test: remove old `pipelines` contents & directory (#1011)
Contributions from: Alexander Larsson, Christian Kellner, Simon Steinbeiss, Thomas Lavocat
— Somewhere on the Internet, 2022-05-11





* Thu Apr 28 2022 Packit <hello@packit.dev> - 53.1-1
CHANGES WITH 53.1:
----------------
 * devices/lvm2.lv: add support for lvm devices files (#1009)
Contributions from: Christian Kellner
— Liberec, 2022-04-28




* Wed Apr 27 2022 Packit <hello@packit.dev> - 55-1
Changes with 55
----------------
  * Support specifying multiple devices in all mkfs versions (like xfs) (#1004)
  * buildroot: don't explicitly add `CAP_MAC_ADMIN` (#1008)
  * devices/lvm2.lv: add support for lvm devices files (#1009)
  * inputs/org.osbuild.tree: fix typo (#1006)
  * inputs: support array of objects references (#1003)
  * workflows/trigger-gitlab: run Gitlab CI in new image-builder project (#1002)
Contributions from: Alexander Larsson, Christian Kellner, Jakub Rusz, Jelle van der Waa
— Somewhere on the Internet, 2022-04-27





* Wed Apr 13 2022 Packit <hello@packit.dev> - 54-1
Changes with 54
----------------
  * Allow specifying subformat for the `vmdk` type in `org.osbuild.qemu` stage (#999)
  * Pin rpmrepo snapshots for CI runners + use them in mockbuild + ci improvements (#1001)
  * Support VMDK subformat in qemu assembler (#1000)
Contributions from: Jakub Rusz, Tomas Hozza
— Somewhere on the Internet, 2022-04-13





* Thu Mar 24 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 53-1
CHANGES WITH 53:
----------------
  * stages/sfdisk: support changing GPT partition attribute bits (#966)
  * Enable scheduled upstream releases (#997)
  * stages/rpm: don't verify package or header signatures when installing (#995)
  * stages/selinux: directly call setfilecon (#993)
  * stages/selinux: directly call setfilecon (#993)
  * stages/selinux: directly call setfilecon (#993)
  * stages/selinux: directly call setfilecon (#993)
  * sources/curl: don't limit total download time (#990)
  * Packit: build SRPMs in Copr (#987)
Contributions from: Christian Kellner, Enric Balletbo i Serra, Laura Barcziova, Simon Steinbeiss, Tom Gundersen, Tomas Hozza
— Somewhere on the Internet, 2022-03-24





* Fri Mar 04 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 52-1
CHANGES WITH 52:
----------------
  * `stages/grub2`: write GRUB_DEFAULT on saved_entry (#981)
  * `stages/firewall`: fix fail when setting only the default zone (#984)
  * `stages/rpm`: option to import gpg keys from tree (#985)
  * LVM2: separate stderr, stdout (#982)
  * Extend firewall stage to set the default zone (#980)
  * runners: add org.osbuild.fedora37 (#983)
  * ci/deploy: use public EPEL-9 (#979)
Contributions from: Christian Kellner, Jakub Rusz, Tomas Hozza, Thomas
Lavocat
— Wien, 2022-03-04




* Wed Mar 02 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 51-1
CHANGES WITH 51:
----------------
  * stages: add the ability to configure pacman repos (#955)
Contributions from: Jelle van der Waa, Simon Steinbeiß
Grenoble Location, 2022-03-02




* Sun Feb 27 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 50-1
CHANGES WITH 50:
----------------
  * util/udev: fix path for udev device inhibitor (#976)
  * Add RHEL-9.1 runner (#975)
Contributions from: Christian Kellner, Tomas Hozza
— Vöcklabruck, 2022-02-27




* Wed Feb 23 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 49-1
CHANGES WITH 49:
----------------
  * `stages/fdo`: add new stage (#857)
  * `stages/clevis-luks-bind`, `stages/luks-remove-key`: add new stages (#967)
  * `stages/oci-archive`: fix creation time format (#973)
  * rpmbuild: run on centos-9 (#974)
  * Host.Service: add signals (#969)
Contributions from: Antonio Murdaca, Christian Kellner, Chloe Kaubisch, Jakub Rusz,
                    Thomas Lavocat
— Vöcklabruck, 2022-02-23




* Wed Feb 16 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 48-1
CHANGES WITH 48:
----------------
  * skopeo stage: remove overlay/backingFsBlockDev file after install (#970)
  * Add support for embedding containers in images (#952)
  * Initial work on more reproducible builds (#962)
  * Bootiso: add the option to compress using lz4 (#951)
  * runners: add rhel-87 (#963)
Contributions from: Alexander Larsson, Christian Kellner, Jakub Rusz, Ondřej Budai, Roy Golan, Thomas Lavocat, jkozol
— Berlin, 2022-02-16




* Wed Feb 02 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 47-1
CHANGES WITH 47:       ----------------   * `util/linux`: fix BLK_IOC_FLSBUF on ppc64le (osbuild#954)   * ci: make jobs interruptible (osbuild#902)   * `test/ci`: fix sonarqube run on main (osbuild#950)   * Enable Sonarqube scan (osbuild#898)
Contributions from: Christian Kellner, Jakub Rusz, Simon Steinbeiss
— Berlin, 2022-02-02



* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 46-1
CHANGES WITH 46:
----------------
  * Add the option of compressing using lz4 (#946)
Contributions from: Thomas Lavocat, Tomáš Hozza
— Vöcklabruck, 2022-01-19




* Fri Jan 07 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 45-1
NGES WITH 45:
----------------
  * `stages/grub2`: ability to not write kernel cmdline (#939)
  * Arch legacy grub compatibility (#941)
  * org.osbuild.kickstart adjustments (#943)
  * Fix typo in tar stage schema option enum (#940)
  * Add mkinitcpio stage (#937)
  * stages: allow using sysconfig stage multiple times. (#938)
  * objectstore: don't store objects by their treesum (#861)
Contributions from: Christian Kellner, Jelle van der Waa, Ondřej Budai, Tom Gundersen, Tomáš Hozza, Simon Steinbeiss
— Drásov (Brno-venkov), 2022-01-07




* Thu Dec 16 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 44-1
CHANGES WITH 44:
----------------
  * LUKS (v2) support (#879)
  * osbuild-mpp: Add support for a pacman resolver (#911)
  * `stages/dnf-automatic`: add new stage for configuring DNF Automatic (#936)
  * `stages/yum.repos`: add new stage for creating YUM / DNF repo files (#932)
  * `stages/users`: explicitly create a home directory (#929)
  * `stages/dnf`: edit /etc/dnf/dnf.conf (#928)
  * `stages/sshd`: support PermitRootLogin option (#917)
  * build root: isolate container environment from the host and set `CONTAINER` (#926)
  * Small fix for `mounts/ostree.deployment` and an order check for `depsolve` (#915)
  * Added poll() with a time out of 10 minutes for building images (#888, #918)
  * Apply autopep8 to osbuild-mpp and resolve Constructor is undefined (#914)
  * Support for on demand pipeline building (#855)
  * util/rmrf: handle broken symlinks (#913)
Contributions from: Aaron Hetherington, Achilleas Koutsou, Christian Kellner, Jelle van der Waa,
                    Ondřej Budai, Sanne Raymaekers, Simon Steinbeiss, Tomas Hozza
— Vöcklabruck, 2021-12-16




* Wed Dec 01 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 43-1
CHANGES WITH 43:
----------------
  * Buildroot: mask `/proc/cmdline` (#895)
  * stages/grub2.inst: Make grub-mkimage binary configurable (#905)
  * tests: enable testing on aarch64 RHEL (#844)
  * gitignore: Ignore generated man pages (#903)
  * stages/ostree.fillvar: fill the correct var (#904)
  * osbuild-mpp: Allow importing multiple pipelines from a manifest (#900)
  * ci: switch to rhel-9 runners (#901)
  * spec: require python3-pyyaml for osbuild-tools (#899)
  * osbuild-mpp: Support loading yaml as well as json files (#893)
  * CI: update the osbuild-ci container (#896)
  * osbuild: Add org.osbuild.gunzip stage (#886)
  * osbuild-mpp: Report the path of the json file when parsing fails (#890)
  * packit: enable copr builds for CS9 on main (#894)
  * tools/osbuild-mpp: add ability to embed files (#859)
  * osbuild-mpp: Add mpp-if feature (#885)
Contributions from: Alexander Larsson, Christian Kellner, Jakub Rusz, Jelle van der Waa, Ondřej Budai, kingsleyzissou
— Berlin, 2021-12-01


















* Thu Nov 18 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 42-1
CHANGES WITH 42:
----------------
  * packit: enable copr build for CS9 (#887)
  * test/lvm2: use LoopControl.loop_for_fd (#884)
  * packit: Use upstream github release description (#880)
Contributions from: Christian Kellner, Ondřej Budai, Simon Steinbeiss
— Cork, 2021-11-17
-----BEGIN PGP SIGNATURE-----
iQIzBAABCAAdFiEErKmAeFdguKfr5RbZC04GHB6SbNcFAmGU3x8ACgkQC04GHB6S
bNcXqBAAxWLL5kFhhrbboXShLmgdVbryYv8muxsyF0YFdE8qHdJmwDZkURoUH2Mh
RzWDl4Lq1FKoGJZ6WP3S0/Mj/8cpHhhXSnUzcGZamz6hJrsoyeUfYRQrB67/Mkm5
HEWWMxYBA1qvf+tfzVAr4BjlUfmDAHqjbRu5loHqANJSKNCmcg2jrHnvV5VrjBQf
t1NCQOm960kik5gjFfAemsmEYlkPN8MtD/VxxUJC2dKCDkY7tQBITB+40fB0lDdF
EIODFooKE0b2rXumEJUr95V6vGmmEOyFOcsOajls58pJSbak01g2I6J6WpSb9EiS
RZbhNYhh59BKNrsbfpO8JAYrqVy+OyPZxTwdpIUYbP4KndNbGe/QH5L/Vbdt1Dv9
HokDnTGD2jLrHyK1HP+NkjHmGy+s5XCiFwtFPbZeI7RIgxugIkJjM985u9vi0Ufd
uzbI0DP302DRiafXgR9CX/YXkEWjHpu8RSeoFsbTj6KzSAZtacK7gXWcSF5TUMlZ
kGVGy/b9xz5Ily2SOI07FBNMCHH705BRXsZGuugPlmslACTEVUh377DpvYcgBHVx
oclxqFXW17xwcxCrC6JBcXM9h2h59KJ60BSGnVHpg2bdqZat01we1p2rbcN6Dn2H
45KWO7O678oRBnIpt4lsnY/Avs7DZ83HfX4ctNfcgdwRDISFyts=
=jsoz
-----END PGP SIGNATURE-----








* Wed Nov 17 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 42-1
CHANGES WITH 42:
----------------
  * packit: enable copr build for CS9 (#887)
  * test/lvm2: use LoopControl.loop_for_fd (#884)
  * packit: Use upstream github release description (#880)
Contributions from: Christian Kellner, Ondřej Budai, Simon Steinbeiss
— Cork, 2021-11-17
-----BEGIN PGP SIGNATURE-----
iQIzBAABCAAdFiEErKmAeFdguKfr5RbZC04GHB6SbNcFAmGU3x8ACgkQC04GHB6S
bNcXqBAAxWLL5kFhhrbboXShLmgdVbryYv8muxsyF0YFdE8qHdJmwDZkURoUH2Mh
RzWDl4Lq1FKoGJZ6WP3S0/Mj/8cpHhhXSnUzcGZamz6hJrsoyeUfYRQrB67/Mkm5
HEWWMxYBA1qvf+tfzVAr4BjlUfmDAHqjbRu5loHqANJSKNCmcg2jrHnvV5VrjBQf
t1NCQOm960kik5gjFfAemsmEYlkPN8MtD/VxxUJC2dKCDkY7tQBITB+40fB0lDdF
EIODFooKE0b2rXumEJUr95V6vGmmEOyFOcsOajls58pJSbak01g2I6J6WpSb9EiS
RZbhNYhh59BKNrsbfpO8JAYrqVy+OyPZxTwdpIUYbP4KndNbGe/QH5L/Vbdt1Dv9
HokDnTGD2jLrHyK1HP+NkjHmGy+s5XCiFwtFPbZeI7RIgxugIkJjM985u9vi0Ufd
uzbI0DP302DRiafXgR9CX/YXkEWjHpu8RSeoFsbTj6KzSAZtacK7gXWcSF5TUMlZ
kGVGy/b9xz5Ily2SOI07FBNMCHH705BRXsZGuugPlmslACTEVUh377DpvYcgBHVx
oclxqFXW17xwcxCrC6JBcXM9h2h59KJ60BSGnVHpg2bdqZat01we1p2rbcN6Dn2H
45KWO7O678oRBnIpt4lsnY/Avs7DZ83HfX4ctNfcgdwRDISFyts=
=jsoz
-----END PGP SIGNATURE-----








* Mon Nov 08 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 41-1
- stages/authconfig: run authconfig (Tom Gundersen)
- stages/yum.config: add an option to configure langpacks plugin (Ondřej Budai)
- formats/v2: fix describe for mount without source (Christian Kellner)
- stages/selinux: ability to force an auto-relabel (Christian Kellner)
- stages/pwquality.conf: set pwquality configuration (Tom Gundersen)
- stages/rhsm: add support to configure yum plugins (Christian Kellner)
- stages/rhsm: extract plugins defintion (Christian Kellner)
- Add new `org.osbuild.yum.config` stage (Tomas Hozza)
- test/cloud-init: add new options to stage test (Achilleas Koutsou)
- stages/cloud-init: disable default_flow_style when writing configs (Achilleas Koutsou)
- stages/cloud-init: add support for configuring output logging (Achilleas Koutsou)
- stages/cloud-init: add support for configuring reporting handlers (Achilleas Koutsou)
- stages/cloud-init: add support for configuring Azure datasource (Achilleas Koutsou)
- stages: add new org.osbuild.cron.script stage (Christian Kellner)
- stages/grub2: add support for terminal, serial and timeout config (Ondřej Budai)
- stages/waagent.conf: set WALinuxAgent configuration (Tom Gundersen)
- stages/sshd.config: set sshd configuration (Tom Gundersen)
- Support 'install' command in org.osbuild.modprobe stage (Tomas Hozza)
- Post release version bump (msehnout)

* Wed Nov 03 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 40-1
- stages/lvm2.create: fix 'size' and add 'extents' (Christian Kellner)
- Let schutzbot do the post-release version bump (Simon Steinbeiss)
- test/data: use ostree.deployment in fedora image (Christian Kellner)
- mounts: add new ostree.deployment service (Christian Kellner)
- mounts: include tree directory in arguments (Christian Kellner)
- mounts: allow empty returns from service (Christian Kellner)
- mounts: separate file system mount service (Christian Kellner)
- meta: allow mounts for all stages (Christian Kellner)
- schema/v2: make mount source and target optional (Christian Kellner)
- mounts: change schema meta information (Christian Kellner)
- mounts: introduce new mount manager class (Christian Kellner)
- devices: add device path helper functions (Christian Kellner)
- devices: introduce new device manager class (Christian Kellner)
- test/data: add RHEL 7 manifests (Christian Kellner)
- test/stages: add check for `parted` stage (Christian Kellner)
- runners: add rhel7 runner (Christian Kellner)
- stages/grub2.legacy: new stage for non-bls config (Christian Kellner)
- stages/parted: new stage to partition a device (Christian Kellner)
- pipeline: don't bind-mount /boot from the host (Christian Kellner)
- buildroot: make mounting /boot optional (Christian Kellner)
- setup.cfg: increase max-statements to 75 (Christian Kellner)
- runners: add new centos9 runner (Christian Kellner)
- ci: remove 8.5 nightly testing (Ondřej Budai)
- mpp: fix long options (Christian Kellner)
- osbuild-mpp: Set the "arch" variable to the current rpm arch (Alexander Larsson)
- osbuild-mpp: Better handling of variable defaults and propagation (Alexander Larsson)
- osbuild-mpp: Better handling of -D overrides (Alexander Larsson)
- osbuild-mpp: Allow using formating in depsolver node (Alexander Larsson)
- osbuild-mpp: Add mpp-join (Alexander Larsson)
- osbuild-mpp: Add mpp-eval (Alexander Larsson)
- Fix GitHub Action tag pattern (Simon Steinbeiss)
- mockbuild: reuse mock repos from the system ones (Ondřej Budai)
- mockbuild: rotate a variable name (Ondřej Budai)
- gitlab: don't save journal (Ondřej Budai)
- deploy: update to the latest composer commit (Ondřej Budai)
- ci: don't register the runners (Ondřej Budai)
- trigger-gitlab: do not interpret the fetch_pulls outputs (Ondřej Budai)
- Bump version numbers ahead of release (Simon Steinbeiss)
- Switch to simple upstream releases (Simon Steinbeiss)
- stages/grub2.inst: ensure /var/tmp exists (Christian Kellner)
- devices/loopback: remove extra "'" from print (Christian Kellner)
- tests/ci: Switch to testing on 8.4 GA (Jakub Rusz)
- tests: enable testing on RHEl-8.5 and RHEL-9.0 (Jakub Rusz)
- .github: Write PR data to a file first in trigger-gitlab (Sanne Raymaekers)
- README: Add a link to our developer guide (Simon Steinbeiss)

* Wed Oct 06 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 39-1
- 39 (Thomas Lavocat)
- packit: enable builds on ppc64le (Tomas Hozza)
- CI: rename rhel-8.5 runners to rhel-8.5-nightly (Achilleas Koutsou)
- mockbuild: add RHEL 8.6 (Achilleas Koutsou)
- docs: document osbuild and selinux integration (Christian Kellner)
- ci: trigger gitlab from checks not tests (Christian Kellner)
- ci: split out checks from tests (Christian Kellner)
- .github: Get PR number from sha (Sanne Raymaekers)
- .github: Use the workflow_run event data in trigger-gitlab (Sanne Raymaekers)
- ci: trigger gitlab ci via workflow run event (Christian Kellner)

* Mon Sep 27 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 38-1
- 38 (Simon Steinbeiss)
- Copy the local_vars dictionary to avoid eval modifying it (Pierre-Yves Chibon)
- Add support for defining variables from other variables or basic expression (Pierre-Yves Chibon)
- test/host: checks for invalid fd handling (Christian Kellner)
- host: check reply_fds before sending them (Christian Kellner)
- host: raise a protocol error for empty messages (Christian Kellner)
- sources: pass items via temporary file (Christian Kellner)
- test/host: add check for call with fds (Christian Kellner)
- host: properly clean up passed fds (Christian Kellner)
- stages/qemu: fix 'compat' option (Christian Kellner)

* Wed Sep 22 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 37-1
- 37 (Martin Sehnoutka)
- sources: port to host services (Christian Kellner)
- org.osbuild.curl: Don't load secrets if not needed (Alexander Larsson)
- pipeline: split out downloading from building (Christian Kellner)
- Fix the assert as `.sort()`  returns None (Pierre-Yves Chibon)
- schutzbot: Update terraform sha (Sanne Raymaekers)
- packit: Propose PRs to all Fedoras (Simon Steinbeiss)
- stages: pam_limits.conf → pam.limits.conf (Christian Kellner)
- Add a new stage for configuring `pam_limits` module (Tomas Hozza)
- ostree.config: add `bootloader` config option (Christian Kellner)
- Add a new stage for setting kernel parameters via sysctl.d (Tomas Hozza)

* Wed Sep 08 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 36-1
- 36 (Diaa Sami)
- Add a new stage `org.osbuild.tmpfilesd` for configuring tmpfiles.d (Tomas Hozza)
- Add a new stage for configuring SELinux state on the system (Tomas Hozza)
- Add a new `org.osbuild.dnf.config` stage for configuring DNF (Tomas Hozza)
- Add new `org.osbuild.tuned` stage for setting active TuneD profile (Tomas Hozza)
- util/rhsm: Check if repositories is None before iterating (Sanne Raymaekers)
- stages/kickstart: set passwords with --iscrypted (Achilleas Koutsou)

* Sun Aug 29 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 35-1
- 35 (Tom Gundersen)
- stages/kickstart: quote ssh-key (Christian Kellner)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1-3
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Martin Sehnoutka <msehnout@redhat.com> - 1-2
- update upstream URL to the new Github organization

* Wed Jul 17 2019 Martin Sehnoutka <msehnout@redhat.com> - 1-1
- Initial package
