%define _hardened_build 1
%define selinux_variants mls strict targeted
%global selinux_policyver %(%{__sed} -e 's,.*selinux-policy-\\([^/]*\\)/.*,\\1,' /usr/share/selinux/devel/policyhelp || echo 0.0.0)


%define logwatch_root %{_datadir}/logwatch
%define logwatch_conf %{logwatch_root}/dist.conf
%define logwatch_scripts %{logwatch_root}/scripts

Name: crossfire
Version: 1.71.0
Release: 31%{?dist}
Summary: Server for hosting crossfire games
# All files GPLv2+ except server/daemon.c which also has MIT attributions
License: GPL-2.0-or-later and MIT
URL: http://crossfire.real-time.com

Source0: http://downloads.sourceforge.net/crossfire/%{name}-%{version}.tar.bz2
Source1: http://downloads.sourceforge.net/crossfire/%{name}-%{version}.arch.tar.bz2
Source2: crossfire.service
Source3: crossfire.sysconfig
Source4: crossfire.logrotate
Source5: crossfire.te
Source6: crossfire.fc
Source7: crossfire.if
Source8: logwatch.logconf.crossfire
Source9: logwatch.script.crossfire
Source10: logwatch.serviceconf.crossfire
#Patch0:  crossfire-1.10.0-log-login.patch
#Patch1:  crossfire-1.11.0-curl.patch
Patch2:  crossfire-1.71.0-snprintf-formatting.patch
Patch3: crossfire-c99.patch
Requires:       crossfire-maps
BuildRequires:  gcc
BuildRequires:  checkpolicy perl-generators selinux-policy-devel hardlink
BuildRequires:  libXt-devel
BuildRequires:  libXext-devel
BuildRequires:  libXaw-devel
BuildRequires:  perl(FileHandle)
BuildRequires:  python3-devel
BuildRequires:  autoconf flex
BuildRequires:  systemd-rpm-macros
BuildRequires: make
BuildRequires: libxcrypt-devel
Requires: %{name}-plugins

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Provides: crossfire-devel = %{version}-%{release}
Obsoletes: crossfire-devel < %{version}-%{release}

%description
Crossfire is a highly graphical role-playing adventure game with
characteristics reminiscent of rogue, nethack, omega, and gauntlet. 
It has multiplayer capability and presently runs under X11.

This package contains the server for hosting crossfire games over a
public or private network.

%package doc
Summary: Documentation files for Crossfire
# Don't require the base package.  The docs can be used without the
# base package, and in fact include docs for both the client and
# server packages.
%description doc
Documentation files for the crossfire game.

#%package devel
#Summary: Development files for writing crossfire plugins
#Requires: %%{name} = %%{version}-%%{release}
#%description devel
#Development files for writing crossfire plugins.

%package plugins
Summary: Plugin modules for the crossfire game server
Requires: %{name} = %{version}-%{release}
%description plugins
Plugin modules for the crossfire game server.

%package client-images
Summary: Image cache for crossfire clients
# No version dependency for the client since the images are pretty
# ignorant of the client version.
Requires: crossfire-client
%description client-images
Image files that can be used with the crossfire clients so that they
don't have to be downloaded from the server.

%package selinux
Summary: SELinux policy files for crossfire
Requires: %{name} = %{version}-%{release}
Requires:       selinux-policy >= %{selinux_policyver}
Requires(post):         /usr/sbin/semodule /usr/sbin/semanage /sbin/fixfiles
Requires(preun):        /usr/sbin/semodule /usr/sbin/semanage /sbin/fixfiles
Requires(postun):       /usr/sbin/semodule
%description selinux
selinux policy files for the Crossfire game server

%package logwatch
Summary: logwatch scripts for the Crossfire game server
Requires: %{name} = %{version}-%{release} logwatch
%description logwatch
logwatch scripts for the Crossfire game server

%prep
%setup -qn crossfire-server-%{version}
%setup -q -a 1 -n crossfire-server-%{version}
#%%patch0 -p0
#%patch1 -p0
%patch -P2 -p0
%patch -P3 -p1
mkdir SELinux
cp  %{SOURCE5} %{SOURCE6} %{SOURCE7} SELinux

