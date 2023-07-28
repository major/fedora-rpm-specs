%global _hardened_build 1

#%%global snapshot 20150714

Summary: Tool for dynamic reconfiguration of validating resolver Unbound
Name: dnssec-trigger
Version: 0.17
Release: %autorelease
License: BSD-3-clause AND MIT AND ISC
Url: https://www.nlnetlabs.nl/projects/dnssec-trigger/

%if 0%{?snapshot:1}
# generated using './makedist.sh -s' in the cloned upstream trunk
Source0: %{name}-%{version}_%{snapshot}.tar.gz
%else
Source0: https://www.nlnetlabs.nl/downloads/dnssec-trigger/%{name}-%{version}.tar.gz
Source1: https://www.nlnetlabs.nl/downloads/dnssec-trigger/%{name}-%{version}.tar.gz.asc
Source2: https://keys.openpgp.org/vks/v1/by-fingerprint/EDFAA3F2CA4E6EB05681AF8E9F6F1C2D7E045F8D#/wouter.asc
%endif
Source3: dnssec-trigger.tmpfiles.d
#Source4: dnssec-trigger-default.conf
#Source5: dnssec-trigger-workstation.conf
Source6: ssh_config.conf

# Patches
# Downstream changes to configuration
Patch1: dnssec-trigger-config-workstation.patch
# Downstream changes to configuration
Patch2: dnssec-trigger-config-default.patch
Patch3: 0003-Move-the-NetworkManager-dispatcher-script-out-of-etc.patch
# https://github.com/NLnetLabs/dnssec-trigger/pull/7
Patch4: 0004-Add-options-edns0-and-trust-ad.patch
Patch5: dnssec-trigger-configure-c99.patch
# https://github.com/NLnetLabs/dnssec-trigger/commit/f187c2be221a26f3c4ef4d9b16f1df67104ae634
Patch6: dnssec-trigger-0.17-allowed-characters.patch

# to obsolete the version in which the panel was in main package
Obsoletes: %{name} < 0.12-22
Suggests: %{name}-panel
# Require a version of NetworkManager that doesn't forget to issue dhcp-change
# https://bugzilla.redhat.com/show_bug.cgi?id=1112248
%if 0%{?rhel} >= 9 || 0%{?fedora} >= 31
Requires: NetworkManager >= 1.20
%elif 0%{?rhel} >= 7
Requires: NetworkManager >= 0.9.9.1-13
%elif 0%{?fedora} >= 21
Requires: NetworkManager >= 0.9.9.95-1
%else
Requires: NetworkManager >= 0.9.9.0-40
%endif
Requires: ldns >= 1.6.10, NetworkManager-libnm, unbound
# needed by /usr/sbin/dnssec-trigger-control-setup
# otherwise it ends with error: /usr/sbin/dnssec-trigger-control-setup: line 180: openssl: command not found
Requires: openssl
# needed for /usr/bin/chattr
Requires: e2fsprogs
BuildRequires: openssl-devel, ldns-devel, python3-devel, gcc
BuildRequires: NetworkManager-libnm-devel
%if 0%{?fedora} && ! 0%{?snapshot:1}
BuildRequires: gnupg2
%endif

BuildRequires: systemd-rpm-macros
%{?systemd_ordering}

# Provides Workstation specific configuration
# - No captive portal detection and no action available on Captive portal (No UI)
Provides: variant_config(Workstation)

%description
dnssec-trigger reconfigures the local Unbound DNS server. Unbound is a
resolver performing DNSSEC validation. dnssec-trigger is a set of daemon
and script. On every network configuration change dnssec-trigger performs
set of tests and configures Unbound based on the current NetworkManager
configuration, its own configuration and results of performed tests.


%package panel
Summary: Applet for interaction between the user and dnssec-trigger
Requires: %{name} = %{version}-%{release}
Obsoletes: %{name} < 0.12-22
Requires: xdg-utils
BuildRequires: gtk2-devel, desktop-file-utils
BuildRequires: make

%description panel
This package provides the GTK panel for interaction between the user
and dnssec-trigger daemon. It is able to show the current state and
results of probing performed by dnssec-trigger daemon. Also in case
some user input is needed, the panel creates a dialog window.


%prep
%if 0%{?fedora} && ! 0%{?snapshot:1}
%gpgverify -d 0 -s 1 -k 2
%endif
%autosetup %{?snapshot:-n %{name}-%{version}_%{snapshot}} -N
%autopatch -m 3 -p1

# don't use DNSSEC for forward zones for now
sed -i "s/validate_connection_provided_zones=yes/validate_connection_provided_zones=no/" dnssec.conf


%build
%configure  \
    --with-keydir=%{_sysconfdir}/dnssec-trigger \
    --with-hooks=networkmanager \
