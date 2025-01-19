Name:            monotone
Version:         1.1
Release:         51%{?dist}
Summary:         A free, distributed version control system
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:         GPL-2.0-or-later
URL:             http://monotone.ca/
Source0:         http://monotone.ca/downloads/%{version}/%{name}-%{version}.tar.bz2
Source1:         monotone.service
Source2:         monotone.sysconfig
Source3:         README.monotone-server
Source4:         monotone-server-tmpfiles.conf
Source5:         monotone-server-initdb
Source6:         monotone-server-migratedb
Source7:         monotone-server-genkey
Source8:         monotone-server-import
Patch0:          monotone-1.0-stacktrace-on-crash.patch
Patch1:          monotone-1.1-iostream.patch
Patch2:          monotone-1.1-lua-integer.patch
Patch3:          monotone-1.1-pcre.patch
Patch4:          monotone-1.1-py3.patch
Patch5:          monotone-1.1-lua-ql.patch
Patch6:          monotone-1.1-boost.patch
Patch7:          monotone-1.1-string-overflow.patch
Patch8:          monotone-1.1-catch.patch
BuildRequires:   gcc-c++
BuildRequires:   make
BuildRequires:   perl-generators
BuildRequires:   zlib-devel
BuildRequires:   boost-devel >= 1.33.1
BuildRequires:   botan-devel >= 1.6.3
BuildRequires:   pcre-devel >= 7.4
BuildRequires:   sqlite-devel >= 3.3.8
BuildRequires:   lua-devel >= 5.1
BuildRequires:   libidn-devel
BuildRequires:   systemd

# Required by the test suite:
BuildRequires:   cvs
BuildRequires:   bash-completion
BuildRequires:   expect


# Filter unwanted dependencies
%{?perl_default_filter}

%description
monotone is a free, distributed version control system.
It provides fully disconnected operation, manages complete
tree versions, keeps its state in a local transactional
database, supports overlapping branches and extensible
metadata, exchanges work over plain network protocols,
performs history-sensitive merging, and delegates trust
functions to client-side RSA certificates.


%package server
Summary: Standalone server setup for monotone
Requires: monotone = %{version}-%{release}
Requires(pre): shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description server
This package provides an easy-to-use standalone server setup for monotone.


%package -n perl-Monotone
Summary: Perl Module for monotone
Requires: monotone = %{version}-%{release}


%description -n perl-Monotone
This is a simple Perl module to start a monotone automate sub-process
and then pass commands to it.


%prep
%autosetup -p1


%build
export LC_MESSAGES=en_US
%configure
%make_build


%check
#export LC_MESSAGES=en_US
#export DISABLE_NETWORK_TESTS=1
#export MTN_STACKTRACE_ON_CRASH=1
#make check || { head -n-0 test/work/*.log; false; }


%install
export LC_MESSAGES=en_US
%make_install
rm -f %{buildroot}%{_infodir}/dir
mv %{buildroot}%{_datadir}/doc/%{name} _doc

%find_lang %{name}

mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_localstatedir}/lib
ln -snf ../bin/mtn %{buildroot}%{_sbindir}/monotone-server
ln -snf mtn.1 %{buildroot}%{_mandir}/man1/monotone-server.1
install -D -m 0644 -p %{SOURCE1} %{buildroot}%{_unitdir}/monotone.service

install -D -m 0644 -p %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/monotone
install -d -m 0755 %{buildroot}%{_sysconfdir}/monotone
install -d -m 0750 %{buildroot}%{_sysconfdir}/monotone/private-keys
install -d -m 0770 %{buildroot}%{_localstatedir}/lib/monotone
install -d -m 0755 %{buildroot}%{_localstatedir}/run/monotone
install -D -m 0644 %{SOURCE4} \
             %{buildroot}%{_tmpfilesdir}/monotone.conf

install -D -m 0755 -p %{SOURCE5} %{buildroot}%{_libexecdir}/monotone-server-initdb
install -D -m 0755 -p %{SOURCE6} %{buildroot}%{_libexecdir}/monotone-server-migratedb
install -D -m 0755 -p %{SOURCE7} %{buildroot}%{_libexecdir}/monotone-server-genkey
install -D -m 0755 -p %{SOURCE8} %{buildroot}%{_libexecdir}/monotone-server-import

# These do not actually wind up in the package, due to %%ghost.
install -m 0440 /dev/null \
             %{buildroot}%{_sysconfdir}/monotone/passphrase.lua
install -m 0640 /dev/null \
             %{buildroot}%{_sysconfdir}/monotone/read-permissions
install -m 0640 /dev/null \
             %{buildroot}%{_sysconfdir}/monotone/write-permissions
install -m 0644 /dev/null \
             %{buildroot}%{_sysconfdir}/monotone/monotonerc