mv arch/ lib/

sed -i 's#\r##' utils/player_dl.pl.in
# Don't use a hardcoded /tmp directory for building the image archive
sed -i "s#^\$TMPDIR=.*#\$TMPDIR=\"`pwd`\";#" lib/adm/collect_images.pl
# Don't map stdio streams to /
# This is fixed in CVS, but didn't make it into the 1.9.1 release.
sed -i 's#    (void) open ("/", O_RDONLY);#    (void) open ("/var/log/crossfire/crossfire.log", O_RDONLY);#' server/daemon.c

# Change the location of the tmp directory
sed -i "s@^#define TMPDIR \"/tmp\"@#define TMPDIR \"%{_var}/games/%{name}/tmp\"@" include/config.h

%build
# Change the localstatedir so that the variable data files are
# put in /var/games/crossfire instead of /var/crossfire.  This is
# in agreement with the FHS.
%configure --localstatedir=%{_var}/games --disable-static

#make %%{?_smp_mflags} # parallel build is broken
make CFLAGS="$RPM_OPT_FLAGS -std=gnu17"

# Build the selinux policy file
pushd SELinux
for variant in %{selinux_variants}
do
    make NAME=${variant} -f %{_datadir}/selinux/devel/Makefile
    mv %{name}.pp %{name}.pp.${variant}
    make NAME=${variant} -f %{_datadir}/selinux/devel/Makefile clean
done
popd

# This will create a tarball of the images for the client.
cd lib && adm/collect_images.pl -archive

%install
make DESTDIR=$RPM_BUILD_ROOT install

# Install the client images
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}-client
tar xf %{name}-images.tar -C $RPM_BUILD_ROOT/%{_datadir}/%{name}-client
# Nuke the installation instructions for the image archive.
rm $RPM_BUILD_ROOT/%{_datadir}/%{name}-client/README

#install -pD -m 0755 %%{SOURCE2} $RPM_BUILD_ROOT%%{_initrddir}/crossfire
install -pD -m 0755 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/crossfire.service

# Move some rarely-used binaries out of /usr/bin and into a
# tools directory.
mkdir $RPM_BUILD_ROOT%{_datadir}/%{name}/tools

# This utility restarts crossfire at periodic intervals.
#mv $RPM_BUILD_ROOT%{_bindir}/crossloop,pl $RPM_BUILD_ROOT%{_datadir}/%{name}/tools

# This submits core files to the developers.
mv $RPM_BUILD_ROOT%{_bindir}/crossloop.web $RPM_BUILD_ROOT%{_datadir}/%{name}/tools

# Allows players to download their player files from a web
# server. This feature relies on a properly configured web server
# which is not handled by this rpm release.
mv $RPM_BUILD_ROOT%{_bindir}/player_dl.pl $RPM_BUILD_ROOT%{_datadir}/%{name}/tools

# Binary for running a crossfire metaserver.  Requires interaction with
# a web server, so we disable this for now.
#rm $RPM_BUILD_ROOT%{_libdir}/%{name}/metaserver.pl

# I have no idea what this is for.
#mv $RPM_BUILD_ROOT%{_libdir}/%{name}/mktable.script $RPM_BUILD_ROOT%{_datadir}/%{name}/tools

# This is not needed anymore based on comments at the top of
# the file itself.
#rm $RPM_BUILD_ROOT%{_libdir}/%{name}/add_throw.perl

# /usr/bin is a better place for the standalone random map generator
#mv $RPM_BUILD_ROOT/usr/libexec/crossfire/random_map $RPM_BUILD_ROOT%{_bindir}/cross_random_map

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.la

# Create the log directory
mkdir -p $RPM_BUILD_ROOT%{_var}/log/%{name}

install -p -D -m 644 %{SOURCE3} \
    $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/%{name}

install -p -D -m 644 %{SOURCE4} \
    $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/%{name}

mkdir $RPM_BUILD_ROOT%{_var}/games/%{name}/tmp

