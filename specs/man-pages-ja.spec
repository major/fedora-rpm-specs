Name: man-pages-ja
Version: 20260815
Release: %autorelease

# BSD-3-Clause - shadow, bsd-games, byacc, bzip2, dhcpcd, dump, file, hdparm, rssh, tcp_wrappers, tcsh
# GFDL-1.3-or-later - GNU_*, cron, glibc-linuxthreads
# BSD-4-Clause-UC/Linux-man-pages-copyleft/GPL-2.0-or-later/BSD-4.3TAHOE/Linux-man-pages-1-para/GPL-1.0-or-later/BSD-3-Clause/MIT/Spencer-94/LicenseRef-LDPL/BSD-2-Clause/LicenseRef-Fedora-UltraPermissive/LicenseRef-Fedora-Public-Domain - LDP_manpages, gnumaniak, ld.so
# GPL-2.0-or-later - SysVinit, acl, apmd, at, autofs, ebtables, eject, e2fsprogs, iptables, logrotate, man-db, net-tools, pciutils, psmisc, rdate, rp-pppoe, rpm, smartmontools, uudeview
# ISC - bind, dhcp, dhcp2, sudo
# GPL-2.0-or-later and LGPL-2.1-or-later - cdparanoia
# Apache-2.0 WITH LLVM-exception AND BSD-3-Clause AND Zlib AND BSD-2-Clause - cups
# ??? - microcode_ctl, procps
# LicenseRef-Fedora-Public-Domain - expect
# GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain - fetchmail
# BSD-3-Clause AND LGPL-2.0-or-later - flex
# GPL-2.0-or-later - mpg123
# BSD-3-Clause - ncftp
# MIT - ncurses
# MIT and GPL-2.0-only and GPL-2.0-or-later and BSD-3-Clause - nfs-utils
# BSD-4.3TAHOE and LGPLv2+ and GPLv2+ and Public Domain - ppp
# GPL+ - procinfo, setserial
# GPL-2.0-or-later or Artistic-1.0-Perl - procmail
# BSD and GPLv2 and GPLv2+ - quota
# GPL-3.0-or-later - rsync
# Sendmail-8.23 - sendmail
# BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND BSD-4-Clause-UC AND ISC AND NTP - tcpdump
# GPLv2 and GPLv2+ and LGPLv2+ and BSD with advertising and Public Domain - util-linux
# GPL-2.0-only WITH vsftpd-openssl-exception - vsftpd
# xinetd - xinetd
# GPLv2 - yp-tools, ypbind-mt, ypserv
License: BSD-3-Clause AND GFDL-1.3-or-later AND BSD-4-Clause-UC AND Linux-man-pages-copyleft AND GPL-2.0-or-later AND BSD-4.3TAHOE AND Linux-man-pages-1-para AND GPL-1.0-or-later AND MIT AND Spencer-94 AND LicenseRef-LDPL AND BSD-2-Clause AND ISC AND LGPL-2.1-or-later AND Apache-2.0 WITH LLVM-exception AND Zlib AND LicenseRef-Fedora-Public-Domain AND LicenseRef-Fedora-UltraPermissive AND GPL-2.0-only AND LGPL-2.0-or-later AND (GPL-2.0-or-later OR Artistic-1.0-Perl) AND GPL-3.0-or-later AND Sendmail-8.23 AND BSD-4-Clause AND NTP AND GPL-2.0-only WITH vsftpd-openssl-exception AND xinetd
BuildArch: noarch
BuildRequires: make
BuildRequires: perl(Env), perl(Encode)
URL: https://github.com/linux-jm/manual

Source: %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1: %{name}-rpm.pl
Source2: %{name}-tail.1
Source3: %{name}-echo.1
Source4: %{name}-tar.1
Source5: %{name}-snmptrapd.8
Patch0: %{name}-fix-configure.perl.patch
Patch1: %{name}-fix-pkgs-list.patch
Patch15: %{name}-358081-sysctl-warn.patch
Patch18: %{name}-433692-printf.1.patch
Patch21: %{name}-456263-top.1.patch
Patch23: %{name}-451238-sysctl.8.patch
Patch25: %{name}-454419-echo.1.patch
Patch26: %{name}-457361-wall.1.patch
Patch27: %{name}-20090615-vmstat.8.patch
Patch28: %{name}-493783-edquota.8.patch
Patch29: %{name}-486655-mkfs.8.patch
Patch32: %{name}-527638-chgrp.1.patch
Patch36: %{name}-600321-snmpd.conf.5.patch
Patch37: %{name}-669646-pmap.1.patch
Patch40: %{name}-993511-crontab.1.patch
Patch41: %{name}-1661363-telnet.1.patch

