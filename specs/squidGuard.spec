%define _hardened_build 1
%define _default_patch_fuzz 2
# $Id: squidGuard.spec,v 1.22 2009/10/26 13:30:17 limb Exp $

# GCC 10 uses -fno-common by default, turn it off for now
%define _legacy_common_support 1

%define			_dbtopdir		%{_var}/%{name}
%define			_dbhomedir		%{_var}/%{name}/blacklists
%define			_cgibin			/var/www/cgi-bin

Name:			squidGuard
Version:		1.4
Release:		49%{?dist}
Summary:		Filter, redirector and access controller plugin for squid

License:		GPL-2.0-only

Source0:		http://www.squidguard.org/Downloads/squidGuard-%{version}.tar.gz
Source1:		squidGuard.logrotate
Source2:		http://squidguard.mesd.k12.or.us/blacklists.tgz
Source3:		http://cuda.port-aransas.k12.tx.us/squid-getlist.html
Source4:		squidGuard-1.4-patch-20150201.tar.gz

# K12LTSP stuff
Source100:		squidGuard.conf
Source101:		update_squidguard_blacklists
#Source102:		squidguard
#Source103:		transparent-proxying
Source104:		squidGuard.service
Source105:		transparent-proxying.service
Source106:		squidGuard-helper
Source107:		transparent-proxying-helper

# SELinux (taken from K12LTSP package)
#Source200:		squidGuard.te
#Source201:		squidGuard.fc

#Patch0:			squidGuard-upstream.patch
#Patch1:			squidGuard-paths.patch
Patch2:			squid-getlist.html.patch
Patch3:			squidGuard-perlwarning.patch
#Patch4:			squidGuard-sed.patch
Patch5:			squidGuard-makeinstall.patch
#Patch6:			squidGuard-1.3-SG-2008-06-13.patch
Patch7:			squidGuard-1.4-20091015.patch
Patch8:			squidGuard-1.4-20091019.patch
Patch9:			squidGuard-1.4-db5.patch
Patch10:		squidGuard-1.4-helper-protocol.patch
Patch11:                squidGuard-1.4-setuserinfo.patch
Patch12:                squidGuard-configure-c99.patch
Patch13:                squidGuard-htunescape-c99.patch

URL:			http://www.squidguard.org/

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	bison, byacc, openldap-devel, flex, libdb-devel
BuildRequires:	perl-generators
BuildRequires:	systemd

Requires:		squid
#Requires(post):	%{_bindir}/chcon
#Requires(post):	/sbin/chkconfig
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
squidGuard can be used to 
- limit the web access for some users to a list of accepted/well known
  web servers and/or URLs only.
- block access to some listed or blacklisted web servers and/or URLs
  for some users.
- block access to URLs matching a list of regular expressions or words
  for some users.
- enforce the use of domainnames/prohibit the use of IP address in
  URLs.
- redirect blocked URLs to an "intelligent" CGI based info page.
- redirect unregistered user to a registration form.
- redirect popular downloads like Netscape, MSIE etc. to local copies.
- redirect banners to an empty GIF.
- have different access rules based on time of day, day of the week,
  date etc.
- have different rules for different user groups.
- and much more.. 

Neither squidGuard nor Squid can be used to
- filter/censor/edit text inside documents 
- filter/censor/edit embeded scripting languages like JavaScript or
  VBscript inside HTML

%prep
%setup -q
%{__cp} %{SOURCE3} .
#%patch0 -p1
#%patch1 -p1 -b .paths
%patch -P2 -p0
%patch -P3 -p2
#%patch4 -p1
%patch -P5	-p1
#%patch6 -p0
%patch -P7 -p0
%patch -P8 -p0
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1

%{__cp} %{SOURCE100} ./squidGuard.conf.k12ltsp.template
%{__cp} %{SOURCE101} ./update_squidguard_blacklists.k12ltsp.sh

%build
# LDAP_DEPRECATED ensures that ldap_init is declared in <ldap.h>.
%set_build_flags
CFLAGS="$CFLAGS -DLDAP_DEPRECATED"

%configure \
	--with-sg-config=%{_sysconfdir}/squid/squidGuard.conf \
	--with-sg-logdir=%{_var}/log/squidGuard \
	--with-sg-dbhome=%{_dbhomedir} \
	--with-ldap=yes
	
#%{__make} %{?_smp_mflags}
%{__make}

pushd contrib
%{__make} %{?_smp_mflags}
popd

