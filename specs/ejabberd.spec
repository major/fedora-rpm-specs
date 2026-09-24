%global _hardened_build 1
%global srcname ejabberd

# Since we require the version in both BuildRequires and Requires, let's make these variables for
# easier maintenance.
%global cache_tab_ver 1.0.34
%global eimp_ver 1.0.27
%global epam_ver 1.0.14
%global erlydtl_ver 0.15.0
%global esip_ver 1.0.60
%global ezlib_ver 1.0.16
%global fast_tls_ver 1.1.26
%global fast_xml_ver 1.1.60
%global fast_yaml_ver 1.0.40
%global idna_ver 7.1.0
%global jose_ver 1.11.12
%global luerl_ver 1.2.0
%global mqtree_ver 1.0.20
%global p1_acme_ver 1.0.31
%global p1_mysql_ver 1.0.28
%global p1_oauth2_ver 0.6.14
%global p1_pgsql_ver 1.1.41
%global p1_utils_ver 1.0.29
%global pkix_ver 1.0.10
%global stringprep_ver 1.0.34
%global stun_ver 1.2.22
%global xmpp_ver 1.13.4
%global yconf_ver 1.0.23

# Define SELinux policy variables
%global selinuxtype targeted
%global selinux_policyver 3.14.2
%global moduletype contrib
%global modulename ejabberd


Name:           ejabberd
Version:        26.07
Release:        %autorelease
BuildArch:      noarch

# The bulk of the code is GPL-2.0-or-later. The MQTT modules (src/mod_mqtt*.erl,
# src/mqtt_codec.erl, include/mqtt.hrl) are Apache-2.0. The bundled JavaScript
# in priv/js and priv/mod_invites/static is MIT.
License:        GPL-2.0-or-later AND Apache-2.0 AND MIT AND BSD-3-Clause
Summary:        A distributed, fault-tolerant Jabber/XMPP server
URL:            https://www.ejabberd.im/
VCS:            git:https://github.com/processone/ejabberd.git
Source0:        https://github.com/processone/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source2:        ejabberd.logrotate

# Support for systemd
Source4:        ejabberd.service

# PAM support
Source9:        ejabberdctl.pam
Source11:       ejabberd.pam

# polkit support
Source12:       ejabberdctl.polkit.actions
Source13:       ejabberdctl.polkit.rules
# SELinux module
Source14:       ejabberd.te
Source15:       ejabberd.fc
Source16:       ejabberd.if
# systemd-sysusers config
Source17:       ejabberd.sysusers


BuildRequires:  erlang-cache_tab >= %{cache_tab_ver}
BuildRequires:  erlang-eimp >= %{eimp_ver}
BuildRequires:  erlang-epam >= %{epam_ver}
BuildRequires:  erlang-erlydtl >= %{erlydtl_ver}
BuildRequires:  erlang-esip >= %{esip_ver}
BuildRequires:  erlang-ezlib >= %{ezlib_ver}
BuildRequires:  erlang-fast_tls >= %{fast_tls_ver}
BuildRequires:  erlang-fast_xml >= %{fast_xml_ver}
BuildRequires:  erlang-fast_yaml >= %{fast_yaml_ver}
BuildRequires:  erlang-idna >= %{idna_ver}
BuildRequires:  erlang-jose >= %{jose_ver}
BuildRequires:  erlang-luerl >= %{luerl_ver}
# For the eunit tests
BuildRequires:  erlang-meck
BuildRequires:  erlang-mqtree >= %{mqtree_ver}
BuildRequires:  erlang-odbc
BuildRequires:  erlang-p1_acme >= %{p1_acme_ver}
BuildRequires:  erlang-p1_mysql >= %{p1_mysql_ver}
BuildRequires:  erlang-p1_oauth2 >= %{p1_oauth2_ver}
BuildRequires:  erlang-p1_pgsql >= %{p1_pgsql_ver}
BuildRequires:  erlang-p1_utils >= %{p1_utils_ver}
BuildRequires:  erlang-pkix >= %{pkix_ver}
BuildRequires:  erlang-provider_asn1
BuildRequires:  erlang-rebar3
BuildRequires:  erlang-rebar3-pc
BuildRequires:  erlang-stringprep >= %{stringprep_ver}
BuildRequires:  erlang-stun >= %{stun_ver}
BuildRequires:  erlang-xmpp >= %{xmpp_ver}
BuildRequires:  erlang-yconf >= %{yconf_ver}
BuildRequires:  expat-devel >= 1.95
BuildRequires:  git
BuildRequires:  libyaml-devel >= 0.1.4
BuildRequires:  openssl-devel >= 1.0.0
BuildRequires:  pam-devel
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-rpm-macros

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make

Requires(post): libselinux-utils
Requires(post): policycoreutils
Requires(post): policycoreutils-python-utils
Requires(post): selinux-policy-base >= %{selinux_policyver}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

# Minified JavaScript libraries shipped by upstream without version information
# https://github.com/davidshimjs/qrcodejs
Provides: bundled(js-qrcode)
# https://github.com/bestiejs/platform.js
Provides: bundled(js-platform)
# https://github.com/tofsjonas/sortable
Provides: bundled(js-sortable)