Summary: Japanese man (manual) pages from the Japanese Manual Project
Requires: man-pages-reader
Supplements: (man-pages and langpacks-ja)

%description
Japanese Manual pages, translated by JM-Project (Japanese Manual Project).

%prep
%autosetup -n %{name}-%{version} -p1

# Remove non-free man-pages
rm ./manual/LDP_man-pages/man2/sysinfo.2
rm ./manual/LDP_man-pages/man2/getitimer.2

%build
sed -ie 's/::/:GNU coreutils:/g' manual/GNU_coreutils/translation_list
perl %{SOURCE1} '$DESTDIR' $RPM_BUILD_DIR/%{name}-%{version}/script/pkgs.list | make

%install
DESTDIR=$RPM_BUILD_ROOT sh installman.sh

rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man1/{chage.1,gpasswd.1,sg.1,apropos.1,man.1,whatis.1,newgrp.1,passwd.1}*
rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man5/{faillog.5,shadow.5,login.defs.5}*
rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man8/{adduser.8,chpasswd.8,faillog.8,groupadd.8,groupdel.8,groupmod.8,grpck.8,grpconv.8,grpunconv.8,lastlog.8,newusers.8,pwck.8,pwconv.8,pwunconv.8,rpm2cpio.8,useradd.8,userdel.8,usermod.8,vipw.8}*
rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man8/{rpmgraph,rpmcache,rpmbuild,rpm,vigr}.8*
# for Bug#580465
rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man8/{halt,init,poweroff,reboot,runlevel,shutdown,telinit}.8*
# for Bug#623986
rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man8/{fastboot,fasthalt}.8*
# for Bug#1611883
rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man1/{manpath,zsoelim}.1*
rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man5/manpath.5*
rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man8/{accessdb,catman,mandb}.8*

# fix su(1) man page.
if [ -f $RPM_BUILD_DIR/%{name}-%{version}/manual/GNU_sh-utils/man1/su.1 ]; then
	rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man1/su.1*
	install -p -m0644 $RPM_BUILD_DIR/%{name}-%{version}/manual/GNU_sh-utils/man1/su.1 $RPM_BUILD_ROOT%{_mandir}/ja/man1/
fi
# fix kill(1) man page.
if [ -f $RPM_BUILD_DIR/%{name}-%{version}/manual/util-linux/man1/kill.1 ]; then
	rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man1/kill.1*
	install -p -m0644 $RPM_BUILD_DIR/%{name}-%{version}/manual/util-linux/man1/kill.1 $RPM_BUILD_ROOT%{_mandir}/ja/man1/
fi
# fix chown(1) man page.
if [ -f $RPM_BUILD_DIR/%{name}-%{version}/manual/GNU_fileutils/man1/chown.1 ]; then
	rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man1/chown.1*
	install -p -m0644 $RPM_BUILD_DIR/%{name}-%{version}/manual/GNU_fileutils/man1/chown.1 $RPM_BUILD_ROOT%{_mandir}/ja/man1/
fi
# fix hostname(1) man page.
if [ -f $RPM_BUILD_DIR/%{name}-%{version}/manual/net-tools/man1/hostname.1 ]; then
	rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man1/hostname.1*
	install -p -m0644 $RPM_BUILD_DIR/%{name}-%{version}/manual/net-tools/man1/hostname.1 $RPM_BUILD_ROOT%{_mandir}/ja/man1/
fi
## For Bug#128612
#mv $RPM_BUILD_ROOT%{_mandir}/ja/man8/in.telned.8.gz $RPM_BUILD_ROOT%{_mandir}/ja/man8/in.telnetd.8.gz
## For Bug#128833
#mv $RPM_BUILD_ROOT%{_mandir}/ja/man8/in.rlogin.8.gz $RPM_BUILD_ROOT%{_mandir}/ja/man8/in.rlogind.8.gz
# For Bug#551476
rm -rf $RPM_BUILD_ROOT%{_mandir}/ja/man1/tail.1*
install -p -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/ja/man1/tail.1
# For Bug#642186
rm -rf $RPM_BUILD_ROOT%{_mandir}/ja/man1/echo.1*
install -p -m644 %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/ja/man1/echo.1
# For Bug#717182
rm -rf $RPM_BUILD_ROOT%{_mandir}/ja/man1/tar.1*
install -p -m644 %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/ja/man1/tar.1
# For Bug#1738420
rm -rf $RPM_BUILD_ROOT%{_mandir}/ja/man8/snmptrapd.8*
install -p -m644 %{SOURCE5} $RPM_BUILD_ROOT%{_mandir}/ja/man8/snmptrapd.8

