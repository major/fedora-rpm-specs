%if 0%{?rhel}
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           cloud-init
Version:        25.3
Release:        %autorelease
Summary:        Cloud instance init scripts
License:        Apache-2.0 OR GPL-3.0-only
URL:            https://github.com/canonical/cloud-init

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        cloud-init-tmpfiles.conf

# https://github.com/canonical/cloud-init/pull/6423
# Fixes systemd dependency cycle on Fedora by adding DefaultDependencies=no
# and including Fedora in distribution-specific conditional blocks
Patch:          0001-fix-avoid-dependency-cycle-on-Fedora.patch

BuildArch:      noarch

BuildRequires:  systemd-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  meson

%if %{with tests}
BuildRequires:  iproute
BuildRequires:  passwd
BuildRequires:  procps-ng
# dnf is needed to make cc_ntp unit tests work
# https://bugs.launchpad.net/cloud-init/+bug/1721573
BuildRequires:  /usr/bin/dnf
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(responses)
BuildRequires:  python3dist(passlib)
BuildRequires:  python3dist(pyserial)
%endif

Requires:       dhcpcd

Requires:       hostname
Requires:       e2fsprogs
Requires:       iproute
Requires:       python3-libselinux
# cloud-init builds with meson and continues to install an egg-info directory.
# It's not clear if it's possible to use the Python auto-generated run-time requirement
# with cloud-init's current setup. Something to try to fix upstream, I suppose.
Requires:       %{py3_dist configobj}
Requires:       %{py3_dist jinja2}
Requires:       %{py3_dist jsonpatch}
Requires:       %{py3_dist jsonschema}
Requires:       %{py3_dist oauthlib}
Requires:       %{py3_dist pyyaml}
Requires:       %{py3_dist requests}
Requires:       policycoreutils-python3
Requires:       procps
Requires:       shadow-utils
Requires:       util-linux
Requires:       xfsprogs
Requires:       openssl
Requires:       /usr/bin/nc

%{?systemd_requires}


%description
Cloud-init is a set of init scripts for cloud instances.  Cloud instances
need special scripts to run during initialization to retrieve and install
ssh keys and to let the user run various scripts.


%prep
%autosetup -p1

# Removing shebang manually because of rpmlint, will update upstream later
sed -i -e 's|#!/usr/bin/python||' cloudinit/cmd/main.py

# Use unittest from the standard library. unittest2 is old and being
# retired in Fedora. See https://bugzilla.redhat.com/show_bug.cgi?id=1794222
find tests/ -type f | xargs sed -i s/unittest2/unittest/
find tests/ -type f | xargs sed -i s/assertItemsEqual/assertCountEqual/

%generate_buildrequires
%pyproject_buildrequires -N requirements.txt


%conf
%meson -Dinit_system=systemd -Ddisable_sshd_keygen=true


%build
%meson_build


%install
%meson_install
%py3_shebang_fix %{buildroot}%{_bindir}/

mkdir -p $RPM_BUILD_ROOT/var/lib/cloud

# /run/cloud-init needs a tmpfiles.d entry
mkdir -p $RPM_BUILD_ROOT/run/cloud-init
mkdir -p $RPM_BUILD_ROOT/%{_tmpfilesdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT/%{_tmpfilesdir}/%{name}.conf

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/rsyslog.d
cp -p tools/21-cloudinit.conf $RPM_BUILD_ROOT/%{_sysconfdir}/rsyslog.d/21-cloudinit.conf


%check
%if %{with tests}
%py3_check_import cloudinit
%meson test -C builddir -v
%else
%py3_check_import cloudinit
%endif

%post
%systemd_post cloud-config.service cloud-config.target cloud-final.service cloud-init-main.service cloud-init.target cloud-init-local.service cloud-init-network.service


%preun
%systemd_preun cloud-config.service cloud-config.target cloud-final.service cloud-init-main.service cloud-init.target cloud-init-local.service cloud-init-network.service


%postun
%systemd_postun cloud-config.service cloud-config.target cloud-final.service cloud-init-main.service cloud-init.target cloud-init-local.service cloud-init-network.service


%files
%license LICENSE LICENSE-Apache2.0 LICENSE-GPLv3
%doc ChangeLog
%doc doc/*
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/cloud/cloud.cfg
%dir               %{_sysconfdir}/cloud/cloud.cfg.d
%config(noreplace) %{_sysconfdir}/cloud/cloud.cfg.d/*.cfg
%doc               %{_sysconfdir}/cloud/cloud.cfg.d/README
%dir               %{_sysconfdir}/cloud/templates
%config(noreplace) %{_sysconfdir}/cloud/templates/*
%dir               %{_sysconfdir}/rsyslog.d
%config(noreplace) %{_sysconfdir}/rsyslog.d/21-cloudinit.conf
%{_udevrulesdir}/66-azure-ephemeral.rules
%{_unitdir}/cloud-config.service
%{_unitdir}/cloud-final.service
%{_unitdir}/cloud-init-main.service
%{_unitdir}/cloud-init-local.service
%{_unitdir}/cloud-init-network.service
%{_unitdir}/cloud-config.target
%{_unitdir}/cloud-init.target
%{_unitdir}/cloud-init-hotplugd.service
%{_unitdir}/cloud-init-hotplugd.socket
%{_unitdir}/sshd-keygen@.service.d/disable-sshd-keygen-if-cloud-init-active.conf
%{_systemdgeneratordir}/cloud-init-generator
%{_tmpfilesdir}/%{name}.conf
%{python3_sitelib}/*
%{_libexecdir}/%{name}
%{_bindir}/cloud-init*
%{_bindir}/cloud-id
%dir /run/cloud-init
%dir /var/lib/cloud
%{_datadir}/bash-completion/completions/cloud-init


%changelog
%autochangelog
