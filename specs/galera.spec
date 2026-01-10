# To both save infrastructure resources and workaround for i686 FTBFS
ExcludeArch: %{ix86}

Name:           galera
Version:        26.4.24
Release:        1%{?dist}
Summary:        Synchronous multi-master wsrep provider (replication engine)

License:        GPL-2.0-only
URL:            https://mariadb.com/docs/galera-cluster

# The Upstream Release Monitoring use this config: https://release-monitoring.org/project/9068/ which checks GitHub tags.
# The MariaDB upstream releases their own - further patched - version (dozens of files added) on their custom download web page. However they only release it with a MariaDB server release. 
# So it can only be accessed through the 'https://archive.mariadb.org/mariadb-.../...' path which contains the major version of the MariaDB server.
# Furthermore there is a lag (can be days, weeks) between when a new tag is done on GitHub and when MariaDB upstream releases the new version on their web with the new MariaDB server release.
Source0:        https://archive.mariadb.org/mariadb-11.8/%{name}-%{version}/src/%{name}-%{version}.tar.gz

Patch0:         cmake_paths.patch
Patch1:         docs.patch
Patch2:         network.patch

BuildRequires:  boost-devel check-devel openssl-devel cmake systemd gcc-c++ asio-devel
Requires:       nmap-ncat
Requires:       procps-ng

%{?systemd_requires}


%description
Galera is a fast synchronous multimaster wsrep provider (replication engine)
for transactional databases and similar applications. For more information
about wsrep API see https://github.com/codership/wsrep-API repository. For a
description of Galera replication engine see https://www.galeracluster.com web.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

# Create a sysusers.d config file
cat >galera.sysusers.conf <<EOF
u garb - 'Galera Arbitrator Daemon' /dev/null -
EOF

%build

%cmake \
       -DCMAKE_BUILD_TYPE="%{?with_debug:Debug}%{!?with_debug:RelWithDebInfo}" \
       -DINSTALL_LAYOUT=RPM \
       -DCMAKE_RULE_MESSAGES:BOOL=OFF \
       \
       -DBUILD_SHARED_LIBS:BOOL=OFF \
       \
       -DINSTALL_DOCDIR="share/doc/%{name}/" \
       -DINSTALL_GARBD="bin" \
       -DINSTALL_GARBD-SYSTEMD="bin" \
       -DINSTALL_CONFIGURATION="/etc/sysconfig/" \
       -DINSTALL_SYSTEMD_SERVICE="lib/systemd/system" \
       -DINSTALL_LIBDIR="%{_lib}/galera" \
       -DINSTALL_MANPAGE="share/man/man8"

cmake -B %_vpath_builddir -N -LAH

%cmake_build


%install
%cmake_install

# PATCH 4:
#  Use a dedicated user for the Systemd service
#  To fix an security issue reported by Systemd:
#
## systemd[1]: /usr/lib/systemd/system/garb.service:14: Special user nobody configured, this is not safe!
##   Subject: Special user nobody configured, this is not safe!
##   Defined-By: systemd
##   Support: https://lists.freedesktop.org/mailman/listinfo/systemd-devel
##   Documentation: https://systemd.io/UIDS-GIDS
##
##   The unit garb.service is configured to use User=nobody.
##
##   This is not safe. The nobody user's main purpose on Linux-based
##   operating systems is to be the owner of files that otherwise cannot be mapped
##   to any local user. It's used by the NFS client and Linux user namespacing,
##   among others. By running a unit's processes under the identity of this user
##   they might possibly get read and even write access to such files that cannot
##   otherwise be mapped.
##
##   It is strongly recommended to avoid running services under this user identity,
##   in particular on systems using NFS or running containers. Allocate a user ID
##   specific to this service, either statically via systemd-sysusers or dynamically
##   via the DynamicUser= service setting.
sed -i 's/User=nobody/User=garb/g' %{buildroot}%{_unitdir}/garb.service
# Maintainers from other distributions also tries to resolve it on the upstream:
#   https://github.com/codership/galera/pull/633

install -m0644 -D galera.sysusers.conf %{buildroot}%{_sysusersdir}/galera.conf


%check
%ctest


%pre
# Fixup after upgrading on system before systemd unit rename
unlink /etc/systemd/system/garb.service || :

%post
/sbin/ldconfig
%systemd_post garb.service

%preun
%systemd_preun garb.service

%postun
/sbin/ldconfig
%systemd_postun_with_restart garb.service


%files
%config(noreplace,missingok) %{_sysconfdir}/sysconfig/garb

%dir %{_docdir}/galera
%dir %{_libdir}/galera

%{_bindir}/garbd

# PATCH 3:
#   Make sure the wrapper script is executable
%attr(755, -, -) %{_bindir}/garb-systemd

%{_mandir}/man8/garbd.8*

%{_unitdir}/garb.service

%{_libdir}/galera/libgalera_smm.so

%doc %{_docdir}/galera/COPYING
%doc %{_docdir}/galera/LICENSE.asio
%doc %{_docdir}/galera/README-MySQL
%{_sysusersdir}/galera.conf


%changelog
%autochangelog
