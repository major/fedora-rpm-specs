%global debug_package %{nil}

# rootfs macros
%global rootfs_qm %{_prefix}/lib/qm/rootfs/

# Define the feature flag: 1 to enable, 0 to disable
# By default it's disabled: 0

# Some bits borrowed from the openstack-selinux and container-selinux packages
%global moduletype services
%global modulenames qm
%global seccomp_json /usr/share/%{modulenames}/seccomp-no-rt.json
%global setup_tool %{_prefix}/share/%{modulenames}/setup

%global _installscriptdir %{_prefix}/lib/%{modulenames}

# Usage: _format var format
# Expand 'modulenames' into various formats as needed
# Format must contain '$x' somewhere to do anything useful
%global _format() export %1=""; for x in %{modulenames}; do %1+=%2; %%1+=" "; done;

# copr_username is only set on copr environments, not on others like koji
# Check if copr is owned by rhcontainerbot
%if "%{?copr_username}" != "rhcontainerbot"
%bcond_with copr
%else
%bcond_without copr
%endif

%if 0%{?fedora}
%global podman_epoch 5
%else
%global podman_epoch 2
%endif

Name: qm
# Set different Epochs for copr and koji
%if %{with copr}
Epoch: 101
%endif
# Keep Version in upstream specfile at 0. It will be automatically set
# to the correct value by Packit for copr and koji builds.
# IGNORE this comment if you're looking at it in dist-git.
Version: 0.7.4
%if %{defined autorelease}
Release: %autorelease
%else
Release: 1
%endif
License: GPL-2.0-only
URL: https://github.com/containers/qm
Summary: Containerized environment for running Quality Management software
Source0: %{url}/archive/v%{version}.tar.gz
BuildArch: noarch
# golang-github-cpuguy83-md2man on CentOS Stream 9 is available in CRB repository
BuildRequires: golang-github-cpuguy83-md2man
BuildRequires: container-selinux
BuildRequires: make
BuildRequires: git-core
BuildRequires: pkgconfig(systemd)
BuildRequires: selinux-policy >= %_selinux_policy_version
BuildRequires: selinux-policy-devel >= %_selinux_policy_version
BuildRequires: bluechi-selinux

Requires: iptables
Requires: parted
Requires: containers-common
Requires: selinux-policy >= %_selinux_policy_version
Requires(post): selinux-policy-base >= %_selinux_policy_version
Requires(post): selinux-policy-any >= %_selinux_policy_version
Recommends: selinux-policy-targeted >= %_selinux_policy_version
Requires(post): policycoreutils
Requires(post): libselinux-utils
Requires: podman >= %{podman_epoch}:4.5
Requires: jq

%description
This package allow users to setup an environment which prevents applications
and container tools from interfering with other all other processes on the
system.

The QM runs its own version of systemd and Podman to isolate not only the
applications and containers launched by systemd and Podman but systemd and
Podman themselves.

Software install into the QM environment under `/usr/lib/qm/rootfs` is
automatically isolated from the host. If developers need to further
isolate there applications from other processes in the QM they should
use container tools like Podman.

%prep
%autosetup -Sgit -n %{name}-%{version}
sed -i 's/^install: man all/install:/' Makefile

%build
%{__make} all

%install
# Create the directory for drop-in configurations
install -d %{buildroot}%{_sysconfdir}/containers/containers.conf.d

# install policy modules
%_format MODULES $x.pp.bz2
%{__make} DESTDIR=%{buildroot} DATADIR=%{_datadir} install

%post
%_format MODULES %{_datadir}/selinux/packages/$x.pp.bz2
. %{_sysconfdir}/selinux/config
%selinux_modules_install -s ${SELINUXTYPE} $MODULES
# Execute the script to create seccomp rules after the package is installed
/usr/share/qm/create-seccomp-rules
/usr/share/qm/comment-tz-local # FIX-ME GH-issue: 367
# podmand netavark requires at host to load or let's ignore in case host don't have it and proceed with the installation
modprobe ip_tables || true

%preun
if [ $1 = 0 ]; then
   # Commands to run before the package is completely removed
   # remove previous configured qm rootfs
   systemctl stop qm
   %{setup_tool} --remove-qm-rootfs &> /dev/null
fi

%postun
if [ $1 -eq 0 ]; then
   # This section executes only on package removal, not on upgrade
   . %{_sysconfdir}/selinux/config
   %selinux_modules_uninstall -s ${SELINUXTYPE} %{modulenames}
   if [ -f %{seccomp_json} ]; then
     /bin/rm -f %{seccomp_json}
   fi