%if 0%{?rhel} < 9 && 0%{?fedora} < 31
    --with-networkmanager-dispatch=%{_sysconfdir}/NetworkManager/dispatcher.d \
%endif
    --with-python=%{__python3} \
    --with-pidfile=%{_rundir}/%{name}d.pid \
    --with-login-command=%{_bindir}/xdg-open \
    --with-login-location="http://hotspot-nocache.fedoraproject.org/"

# hotspot-nocache should have TTL=0

%make_build

%autopatch -p1 2
cp -p example.conf dnssec-trigger-workstation.conf
%autopatch -p1 1


%install
# https://github.com/NLnetLabs/dnssec-trigger/pull/13
install -d -m 0755 %{buildroot}%{_libexecdir}
%make_install

install -d 0755 %{buildroot}%{_unitdir}
install -p -m 0644 example.conf %{buildroot}%{_sysconfdir}/%{name}/dnssec-trigger-default.conf
install -p -m 0644 dnssec-trigger-workstation.conf %{buildroot}%{_sysconfdir}/%{name}/

desktop-file-install --dir=%{buildroot}%{_datadir}/applications dnssec-trigger-panel.desktop

# install the configuration for /var/run/dnssec-trigger into tmpfiles.d dir
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 644 %{SOURCE3} ${RPM_BUILD_ROOT}%{_tmpfilesdir}/%{name}.conf
# we must create the /var/run/dnssec-trigger directory
mkdir -p %{buildroot}%{_localstatedir}/run
install -d -m 0755 %{buildroot}%{_localstatedir}/run/%{name}

# supress the panel name everywhere including the gnome3 panel at the bottom
ln -s dnssec-trigger-panel %{buildroot}%{_bindir}/dnssec-trigger

# Make dnssec-trigger.8 manpage available under names of all dnssec-trigger-*
# executables
for all in dnssec-trigger-control dnssec-trigger-control-setup dnssec-triggerd; do
    ln -s dnssec-trigger.8 %{buildroot}/%{_mandir}/man8/"$all".8
done
ln -s dnssec-trigger.8 %{buildroot}/%{_mandir}/man8/dnssec-trigger.conf.8

install -d -m 0755 %{buildroot}%{_sysconfdir}/ssh/ssh_config.d
install -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/ssh/ssh_config.d/10-%{name}.conf

%post
%systemd_post %{name}d.service

%preun
%systemd_preun %{name}d.service

%postun
%systemd_postun_with_restart %{name}d.service

%posttrans
# If we don't yet have a symlink or existing file for dnssec-trigger.conf,
# create it..
if [ ! -e %{_sysconfdir}/%{name}/dnssec-trigger.conf ]; then
    # Import /etc/os-release to get the variant definition
    . /etc/os-release || :

    case "$VARIANT_ID" in
        workstation)
            ln -sf %{name}-workstation.conf %{_sysconfdir}/%{name}/dnssec-trigger.conf || :
            ;;
        *)
            ln -sf %{name}-default.conf %{_sysconfdir}/%{name}/dnssec-trigger.conf || :
            ;;
        esac
fi



%files
%license LICENSE
%doc README
%{_bindir}/dnssec-trigger
%{_sbindir}/dnssec-trigger*
%{_libexecdir}/dnssec-trigger-script
%{_unitdir}/%{name}d.service
%{_unitdir}/%{name}d-keygen.service
%if 0%{?rhel} >= 9 || 0%{?fedora} >= 31
%attr(0755,root,root) %{_prefix}/lib/NetworkManager/dispatcher.d/01-dnssec-trigger
%else
%attr(0755,root,root) %{_sysconfdir}/NetworkManager/dispatcher.d/01-dnssec-trigger
%endif
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/dnssec.conf
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}
%attr(0644,root,root) %ghost %config(noreplace) %{_sysconfdir}/%{name}/dnssec-trigger.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/dnssec-trigger-default.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/dnssec-trigger-workstation.conf
%attr(0755,root,root) %dir %{_sysconfdir}/ssh/ssh_config.d
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/ssh/ssh_config.d/10-%{name}.conf
%dir %{_localstatedir}/run/%{name}
%{_tmpfilesdir}/%{name}.conf
%{_mandir}/man8/dnssec-trigger*

%files panel
%{_bindir}/dnssec-trigger-panel
%attr(0755,root,root) %dir %{_datadir}/%{name}
%attr(0644,root,root) %{_datadir}/%{name}/*
%attr(0644,root,root) %{_datadir}/applications/dnssec-trigger-panel.desktop
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/xdg/autostart/dnssec-trigger-panel.desktop


%changelog
%autochangelog
