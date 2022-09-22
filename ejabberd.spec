%global _hardened_build 1
%global srcname ejabberd

# Since we require the version in both BuildRequires and Requires, let's make these variables for
# easier maintenance.
%global base64url_ver 1.0
%global cache_tab_ver 1.0.25
%global eimp_ver 1.0.17
%global epam_ver 1.0.9
%global esip_ver 1.0.37
%global ezlib_ver 1.0.8
%global fast_tls_ver 1.1.8
%global fast_xml_ver 1.1.43
%global fast_yaml_ver 1.0.27
%global idna_ver 6.0.0
%global jiffy_ver 1.0.5
%global jose_ver 1.9.0
%global luerl_ver 0.3
%global mqtree_ver 1.0.10
%global p1_acme_ver 1.0.8
%global p1_mysql_ver 1.0.16
%global p1_oauth2_ver 0.6.7
%global p1_pgsql_ver 1.1.10
%global p1_utils_ver 1.0.20
%global pkix_ver 1.0.6
%global stringprep_ver 1.0.22
%global stun_ver 1.0.37
%global xmpp_ver 1.4.9
%global yconf_ver 1.0.7

# Define SELinux policy variables
%global selinuxtype targeted
%global selinux_policyver 3.14.2
%global moduletype contrib
%global modulename ejabberd


Name:           ejabberd
Version:        20.07
Release:        7%{?dist}
BuildArch:      noarch

License:        GPLv2+
Summary:        A distributed, fault-tolerant Jabber/XMPP server
URL:            https://www.ejabberd.im/
VCS:            scm:git:https://github.com/processone/ejabberd.git
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


# Fedora-specific
Patch3: ejabberd-0003-Install-into-BINDIR-instead-of-SBINDIR.patch
# Fedora-specific
Patch4: ejabberd-0004-Enable-systemd-notification-if-available.patch


BuildRequires:  elixir >= 1.4.4
BuildRequires:  erlang-base64url >= %{base64url_ver}
BuildRequires:  erlang-cache_tab >= %{cache_tab_ver}
BuildRequires:  erlang-eimp >= %{eimp_ver}
BuildRequires:  erlang-epam >= %{epam_ver}
BuildRequires:  erlang-esip >= %{esip_ver}
BuildRequires:  erlang-ezlib >= %{ezlib_ver}
BuildRequires:  erlang-fast_tls >= %{fast_tls_ver}
BuildRequires:  erlang-fast_xml >= %{fast_xml_ver}
BuildRequires:  erlang-fast_yaml >= %{fast_yaml_ver}
BuildRequires:  erlang-idna >= %{idna_ver}
BuildRequires:  erlang-jiffy >= %{jiffy_ver}
BuildRequires:  erlang-jose >= %{jose_ver}
BuildRequires:  erlang-lager >= 3.6
BuildRequires:  erlang-luerl >= %{luerl_ver}
BuildRequires:  erlang-mqtree >= %{mqtree_ver}
BuildRequires:  erlang-odbc
BuildRequires:  erlang-p1_acme >= %{p1_acme_ver}
BuildRequires:  erlang-p1_mysql >= %{p1_mysql_ver}
BuildRequires:  erlang-p1_oauth2 >= %{p1_oauth2_ver}
BuildRequires:  erlang-p1_pgsql >= %{p1_pgsql_ver}
BuildRequires:  erlang-p1_utils >= %{p1_utils_ver}
BuildRequires:  erlang-pkix >= %{pkix_ver}
BuildRequires:  erlang-rebar
BuildRequires:  erlang-sd_notify
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

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires: make

# For creating user and group
Requires(pre):  shadow-utils

Requires(post): /usr/bin/openssl
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

Provides: user(%{name})
Provides: group(%{name})

Requires:  ejabberd-selinux == %{version}-%{release}
# From rebar
Requires:  elixir >= 1.4.4
Requires:  erlang-base64url >= %{base64url_ver}
Requires:  erlang-cache_tab >= %{cache_tab_ver}
Requires:  erlang-eimp >= %{eimp_ver}
Requires:  erlang-epam >= %{epam_ver}
Requires:  erlang-esip >= %{esip_ver}
Requires:  erlang-ezlib >= %{ezlib_ver}
Requires:  erlang-fast_tls >= %{fast_tls_ver}
Requires:  erlang-fast_xml >= %{fast_xml_ver}
Requires:  erlang-fast_yaml >= %{fast_yaml_ver}
Requires:  erlang-idna >= %{idna_ver}
Requires:  erlang-jiffy >= %{jiffy_ver}
Requires:  erlang-jose >= %{jose_ver}
Requires:  erlang-luerl >= %{luerl_ver}
Requires:  erlang-mqtree >= %{mqtree_ver}
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


%package selinux
BuildArch: noarch

Summary: SELinux policy for ejabberd

