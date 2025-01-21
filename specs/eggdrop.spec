# Private libraries must not be exposed globally by RPM
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$

Summary:        World's most popular Open Source IRC bot
Name:           eggdrop
Version:        1.10.0
Release:        1%{?dist}
# Eggdrop itself is GPL-2.0-or-later but uses other source codes, breakdown:
# GPL-2.0-only: src/mod/pbkdf2.mod/{pbkdf2,tclpbkdf2}.c
# BSD-3-Clause: src/compat/inet_aton.c
# ISC: src/compat/{base64,explicit_bzero,inet_aton,strlcpy}.c
# LicenseRef-Fedora-Public-Domain: src/md5/{md5.h,md5c.c}
# MIT: doc/html/_static/{jquery,underscore}.js
License:        GPL-2.0-or-later AND GPL-2.0-only AND BSD-3-Clause AND ISC AND LicenseRef-Fedora-Public-Domain AND MIT
URL:            https://www.eggheads.org/
Source0:        https://ftp.eggheads.org/pub/eggdrop/source/1.10/%{name}-%{version}.tar.gz
Source1:        https://ftp.eggheads.org/pub/eggdrop/source/1.10/%{name}-%{version}.tar.gz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/E01C240484DE7DBE190FE141E7667DE1D1A39AFF
Patch0:         eggdrop-1.6.17-langdir.patch
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tcl-devel >= 8.5
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  python-devel >= 3.8.0
%else
# Application Stream supported until EOL of RHEL 8
BuildRequires:  python3.12-devel
%endif

%description
Eggdrop is the world's most popular Open Source IRC bot, designed
for flexibility and ease of use. It is extendable with Tcl scripts
and/or C modules, has support for the big five IRC networks and is
able to form botnets, share partylines and userfiles between bots.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch -P0 -p1 -b .langdir
touch -c -r doc/man1/%{name}.1{.langdir,}

%build
export CFLAGS="$RPM_OPT_FLAGS -std=gnu17"  # https://github.com/eggheads/eggdrop/issues/1740
%configure
make config
# Parallel builds are not supported 
make

%install
mkdir -p $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_libdir},%{_mandir}/man1}/
%make_install DEST=$RPM_BUILD_ROOT%{_datadir}/%{name}

rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/{README,doc,eggdrop*,filesys,logs,modules,scripts/CONTENTS}
install -D -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

# Fix paths while installing man page
sed -e 's@doc/@%{_pkgdocdir}/@g' doc/man1/%{name}.1 > $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
touch -c -r doc/man1/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

# Move modules into /usr/lib*
mv -f $RPM_BUILD_ROOT{%{_datadir}/%{name}/modules-%{version},%{_libdir}/%{name}}/

# Fix paths of example eggdrop(-basic).conf
for conf in eggdrop.conf eggdrop-basic.conf; do
  sed -e '2d' -e '1s@^.*@#!%{_bindir}/%{name}@' \
      -e 's@scripts/@%{_datadir}/%{name}/scripts/@g' \
      -e 's@help/@%{_datadir}/%{name}/help/@g' \
      -e 's@modules/@%{_libdir}/%{name}/@g' \
      -e 's@text/"@%{_datadir}/%{name}/text/"@g' \
      -e 's@/etc/ssl/@%{_sysconfdir}/pki/tls/certs/@g' \
      -e 's@^#\(set ssl-cafile\) ""@\1 "%{_sysconfdir}/pki/tls/certs/ca-bundle.crt"@g' \
      ${conf} > ${conf}.mod
  touch -c -r ${conf}{,.mod}; mv -f ${conf}{.mod,}
done