#Apply squidGuard-1.4-patch-20150201.tar.gz
tar -xzf %{SOURCE4} --overwrite -C samples/ --strip-components=1

%install
%{__rm} -rf $RPM_BUILD_ROOT

#%{__make} DESTDIR=$RPM_BUILD_ROOT install
# This broke as of 1.2.1.
%{__install} -p -D -m 0755 src/squidGuard $RPM_BUILD_ROOT%{_bindir}/squidGuard

%{__install} -p -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/squidGuard
%{__install} -p -D -m 0644 samples/sample.conf $RPM_BUILD_ROOT%{_sysconfdir}/squid/squidGuard.conf
%{__install} -p -D -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_dbtopdir}/blacklists.tar.gz

# Don't use SOURCE3, but use the allready patched one #165689
%{__install} -p -D -m 0755 squid-getlist.html $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/squidGuard

#%{__install} -p -D %{SOURCE200} $RPM_BUILD_ROOT%{_sysconfdir}/selinux/targeted/src/policy/domains/program/squidGuard.te
#%{__install} -p -D %{SOURCE201} $RPM_BUILD_ROOT%{_sysconfdir}/selinux/targeted/src/policy/file_contexts/program/squidGuard.fc

%{__install} -p -d $RPM_BUILD_ROOT%{_cgibin}
%{__install} samples/squid*cgi $RPM_BUILD_ROOT%{_cgibin}

%{__install} contrib/hostbyname/hostbyname $RPM_BUILD_ROOT%{_bindir}
%{__install} contrib/sgclean/sgclean $RPM_BUILD_ROOT%{_bindir}

#%{__install} -p -D -m 0755 %{SOURCE102} $RPM_BUILD_ROOT%{_initrddir}/squidGuard
#%{__install} -p -D -m 0755 %{SOURCE103} $RPM_BUILD_ROOT%{_initrddir}/transparent-proxying

%{__install} -p -D -m 0644 %{SOURCE104} $RPM_BUILD_ROOT%{_unitdir}/squidGuard.service
%{__install} -p -D -m 0644 %{SOURCE105} $RPM_BUILD_ROOT%{_unitdir}/transparent-proxying.service

%{__install} -p -D -m 0744 %{SOURCE106} $RPM_BUILD_ROOT%{_bindir}/squidGuard-helper
%{__install} -p -D -m 0744 %{SOURCE107} $RPM_BUILD_ROOT%{_bindir}/transparent-proxying-helper

#pushd $RPM_BUILD_ROOT%{_dbhomedir}
tar xfz $RPM_BUILD_ROOT%{_dbtopdir}/blacklists.tar.gz
#popd

sed -i "s,dest/adult/,blacklists/porn/,g" $RPM_BUILD_ROOT%{_sysconfdir}/squid/squidGuard.conf

%{__install} -p -D -m 0644 samples/babel.* $RPM_BUILD_ROOT%{_cgibin}

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/squidGuard
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/squid
ln -s ../squidGuard/squidGuard.log  $RPM_BUILD_ROOT%{_localstatedir}/log/squid/squidGuard.log

%post
# fix SELinux bits
#%{_bindir}/chcon -R system_u:object_r:squid_cache_t /var/squidGuard >/dev/null 2>&1
#%{_bindir}/chcon -R system_u:object_r:squid_log_t /var/log/squidGuard >/dev/null 2>&1

## do we need a new config file?
#if [ -s %{_sysconfdir}/squid/squidGuard.conf ]; then
#	CONFFILE="%{_sysconfdir}/squid/squidGuard.conf.rpmnew"
#    echo "/etc/squid/squidGuard.conf created as /etc/squid/squidGuard.conf.rpmnew"
#else
#	CONFFILE="/etc/squid/squidGuard.conf"
#fi
#cat %{_docdir}/%{name}-%{version}/squidGuard.conf.k12ltsp.template | \
#	sed s/SERVERNAME/$HOSTNAME/g > $CONFFILE

#/sbin/chkconfig --add squidGuard
#/sbin/chkconfig --add transparent-proxying
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi


# reload SELinux policies
#echo "Loading new SELinux policy"
#pushd %{_sysconfdir}/selinux/targeted/src/policy/
#%{__make} load &> /dev/null
#popd

#### End of %post