install -m 0640 /dev/null \
             %{buildroot}%{_localstatedir}/lib/monotone/server.mtn

install -m 0644 -p %{SOURCE3} .

install -D -m 0644 -p contrib/Monotone.pm \
             %{buildroot}%{perl_vendorlib}/Monotone.pm

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv %{buildroot}%{_sysconfdir}/bash_completion.d/monotone.bash_completion \
             %{buildroot}%{_datadir}/bash-completion/completions/%{name}.bash_completion


%files -f %{name}.lang
%doc AUTHORS NEWS README UPGRADE
%doc _doc/*
%license COPYING
%{_bindir}/mtn
%{_bindir}/mtnopt
%{_bindir}/mtn-cleanup
%{_infodir}/monotone.info*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}.bash_completion
%{_mandir}/man1/mtn.1*
%{_mandir}/man1/mtnopt.1*
%{_mandir}/man1/mtn-cleanup.1*
%{_datadir}/monotone


%files -n perl-Monotone
%{perl_vendorlib}/Monotone.pm


%files server
%doc README.monotone-server
%{_sbindir}/monotone-server
%{_mandir}/man1/monotone-server.1*
%{_unitdir}/monotone.service
%{_libexecdir}/monotone-server-initdb
%{_libexecdir}/monotone-server-migratedb
%{_libexecdir}/monotone-server-genkey
%{_libexecdir}/monotone-server-import
%dir %attr(0755,monotone,monotone) %{_localstatedir}/run/monotone
%{_tmpfilesdir}/monotone.conf
%config(noreplace) %{_sysconfdir}/sysconfig/monotone
%dir %attr(0755,root,monotone) %{_sysconfdir}/monotone
%dir %attr(0750,root,monotone) %{_sysconfdir}/monotone/private-keys
%attr(0640,root,monotone) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) %{_sysconfdir}/monotone/monotonerc
%attr(0440,root,monotone) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) %{_sysconfdir}/monotone/passphrase.lua
%attr(0640,root,monotone) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) %{_sysconfdir}/monotone/read-permissions
%attr(0640,root,monotone) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) %{_sysconfdir}/monotone/write-permissions
%dir %attr(0770,monotone,monotone) %{_localstatedir}/lib/monotone
%attr(0660,monotone,monotone) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) %{_localstatedir}/lib/monotone/server.mtn


%pre server
# Add "monotone" user per http://fedoraproject.org/wiki/Packaging/UsersAndGroups
getent group monotone > /dev/null || groupadd -r monotone
getent passwd monotone > /dev/null ||
useradd -r -g monotone -r -d %{_localstatedir}/lib/monotone -s /sbin/nologin \
        -c "Monotone Netsync Server" monotone
exit 0


%post server
%systemd_post monotone.service


%preun server
%systemd_preun monotone.service


%postun server
%systemd_postun monotone.service


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1-50
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-43
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-40
- Perl 5.34 rebuild

* Mon Feb  8 2021 Thomas Moschny <thomas.moschny@gmx.de> - 1.1-39
- Move bash completions to /usr/share/bash-completion/completions (bz#1855768).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-37
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Jerry James <loganjerry@gmail.com> - 1.1-35
- Add lua-ql patch due to removal of LUA_QL from lua
- Add boost patch to fix single-letter macro name clash (bz 1851313)
- Add string-overflow patch to fix a potential buffer overflow
- Add catch patch to silence a large number of compiler warnings

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-35
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 Thomas Moschny <thomas.moschny@gmx.de> - 1.1-33
- Patch extra/mtn-hooks/monotone-ciabot.py to use Python3 (bz#1738073).

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-31
- Perl 5.30 rebuild

* Sat Feb  9 2019 Thomas Moschny <thomas.moschny@gmx.de> - 1.1-30
- Fix F30 FTBFS.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-27
- Perl 5.28 rebuild

* Tue May 22 2018 Thomas Moschny <thomas.moschny@gmx.de> - 1.1-26
- Add patch for PCRE >= 8.42 (rhbz#1555231, thanks P. Pisar).

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-22
- Perl 5.26 rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.1-19
- Rebuilt for Boost 1.63

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.1-18
- Rebuilt for Boost 1.63

* Sat Jan 14 2017 Ville Skyttä <ville.skytta@iki.fi> - 1.1-17
- Move tmpfiles.d config to %%{_tmpfilesdir}

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-15
- Perl 5.24 rebuild

* Sun Feb 14 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.1-14
- Switch monotone-server to systemd (#789901).
- Mark COPYING as %%license.
- Do not own /etc/bash_completion.d.
- Update README.monotone-server.

* Mon Feb  8 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.1-13
- Rebuild for Botan 1.10.12.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.1-11
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.1-10
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.1-8
- rebuild for Boost 1.58

* Mon Jun 22 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.1-7
- Add patch to fix FTBFS with Lua 5.3 (rhbz#1185790).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-5
- Perl 5.22 rebuild

* Thu Jan 29 2015 Petr Machata <pmachata@redhat.com> - 1.1-4
- Rebuild for boost 1.57.0
- Include <iostream> in tests/merge_3way.cc
  (monotone-1.1-iostream.patch)

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.1-1
- Update to 1.1.
- Remove patches and fixes not needed anymore.
- Modernize spec file.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.0-16
- Rebuild for boost 1.55.0

* Tue Oct  8 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.0-15
- Add patches for building with Botan 1.10, Lua 5.2,
  and Texinfo >= 5.0.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.0-13
- Rebuild for boost 1.54.0

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.0-12
- Perl 5.18 rebuild

* Sat Mar  9 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.0-11
- Fix building against Boost 1.53 (FTBFS bug rhbz#914191).
- Fix failing bash completion test.
- Add patch to temporarily disable a failing check in one test (rhbz#919827).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 1.0-8
- Perl 5.16 rebuild

* Thu Feb 16 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.0-7
- Add patch to fix building with newer pcre.

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 1.0-6
- Rebuild against PCRE 8.30

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 26 2011 Dan Horák <dan[at]danny.cz> - 1.0-4
- fix FTBFS due a symbol conflict with boost

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.0-3
- Perl mass rebuild

* Thu Jun 09 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.0-2
- Perl 5.14 mass rebuild

* Sat May 14 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.0-1
- Update to 1.0.
  - Upstream ships bzip2 archives now.
  - monotone.el is no longer shipped.
  - Bash completion is installed by 'make install'.
  - Add BR on bash-completion, needed for the testsuite.
- Fix postun snippet for -server package.
- On Fedora 15 and later, use the tmpfiles.d service to create the
  /var/run/monotone directory.
- Add a patch to prevent a name clash with struct file_handle defined
  by fcntl.h in glibc 2.14.
- Add a patch fixing broken helptexts and manpage.
- Explicitly disable network access by the testsuite.
- Fix some rpmlint warnings.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 31 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.99.1-1
- Update to 0.99.1.
- Remove patch already applied upstream.

* Fri Oct 29 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.99-1
- Update to 0.99.
- Remove patch already applied upstream.
- Add patch for monotone bug #100.
- Include the monotone manpage in the package.
- Specfile cleanups.

* Wed Oct 27 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.48.1-1
- Update to 0.48.1.
- Add patch from upstream to support newer sqlite.

* Mon Jun 14 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.48-1
- Update to 0.48.

* Sat May  8 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.47-3
- Add patch from upstream for a bug that prevents successful execution
  of push / pull / sync over pipes.

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.47-2
- Mass rebuild with perl-5.12.0

* Sun Apr 11 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.47-1
- Update to 0.47.
- Remove patch applied upstream.

* Sat Jan 23 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.46-1
- Update to 0.46.
- Remove patch applied upstream.
- Add patch from trunk for failing test.
- Fix installation of documentation: include figures in the package.
- Let tests in the testsuite run in parallel.

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.45-2
- rebuild against perl 5.10.1

* Sat Sep 12 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.45-1
- Update to 0.45.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 13 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.44-1
- Update to 0.44.

* Sat Apr 25 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.43-2
- Rebuilt for new botan version.

* Fri Mar 27 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.43-1
- Update to 0.43.
- Add BRs for libraries monotone doesn't bundle anylonger.
- Drop patches applied upstream.

* Fri Feb 27 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.42-5
- Add one more netsync related patch from trunk.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb  9 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.42-3
- Disable %%{_smp_mflags} in the testsuite, causes strange errors.
- Fix two issues with gcc44.
- Add patch from upstream fixing netsync printing an error message of
  the form "peer [...] IO failed in confirmed state (success)".

* Fri Jan  2 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.42-2
- Pack Monotone.pm (in a subpackage). (#450267)

* Fri Jan  2 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.42-1
- Updated for 0.42 release.

* Fri Sep 12 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.41-1
- Updated for 0.41 release.
- Added mtnopt helper.

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.40-2
- fix license tag

* Mon Apr 14 2008 Roland McGrath <roland@redhat.com> - 0.40-1
- Updated for 0.40 release.
- Tweaked trivia for packaging guidelines nits.

* Mon Feb 25 2008 Roland McGrath <roland@redhat.com> - 0.39-1
- Updated for 0.39 release.

* Sat Dec 22 2007 Roland McGrath <roland@redhat.com> - 0.38-2
- Fix monotone-server user creation. (#426607)
- Moved monotone-server database to /var/lib. (#426608)
- Use monotone@ in server key name. (#426609)

* Fri Dec 21 2007 Roland McGrath <roland@redhat.com> - 0.38-1
- Updated for 0.38 release.

* Sat Oct 27 2007 Roland McGrath <roland@redhat.com> - 0.37-3
- Updated for 0.37 release.
- Prevent destroying old passphrase file with 'service monotone genkey'.
- Put LSB standard comments in monotone.init for monotone-server subpackage.

* Tue Aug 28 2007 Roland McGrath <roland@redhat.com> - 0.36-2
- Clean up %%pre script per packaging guidelines.
- Disable ppc and ppc64 builds temporarily since make check fails. (#259161)

* Fri Aug  3 2007 Roland McGrath <roland@redhat.com> - 0.36-1
- Updated for 0.36 release.

* Fri Jul 06 2007 Florian La Roche <laroche@redhat.com> - 0.35-4
- add more requires

* Wed May 16 2007 Roland McGrath <roland@redhat.com> - 0.35-3
- Fix locale dependency in monotone-server init script. (#213893)

* Wed May  9 2007 Roland McGrath <roland@redhat.com> - 0.35-2
- Updated for 0.35 release.
- Avoid unnecessary "db migrate" in monotone-server init script. (#213893)

* Wed Apr  4 2007 Roland McGrath <roland@redhat.com> - 0.34-1
- Updated for 0.34 release.

* Thu Mar  1 2007 Roland McGrath <roland@redhat.com> - 0.33-1
- Updated for 0.33 release.
- Install monotone.bash_completion file.

* Wed Feb 28 2007 Roland McGrath <roland@redhat.com> - 0.32-1
- Updated for 0.32 release.

* Thu Dec 21 2006 Kevin Fenzi <kevin@tummy.com> - 0.31-2
- Bump and rebuild to fix upgrade path

* Sat Nov 11 2006 Roland McGrath <roland@redhat.com> - 0.31-1
- Updated for 0.31 release.

* Tue Oct 10 2006 Roland McGrath <roland@redhat.com> - 0.30-1
- Updated for 0.30 release.
- Fix service script to work around buggy init.d/functions. (#198761)

* Thu Aug  3 2006 Roland McGrath <roland@redhat.com> - 0.28-2
- Updated for 0.28 release. (#198652)
- Move server PID file into /var/run/monotone subdirectory. (#198761)

* Tue Jul 11 2006 Roland McGrath <roland@redhat.com> - 0.27-1
- Updated for 0.27 release.

* Mon May  8 2006 Roland McGrath <roland@redhat.com> - 0.26-2
- Fix service script genkey subcommand.

* Mon Apr 10 2006 Roland McGrath <roland@redhat.com> - 0.26-1
- Updated for 0.26 release.
  - Major changes; see UPGRADE doc file for details.

* Fri Jan  6 2006 Roland McGrath <roland@redhat.com> - 0.25-2
- Restore testsuite fix for nonroot owner of / in build chroot.

* Thu Jan  5 2006 Roland McGrath <roland@redhat.com> - 0.25-1
- Updated for 0.25 release.

* Sun Dec 11 2005 Roland McGrath <roland@redhat.com> - 0.24-1
- Updated for 0.24 release.

* Mon Oct  3 2005 Roland McGrath <roland@redhat.com> - 0.23-1
- Updated for 0.23 release.

* Mon Aug 22 2005 Roland McGrath <roland@redhat.com> - 0.22-4
- Updated for 0.22 release.
- Added monotone-server package.

* Sun Aug  7 2005 Roland McGrath <roland@redhat.com> - 0.21-3
- Work around non-root build user owning / in mock chroot builds.

* Wed Jul 27 2005 Roland McGrath <roland@redhat.com> - 0.21-2
- Include monotone-nav.el too.
- Add BuildRequires on cvs so the test suite can run.

* Mon Jul 18 2005 Roland McGrath <roland@redhat.com> - 0.21-1
- Updated for 0.21 release.
- Install Emacs support.

* Thu Jul  7 2005 Roland McGrath <roland@redhat.com> - 0.20-0.1
- Updated for 0.20 release.
- Added %%check section.
- Cannot use FC4 native sqlite3, need newer bundled one.

* Mon Apr 18 2005 Jeffrey C. Ollie <jcollie@lt16586.campus.dmacc.edu> - 0.18-0.4
- Modified summary so that it doesn't contain the name

* Thu Apr 14 2005 Jeffrey C. Ollie <jcollie@lt16586.campus.dmacc.edu> - 0.18-0.3
- Modified install-info commands to prevent errors in case of --excludedocs

* Wed Apr 13 2005 Jeffrey C. Ollie <jcollie@lt16586.campus.dmacc.edu> - 0.18-0.2
- Added post and postun scripts to take care of .info file
- Added parallel make flags

* Wed Apr 13 2005 Jeffrey C. Ollie <jcollie@lt16586.campus.dmacc.edu> - 0.18-0.1
- First version.