%files
%license COPYING
%doc FEATURES NEWS README doc/Changes1.10 eggdrop.conf eggdrop-basic.conf
%doc doc/ABOUT doc/ACCOUNTS doc/AUTOSCRIPTS doc/BANS doc/BOTNET doc/BUG-REPORT
%doc doc/FIRST-SCRIPT doc/IPV6 doc/IRCv3 doc/PARTYLINE doc/PBKDF2 doc/TLS
%doc doc/TRICKS doc/TWITCH doc/USERS doc/tcl-commands.doc doc/settings doc/html
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Jan 19 2025 Robert Scheck <robert@fedoraproject.org> 1.10.0-1
- Upgrade to 1.10.0 (#2337700, #2338018)

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Robert Scheck <robert@fedoraproject.org> 1.9.5-1
- Upgrade to 1.9.5 (#2169600)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 15 2022 Robert Scheck <robert@fedoraproject.org> 1.9.4-1
- Upgrade to 1.9.4 (#2142049)

* Sat Aug 13 2022 Robert Scheck <robert@fedoraproject.org> 1.9.3-1
- Upgrade to 1.9.3 (#2106485)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 09 2022 Robert Scheck <robert@fedoraproject.org> 1.9.2-1
- Upgrade to 1.9.2 (#2033908)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.9.1-3
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 31 2021 Robert Scheck <robert@fedoraproject.org> 1.9.1-1
- Upgrade to 1.9.1 (#1958575)

* Sun Mar 28 2021 Robert Scheck <robert@fedoraproject.org> 1.9.0-1
- Upgrade to 1.9.0 (#1933540)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Robert Scheck <robert@fedoraproject.org> 1.8.4-1
- Upgrade to 1.8.4 (#1546581)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 1.6.21-21
- Add missing #include for gcc-10

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Robert Scheck <robert@fedoraproject.org> 1.6.21-15
- Added patch for build failures with "-Werror=format-security" 

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.6.21-13
- Rebuild due to bug in RPM (RHBZ #1468476)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 20 2015 Robert Scheck <robert@fedoraproject.org> 1.6.21-10
- Added patch to make rebuilding with GCC 5 working

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.6.21-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 08 2012 Robert Scheck <robert@fedoraproject.org> 1.6.21-2
- Private libraries are not be exposed globally by RPM

* Sun Jan 08 2012 Robert Scheck <robert@fedoraproject.org> 1.6.21-1
- Upgrade to 1.6.21 (#771492)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 28 2010 Robert Scheck <robert@fedoraproject.org> 1.6.20-1
- Upgrade to 1.6.20

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.6.19-6
- Use bzipped upstream tarball.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 26 2009 Robert Scheck <robert@fedoraproject.org> 1.6.19-4
- Added upstream ctcpfix to solve CVE-2009-1789 (#502650)

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 1.6.19-3
- Rebuild for gcc 4.4 and rpm 4.6

* Sat Aug 30 2008 Robert Scheck <robert@fedoraproject.org> 1.6.19-2
- Re-diffed eggdrop configuration patch for no fuzz

* Tue Apr 22 2008 Robert Scheck <robert@fedoraproject.org> 1.6.19-1
- Upgrade to 1.6.19

* Mon Feb 25 2008 Robert Scheck <robert@fedoraproject.org> 1.6.18-16
- Cause the DNS linking against libc rather libdns (#433111)

* Fri Feb 15 2008 Robert Scheck <robert@fedoraproject.org> 1.6.18-15
- Rebuild for bind 9.5.0

* Sun Feb 10 2008 Robert Scheck <robert@fedoraproject.org> 1.6.18-14
- Added patch to provide better non-latin support (#429621)

* Sat Jan 05 2008 Robert Scheck <robert@fedoraproject.org> 1.6.18-13
- Rebuild for tcl 8.5

* Sat Dec 08 2007 Robert Scheck <robert@fedoraproject.org> 1.6.18-12
- Added a patch to fix some stack based overflows (CVE-2007-2807)

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.6.18-11
- Rebuild for selinux ppc32 issue.

* Tue Aug 28 2007 Robert Scheck <robert@fedoraproject.org> 1.6.18-10
- Updated the license tag according to the guidelines

* Thu Jul 19 2007 Jesse Keating <jkeating@redhat.com> 1.6.18-9
- Rebuild for new bind

* Mon May 07 2007 Robert Scheck <robert@fedoraproject.org> 1.6.18-8
- Rebuild

* Tue Mar 13 2007 Robert Scheck <robert@fedoraproject.org> 1.6.18-7
- Rebuild for bind 9.4.0

* Wed Feb 14 2007 Robert Scheck <robert@fedoraproject.org> 1.6.18-6
- Rebuild for tcl 8.4

* Sat Feb 03 2007 Robert Scheck <robert@fedoraproject.org> 1.6.18-5
- Rebuild for tcl 8.5

* Wed Oct 25 2006 Robert Scheck <robert@fedoraproject.org> 1.6.18-4
- Rebuild

* Mon Oct 16 2006 Robert Scheck <robert@fedoraproject.org> 1.6.18-3
- Rebuild

* Sun Sep 03 2006 Robert Scheck <robert@fedoraproject.org> 1.6.18-2
- Rebuild for Fedora Core 6

* Sat Jul 15 2006 Robert Scheck <robert@fedoraproject.org> 1.6.18-1
- Upgrade to 1.6.18

* Mon Jun 19 2006 Robert Scheck <robert@fedoraproject.org> 1.6.17-4
- Replaced hardcoded LANGDIR with /usr/share/eggdrop/language to
  avoid use of EGG_LANGDIR env variable per default (#194481 #c9)

* Sun Jun 18 2006 Robert Scheck <robert@fedoraproject.org> 1.6.17-3
- Changes to match with Fedora Packaging Guidelines (#194481)

* Sun Mar 12 2006 Robert Scheck <robert@fedoraproject.org> 1.6.17-2
- Don't deliver autobotchk and botchk as documentation

* Sun Jan 22 2006 Robert Scheck <robert@fedoraproject.org> 1.6.17-1
- Upgrade to 1.6.17
- Initial spec file for Fedora Core