%preun
#if [ $1 = 0 ] ; then
#    service squidGuard stop >/dev/null 2>&1
#    /sbin/chkconfig --del squidGuard
#	/sbin/chkconfig --del transparent-proxying
#fi
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable squidGuard.service > /dev/null 2>&1 || :
    /bin/systemctl stop squidGuard.service > /dev/null 2>&1 || :
    /bin/systemctl --no-reload disable transparent-proxying.service > /dev/null 2>&1 || :
    /bin/systemctl stop transparent-proxying.service > /dev/null 2>&1 || :
fi

%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart squidGuard.service >/dev/null 2>&1 || :
    /bin/systemctl try-restart transparent-proxying.service >/dev/null 2>&1 || :
fi

%triggerun -- squidGuard < 1.4-13
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply squidGuard
# and systemd-sysv-convert --apply transparent-proxying
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save squidGuard >/dev/null 2>&1 ||:
/usr/bin/systemd-sysv-convert --save transparent-proxying >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del squidGuard >/dev/null 2>&1 || :
/sbin/chkconfig --del transparent-proxying >/dev/null 2>&1 || :
/bin/systemctl try-restart squidGuard.service >/dev/null 2>&1 || :
/bin/systemctl try-restart transparent-proxying.service >/dev/null 2>&1 || :