## drop manpages not shipped English manpages in Fedora
rm -rf $RPM_BUILD_ROOT%{_mandir}/ja/man1/{achfile,acleandir,aecho,afile,apm,apmsleep,apple_cp,apple_mv,apple_rm,biff,bzegrep,bzfgrep,cardinfo,cccp,cdrecord,chkdupexe,copydir,cvpasswd,cvsup,dnskeygen,dnsquery,expiry,forward,gasp,getzones,hman,line,lpq,lpr,lprm,lptest,man2html,manlint,mirrordir,nbp,nbplkup,nbprgstr,nbpunrgstr,nlmconv,pap,papstatus,pg,pidof,pppoe-wrapper,pslogin,psorder,rbash,readcd,recursdir,rpcgen,scgcheck,secure-mcserv,tcpdump,tkpppoe,updatedb,xapm,zebedee}.1*
rm -rf $RPM_BUILD_ROOT%{_mandir}/ja/man2/{pciconfig_iobase,pciconfig_read,pciconfig_write}.2*
rm -rf $RPM_BUILD_ROOT%{_mandir}/ja/man3/{atalk_aton,btree,db,dbopen,hash,mpool,nbp_name,pthread_mutexattr_getkind_np,pthread_mutexattr_setkind_np,pw_auth,recno,setproctitle}.3*
rm -rf $RPM_BUILD_ROOT%{_mandir}/ja/man4/{atalk,i82365,magic,pcmcia_core}.4*
rm -rf $RPM_BUILD_ROOT%{_mandir}/ja/man5/{atalkd.conf,bootparams,dm.conf,ftpconversions,ftphosts,ftpservers,initscript,lilo.conf,limits,locatedb,login.access,man.conf,papd.conf,pcmcia,porttime,printcap,stab,suauth}.5*
rm -rf $RPM_BUILD_ROOT%{_mandir}/ja/man6/{banner,bs,factor,fish,wargames}.6*
rm -rf $RPM_BUILD_ROOT%{_mandir}/ja/man7/{groff_mwww,mmroff}.7*
rm -rf $RPM_BUILD_ROOT%{_mandir}/ja/man8/{adsl-connect,adsl-setup,adsl-start,adsl-status,adsl-stop,apmd,apple_driver,atalkd,cardctl,cardmgr,comsat,cvsupd,cytune,dhcpcd,display-services,dm,dmesg,domainname,dpasswd,dump_cis,elvtune,fetchmailconf,fsck.minix,ftl_check,ftl_format,ftpd,ftprestart,ide_info,ifport,ifuser,in.comsat,in.ftpd,in.writed,inetd,ipchains,ipcrm,ipcs,ipfwadm,isoinfo,lidsadm,lidsconf,lilo,lockd,logoutd,lpc,lpd,lspnp,mail.local,makewhatis,mkfs.bfs,mkfs.minix,mkhybrid,mkisofs,mkpasswd,mkrescue,named-bootconf,named-xfer,ndc,need,nhfsgraph,nhfsnums,nhfsrun,nhfsstone,nisdomainname,nslookup,nsupdate,pack_cis,papd,papstatus,pcinitrd,provide,psf,pwauth,qtool,quot,ramsize,rarp,raw,rdev,renice,ripquery,rootflags,routed,rpc.lockd,rpc.ugidd,scsi_info,setfdprm,setpnp,setsid,shadowconfig,simpleinit,strfile,tcpdchk,telnetlogin,timed,timedc,ugidd,vidmode,writed,ypdomainname}.8*

# accumulate translation_lists
mkdir $RPM_BUILD_DIR/%{name}-%{version}/translation_lists
(cd $RPM_BUILD_DIR/%{name}-%{version}/manual
for i in `find -type f -name translation_list`; do
	package=`basename \`dirname $i\``;
	name=`basename $i`;
	if [ -s $i ]; then
		cp -a $i $RPM_BUILD_DIR/%{name}-%{version}/translation_lists/$package.$name;
	fi
done
)
 
%files
%doc README translation_lists
%{_mandir}/ja/man*/*


%changelog
%autochangelog