Requires: selinux-policy >= %{selinux_policyver}
Obsoletes: ejabberd-selinux < 26.07

# From rebar
Requires:  erlang-cache_tab >= %{cache_tab_ver}
Requires:  erlang-eimp >= %{eimp_ver}
Requires:  erlang-epam >= %{epam_ver}
Requires:  erlang-erlydtl >= %{erlydtl_ver}
Requires:  erlang-esip >= %{esip_ver}
Requires:  erlang-ezlib >= %{ezlib_ver}
Requires:  erlang-fast_tls >= %{fast_tls_ver}
Requires:  erlang-fast_xml >= %{fast_xml_ver}
Requires:  erlang-fast_yaml >= %{fast_yaml_ver}
Requires:  erlang-idna >= %{idna_ver}
Requires:  erlang-jose >= %{jose_ver}
Requires:  erlang-luerl >= %{luerl_ver}
Requires:  erlang-mqtree >= %{mqtree_ver}
Requires:  erlang-odbc
Requires:  erlang-os_mon
Requires:  erlang-p1_acme >= %{p1_acme_ver}
Requires:  erlang-p1_mysql >= %{p1_mysql_ver}
Requires:  erlang-p1_oauth2 >= %{p1_oauth2_ver}
Requires:  erlang-p1_pgsql >= %{p1_pgsql_ver}
Requires:  erlang-p1_utils >= %{p1_utils_ver}
Requires:  erlang-pkix >= %{pkix_ver}
Requires:  erlang-stringprep >= %{stringprep_ver}
Requires:  erlang-stun >= %{stun_ver}
Requires:  erlang-xmpp >= %{xmpp_ver}
Requires:  erlang-yconf >= %{yconf_ver}
# We install a logrotate.d file
Requires:   logrotate
# for /usr/bin/pkexec
Requires:   polkit
# for flock in ejabberdctl
Requires:   util-linux


%description
ejabberd is a Free and Open Source distributed fault-tolerant
Jabber/XMPP server. It is mostly written in Erlang, and runs on many
platforms (tested on Linux, FreeBSD, NetBSD, Solaris, Mac OS X and
Windows NT/2000/XP).


%prep
%autosetup -p1

# The rebar3_hex plugin is only needed for publishing to hex.pm and isn't
# packaged in Fedora. Drop it so rebar3 doesn't try to fetch it.
sed -i 's/{rebar3_hex, "[^"]*"},//' rebar.config

# The JSON map encoding test asserts a particular key order which depends on
# the internal map representation and doesn't hold on Erlang/OTP 27.3.
sed -i '/^-ifndef(OTP_BELOW_27)\./,/^-endif\./d' test/json_test.erl

# The unDraw illustration is under a license which forbids redistribution of
# the assets. The invite page still works without it.
rm -f priv/mod_invites/static/illus-empty.svg priv/mod_invites/copyright

cp %{S:14} %{S:15} %{S:16} .


%build
autoreconf -ivf

%configure \
    --with-rebar=%{__rebar3} \
    --enable-system-deps \
    --enable-debug \
    --enable-odbc \
    --enable-mysql \
    --enable-pgsql \
    --enable-lua \
    --enable-pam \
    --enable-sip \
    --enable-stun \
    --enable-zlib \
    --disable-redis \
    --disable-sqlite \
    --libdir=%{_erllibdir}

%{rebar3_compile}

# Generate the ejabberdctl script with Fedora paths baked in
make ejabberdctl.example

# Build the SELinux policy
make NAME=ejabberd -f /usr/share/selinux/devel/Makefile DISTRO=fedora%{fedora}
bzip2 ejabberd.pp


%install
%{erlang3_install}

install -d -m 0750 %{buildroot}%{_sysconfdir}/%{name}
install -D -p -m 0644 ejabberd.yml.example %{buildroot}%{_sysconfdir}/%{name}/ejabberd.yml
install -D -p -m 0644 ejabberdctl.cfg.example %{buildroot}%{_sysconfdir}/%{name}/ejabberdctl.cfg
install -D -p -m 0644 inetrc %{buildroot}%{_sysconfdir}/%{name}/inetrc

install -D -p -m 0755 ejabberdctl.example %{buildroot}%{_bindir}/ejabberdctl

install -d -m 0750 %{buildroot}%{_sharedstatedir}/ejabberd
install -d -m 0750 %{buildroot}%{_localstatedir}/log/ejabberd

install -D -p -m 0755 tools/captcha.sh %{buildroot}%{erlang_appdir}/priv/bin/captcha.sh
install -D -p -m 0755 tools/captcha-ng.sh %{buildroot}%{erlang_appdir}/priv/bin/captcha-ng.sh

install -D -p -m 0644 %{S:9} %{buildroot}%{_sysconfdir}/pam.d/ejabberdctl
install -D -p -m 0644 %{S:11} %{buildroot}%{_sysconfdir}/pam.d/ejabberd

# install systemd entry
install -D -m 0644 -p %{S:4} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 -p %{S:17} %{buildroot}%{_sysusersdir}/%{name}.conf