Requires: selinux-policy >= %{selinux_policyver}
Requires(post): selinux-policy-base >= %{selinux_policyver}
Requires(post): libselinux-utils
Requires(post): policycoreutils
Requires(post): policycoreutils-python-utils


%description selinux
This is the SELinux policy for ejabberd.


%prep
%autosetup -p1

# Upstream seems to import erlang-xmpp and erlang-fast_xml in a way that isn't compatible with them
# being system libraries. We need to patch the include statements to fix this.
# https://github.com/processone/ejabberd/pull/1446/
find . -name "*.hrl" | xargs sed -i \
    "s/include(\"fxml.hrl/include_lib(\"fast_xml\/include\/fxml.hrl/"
find . -name "*.erl" | xargs sed -i "s/include(\"jid.hrl/include_lib(\"xmpp\/include\/jid.hrl/"
find . -name "*.hrl" | xargs sed -i "s/include(\"ns.hrl/include_lib(\"xmpp\/include\/ns.hrl/"
find . -name "*.erl" | xargs sed -i "s/include(\"xmpp.hrl/include_lib(\"xmpp\/include\/xmpp.hrl/"
find . -name "*.hrl" | xargs sed -i \
    "s/include(\"xmpp_codec.hrl/include_lib(\"xmpp\/include\/xmpp_codec.hrl/"

# A few dependencies are configured to be found in the deps folder instead of in system libs
# https://github.com/processone/ejabberd/issues/1850
perl -p -i -e "s|deps/p1_utils/include|$(rpm -ql erlang-p1_utils | grep -E '/include$' )|g" rebar.config
perl -p -i -e "s|deps/fast_xml/include|$(rpm -ql erlang-fast_xml | grep -E '/include$' )|g" rebar.config
perl -p -i -e "s|deps/xmpp/include|$(rpm -ql erlang-xmpp | grep -E '/include$' )|g"   rebar.config

cp %{S:14} %{S:15} %{S:16} .


%build
autoreconf -ivf

%configure --disable-graphics --enable-odbc --enable-mysql --enable-pgsql --enable-pam --enable-zlib --enable-debug --libdir=%{_libdir}/erlang/lib/ --with-erlang=%{_libdir}/erlang/ --enable-system-deps --enable-stun

%{erlang_compile}

# Build the SELinux policy
make NAME=ejabberd -f /usr/share/selinux/devel/Makefile DISTRO=fedora%{fedora}
bzip2 ejabberd.pp


%install
%{erlang_install}

sed -e "s*{{rootdir}}*%{_prefix}*" \
    -e "s*{{installuser}}*%{name}*" \
    -e "s*{{bindir}}*%{_bindir}*" \
    -e "s*{{libdir}}*%{_erllibdir}*" \
    -e "s*{{sysconfdir}}*%{_sysconfdir}*" \
    -e "s*{{localstatedir}}*/var*" \
    -e "s*{{docdir}}*%{_datadir}/doc/%{name}*" \
    -e "s*{{erl}}*%{_bindir}/erl*" \
    -e "s*{{epmd}}*%{_bindir}/epmd*" ejabberdctl.template \
> ejabberdctl.example

install -d -m 0750 %{buildroot}%{_sysconfdir}/%{name}
install -D -p -m 0644 ejabberd.yml.example %{buildroot}%{_sysconfdir}/%{name}/ejabberd.yml
install -D -p -m 0644 ejabberdctl.cfg.example %{buildroot}%{_sysconfdir}/%{name}/ejabberdctl.cfg
install -D -p -m 0644 inetrc %{buildroot}%{_sysconfdir}/%{name}/inetrc

install -D -p -m 0755 ejabberdctl.example %{buildroot}%{_bindir}/ejabberdctl

install -d -m 0750 %{buildroot}/var/lib/ejabberd
install -d -m 0750 %{buildroot}/var/lock/ejabberdctl
install -d -m 0750 %{buildroot}/var/log/ejabberd

# fix example SSL certificate path to real one, which we created recently (see above)
%{__perl} -pi -e 's!/path/to/ssl.pem!/etc/ejabberd/ejabberd.pem!g' %{buildroot}/etc/ejabberd/ejabberd.yml

install -D -p -m 0755 tools/captcha.sh %{buildroot}%{_erllibdir}/%{name}-%{version}/priv/bin/captcha.sh
# fix captcha path
%{__perl} -pi -e 's!/lib/ejabberd/priv/bin/captcha.sh!%{_libdir}/%{name}/priv/bin/captcha.sh!g' %{buildroot}/etc/ejabberd/ejabberd.yml

install -D -p -m 0644 %{S:9} %{buildroot}%{_sysconfdir}/pam.d/ejabberdctl
install -D -p -m 0644 %{S:11} %{buildroot}%{_sysconfdir}/pam.d/ejabberd

# install systemd entry
install -D -m 0644 -p %{S:4} %{buildroot}%{_unitdir}/%{name}.service