%files
%doc samples/*.conf
%doc samples/*.cgi
%doc samples/dest/blacklists.tar.gz
%doc COPYING GPL 
%doc doc/*.txt doc/*.html doc/*.gif
%doc squidGuard.conf.k12ltsp.template
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/squid/squidGuard.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/squidGuard
%config(noreplace) %{_sysconfdir}/cron.daily/squidGuard
%{_dbtopdir}/
#%{_sysconfdir}/selinux/targeted/src/policy/domains/program/squidGuard.te
#%{_sysconfdir}/selinux/targeted/src/policy/file_contexts/program/squidGuard.fc
%attr(0755,root,root) %{_cgibin}/*.cgi
%config(noreplace) %{_cgibin}/squidGuard.cgi
%{_cgibin}/babel.*
%{_unitdir}/squidGuard.service
%{_unitdir}/transparent-proxying.service
%attr(0755,squid,squid) %{_localstatedir}/log/squidGuard
%attr(0755,squid,squid) %{_localstatedir}/log/squid/squidGuard.log

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.4-45
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Florian Weimer <fweimer@redhat.com> - 1.4-43
- Fixes for building in strict(er) C99 mode (#2148639)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4-36
- Patch for 64-bit segfault.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  9 2018 Bojan Smojver <bojan@rexursive.com> - 1.4-32
- add gcc build requirement

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 19 2017 Bojan Smojver <bojan@rexursive.com> - 1.4-28
- Helper protocol patch (bug #1443273, bug #1418267)
- Fix logrotate configuration (bug #1394601)
- Fix typo in transparent-proxying.service

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 21 2016 Jon Ciesla <limburgher@gmail.com> - 1.4-26
- Fix unitfile typo.

* Tue Jun 21 2016 Jon Ciesla <limburgher@gmail.com> - 1.4-25
- Patch for 20150201 (CVE-2015-8936).
- Fix log permissions.
- logrotate correction.
- Corrected config file.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 21 2014 Kevin Fenzi <kevin@scrye.com> - 1.4-22
- Rebuild for rpm bug 1131960

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.4-18
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Bojan Smojver <bojan@rexursive.com> - 1.4-16
- Fix for Berkeley DB 5

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Jon Ciesla <limburgher@gmail.com> - 1.4-14
- Build with LDAP support, BZ 834916.
- Dropped db4-isms.

* Tue Apr 17 2012 Jon Ciesla <limburgher@gmail.com> - 1.4-13
- Migrate to systemd.
- Stop messing with config noreplace for the config file in post.

* Mon Apr 16 2012 Jon Ciesla <limburgher@gmail.com> - 1.4-12
- Build against libdb again.

* Fri Apr 13 2012 Jon Ciesla <limburgher@gmail.com> - 1.4-11
- Add hardened build.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 26 2009 Jon Ciesla <limb@jcomserv.net> - 1.4-8
- Applying upstream patches for CVE-2009-3700, BZ 530862.

* Thu Sep 24 2009 Jon Ciesla <limb@jcomserv.net> - 1.4-7
- Make squidGuard.cgi config(noreplace)
- Relocated logs, updated logrotate file.
- Updated blacklist URL.

* Wed Sep 09 2009 Jon Ciesla <limb@jcomserv.net> - 1.4-6
- Include babel files, BZ 522038.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 05 2009 Jon Ciesla <limb@jcomserv.net> - 1.4-4
- Initscript cleanup, BZ 247065.

* Tue Feb 24 2009 Jon Ciesla <limb@jcomserv.net> - 1.4-3
- Drop chcon Req.

* Mon Feb 23 2009 Jon Ciesla <limb@jcomserv.net> - 1.4-2
- Dropping selinux policy and chcon, BZ 486634.
- Fixed URL of Source0.

* Wed Feb 18 2009 Jon Ciesla <limb@jcomserv.net> - 1.4-1
- Update to 1.4, BZ 485530.
- Building against compat-db46 until next version.

* Wed Feb 11 2009 Jon Ciesla <limb@jcomserv.net> - 1.3-1
- Update to 1.3.
- Dropped paths, sed patches, applied upstream.
- New SG-2008-06-13 patch.
 
* Wed Feb 11 2009 Jon Ciesla <limb@jcomserv.net> - 1.2.1-2
- Fix sg-2008-06-13, BZ 452467.

* Wed Feb 11 2009 Jon Ciesla <limb@jcomserv.net> - 1.2.1-1
- Update to 1.2.1,  BZ 245377.
- Dropped upstream patch.
- Updated blacklists.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.0-18
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.2.0-17
 - Rebuild for deps

* Fri Nov 16 2007 John Berninger <john at ncphotography dot com> 1.2.0-16
- Fix perms on cgi-bin files

* Mon Mar 26 2007 John Berninger <jwb at redhat dot com>	1.2.0-15
- Assert ownership of /var/squidGuard - bz 233915

* Tue Aug 29 2006 John Berninger <jwb at redhat dot com>	1.2.0-14
- Bump release 'cause I forgot to add a patch file that's required

* Tue Aug 29 2006 John Berninger <jwb at redhat dot com>	1.2.0-13
- general updates to confirm build on FC5/FC6
- updates to BuildRequires

* Fri Sep 09 2005 Oliver Falk <oliver@linux-kernel.at>		- 1.2.0-12
- Make it K12LTSP compatible, so a possible upgrade doesn't break
  anything/much...
  - Add SELinux stuff
  - Move dbdir to /var/squidGuard/blacklists, instead of /var/lib/squidGuard
  - Added update script and template config from/for K12
  - Add perlwarnings and sed patch
  - Install cgis in /var/www/cgi-bin
  - Added initrd stuff
- Remove questionable -ldb from make
- Remove questionable db version check

* Tue Sep 06 2005 Oliver Falk <oliver@linux-kernel.at>		- 1.2.0-11
- More bugs from Bug #165689
  Install cron script with perm 755
  Don't use SOURCE3 in install section, we need to use the patched one
  
* Mon Sep 05 2005 Oliver Falk <oliver@linux-kernel.at>		- 1.2.0-10
- Include GPL in doc section

* Mon Sep 05 2005 Oliver Falk <oliver@linux-kernel.at>		- 1.2.0-9
- More 'bugs' from Bug #165689
  Make changed on squid-getlist.html a patch, as sources should
  match upstream sources, so they are wget-able...

* Mon Sep 05 2005 Oliver Falk <oliver@linux-kernel.at>		- 1.2.0-8
- Bug #165689

* Thu May 19 2005 Oliver Falk <oliver@linux-kernel.at>		- 1.2.0-7
- Update blacklists
- Cleanup specfile

* Fri Apr 08 2005 Oliver Falk <oliver@linux-kernel.at>		- 1.2.0-6
- Fix build on RH 8 with db 4.0.14, by not applying the db4 patch

* Mon Feb 21 2005 Oliver Falk <oliver@linux-kernel.at> 		- 1.2.0-5
- Specfile cleaning
- Make it build with db4 again, by adding the db4-patch

* Fri Apr 12 2002 Oliver Pitzeier <oliver@linux-kernel.at>	- 1.2.0-4
- Tweaks

* Mon Apr 08 2002 Oliver Pitzeier <oliver@linux-kernel.at> 	- 1.2.0-3
- Rebuild

* Mon Apr 08 2002 Oliver Pitzeier <oliver@linux-kernel.at> 	- 1.2.0-2
- Updated the blacklists and put it into the right place
  I also descompress them
- Added a new "forbidden" script - the other ones are too
  old and don't work.  

* Fri Apr 05 2002 Oliver Pitzeier <oliver@linux-kernel.at> 	- 1.2.0-1
- Update to version 1.2.0

* Fri Jun  1 2001 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>
- cleaned up for rhcontrib

* Fri Oct 13 2000 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>
- initial build