# install config for logrotate
install -D -p -m 0644  %{S:2} %{buildroot}%{_sysconfdir}/logrotate.d/ejabberd

# install sql-scripts for creating db schemes for various RDBMS
install -d -m 0755 %{buildroot}%{erlang_appdir}/priv/sql/
install -p -m 0644 sql/*.sql %{buildroot}%{erlang_appdir}/priv/sql/
# Install css files
install -d -m 0755 %{buildroot}%{erlang_appdir}/priv/css
install -p -m 0644 priv/css/* %{buildroot}%{erlang_appdir}/priv/css/
# Install img files
install -d -m 0755 %{buildroot}%{erlang_appdir}/priv/img
install -p -m 0644 priv/img/* %{buildroot}%{erlang_appdir}/priv/img/
# Install js files
install -d -m 0755 %{buildroot}%{erlang_appdir}/priv/js
install -p -m 0644 priv/js/* %{buildroot}%{erlang_appdir}/priv/js/
# Install mod_invites templates and static files
cp -a priv/mod_invites %{buildroot}%{erlang_appdir}/priv/
# Install translations
install -d -m 0755 %{buildroot}%{erlang_appdir}/priv/msgs/
install -p -m 0644 priv/msgs/*.msg %{buildroot}%{erlang_appdir}/priv/msgs/

# Install man page
install -d -m 0755 %{buildroot}%{_mandir}/man5/
install -p -m 0644 man/ejabberd.yml.5 %{buildroot}%{_mandir}/man5/

# Install polkit-related files
install -D -p -m 0644 %{S:12} %{buildroot}%{_datadir}/polkit-1/actions/ejabberdctl.policy
install -D -p -m 0644 %{S:13} %{buildroot}%{_datadir}/polkit-1/rules.d/51-ejabberdctl.rules

# Install the SELinux policy
install -d %{buildroot}%{_datadir}/selinux/packages
install -d -p %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}

install -p -m 0644 ejabberd.if %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}
install -p -m 0644 ejabberd.pp.bz2 %{buildroot}%{_datadir}/selinux/packages


%check
%{rebar3_eunit}


%pre
if [ $1 -gt 1 ]; then
    # we should backup DB in every upgrade
    if ejabberdctl status >/dev/null ; then
        # Use timestamp to make database restoring easier
        TIME=$(date +%%Y-%%m-%%dT%%H:%%M:%%S)
        BACKUPDIR=$(mktemp -d -p /var/tmp/ ejabberd-$TIME.XXXXXX)
        chown ejabberd:ejabberd $BACKUPDIR
        BACKUP=$BACKUPDIR/ejabberd-database
        ejabberdctl backup $BACKUP
        # Change ownership to root:root because ejabberd user might be
        # removed on package removal.
        chown -R root:root $BACKUPDIR
        chmod 700 $BACKUPDIR
        echo
        echo The ejabberd database has been backed up to $BACKUP.
        echo
    fi

    # fix cookie path (since ver. 2.1.0 cookie stored in /var/lib/ejabberd/spool
    # rather than in /var/lib/ejabberd
    if [ -f /var/lib/ejabberd/spool/.erlang.cookie ]; then
        cp -pu /var/lib/ejabberd/{spool/,}.erlang.cookie
        echo
        echo The ejabberd cookie file was moved again.
        echo Please delete old one from /var/lib/ejabberd/spool/.erlang.cookie
        echo
    fi
fi
%selinux_relabel_pre -s %{selinuxtype}


%post
%systemd_post %{name}.service
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{modulename}.pp.bz2


%posttrans
/usr/sbin/restorecon -i -R /var/lib/ejabberd/
/usr/sbin/restorecon -i -R /var/log/ejabberd/
%selinux_relabel_post -s %{selinuxtype}


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi


%files
%license COPYING
%doc CHANGELOG.md CONTRIBUTING.md CONTRIBUTORS.md README.md

%attr(750,ejabberd,ejabberd) %dir %{_sysconfdir}/ejabberd
%attr(640,ejabberd,ejabberd) %config(noreplace) %{_sysconfdir}/ejabberd/ejabberd.yml
%attr(640,ejabberd,ejabberd) %config(noreplace) %{_sysconfdir}/ejabberd/ejabberdctl.cfg
%attr(640,ejabberd,ejabberd) %config(noreplace) %{_sysconfdir}/ejabberd/inetrc

%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf

%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/ejabberdctl
%{_mandir}/man5/ejabberd.yml.5*
%{_datadir}/polkit-1/actions/ejabberdctl.policy
%{_datadir}/polkit-1/rules.d/51-ejabberdctl.rules
%{_datadir}/selinux/devel/include/%{moduletype}/ejabberd.if
%{_datadir}/selinux/packages/ejabberd.pp.bz2
%{_bindir}/ejabberdctl

%{erlang_appdir}

%attr(750,ejabberd,ejabberd) %dir %{_sharedstatedir}/ejabberd
%attr(750,ejabberd,ejabberd) %dir %{_localstatedir}/log/ejabberd


%changelog
%autochangelog
