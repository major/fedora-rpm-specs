%global modulename dnsconfd
%global selinuxtype targeted

Name:           dnsconfd
Version:        2.2.2
Release:        1%{?dist}
Summary:        Local DNS cache configuration daemon
License:        MIT
URL:            https://github.com/InfrastructureServices/dnsconfd
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        dnsconfd.sysusers

BuildRequires:  pkgconfig(liburiparser) pkgconfig(jansson) pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(glib-2.0) pkgconfig(libsystemd) pkgconfig(gio-2.0) pkgconfig(libidn2)
BuildRequires:  pkgconfig(check)
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  meson gcc
%if 0%{?with_asan}
BuildRequires:  libasan
%endif
%if %{defined fedora} && 0%{?fedora} < 42 || %{defined rhel} && 0%{?rhel} < 11
%{?sysusers_requires_compat}
%endif

Requires:  (%{name}-selinux if selinux-policy-%{selinuxtype})
Requires:  dbus-common
Requires:  %{name}-cache
Suggests:  %{name}-unbound
Requires:  (%{name}-unbound = %{version}-%{release} if %{name}-unbound)
Provides:  %{name}-micro = %{version}-%{release}
Obsoletes: %{name}-micro < %{version}-%{release}

%description
Dnsconfd configures local DNS cache services.

# SELinux subpackage
%package selinux
Summary:             dnsconfd SELinux policy
BuildArch:           noarch
Requires:            %{name} = %{version}-%{release}
Requires:            selinux-policy-%{selinuxtype}
Requires(post):      selinux-policy-%{selinuxtype}
BuildRequires:       selinux-policy-devel
%{?selinux_requires_min}

%description selinux
Dnsconfd SELinux policy module.

%package unbound
Summary:             dnsconfd unbound module
BuildArch:           noarch
Requires:            %{name} = %{version}-%{release}
Requires:            unbound
Provides:            %{name}-cache = %{version}-%{release}

%description unbound
Dnsconfd management of unbound server

%package dracut
Summary:            dnsconfd dracut module
Requires:           %{name} = %{version}-%{release}
Requires:           unbound
Requires:           dracut
Requires:           dracut-network
Requires:           unbound-dracut

%description dracut
Dnsconfd dracut module

%prep
%autosetup

%build
%if 0%{?with_asan}
%meson -Db_sanitize=address -Doptimization=g
%else
%meson
%endif
%meson_build

%if %{defined fedora} && 0%{?fedora} < 40 || %{defined rhel} && 0%{?rhel} < 10
    echo '/var/run/dnsconfd(/.*)? gen_context(system_u:object_r:dnsconfd_var_run_t,s0)' >> distribution/dnsconfd.fc
%endif

%if 0%{?with_asan}
    echo 'allow dnsconfd_t dnsconfd_t:process ptrace;' >> distribution/dnsconfd.te
%endif

make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp

%install
%meson_install
mkdir   -m 0755 -p %{buildroot}%{_datadir}/dbus-1/system.d/
mkdir   -m 0755 -p %{buildroot}%{_datadir}/dbus-1/system-services/
mkdir   -m 0755 -p %{buildroot}%{_sysconfdir}/unbound/conf.d/
mkdir   -m 0755 -p %{buildroot}%{_unitdir}
mkdir   -m 0755 -p %{buildroot}%{_unitdir}/unbound.service.d
mkdir   -m 0755 -p %{buildroot}%{_unitdir}/dnsconfd.service.d
mkdir   -m 0755 -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir   -m 0755 -p %{buildroot}/%{_mandir}/man8
mkdir   -m 0755 -p %{buildroot}/%{_mandir}/man5
mkdir   -m 0755 -p %{buildroot}%{_rundir}/dnsconfd
mkdir   -m 0755 -p %{buildroot}%{_tmpfilesdir}
mkdir   -m 0755 -p %{buildroot}%{_prefix}/lib/dracut/modules.d/70dnsconfd
mkdir   -m 0755 -p %{buildroot}%{_libexecdir}

install -m 0644 -p distribution/com.redhat.dnsconfd.conf %{buildroot}%{_datadir}/dbus-1/system.d/com.redhat.dnsconfd.conf
install -m 0644 -p distribution/com.redhat.dnsconfd.service %{buildroot}%{_datadir}/dbus-1/system-services/com.redhat.dnsconfd.service
install -m 0644 -p distribution/dnsconfd.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/dnsconfd
install -m 0644 -p distribution/dnsconfd.service %{buildroot}%{_unitdir}/dnsconfd.service
install -m 0644 -p distribution/dnsconfd-unbound-control.path %{buildroot}%{_unitdir}/dnsconfd-unbound-control.path
install -m 0644 -p distribution/dnsconfd-unbound-control.service %{buildroot}%{_unitdir}/dnsconfd-unbound-control.service
mkdir   -m 0755 -p %{buildroot}%{_sysconfdir}/dnsconfd/conf.d
install -m 0644 -p distribution/dnsconfd.conf %{buildroot}%{_sysconfdir}/dnsconfd/dnsconfd.conf
install -m 0644 -p distribution/dnsconfd-tmpfiles.conf %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -m 0644 -p distribution/dnsconfd-unbound-tmpfiles.conf %{buildroot}%{_tmpfilesdir}/%{name}-unbound.conf
install -m 0755 -p distribution/dracut_module/module-setup.sh %{buildroot}%{_prefix}/lib/dracut/modules.d/70dnsconfd
install -m 0755 -p distribution/dnsconfd-prepare.sh %{buildroot}%{_libexecdir}/dnsconfd-prepare
install -m 0755 -p distribution/dnsconfd-prepare.sh %{buildroot}%{_libexecdir}/dnsconfd-cleanup
install -m 0755 -p distribution/dnsconfd-unbound-control.sh %{buildroot}%{_libexecdir}/dnsconfd-unbound-control.sh

