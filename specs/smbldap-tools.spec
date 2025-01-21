Summary:	User and group administration tools for Samba/OpenLDAP
Name:		smbldap-tools
Version:	0.9.11
Release:	28%{?dist}
License:	GPL-2.0-or-later
URL:		http://gna.org/projects/smbldap-tools/
Source0:	http://download.gna.org/smbldap-tools/sources/%{version}/smbldap-tools-%{version}.tar.gz
Patch0:		smbldap-tools-0.9.11-bz1456783.patch
Patch10:	smbldap-tools-0.9.9-config.patch
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	openssl
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(English)
BuildRequires:	sed
BuildRequires:	/usr/bin/pod2man
# Applications
BuildRequires:	perl(constant)
BuildRequires:	perl(Crypt::SmbHash)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(Encode)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(Getopt::Std)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IO::Socket::SSL)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Net::LDAP)
BuildRequires:	perl(Net::LDAP::Entry)
BuildRequires:	perl(Net::LDAP::Extension::SetPassword)
BuildRequires:	perl(Net::LDAP::LDIF)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(strict)
BuildRequires:	perl(Time::Local)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
# Dependencies
%if 0%{?fedora} < 38 && 0%{?rhel} < 10
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
%endif
# Need perl(IO::Socket::SSL) for LDAP over SSL (#122066, #207430)
Requires:	perl(IO::Socket::SSL)

%description
In conjunction with OpenLDAP and Samba-LDAP servers, this collection is useful
to add, modify and delete users and groups, and to change Unix and Samba
passwords. In those contexts they replace the system tools to manage users,
groups and passwords.

%prep
%setup -q

# Use usersdn instead of full LDAP search base when looking for user accounts (#1456783)
%patch -P 0

# Fedora integration
%patch -P 10

# Not allowed to have executable docs any more
chmod -R -c -x+X doc/

# Should still fix script interpreters though
sed -i -e 's|@PERL_COMMAND@|/usr/bin/perl|' smbldap-config.pl

%build
%configure
make

%install
make install DESTDIR=%{buildroot}
install -d -m 755 %{buildroot}%{_mandir}/man8/
install -p -m 644 smbldap-*.8 %{buildroot}%{_mandir}/man8/
install -d -m 755 %{buildroot}%{_sysconfdir}/smbldap-tools/
install -p -m 644 smbldap.conf %{buildroot}%{_sysconfdir}/smbldap-tools/smbldap.conf
install -p -m 600 smbldap_bind.conf %{buildroot}%{_sysconfdir}/smbldap-tools/smbldap_bind.conf

# Install migration script for pre-0.9.7 users
sed -e 's|@PERL_COMMAND@|/usr/bin/perl|' smbldap-upgrade-0.9.6.pl > \
	%{buildroot}%{_sbindir}/smbldap-upgrade-0.9.6.pl
chmod 755 %{buildroot}%{_sbindir}/smbldap-upgrade-0.9.6.pl