# install config for logrotate
install -D -p -m 0644  %{S:2} %{buildroot}%{_sysconfdir}/logrotate.d/ejabberd

# create room for additional files (such as SQL schemas)
install -d -m 0755 %{buildroot}%{_erllibdir}/%{name}-%{version}/priv/sql/
# install sql-scripts for creating db schemes for various RDBMS
install -p -m 0644 sql/lite.sql %{buildroot}%{_erllibdir}/%{name}-%{version}/priv/sql/
install -p -m 0644 sql/mssql.sql %{buildroot}%{_erllibdir}/%{name}-%{version}/priv/sql/
install -p -m 0644 sql/mysql.sql %{buildroot}%{_erllibdir}/%{name}-%{version}/priv/sql/
install -p -m 0644 sql/pg.sql %{buildroot}%{_erllibdir}/%{name}-%{version}/priv/sql/
# Install css files
install -d -m 0755 %{buildroot}%{_erllibdir}/%{name}-%{version}/priv/css
install -p -m 0644 priv/css/* %{buildroot}%{_erllibdir}/%{name}-%{version}/priv/css/
# Install img files
install -d -m 0755 %{buildroot}%{_erllibdir}/%{name}-%{version}/priv/img
install -p -m 0644 priv/img/* %{buildroot}%{_erllibdir}/%{name}-%{version}/priv/img/
# Install js files
install -d -m 0755 %{buildroot}%{_erllibdir}/%{name}-%{version}/priv/js
install -p -m 0644 priv/js/* %{buildroot}%{_erllibdir}/%{name}-%{version}/priv/js/
# Install lua files
install -d -m 0755 %{buildroot}%{_erllibdir}/%{name}-%{version}/priv/lua
install -p -m 0644 priv/lua/* %{buildroot}%{_erllibdir}/%{name}-%{version}/priv/lua/

install -d -m 0755 %{buildroot}%{_erllibdir}/%{name}-%{version}/priv/msgs/
install -p -m 0644 priv/msgs/*.msg %{buildroot}%{_erllibdir}/%{name}-%{version}/priv/msgs/

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
%{rebar_eunit}


%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -M \
-c "ejabberd" %{name} 2>/dev/null || :


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


%pre selinux
%selinux_relabel_pre -s %{selinuxtype}


%post
%systemd_post %{name}.service

# Create SSL certificate with default values if it doesn't exist
(cd /etc/ejabberd
if [ ! -f ejabberd.pem ]
then
    echo "Generating SSL certificate /etc/ejabberd/ejabberd.pem..."
    HOSTNAME=$(hostname -s 2>/dev/null || echo "localhost")
    DOMAINNAME=$(hostname -d 2>/dev/null || echo "localdomain")
    openssl req -new -x509 -days 365 -nodes -out ejabberd.pem \
                -keyout ejabberd.pem > /dev/null 2>&1 <<+++
.
.
.
$DOMAINNAME
$HOSTNAME
ejabberd
root@$HOSTNAME.$DOMAINNAME
+++
chown ejabberd:ejabberd ejabberd.pem
chmod 600 ejabberd.pem
fi)


%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{modulename}.pp.bz2


%posttrans selinux
/usr/sbin/restorecon -i -R /var/lib/ejabberd/
/usr/sbin/restorecon -i -R /var/log/ejabberd/
%selinux_relabel_post -s %{selinuxtype}


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%postun selinux
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

%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/ejabberdctl
%{_mandir}/man5/ejabberd.yml.5*
%{_datadir}/polkit-1/actions/ejabberdctl.policy
%{_datadir}/polkit-1/rules.d/51-ejabberdctl.rules
%{_bindir}/ejabberdctl

%{_erllibdir}/%{name}-%{version}

%attr(750,ejabberd,ejabberd) %dir /var/lib/ejabberd
%attr(750,ejabberd,ejabberd) %dir /var/log/ejabberd


%files selinux
%{_datadir}/selinux/devel/include/%{moduletype}/ejabberd.if
%{_datadir}/selinux/packages/ejabberd.pp.bz2


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Randy Barlow <bowlofeggs@fedoraproject.org> - 20.07-5
- Allow to bind to name_bind on udp (#1901466).

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20.07-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 20.07-1
- Update to 20.07 (#1807271).
- https://www.process-one.net/blog/ejabberd-20-07/

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 14 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 20.01-1
- Update to 20.01 (#1792572).
- https://blog.process-one.net/ejabberd-20-01/

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.09.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 19.09.1-1
- Update to 19.09.1 (#1742538).
- https://blog.process-one.net/ejabberd-19-08/
- https://blog.process-one.net/ejabberd-19-09/
- https://blog.process-one.net/ejabberd-19-09-1/

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 19.05-1
- Update to 19.05.
- https://blog.process-one.net/ejabberd-19-05/

* Sat Apr 13 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 19.02-1
- Update to 19.02 (#1683310).
- https://blog.process-one.net/ejabberd-19-02-the-mqtt-edition/

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