touch %{buildroot}%{_rundir}/dnsconfd/unbound.conf
chmod 0644 %{buildroot}%{_rundir}/dnsconfd/unbound.conf

# hook to inform us about unbound state
install -m 0644 -p distribution/dnsconfd.service.d-unbound.conf %{buildroot}%{_unitdir}/unbound.service.d/dnsconfd.conf
# hook to enable unbound_control file
install -m 0644 -p distribution/dnsconfd-unbound-control.conf %{buildroot}%{_unitdir}/dnsconfd.service.d/dnsconfd-unbound-control.conf

install -m 0644 -p distribution/unbound-dnsconfd.conf %{buildroot}%{_sysconfdir}/unbound/conf.d/unbound.conf

install -D -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

install -m 0644 -p distribution/dnsconfd.8 %{buildroot}/%{_mandir}/man8/dnsconfd.8
install -m 0644 -p distribution/dnsconfd-config.8 %{buildroot}/%{_mandir}/man8/dnsconfd-config.8
install -m 0644 -p distribution/dnsconfd-reload.8 %{buildroot}/%{_mandir}/man8/dnsconfd-reload.8
install -m 0644 -p distribution/dnsconfd-status.8 %{buildroot}/%{_mandir}/man8/dnsconfd-status.8
install -m 0644 -p distribution/dnsconfd.conf.5 %{buildroot}/%{_mandir}/man5/dnsconfd.conf.5

install -p -D -m 0644 distribution/dnsconfd.sysusers %{buildroot}%{_sysusersdir}/dnsconfd.conf

%check
%meson_test

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} -p 200 %{modulename}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%if %{defined fedora} && 0%{?fedora} < 42 || %{defined rhel} && 0%{?rhel} < 11
%pre
%sysusers_create_compat %{SOURCE1}

%pre unbound
%sysusers_create_compat %{SOURCE1}
%endif

%post unbound
%systemd_post dnsconfd-unbound-control.path

%preun unbound
%systemd_preun dnsconfd-unbound-control.path

%postun unbound
%systemd_postun dnsconfd-unbound-control.path

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%posttrans
# Warn about legacy /etc/dnsconfd.conf left behind after upgrade from < 2.1.0
if [ -s %{_sysconfdir}/dnsconfd.conf.rpmsave ] && [ ! -L %{_sysconfdir}/dnsconfd.conf.rpmsave ]; then
    echo "dnsconfd: WARNING: legacy configuration found at %{_sysconfdir}/dnsconfd.conf.rpmsave" >&2
    echo "  The configuration file has moved to %{_sysconfdir}/dnsconfd/dnsconfd.conf." >&2
    echo "  Please move your customizations to the new location and remove the old file." >&2
fi

%files
%license LICENSE
%{_bindir}/dnsconfd
%{_datadir}/dbus-1/system.d/com.redhat.dnsconfd.conf
%{_datadir}/dbus-1/system-services/com.redhat.dnsconfd.service
%config(noreplace) %{_sysconfdir}/sysconfig/dnsconfd
%dir %{_sysconfdir}/dnsconfd
%dir %{_sysconfdir}/dnsconfd/conf.d
%config(noreplace) %{_sysconfdir}/dnsconfd/dnsconfd.conf
%{_unitdir}/dnsconfd.service
%{_libexecdir}/dnsconfd-prepare
%{_libexecdir}/dnsconfd-cleanup
%{_mandir}/man8/dnsconfd*.8*
%{_mandir}/man5/dnsconfd.conf.5*
%{_sysusersdir}/dnsconfd.conf
%doc README.md docs/com.redhat.dnsconfd.md
%dir %attr(755,dnsconfd,dnsconfd) %{_rundir}/dnsconfd
%{_tmpfilesdir}/%{name}.conf

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.*
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}

%files unbound
%{_unitdir}/unbound.service.d/dnsconfd.conf
%{_unitdir}/dnsconfd.service.d/dnsconfd-unbound-control.conf
%config(noreplace) %attr(644,unbound,unbound) %{_sysconfdir}/unbound/conf.d/unbound.conf
%attr(664,dnsconfd,dnsconfd) %{_rundir}/dnsconfd/unbound.conf
%{_sysusersdir}/dnsconfd.conf
%{_tmpfilesdir}/dnsconfd-unbound.conf
%{_unitdir}/dnsconfd-unbound-control.path
%{_unitdir}/dnsconfd-unbound-control.service
%{_libexecdir}/dnsconfd-unbound-control.sh

%files dracut
%{_prefix}/lib/dracut/modules.d/70dnsconfd

%changelog
%autochangelog
