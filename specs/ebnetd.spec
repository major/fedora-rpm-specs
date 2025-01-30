%global _hardened_build 1

%global username	ebnetd
%global gecos		EBNET User
%global base_homedir	%{_localstatedir}/lib/
%global homedir		%{base_homedir}%{username}

Name:		ebnetd
Version:	1.0
Release:	53%{?dist}
License:	GPL-2.0-or-later
URL:		http://www.sra.co.jp/people/m-kasahr/ebnetd/
# For systemd.macros
BuildRequires:	systemd
BuildRequires:	eb-devel
BuildRequires:	gcc autoconf automake libtool
BuildRequires: make

Source0:	ftp://ftp.sra.co.jp/pub/misc/eb/%{name}-%{version}.tar.gz
Source1:	ebhttpd-README.dist
Source2:	%{name}-tmpfiles.conf
Source11:	ebnetd.socket
Source12:	ebnetd@.service
Source13:	ebnetd-instances.target
Source21:	ndtpd.socket
Source22:	ndtpd@.service
Source23:	ndtpd-instances.target
Source31:	ebhttpd.socket
Source32:	ebhttpd@.service
Source33:	ebhttpd-instances.target
Patch0:		ebnetd-1.0-info.patch
Patch1:		%{name}-aarch64.patch
Patch2:		%{name}-fix-conflict.patch
Patch3:		%{name}-gcc10.patch
Patch4:		%{name}-fedora-c99.patch
Patch5:		%{name}-fix-build.patch
Patch6:		%{name}-ftbfs.patch


Summary:	EBNET protocol server
Requires:	%{name}-common = %{version}-%{release}

%description
EBNET is a protocol to communicate to the EB library that is a C library
for accessing "CD-ROM books".

This package contains a EBNET protocol server.


%package common
Summary:		Common package for ebnetd families
Requires(pre):		shadow-utils
%{?systemd_requires}

%description common
EBNET is a protocol to communicate to the EB library that is a C library
for accessing "CD-ROM books".

This package contains a bunch of the common programs/files to be shared
by ebnetd families.


%package -n ndtpd
Summary:	Network Dictionary Transfer Protocol server
Requires:	%{name}-common = %{version}-%{release}

%description -n ndtpd
This package contains a daemon program to speak Network Dictionary Transfer
Protocol.


%package -n ebhttpd
Summary:	HTTP server for accessing "CD-ROM books"
Requires:	%{name}-common = %{version}-%{release}

%description -n ebhttpd
This package contains a specialized HTTP server that supports HTTP/1.0 and
HTTP/1.1. which provide a way to access "CD-ROM books" through the EB library.

Note that ebhttpd can't be used for generic WWW purposes.


%prep
%autosetup -p1
cp -p %{SOURCE1} .
autoreconf -i # to remove the unnecessary checking like g++

%build
%configure --disable-static --enable-ipv6 --with-eb-conf=%{_libdir}/eb.conf --with-logdir=%{_localstatedir}/log/ebnetd --localstatedir=%{base_homedir}

make

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="/usr/bin/install -p"

install -d $RPM_BUILD_ROOT%{_localstatedir}/run/ebnetd
install -d $RPM_BUILD_ROOT%{_tmpfilesdir}
install -d $RPM_BUILD_ROOT/lib/systemd/system
install -p -m0644 %{SOURCE11} $RPM_BUILD_ROOT/lib/systemd/system/
install -p -m0644 %{SOURCE21} $RPM_BUILD_ROOT/lib/systemd/system/
install -p -m0644 %{SOURCE31} $RPM_BUILD_ROOT/lib/systemd/system/
install -p -m0644 %{SOURCE12} $RPM_BUILD_ROOT/lib/systemd/system/
install -p -m0644 %{SOURCE22} $RPM_BUILD_ROOT/lib/systemd/system/
install -p -m0644 %{SOURCE32} $RPM_BUILD_ROOT/lib/systemd/system/
install -p -m0644 %{SOURCE13} $RPM_BUILD_ROOT/lib/systemd/system/
install -p -m0644 %{SOURCE23} $RPM_BUILD_ROOT/lib/systemd/system/
install -p -m0644 %{SOURCE33} $RPM_BUILD_ROOT/lib/systemd/system/
install -p -m0644 %{SOURCE2} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf

# correct timestamp
## for patch0
touch -r doc/ebnetd.info-1 doc/ebnetd.info
touch -r doc-ja/ebnetd-ja.info-1 doc/ebnetd-ja.info

for i in `echo $RPM_BUILD_ROOT%{_infodir}/ebnetd-ja*`; do
	iconv -f euc-jp -t utf-8 $i > $i-utf8 && mv $i-utf8 $i && touch -r doc-ja/`basename $i` $i
done

sed -i	-e 's/^\(user[ 	]*\)[a-z].*$/\1ebnetd/' \
	-e 's/^\(group[ 	]*\)[a-z].*$/\1ebnetd/' \
	-e 's,^\# \(work-path[ 	]*\)[a-z/].*$,\1/var/run/ebnetd,' \
	-e 's/^\(syslog-facility[ 	]*\)[a-z0-9].*$/\1daemon/' \
	-e '/^begin .*$/,/^end$/{D}' $RPM_BUILD_ROOT%{_sysconfdir}/ebnetd.conf.sample && \
mv $RPM_BUILD_ROOT%{_sysconfdir}/ebnetd.conf{.sample,} && \
touch -r ebnetd.conf.sample $RPM_BUILD_ROOT%{_sysconfdir}/ebnetd.conf

mkdir -p $RPM_BUILD_ROOT%{homedir} || :

# remove unnecessary files
rm -f $RPM_BUILD_ROOT%{_infodir}/dir


%post
%systemd_post ebnetd.socket