# Install selinux policies
pushd SELinux
for variant in %{selinux_variants}
do
    install -d $RPM_BUILD_ROOT%{_datadir}/selinux/${variant}
    install -p -m 644 %{name}.pp.${variant} \
           $RPM_BUILD_ROOT%{_datadir}/selinux/${variant}/%{name}.pp
done
popd
# Hardlink identical policy module packages together
/usr/bin/hardlink -cv $RPM_BUILD_ROOT%{_datadir}/selinux

# Install logwatch files
install -pD -m 0644 %{SOURCE8} $RPM_BUILD_ROOT%{logwatch_conf}/logfiles/%{name}.conf
install -pD -m 0755 %{SOURCE9} $RPM_BUILD_ROOT%{logwatch_scripts}/services/%{name}
install -pD -m 0644 %{SOURCE10} $RPM_BUILD_ROOT%{logwatch_conf}/services/%{name}.conf


%pre
getent group crossfire >/dev/null || groupadd -r crossfire
getent passwd crossfire >/dev/null || \
useradd -r -g crossfire -d %{_datadir}/%{name} -s /sbin/nologin \
    -c "Daemon account for the crossfire server" crossfire
exit 0

%post
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi


%post selinux
# Install SELinux policy modules
for selinuxvariant in %{selinux_variants}
do
  /usr/sbin/semodule -s ${selinuxvariant} -i \
    %{_datadir}/selinux/${selinuxvariant}/%{name}.pp &> /dev/null || :
done
/usr/sbin/semanage port -a -t %{name}_port_t -p tcp 13327 > /dev/null 2>&1 || :
/sbin/fixfiles -R %{name} restore || :
/sbin/service %{name} condrestart > /dev/null 2>&1 || :

%preun
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable crossfire.service > /dev/null 2>&1 || :
    /bin/systemctl stop crossfire.service > /dev/null 2>&1 || :
fi


%preun selinux
if [ "$1" -lt "1" ] ; then
    # Unload the module
    /usr/sbin/semanage port -d -t %{name}_port_t -p tcp 13327 >/dev/null 2>&1 || :
    for variant in %{selinux_variants} ; do
        /usr/sbin/semodule -s ${variant} -r %{name} &> /dev/null || :
    done
    # Set the context back
    /sbin/fixfiles -R %{name} restore || :
fi

%postun
#if [ "$1" -ge "1" ]; then
#    /sbin/service crossfire condrestart >/dev/null 2>&1
#fi
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart crossfire.service >/dev/null 2>&1 || :
fi


%postun selinux
if [ "$1" -ge "1" ] ; then
    # Replace the module if it is already loaded. semodule -u also
    # checks the module version
    for variant in %{selinux_variants} ; do
        /usr/sbin/semodule -u %{_datadir}/selinux/${variant}/%{name}.pp || :
    done
fi