fi

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc CODE-OF-CONDUCT.md NOTICE README.md SECURITY.md
%dir %{_datadir}/selinux
%{_datadir}/selinux/*
%dir %{_datadir}/qm
%{_datadir}/qm/containers.conf
%{_datadir}/qm/contexts
%{_datadir}/qm/file_contexts
%{_datadir}/qm/setup
%{_datadir}/qm/create-seccomp-rules
%{_datadir}/qm/qm-rootfs
%{_datadir}/qm/qm-storage-settings
%{_datadir}/qm/comment-tz-local
%{_datadir}/qm/qm-is-ostree
%ghost %dir %{_datadir}/containers
%ghost %dir %{_datadir}/containers/systemd
%{_datadir}/containers/systemd/qm.container
%{_mandir}/man8/*
%ghost %dir %{_installscriptdir}
%ghost %dir %{_installscriptdir}/rootfs
%ghost %{_installscriptdir}/rootfs/*

%changelog
* Tue Mar 18 2025 Packit <hello@packit.dev> - 0.7.4-1
- Update to version 0.7.4

* Wed Mar 05 2025 Packit <hello@packit.dev> - 0.7.3-1
- Update to version 0.7.3

* Fri Feb 28 2025 Packit <hello@packit.dev> - 0.7.2-1
- Update to version 0.7.2

* Thu Feb 27 2025 Packit <hello@packit.dev> - 0.7.1-1
- Update to version 0.7.1

* Wed Feb 26 2025 Packit <hello@packit.dev> - 0.7.0-1
- Update to version 0.7.0

* Sat Jan 04 2025 Packit <hello@packit.dev> - 0.6.9-1
- Update to version 0.6.9

* Wed Nov 13 2024 Packit <hello@packit.dev> - 0.6.8-1
- Update to version 0.6.8

* Thu Sep 12 2024 Packit <hello@packit.dev> - 0.6.7-1
- Update to version 0.6.7

* Fri Jun 28 2024 Packit <hello@packit.dev> - 0.6.5-1
- Update to version 0.6.5

* Tue May 14 2024 Packit <hello@packit.dev> - 0.6.4-1
- Update to version 0.6.4

* Tue May 07 2024 Douglas Schilling Landgraf <dougsland@redhat.com> - 0.6.3-1
- Update to 0.6.3 upstream release

* Fri Jan 26 2024 Douglas Schilling Landgraf <dougsland@redhat.com> - 0.6.2-1
- Update to version v0.6.2

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Douglas Schilling Landgraf <dougsland@redhat.com> - 0.6.1-2
- add vsomeip3-selinux as buildrequires

* Thu Jan 18 2024 Douglas Schilling Landgraf <dougsland@redhat.com> - 0.6.1-1
- Update to version 0.6.1

* Mon Nov 27 2023 Douglas Schilling Landgraf <dougsland@redhat.com> - 0.6.0-2
- sources v0.6.0

* Mon Nov 27 2023 Douglas Schilling Landgraf <dougsland@redhat.com> - 0.6.0-1
- v0.6.0

* Wed Nov 01 2023 Packit <hello@packit.dev> - 0.5.8-1
- [packit] 0.5.8 upstream release

* Thu Sep 07 2023 Packit <hello@packit.dev> - 0.5.7-1
- [packit] 0.5.7 upstream release

* Fri Sep 01 2023 Packit <hello@packit.dev> - 0.5.6-1
- [packit] 0.5.6 upstream release

* Wed Aug 30 2023 Packit <hello@packit.dev> - 0.5.5-1
- [packit] 0.5.5 upstream release

* Tue Aug 29 2023 Packit <hello@packit.dev> - 0.5.4-1
- [packit] 0.5.4 upstream release

* Mon Aug 28 2023 Packit <hello@packit.dev> - 0.5.3-1
- [packit] 0.5.3 upstream release

* Wed Aug 16 2023 Packit <hello@packit.dev> - 0.5.1-1
- [packit] 0.5.1 upstream release

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 18 2023 Packit <hello@packit.dev> - 0.4.1-1
- [packit] 0.4.1 upstream release

* Thu May 18 2023 Packit <hello@packit.dev> - 0.4.0-1
- [packit] 0.4.0 upstream release

* Tue May 16 2023 Packit <hello@packit.dev> - 0.2.0-1
- [packit] 0.2.0 upstream release

* Tue May 09 2023 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1.0-1
- Resolves: #2193400 - initial upload
