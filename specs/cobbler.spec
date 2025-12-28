%global tftpboot_dir %{_sharedstatedir}/tftpboot/

%global commit 700eb5bdfb28baba4de5e4083bec9e132a763bcb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global selinuxtype targeted

# Tests require an installed system with root access
%bcond check 0

Name:           cobbler
Version:        3.3.7
Release:        %autorelease
Summary:        Boot server configurator
URL:            https://cobbler.github.io/
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Source0:        https://github.com/cobbler/cobbler/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        migrate-settings.sh
Source2:        %{name}.te
Source3:        %{name}.if
Source4:        %{name}.fc

# Do not run coverage tests
Patch0:         cobbler-nocov.patch
# Python 3.13 support (backport of https://github.com/cobbler/cobbler/pull/3842)
# https://bugzilla.redhat.com/show_bug.cgi?id=2335620
Patch1:         cobbler-python3.13.patch
# Upstream fix for reposync --tries
# https://bugzilla.redhat.com/show_bug.cgi?id=2401605
# Backport of https://github.com/cobbler/cobbler/pull/3378
Patch2:         cobbler-reposync.patch
# Use systemctl is-active to prevent some SELinux denials checking service status
# https://bugzilla.redhat.com/show_bug.cgi?id=2353898
Patch3:         https://github.com/cobbler/cobbler/pull/3945.patch
BuildArch:      noarch

BuildRequires: make
BuildRequires: python%{python3_pkgversion}-devel
# Cheetah switched names from Cheetah3 to CT3 in its metadata in version 3.3.0.
# https://github.com/CheetahTemplate3/cheetah3/commit/673259b2d139b4ea970b1c2da12607b7ac39cbec
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 10
BuildRequires: %{py3_dist ct3}
%else
BuildRequires: %{py3_dist cheetah3}
%endif
BuildRequires: %{py3_dist distro}
BuildRequires: %{py3_dist netaddr}
BuildRequires: %{py3_dist pyyaml}
BuildRequires: %{py3_dist requests}
BuildRequires: %{py3_dist schema}
BuildRequires: %{py3_dist setuptools}
# For docs
BuildRequires: %{py3_dist sphinx}
%if %{with check}
# For tests
BuildRequires: %{py3_dist crypt-r}
BuildRequires: %{py3_dist dnspython}
BuildRequires: %{py3_dist file-magic}
BuildRequires: %{py3_dist pytest-benchmark}
%endif

# This ensures that the *-selinux package and all it’s dependencies are not pulled
# into containers and other systems that do not use SELinux
Requires: (%{name}-selinux if selinux-policy-%{selinuxtype})

Requires: httpd
Requires: tftp-server
Requires: dosfstools
Requires: createrepo_c
Requires: rsync
Requires: xorriso

Requires: genisoimage
# Not everyone wants bash-completion...?
Recommends: bash-completion
Requires: dnf-plugins-core
# syslinux is only available on x86
Requires: (syslinux if (filesystem(x86-64) or filesystem(x86-32)))
# grub2 efi stuff is only available on x86
Recommends: grub2-efi-ia32
Recommends: grub2-efi-x64
Recommends: logrotate
Recommends: %{py3_dist librepo}
Obsoletes: cobbler-web < 3.3

BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Cobbler is a network install server. Cobbler supports PXE, ISO
virtualized installs, and re-installing existing Linux machines. The
last two modes use a helper tool, 'koan', that integrates with cobbler.
Cobbler's advanced features include importing distributions from DVDs
and rsync mirrors, kickstart templating, integrated yum mirroring, and
built-in DHCP/DNS Management. Cobbler has a XML-RPC API for integration
with other applications.


%package selinux
Summary:        SELinux policies for %{name}
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel
BuildArch:      noarch
%{?selinux_requires}


%description selinux
SELinux policies for %{name}.


%package tests
Summary:        Unit tests for cobbler
Requires:       cobbler = %{version}-%{release}

%description tests
Unit test files from the Cobbler project.


%package tests-containers
Summary:        Dockerfiles and scripts to setup testing containers
Requires:       cobbler = %{version}-%{release}

%description tests-containers
Dockerfiles and scripts to setup testing containers.


%prep
%autosetup -p1
mkdir -p selinux
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} selinux/

# Cheetah switched names from Cheetah3 to CT3 in its metadata in version 3.3.0.
# https://github.com/CheetahTemplate3/cheetah3/commit/673259b2d139b4ea970b1c2da12607b7ac39cbec
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 10
sed -e 's/Cheetah3/CT3/' -i setup.py
%endif


%build
. ./distro_build_configs.sh
%py3_build
make man