%preun
%systemd_preun ebnetd.socket ebnetd-instances.target

%postun
%systemd_postun_with_restart ebnetd.socket ebnetd-instances.target

%pre common
getent group %{username} > /dev/null || groupadd -r %{username}
getent passwd %{username} > /dev/null || useradd -r -g %{username} -d %{homedir} -s /sbin/nologin -c '%{gecos}' %{username}
exit 0

%post	-n ndtpd
%systemd_post ndtpd.socket

%preun	-n ndtpd
%systemd_preun ndtpd.socket ndtpd-instances.target

%postun	-n ndtpd
%systemd_postun_with_restart ndtpd.socket ndtpd-instances.target

%post	-n ebhttpd
%systemd_post ebnttpd.socket

%preun	-n ebhttpd
%systemd_preun ebhttpd.socket ebhttpd-instances.target

%postun	-n ebhttpd
%systemd_postun_with_restart ebhttpd.socket ebhttpd-instances.target

%files
%{_sbindir}/ebnetd
%{_sbindir}/ebncontrol
%{_sbindir}/ebncheck
%{_libexecdir}/ebnstat
/lib/systemd/system/ebnetd.socket
/lib/systemd/system/ebnetd@.service
/lib/systemd/system/ebnetd-instances.target

%files common
%license COPYING
%doc AUTHORS ChangeLog NEWS README UPGRADE
%lang(ja) %doc README-ja UPGRADE-ja
%{_sbindir}/ebndaily
%{_sbindir}/ebnupgrade
%{_infodir}/ebnetd.info*
%lang(ja) %doc %{_infodir}/ebnetd-ja.info*
%config(noreplace) %{_sysconfdir}/ebnetd.conf
%attr (-, ebnetd, ebnetd) %{homedir}
%attr (-, ebnetd, ebnetd) %{_localstatedir}/run/ebnetd
%{_tmpfilesdir}/%{name}.conf

%files -n ndtpd
%{_sbindir}/ndtp*
%{_libexecdir}/ndtpstat
/lib/systemd/system/ndtpd.socket
/lib/systemd/system/ndtpd@.service
/lib/systemd/system/ndtpd-instances.target

%files -n ebhttpd
%doc ebhttpd-README.dist
%{_sbindir}/ebht*
%{_libexecdir}/ebhtstat
/lib/systemd/system/ebhttpd.socket
/lib/systemd/system/ebhttpd@.service
/lib/systemd/system/ebhttpd-instances.target


%changelog
* Tue Jan 28 2025 Akira TAGOH <tagoh@redhat.com> - 1.0-53
- Fix FTBFS
  Resolves: rhbz#2340109

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May  8 2024 Akira TAGOH <tagoh@redhat.com> - 1.0-50
- Fix FTBFS.
  Resolves: rhbz#2261073

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb  8 2023 DJ Delorie <dj@redhat.com> - 1.0-46
- Fix C99 compatibility issue

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Akira TAGOH <tagoh@redhat.com> - 1.0-44
- Convert License tag to SPDX.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Akira TAGOH <tagoh@redhat.com> - 1.0-38
- Fix FTBFS.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Akira TAGOH <tagoh@redhat.com> - 1.0-33
- Drop R: initscripts. (#1592350)

* Mon Jun 18 2018 Akira TAGOH <tagoh@redhat.com> - 1.0-32
- Remove install-info from scriptlet according to
  https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/MP2QVJZBOJZEOQO2G7UB2HLXKXYPF2G5/

* Mon Feb 19 2018 Akira TAGOH <tagoh@redhat.com> - 1.0-31
- Add BR: gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Akira TAGOH <tagoh@redhat.com> - 1.0-29
- Replace systemd-units deps with %%{?systemd_requires}

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 14 2017 Ville Skyttä <ville.skytta@iki.fi> - 1.0-25
- Move tmpfiles.d config to %%{_tmpfilesdir}
- Install COPYING as %%license

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 10 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0-20
- Add BR: systemd for systemd.macros (RHBZ #1017688).

* Mon Sep  2 2013 Akira TAGOH <tagoh@redhat.com> - 1.0-19
- Rebuilt against the latest eb.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 24 2013 Akira TAGOH <tagoh@redhat.com> - 1.0-17
- Rebuilt with PIE flags. (#955455)

* Tue Mar 26 2013 Akira TAGOH <tagoh@redhat.com> - 1.0-16
- Rebuilt for aarch64 support (#925291)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 29 2012 Akira TAGOH <tagoh@redhat.com> - 1.0-14
- Update scriptlets with new systemd rpm macros (#850099)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Akira TAGOH <tagoh@redhat.com> - 1.0-12
- systemd support. (Jóhann B. Guðmundsson, #737695)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu May 26 2011 Akira TAGOH <tagoh@redhat.com> - 1.0-10
- Correct a typo to support tmpfiles.d.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb  7 2011 Akira TAGOH <tagoh@redhat.com> - 1.0-8
- tmpfiles.d support. (#656580)

* Mon Aug 31 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-7
- F-12: Rebuild against new eb

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Oct 12 2008 Akira TAGOH <tagoh@redhat.com> - 1.0-4
- Rename ebhttpd-README.fedora to ebhttpd-README.dist.

* Sat Oct 11 2008 Akira TAGOH <tagoh@redhat.com> - 1.0-3
- Add ebhttpd-README.fedora file.
- Get rid of Conflicts from ebhttpd.

* Mon Jul  7 2008 Akira TAGOH <tagoh@redhat.com> - 1.0-2
- Remove %%{_infodir}/dir.
- Remove doc files in all subpackages except -common.

* Fri May 16 2008 Akira TAGOH <tagoh@redhat.com> - 1.0-1
- Initial packaging.