%files
%license COPYING
%doc README NEWS AUTHORS
#%%{_bindir}/crossedit
#%%{_bindir}/crossfire
%{_bindir}/crossfire-server
%{_bindir}/crossloop
%{_datadir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/*
%config(noreplace) %{_sysconfdir}/%{name}/ban_file
%config(noreplace) %{_sysconfdir}/%{name}/dm_file
%config(noreplace) %{_sysconfdir}/%{name}/exp_table
%config(noreplace) %{_sysconfdir}/%{name}/forbid
%config(noreplace) %{_sysconfdir}/%{name}/motd
%config(noreplace) %{_sysconfdir}/%{name}/news
%config(noreplace) %{_sysconfdir}/%{name}/rules
%config(noreplace) %{_sysconfdir}/%{name}/settings
%config(noreplace) %{_sysconfdir}/%{name}/metaserver2
%config(noreplace) %{_sysconfdir}/%{name}/stat_bonus
%attr(-,crossfire,root) %{_var}/games/%{name}
%attr(-,crossfire,root) %{_var}/log/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_mandir}/man6/*
%{_unitdir}/%{name}.service

%files doc
%doc doc/Developers doc/playbook* doc/scripts doc/spell-docs doc/spoiler doc/spoiler-html doc/*.txt

#%files devel
#%defattr(-,root,root,-)
#%%{_bindir}/crossfire-config
#%doc doc/plugins

%files plugins
%{_libdir}/%{name}/plugins

%files client-images
%{_datadir}/%{name}-client

%files selinux
%doc SELinux/*.??
%{_datadir}/selinux/*/%{name}.pp

%files logwatch
%{logwatch_conf}/logfiles/%{name}.conf
%{logwatch_conf}/services/%{name}.conf
%{logwatch_scripts}/services/%{name}


%changelog
* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 1.71.0-31
- Add explicit BR: libxcrypt-devel

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> = 1.71.0-25
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Florian Weimer <fweimer@redhat.com> - 1.71.0-23
- C99 compatibility fix

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 01 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.71.0-17
- Add perl(FileHandle) for build

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 15 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.71.0-15
- Fix FTBTS

* Tue Aug 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.71.0-14
- Python 3.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.71.0-12
- Fix FTBFS due to hardlink path.

* Wed Mar 20 2019 Peter Robinson <pbrobinson@fedoraproject.org> - 1.71.0-11
- Drop legacy bits, use %%license

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.71.0-9
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.71.0-6
- Rebuilt for switch to libxcrypt

* Fri Dec 15 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.71.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 19 2016 Jon Ciesla <limburgher@gmail.com> - 1.71.0-1
- 1.71.0, BZ 1310012.
- Obsolete devel subpackage.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.70.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.70.0-6
- Perl 5.18 rebuild

* Thu Jun 06 2013 Jon Ciesla <limburgher@gmail.com> - 1.70.0-5
- Fix unit file, BZ 971088.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Jon Ciesla <limburgher@gmail.com> - 1.70.0-2
- Add hardened build.

* Tue Mar 27 2012 Jon Ciesla <limburgher@gmail.com> - 1.70.0-1
- New upstream.
- Curl patch upstreamed.

* Tue Jan 31 2012 Jon Ciesla <limburgher@gmail.com> - 1.60.0-2
- Migrate to systemd, BZ 771752.

* Wed Jan 11 2012 Jon Ciesla <limburgher@gmail.com> - 1.60.0-1
- New upstream.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.11.0-2
- Rebuild for Python 2.6

* Thu Jul 24 2008 Wart <wart@kobold.org> 1.11.0-1
- Update to 1.11.0

* Tue Jul 22 2008 Wart <wart@kobold.org> 1.10.0-6
- Fix selinux policy with regard to sock_file

* Wed Jun 18 2008 Wart <wart@kobold.org> 1.10.0-5
- Fix creation of the crossfire user (BZ #442384)

* Sat Feb 9 2008 Wart <wart@kobold.org> 1.10.0-4
- Rebuild for gcc 4.3

* Fri Aug 17 2007 Wart <wart@kobold.org> 1.10.0-3
- License tag clarification
- Update user creation to conform to recently modified guidelines

* Thu Jul 12 2007 Wart <wart@kobold.org> 1.10.0-2
- Move client images outside of the server data directory.
- Update selinux policy

* Tue May 22 2007 Wart <wart@kobold.org> 1.10.0-1
- Update to 1.10.0
- Drop patch that was accepted upstream
- Add logwatch subpackage

* Fri Dec 8 2006 Wart <wart@kobold.org> 1.9.1-3
- Rebuild for new python 2.5

* Thu Aug 31 2006 Wart <wart@kobold.org> 1.9.1-2
- Added upstream patch to fix configure bug.
- Added selinux security policy
- Don't use /tmp for the map file cache

* Thu Jul 6 2006 Wart <wart@kobold.org> 1.9.1-1
- Update to 1.9.1

* Tue May 16 2006 Wart <wart@kobold.org> 1.9.0-4
- Added -doc subpackage
- Own /etc/crossfire
- Add crossfire-client dependency for crossfire-client-images

* Tue May 16 2006 Wart <wart@kobold.org> 1.9.0-3
- Added patch to fix missing stdout problem with python plugin.

* Mon May 15 2006 Wart <wart@kobold.org> 1.9.0-2
- Generate the -client-images subpackage here instead of relying
  on upstream's missing -client-images tarball.

* Thu Mar 9 2006 Wart <wart@kobold.org> 1.9.0-1
- Initial spec file following Fedora Extras conventions