# SELinux
make -f %{_datadir}/selinux/devel/Makefile %{name}.pp
bzip2 -9 %{name}.pp


%install
. ./distro_build_configs.sh
# bypass install errors ( don't chown in install step)
%py3_install ||:

# cobbler
rm %{buildroot}%{_sysconfdir}/cobbler/cobbler.conf

mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mv %{buildroot}%{_sysconfdir}/cobbler/cobblerd_rotate %{buildroot}%{_sysconfdir}/logrotate.d/cobblerd

# Create data directories in tftpboot_dir
mkdir -p %{buildroot}%{tftpboot_dir}/{boot,etc,grub/system{,_link},images{,2},ppc,pxelinux.cfg,s390x}

# systemd - move to proper location
mkdir -p %{buildroot}%{_unitdir}
mv %{buildroot}%{_sysconfdir}/cobbler/cobblerd.service %{buildroot}%{_unitdir}

# ghosted files
touch %{buildroot}%{_sharedstatedir}/cobbler/web.ss

# migrate-settings.sh
install -p -m0755 %SOURCE1 %{buildroot}%{_datadir}/cobbler/bin/migrate-settings.sh

# SELinux
install -D -m 0644 %{name}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
install -D -p -m 0644 selinux/%{name}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{name}.if


%if %{with check}
%check
%pytest -v
%endif


%pre
if [ $1 -ge 2 ]; then
    # package upgrade: backup configuration
    DATE=$(date "+%%Y%%m%%d-%%H%%M%%S")
    if [ ! -d "%{_sharedstatedir}/cobbler/backup/upgrade-${DATE}" ]; then
        mkdir -p "%{_sharedstatedir}/cobbler/backup/upgrade-${DATE}"
    fi
    for i in "config" "snippets" "templates" "triggers" "scripts"; do
        if [ -d "%{_sharedstatedir}/cobbler/${i}" ]; then
            cp -r "%{_sharedstatedir}/cobbler/${i}" "%{_sharedstatedir}/cobbler/backup/upgrade-${DATE}"
        fi
    done
    if [ -d %{_sysconfdir}/cobbler ]; then
        cp -r %{_sysconfdir}/cobbler "%{_sharedstatedir}/cobbler/backup/upgrade-${DATE}"
    fi
fi