%files
%license COPYING
%doc ChangeLog CONTRIBUTORS FILES INFRA INSTALL README TODO
%doc doc/*.conf.example doc/migration_scripts/ doc/*.pdf
%dir %{_sysconfdir}/smbldap-tools/
%config(noreplace) %{_sysconfdir}/smbldap-tools/smbldap.conf
%config(noreplace) %{_sysconfdir}/smbldap-tools/smbldap_bind.conf
%{_sbindir}/smbldap-config
%{_sbindir}/smbldap-groupadd
%{_sbindir}/smbldap-groupdel
%{_sbindir}/smbldap-grouplist
%{_sbindir}/smbldap-groupmod
%{_sbindir}/smbldap-groupshow
%{_sbindir}/smbldap-passwd
%{_sbindir}/smbldap-populate
%{_sbindir}/smbldap-upgrade-0.9.6.pl
%{_sbindir}/smbldap-useradd
%{_sbindir}/smbldap-userdel
%{_sbindir}/smbldap-userlist
%{_sbindir}/smbldap-usermod
%{_sbindir}/smbldap-userinfo
%{_sbindir}/smbldap-usershow
%{perl_vendorlib}/smbldap_tools.pm
%{_mandir}/man8/smbldap-config.8*
%{_mandir}/man8/smbldap-groupadd.8*
%{_mandir}/man8/smbldap-groupdel.8*
%{_mandir}/man8/smbldap-grouplist.8*
%{_mandir}/man8/smbldap-groupmod.8*
%{_mandir}/man8/smbldap-groupshow.8*
%{_mandir}/man8/smbldap-passwd.8*
%{_mandir}/man8/smbldap-populate.8*
%{_mandir}/man8/smbldap-useradd.8*
%{_mandir}/man8/smbldap-userdel.8*
%{_mandir}/man8/smbldap-userinfo.8*
%{_mandir}/man8/smbldap-userlist.8*
%{_mandir}/man8/smbldap-usermod.8*
%{_mandir}/man8/smbldap-usershow.8*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.11-22
- Perl 5.36 rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.11-19
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.11-16
- Perl 5.32 rebuild

* Tue Mar 10 2020 Paul Howarth <paul@city-fan.org> - 0.9.11-15
- This package uses English

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.11-12
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.11-9
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Paul Howarth <paul@city-fan.org> - 0.9.11-6
- Use usersdn instead of full LDAP search base when looking for user accounts
  (#1456783)
- Drop EL-5 support
  - Drop BuildRoot: and Group: tags
  - Drop explicit buildroot cleaning in %%install section
  - Drop explicit %%clean section

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.11-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug  2 2016 Paul Howarth <paul@city-fan.org> - 0.9.11-3
- BR: perl-generators where available

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.11-2
- Perl 5.24 rebuild

* Tue May 10 2016 Paul Howarth <paul@city-fan.org> - 0.9.11-1
- Update to 0.9.11
  - smbldap.conf: New parameter: lanmanPassword (disabled by default)
  - smbldap_tools.pm: Export account_base_rid() for smbldap-usermod
  - smbldap-useradd:
    - Do not add dummy userPassword attribute
    - Die if adding a user entry fails
    - Set random password instead of insecure one on 'smbpasswd -a'
    - Check if specified UID is owned by local user (bug #2974)
    - Report error on exec() failure
  - smbldap-config:
    - Add support for renamed and new parameters (bug #2914)
    - Add POD text (bug #3013)
    - Do not assume "ou=..."-style value for "ldap users suffix", "ldap
      groups suffix" and "ldap machine suffix" in smb.conf
- Drop upstreamed patches
- Specify all dependencies as build dependencies too

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan  6 2016 Paul Howarth <paul@city-fan.org> - 0.9.10-9
- Drop support for legacy cert directory location
- Drop %%defattr, redundant since rpm 4.4

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.10-7
- Perl 5.22 rebuild

* Tue Feb 24 2015 Paul Howarth <paul@city-fan.org> - 0.9.10-6
- Add missing export of account_base_rid, needed by smbldap_usermod (#1138608)
  (https://gna.org/support/?3213)
- Use %%license where possible

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.10-5
- Perl 5.20 rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.9.10-2
- Perl 5.18 rebuild

* Fri Feb 15 2013 Paul Howarth <paul@city-fan.org> - 0.9.10-1
- Update to 0.9.10
  - smbldap_tools.pm: read_user_human_readable: Protect attribute values from
    Encode::decode_utf8() with Encode::FB_CROAK
  - smbldap_tools.pm: add is_attr_single_value() to check if a specified
    attribute is defined as single-value in the LDAP schema
  - smbldap-useradd, smbldap-usermod: check if mailRoutingAddress attribute is
    single-value or not
  - smbldap-usermod: remove mailRoutingAddress attribute if empty
  - smbldap-usermod: suppress "no such attribute" error on remove mail or
    mailLocalAddress attribute when already absent
- BR: /usr/bin/pod2man for man page generation
- smbldap-config now a regular script rather than treated as documentation
- Add POD to smbldap-config so we don't generate an empty manpage
  (https://gna.org/support/index.php?3013)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug  8 2012 Paul Howarth <paul@city-fan.org> - 0.9.9-1
- Update to 0.9.9
  - smbldap-userlist, smbldap-grouplist: specify Net::LDAP search attributes
    as an array ref, not a string
    (http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=681350)
  - smbldap-useradd: fix smbldap-passwd name
  - smbldap_tools.pm: $config{masterLDAP} and $config{slaveLDAP} can take a
    LDAP URI
  - smbldap_tools.pm: non-root user cannot run smbldap-passwd,
    smbldap-userinfo, smbldap-userlist and smbldap-grouplist with SSL-enabled
    LDAP server (http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=647860)
- Update config patch to reflect use of URIs for LDAP servers
- Drop upstreamed samba net location patch

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.9.8-2
- Perl 5.16 rebuild

* Wed Mar  7 2012 Paul Howarth <paul@city-fan.org> - 0.9.8-1
- NOTE: USERS THAT WISH TO KEEP USING THE LEGACY RID ALLOCATION ALGORITHM OF
  samba 2.x, WHICH WAS THE DEFAULT IN PREVIOUS VERSIONS OF smbldap-tools,
  SHOULD RUN THE smbldap-upgrade-0.9.6.pl SCRIPT AFTER UPGRADING TO THIS
  VERSION
- Update to 0.9.8
  - introduce autoconf (configure.in, Makefile.in and so on)
  - smbldap_tools.pm: use Encode instead of Unicode::MapUTF8
  - smbldap-populate, smbldap_tools.pm: use /nonexistent instead of /dev/null
    for guest's and computer's homeDirectory
  -  smbldap_tools.pm: add read_password() to avoid `stty -echo` hacks
  - use /usr/sbin/nscd -i instead of /etc/init.d/nscd
  - smbldap-passwd: do not use permuted -s option for the smbpasswd(1)
    command-line because the plain-old getopt(3) does not support it
  - add shadowAccount parameter in smbldap.conf to control whether to treat
    shadowAccount objectclass and attributes or not
  - rename smbldap.conf parameters:
    - hash_encrypt -> password_hash
    - crypt_salt_format -> password_crypt_salt_format
  - LDAPv3 Password Modify (RFC 3062) extended operation support when
    password_hash="exop" in smbldap.conf
  - use sambaNextRid attribute in sambaDomain entry for the next RID, same as
    Samba 3.0+ (only when sambaAlgorithmicRidBase attribute does NOT exist in
    sambaDomain entry for backward compatibility)
  - smbldap-populate: use Net::LDAP::Entry for populating entries
  - smbldap-usermod: new option: --ou NODE (move user entry to the specified
    organizational unit)
  - canonicalize user name to treat the memberUid as case-sensitive attribute
    (but the uid attribute is case-insensitive)
  - smbldap-useradd: new option: -p (allow to set password from STDIN without
    verification, e.g. using a pipe)
  - smbldap-useradd: new option: --non-unique (allow the creation of a user
    account with a duplicate [non-unique] UID)
  - smbldap-populate: create parent entry for $config{usersdn} (and others) if
    it does not exist (e.g. usersdn="ou=Users,ou=parent,${suffix}" in
    smbldap.conf)
  - smbldap-config: rename from configure.pl
  - smbldap-populate: create parent entry for $config{sambaUnixIdPooldn} if it
    does not exist
  - use Digest::SHA instead of Digest::SHA1 if Perl version > 5.10.0
  - smbldap-usermod: -M, -O, -T option: remove associated attribute when the
    null value is specified
- No longer need to remove IDEALX paths
- Drop now-redundant nscd and UTF-8 patches
- Use upstream build/install methodology
- Add patch to fix location of samba "net" command

* Sun Jan  8 2012 Paul Howarth <paul@city-fan.org> - 0.9.6-6
- Nobody else likes macros for commands

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.9.6-5
- Perl mass rebuild

* Fri Jun 10 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.9.6-4
- Perl 5.14 mass rebuild

* Mon Mar  7 2011 Paul Howarth <paul@city-fan.org> - 0.9.6-3
- update to upstream svn revision 36
  - fix broken configure.pl script (#677272)
  - smbldap_tools.pm: various minor fixes
  - smbldap-populate: fix wrong sambaGroupType values for local groups
  - smbldap-useradd: use -h option for chown of home directory
  - smbldap-useradd: extend -Z option to take multiple options
  - smbldap-usermod: set sambaPwdLastSet to the current time if "-B 0" is used
  - smbldap-usermod: extend -Z (--attr) option:
    - take multiple -Z options
    - append a value to a multi-value attribute by -Z +name=value
    - remove a value from a multi-value attribute by -Z -name=value
    - remove an attribute by -Z -name
- drop UTF-8 patch, no longer needed
- renumber patches to separate upstream and downstream patches
- rediff patches to apply cleanly to new base
- use a patch to recode the docs as UTF-8 rather than brute-force iconv

* Wed Feb  9 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec  9 2010 Paul Howarth <paul@city-fan.org> - 0.9.6-1
- update to 0.9.6
  - new tool: smbldap-grouplist (list LDAP groups)
  - smbldap-useradd, smbldap-usershow, smbldap-usermod:
    - change default encoding of givenName and sn to UTF-8 (bug #11717)
    - new option: -X (input/output encoding, defaults to UTF-8)
    - new option: -O (localMailAddress attribute)
    - changed option: -M (now sets only mail attribute)
    - home directory is now chowned as $userUidNumber:$userGidNumber
      to avoid race conditions (bug #11721)
    - use gecos as displayName if givenName and userSN not provided
      (bug #14517)
  - smbldap-passwd:
    - new option: -p (allow root to set password from STDIN without
      verification, e.g. using a pipe) (bug #11964)
    - change userPassword, shadowLastChange and shadowMax individually e.g. no
      shadow class or user may not have rights (bug #15052)
  - smbldap-groupmod: allow deletion of users from groups without a defined
    samba group SID)
  - remove references to smbldap_conf.pm
  - fix Z option in smbldap-useradd (custom LDAP attribute) (fixes #590429)
  - alphabetically reorganize options
  - fix several mis-spellings and typos in smbldap-useradd
- update source URL to reflect new upstream file layout
- drop upstreamed chown patch
- update remaining patches to remove fuzz
- drop dependency on openldap-servers (for /usr/sbin/slappasswd) as the
  default configuration is to hash passwords directly rather than calling out
  to slappasswd (#609056)
- drop dependency on samba-common (for /usr/bin/smbpasswd) as the default
  configuration handles the functionality directly rather than calling out to
  smbpasswd
- drop execute permissions from configuration/migration scripts in %%doc

* Wed Jun  2 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.9.5-7
- mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.9.5-6
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-5
- rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar  6 2009 Paul Howarth <paul@city-fan.org> 0.9.5-4
- change dependencies on samba and openldap-clients to samba-common and
  openldap-servers respectively
- invalidate nscd caches rather than restart nscd (#476504)
- add descriptions and bugzilla references to patch references in spec

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.9.5-3
- rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu May 22 2008 Paul Howarth <paul@city-fan.org> 0.9.5-2
- assume the user's locale uses UTF-8 rather than ISO-8859-1 (#441833)
- set ownership of home directory created by smbldap-useradd -m using UID
  number rather than username so that delays in LDAP replication don't
  affect the operation (#447758)

* Wed Apr 23 2008 Paul Howarth <paul@city-fan.org> 0.9.5-1
- update to 0.9.5
- update config patch

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.4-2
- rebuild for new perl

* Wed Sep 26 2007 Paul Howarth <paul@city-fan.org> 0.9.4-1
- update to 0.9.4
- new upstream, new URLs
- drop useradd_option-o enhancement patch, new included upstream
- update config patch
- new script smbldap-userlist included
- convert docs to UTF-8
- HTML docs no longer included with upstream source
- make and include manpages

* Thu Aug 23 2007 Paul Howarth <paul@city-fan.org> 0.9.2a-1
- update URLs, as original upstream source is now dead
- apply useradd_option-o enhancement patch from upstream
- clarify license as GPL version 2 or later
- add openssl buildreq for detection of TLS cert/key directory

* Sun Oct 29 2006 Paul Howarth <paul@city-fan.org> 0.9.2-5
- perl(Unicode::MapUTF8) now available on x86_64, so remove ExcludeArch
  and revert to noarch package (#211866)

* Mon Oct 23 2006 Paul Howarth <paul@city-fan.org> 0.9.2-4
- Exclude x86_64 as perl(Unicode::MapUTF8) is unavailable (#211866)
- A consequence of this is that the package can no longer be noarch
- Install smbldap_tools.pm without unnecessary exec bits
- Fix example idmapdn entry in config file

* Fri Sep 22 2006 Paul Howarth <paul@city-fan.org> 0.9.2-3
- Require IO::Socket::SSL to ensure we have SSL support even if perl-LDAP
  doesn't enforce this dependency (#122066, #207430)

* Fri Jan 27 2006 Paul Howarth <paul@city-fan.org> 0.9.2-2
- Incorporate smbldap.conf review suggestions from Steven Pritchard (#178905)
  Undefine SID so it is fetched with "net getlocalsid"
  Undefine sambaDomain so it is fetched from smb.conf
  TLS keys and certs should go in /etc/pki/tls/certs
  usersdn should be "ou=People,${suffix}" to match OpenLDAP migration tools
  groupsdn should be "ou=Group,${suffix}" to match OpenLDAP migration tools

* Wed Jan 25 2006 Paul Howarth <paul@city-fan.org> 0.9.2-1
- Update to 0.9.2

* Tue Jan 17 2006 Paul Howarth <paul@city-fan.org> 0.9.1-2
- Unpack tarball quietly
- Clean up file list
- Put smbldap_tools.pm in %%{perl_vendorlib} rather than %%{_sbindir}
- Add %%{?dist} tag

* Sat Jun 04 2005 Dag Wieers <dag@wieers.com> - 0.9.1-1 - 3108+/dag
- Updated to release 0.9.1.

* Tue Apr 05 2005 Dag Wieers <dag@wieers.com> - 0.8.8-1
- Updated to release 0.8.8.

* Wed Feb 16 2005 Dag Wieers <dag@wieers.com> - 0.8.7-2
- Fixed locations, removed /opt/IDEALX. (Alain Rykaert)

* Tue Feb 15 2005 Dag Wieers <dag@wieers.com> - 0.8.7-1
- Updated to release 0.8.7.

* Sat Jan 22 2005 Dag Wieers <dag@wieers.com> - 0.8.6-1
- Updated to release 0.8.6.

* Sun Jun 20 2004 Dag Wieers <dag@wieers.com> - 0.8.5-1
- Updated to release 0.8.5.

* Sat Mar 13 2004 Dag Wieers <dag@wieers.com> - 0.8.4-1
- Updated to release 0.8.4.

* Fri Dec 05 2003 Dag Wieers <dag@wieers.com> - 0.8.2-0
- Updated to release 0.8.2.

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 0.8.1-0
- Initial package. (using DAR)