%post
%systemd_post cobblerd.service
# Fixup permission for world readable settings files
chmod 640 %{_sysconfdir}/cobbler/settings.yaml
chmod 600 %{_sysconfdir}/cobbler/mongodb.conf
chmod 600 %{_sysconfdir}/cobbler/modules.conf
chmod 640 %{_sysconfdir}/cobbler/users.conf
chmod 640 %{_sysconfdir}/cobbler/users.digest
chmod 750 %{_sysconfdir}/cobbler/settings.d
chmod 640 %{_sysconfdir}/cobbler/settings.d/*
chgrp apache %{_sysconfdir}/cobbler/settings.yaml
chgrp apache %{_sysconfdir}/cobbler/users.conf
chgrp apache %{_sysconfdir}/cobbler/users.digest
chgrp apache %{_sysconfdir}/cobbler/settings.d
chgrp apache %{_sysconfdir}/cobbler/settings.d/*
# Change from apache
if [ -f %{_sharedstatedir}/cobbler/web.ss ]; then
    chown root %{_sharedstatedir}/cobbler/web.ss
fi

%posttrans
# Migrate pre-3.2.1 settings to settings.yaml
if [ -f %{_sysconfdir}/cobbler/settings.rpmsave ]; then
    echo warning: migrating old settings to settings.yaml
    mv %{_sysconfdir}/cobbler/settings.yaml{,.rpmnew}
    cp -a %{_sysconfdir}/cobbler/settings.{rpmsave,rpmorig}
    mv %{_sysconfdir}/cobbler/settings.{rpmsave,yaml}
    %{_datadir}/cobbler/bin/migrate-settings.sh
fi
# Add some missing options if needed
grep -q '^reposync_rsync_flags:' %{_sysconfdir}/cobbler/settings.yaml || echo -e '#ADDED:\nreposync_rsync_flags: "-rltDv --copy-unsafe-links"' >> %{_sysconfdir}/cobbler/settings.yaml

%preun
%systemd_preun cobblerd.service

%postun
%systemd_postun_with_restart cobblerd.service


%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}

if [ "$1" -le "1" ]; then # First install
   # the daemon needs to be restarted for the custom label to be applied
   %systemd_postun_with_restart cobblerd.service
fi

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}
    %selinux_relabel_post -s %{selinuxtype}
fi


%files
%license COPYING
%doc AUTHORS.in README.md
%doc docs/developer-guide.rst docs/quickstart-guide.rst docs/installation-guide.rst
%dir %{_sysconfdir}/cobbler
%config(noreplace) %{_sysconfdir}/cobbler/auth.conf
%config(noreplace) %{_sysconfdir}/cobbler/boot_loader_conf/
%config(noreplace) %{_sysconfdir}/cobbler/cheetah_macros
%config(noreplace) %{_sysconfdir}/cobbler/dhcp.template
%config(noreplace) %{_sysconfdir}/cobbler/dhcp6.template
%config(noreplace) %{_sysconfdir}/cobbler/dnsmasq.template
%config(noreplace) %{_sysconfdir}/cobbler/genders.template
%config(noreplace) %{_sysconfdir}/cobbler/import_rsync_whitelist
%config(noreplace) %{_sysconfdir}/cobbler/iso/
%config(noreplace) %{_sysconfdir}/cobbler/logging_config.conf
%attr(600, root, root) %config(noreplace) %{_sysconfdir}/cobbler/modules.conf
%attr(600, root, root) %config(noreplace) %{_sysconfdir}/cobbler/mongodb.conf
%config(noreplace) %{_sysconfdir}/cobbler/named.template
%config(noreplace) %{_sysconfdir}/cobbler/ndjbdns.template
%config(noreplace) %{_sysconfdir}/cobbler/reporting/
%config(noreplace) %{_sysconfdir}/cobbler/rsync.exclude
%config(noreplace) %{_sysconfdir}/cobbler/rsync.template
%config(noreplace) %{_sysconfdir}/cobbler/secondary.template
%attr(640, root, apache) %config(noreplace) %{_sysconfdir}/cobbler/settings.yaml
%attr(750, root, apache) %dir %{_sysconfdir}/cobbler/settings.d
%attr(640, root, apache) %config(noreplace) %{_sysconfdir}/cobbler/settings.d/bind_manage_ipmi.settings
%attr(640, root, apache) %config(noreplace) %{_sysconfdir}/cobbler/settings.d/manage_genders.settings
%attr(640, root, apache) %config(noreplace) %{_sysconfdir}/cobbler/settings.d/nsupdate.settings
%attr(640, root, apache) %config(noreplace) %{_sysconfdir}/cobbler/settings.d/windows.settings
%attr(640, root, apache) %config(noreplace) %{_sysconfdir}/cobbler/users.conf
%attr(640, root, apache) %config(noreplace) %{_sysconfdir}/cobbler/users.digest
%config(noreplace) %{_sysconfdir}/cobbler/version
%config(noreplace) %{_sysconfdir}/cobbler/windows/
%config(noreplace) %{_sysconfdir}/cobbler/zone.template
%config(noreplace) %{_sysconfdir}/cobbler/zone_templates/
%config(noreplace) %{_sysconfdir}/logrotate.d/cobblerd
%config(noreplace) /etc/httpd/conf.d/cobbler.conf
%{_bindir}/cobbler
%{_bindir}/cobbler-settings
%{_bindir}/cobbler-ext-nodes
%{_bindir}/cobblerd
%{_datadir}/bash-completion/
%dir %{_datadir}/cobbler
%{_datadir}/cobbler/bin
%{_mandir}/man1/cobbler.1*
%{_mandir}/man5/cobbler.conf.5*
%{_mandir}/man8/cobblerd.8*
%{python3_sitelib}/cobbler/
%{python3_sitelib}/cobbler*.egg-info
%{_unitdir}/cobblerd.service
%{tftpboot_dir}/*
/var/www/cobbler
%dir %{_sharedstatedir}/cobbler
%ghost %attr(0755,root,root) %{_sharedstatedir}/cobbler/backup/
%config(noreplace) %{_sharedstatedir}/cobbler/collections/
%config(noreplace) %{_sharedstatedir}/cobbler/distro_signatures.json
%config(noreplace) %{_sharedstatedir}/cobbler/grub_config/
%config(noreplace) %{_sharedstatedir}/cobbler/loaders/
%config(noreplace) %{_sharedstatedir}/cobbler/scripts/
%config(noreplace) %{_sharedstatedir}/cobbler/snippets/
%config(noreplace) %{_sharedstatedir}/cobbler/templates/
%config(noreplace) %{_sharedstatedir}/cobbler/triggers/
%ghost %attr(0644,root,root) %{_sharedstatedir}/cobbler/lock
# Currently used for cli auth
%ghost %attr(0644,root,root) %{_sharedstatedir}/cobbler/web.ss
/var/log/cobbler

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.*
%{_datadir}/selinux/devel/include/distributed/%{name}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{name}

%files tests
%{_datadir}/cobbler/tests/

%files tests-containers
%{_datadir}/cobbler/docker/


%changelog
%autochangelog
