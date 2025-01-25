%define _hardened_build 1
%define privoxyconf %{_sysconfdir}/%{name}
%define privoxy_uid 73
%define privoxy_gid 73
%define beta_or_stable stable
#define beta_or_stable beta

Name: privoxy
Version: 4.0.0
Release: 1%{?dist}
Summary: Privacy enhancing proxy
License: GPL-2.0-or-later
Source0: http://downloads.sourceforge.net/ijbswa/%{name}-%{version}-%{beta_or_stable}-src.tar.gz
Source1: privoxy.service
Source2: privoxy.logrotate
URL: http://www.privoxy.org/
Requires(pre): shadow-utils
BuildRequires: make
BuildRequires: libtool autoconf pcre2-devel zlib-devel systemd

%description 
Privoxy is a web proxy with advanced filtering capabilities for
protecting privacy, filtering web page content, managing cookies,
controlling access, and removing ads, banners, pop-ups and other
obnoxious Internet junk. Privoxy has a very flexible configuration and
can be customized to suit individual needs and tastes. Privoxy has application
for both stand-alone systems and multi-user networks.

Privoxy is based on the Internet Junkbuster.

%prep
%setup -q -n %{name}-%{version}-%{beta_or_stable}

%build
rm -rf autom4te.cache
autoreconf
# lets test how it works with dynamic pcre:
#configure --disable-dynamic-pcre
%configure
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_sbindir} \
         %{buildroot}%{_mandir}/man8 \
         %{buildroot}%{_localstatedir}/log/%{name} \
         %{buildroot}%{privoxyconf}/templates \
         %{buildroot}%{_unitdir}

install -p -m 755 %{name} %{buildroot}%{_sbindir}/%{name}
install -p -m 644 {config,*.action,default.filter,trust} %{buildroot}%{privoxyconf}/
install -p -m 644 templates/* %{buildroot}%{privoxyconf}/templates
install -p -m 644 %{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -p -m 711 -d %{buildroot}%{_localstatedir}/log/%{name}

# Customize the configuration file
sed -i -e 's@^confdir.*@confdir %{privoxyconf}@g' %{buildroot}%{privoxyconf}/config
sed -i -e 's@^logdir.*@logdir %{_localstatedir}/log/%{name}@g' %{buildroot}%{privoxyconf}/config

touch %{buildroot}%{_sysconfdir}/privoxy/user.filter

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d
cp -p %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/%{name}


%pre
# Add user/group on install
if [ $1 -eq "1" ]; then
    %{_sbindir}/groupadd -g %{privoxy_gid} %{name} > /dev/null 2>&1 ||:
    %{_sbindir}/useradd -u %{privoxy_uid} -g %{privoxy_gid} -d %{privoxyconf} -r -s "/sbin/nologin" %{name} > /dev/null 2>&1 ||:
fi


%post
%systemd_post privoxy.service

if [[ ! -f %{_sysconfdir}/privoxy/user.filter ]]
then
    touch %{_sysconfdir}/privoxy/user.filter
fi

%preun
%systemd_preun privoxy.service

%postun
%systemd_postun_with_restart privoxy.service


%files
%defattr(-,%{name},%{name},-)
%dir %{_localstatedir}/log/%{name}

# Owned by root
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/privoxy/user.filter
%attr(0755,root,root)%{_sbindir}/%{name}
%config(noreplace) %{privoxyconf}
%attr(0644,root,root) %{_unitdir}/%{name}.service
%{_mandir}/man8/%{name}.*
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%doc README AUTHORS ChangeLog LICENSE 
%doc doc

%changelog
* Thu Jan 23 2025 Gwyn Ciesla <gwync@protonmail.com> - 4.0.0-1
- 4.0.0

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.34-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.34-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.0.34-9
- Patch for connection crash.

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.34-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Florian Weimer <fweimer@redhat.com> - 3.0.34-7
- Fix bug in C compatibility fixes

* Mon Dec 18 2023 Florian Weimer <fweimer@redhat.com> - 3.0.34-6
- Fix C compatibility issue in configure script

* Mon Aug 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0.34-5
- Additional pcre2 patches from upstream.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0.34-3
- Upstream patch to move to pcre2.

* Sat Mar 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0.34-2
- migrated to SPDX license

* Mon Feb 06 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0.34-1
- 3.0.34

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.0.33-1
- 3.0.33

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.32-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Mar 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.0.32-1
- 3.0.32

* Mon Feb 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.0.31-1
- 3.0.31

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.0.29-1
- 3.0.29

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 19 2019 josef radinger <cheese@nosuchhost.net> - 3.0.28-1
- bump version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Petr Pisar <ppisar@redhat.com> - 3.0.26-8
- Rebuild against patched libpcreposix library (bug #1667614)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Jon Ciesla <limburgher@gmail.com> - 3.0.26-3
- systemd cleanup

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 29 2016 Jon Ciesla <limburgher@gmail.com> - 3.0.26-1
- 3.0.26 stable, BZ 1371151

* Mon Jun 27 2016 Jon Ciesla <limburgher@gmail.com> - 3.0.25-1.beta
- Unit file fix, BZ 1350097

* Tue Jun 07 2016 Jon Ciesla <limburgher@gmail.com> - 3.0.25-0.beta
- 3.0.25 beta, BZ 1341424.

* Mon Apr 11 2016 Jon Ciesla <limburgher@gmail.com> - 3.0.24-1
- 3.0.24, CVE-2016-1982 and CVE-2016-1983 fixes upstreamed.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Jon Ciesla <limburgher@gmail.com> - 3.0.23-3
- Patch for CVE-2016-1982-3.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Jon Ciesla <limburgher@gmail.com> - 3.0.23-1
- Latest upstream, BZ 1185925.

* Fri Nov 21 2014 Jon Ciesla <limburgher@gmail.com> - 3.0.22-1
- Latest upstream, BZ 166398.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 15 2013 Jon Ciesla <limburgher@gmail.com> - 3.0.21-6
- Fix logrotate file issue, BZ 997382.

* Mon Aug 05 2013 Jon Ciesla <limburgher@gmail.com> - 3.0.21-5
- Fix dates, add systemd BR to fix FTBFS, BZ 992823.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 23 2013 Jon Ciesla <limburgher@gmail.com> - 3.0.21-3
- Rotate logs, BZ 966332.

* Wed Mar 27 2013 Jon Ciesla <limburgher@gmail.com> - 3.0.21-2
- Create user.filter if it doesn't exist, BZ 926019.

* Tue Mar 12 2013 Jon Ciesla <limburgher@gmail.com> - 3.0.21-1
- 3.0.21, fix for CVE-2013-2503.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 23 2013 Jon Ciesla <limburgher@gmail.com> - 3.0.19-4
- Add user.filter, BZ 896753.

* Tue Oct 02 2012 Jon Ciesla <limburgher@gmail.com> - 3.0.19-3
- Add hardened build.

* Mon Oct 01 2012 Jon Ciesla <limburgher@gmail.com> - 3.0.19-2
- Change ownership of binary and config to root.

* Mon Oct 01 2012 Jon Ciesla <limburgher@gmail.com> - 3.0.19-1
- Latest upstream.
- Allow execution by all users, BZ 849932.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Jon Ciesla <limburgher@gmail.com> - 3.0.16-7
- Migrate to systemd, BZ 784090.

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 3.0.16-6
- Rebuild against PCRE 8.30
- Rebase chkconfig patch

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Apr 29 2010 Karsten Hopp <karsten@redhat.com> 3.0.16-3
- add zlib-devel to build requirements (#509557)

* Thu Mar 25 2010 Karsten Hopp <karsten@redhat.com> 3.0.16-2
- add chkconfig header to init script (#576641)
- fix patch to config files (#576642)

* Tue Mar 23 2010 Karsten Hopp <karsten@redhat.com> 3.0.16-1
- update to 3.0.16

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.13-beta.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Karsten Hopp <karsten@redhat.com> 3.0.13-beta.1
- update to 3.0.13-beta
- drop obsolete patches

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 24 2008 Karsten Hopp <karsten@redhat.com> 3.0.10-2
- fix summary

* Mon Aug 25 2008 Karsten Hopp <karsten@redhat.com> 3.0.10-1
- privoxy 3.0.10

* Wed Mar 05 2008 Karsten Hopp <karsten@redhat.com> 3.0.8-2
- fix source URL

* Mon Feb 25 2008 Karsten Hopp <karsten@redhat.com> 3.0.8-1
- privoxy-3.0.8

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.0.6-9
- Autorebuild for GCC 4.3

* Mon Aug 27 2007 Karsten Hopp <karsten@redhat.com> 3.0.6-8
- fix license
- rebuild

* Mon Mar 05 2007 Karsten Hopp <karsten@redhat.com> 3.0.6-7
- rpmlint fixes

* Mon Mar 05 2007 Karsten Hopp <karsten@redhat.com> 3.0.6-6
- add upstream patch for dynamic pcre (#226316)
- use kill -s HUP instead of 'kill -HUP' (#193159)

* Mon Feb 26 2007 Karsten Hopp <karsten@redhat.com> 3.0.6-5
- add disttag
- don't convert manpage to UTF-8
- use dynamic pcre
- drop license text from spec file, it's already covered in %%doc

* Thu Feb 22 2007 Karsten Hopp <karsten@redhat.com> 3.0.6-4
- remove changelog from init script
- added many spec file fixes from Sarantis Paskalis <paskalis@di.uoa.gr>:
- remove unnecessary perl invocation
- fix Requires(pre), (post), (preun) and (postun) for scriptlets
- fix rpmlint 'conffile-marked-as-executable'
- fix other stuff, so that it can actually be installed and erased
- do not remove user/group on erase because due to logs remaining
- major cleanup of the spec file 

* Tue Nov 28 2006 Karsten Hopp <karsten@redhat.com> 3.0.6-2
- fix download URL
- cleanups

* Tue Nov 21 2006 Karsten Hopp <karsten@redhat.com> 3.0.6-1
- privoxy-3.0.6

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.0.3-9.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.0.3-9.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.0.3-9.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Sep 08 2005 Karsten Hopp <karsten@redhat.de> 3.0.3-9
- fix invalid javascript created by quote unaware match in default.filter
  Anduin Withers (#126366)

* Tue May 10 2005 Karsten Hopp <karsten@redhat.de> 3.0.3-8
- enable debuginfo

* Wed Mar 02 2005 Karsten Hopp <karsten@redhat.de> 3.0.3-7
- build with gcc-4

* Thu Nov 25 2004 Miloslav Trmac <mitr@redhat.com> - 3.0.3-6
- Convert man page to UTF-8

* Thu Sep  9 2004 Bill Nottingham <notting@redhat.com> 3.0.3-5
- don't run by default (again :) )
* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 23 2004 Karsten Hopp <karsten@redhat.de> 3.0.3-3 
- rebuild with sane release number

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sun Feb 01 2004 Karsten Hopp <karsten@redhat.de> 3.0.3-0.6x
- build for upstream

* Sat Jan 31 2004 Karsten Hopp <karsten@redhat.de> 3.0.3-0.9
- build for upstream

* Thu Jan 22 2004 Karsten Hopp <karsten@redhat.de> 3.0.3-0.1 
- privoxy 3.0.3 beta

* Mon Jul 14 2003 Karsten Hopp <karsten@redhat.de> 3.0.2-7
- new upstream default.action

* Wed Jul 09 2003 Karsten Hopp <karsten@redhat.de> 3.0.2-6
- new upstream default.action
- added workaround for #74068

* Thu Jun 26 2003 Karsten Hopp <karsten@redhat.de> 3.0.2-5
- add patch from Hal Burgiss to disable filtering of downloaded source code

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com> 3.0.2-4.1
- rebuilt

* Thu May 08 2003 Karsten Hopp <karsten@redhat.de> 3.0.2-3.1
- fix https port

* Thu May 08 2003 Karsten Hopp <karsten@redhat.de> 3.0.2-3.0
- rebuild

* Thu May 08 2003 Karsten Hopp <karsten@redhat.de> 3.0.2-2.2
- fix typo in https port

* Wed May 07 2003 Karsten Hopp <karsten@redhat.de> 3.0.2-2.1
- fix memleak (patch from privoxy CVS)

* Wed Mar 26 2003 Karsten Hopp <karsten@redhat.de> 3.0.2-1
- update to 3.0.2

* Wed Feb 12 2003 Karsten Hopp <karsten@redhat.de> 3.0.0-8
- fix sig_child handling (#84103)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Sat Dec 21 2002 Karsten Hopp <karsten@redhat.de>
- /sbin/nologin as shell (#80174)

* Tue Dec 17 2002 Bill Nottingham <notting@redhat.com> 3.0.0-5
- don't run by default

* Wed Dec 04 2002 Karsten Hopp <karsten@redhat.de>
- better service description (#77716)

* Tue Nov 19 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches

* Wed Aug 28 2002 Karsten Hopp <karsten@redhat.de>
- 3.0.0 final, only docu updates

* Mon Aug 26 2002 Karsten Hopp <karsten@redhat.de>
 - 3.0.0rc1  (good timing, they don't even know our schedule)
 - docu/templates and filter updates.

* Sun Aug 25 2002 Hal Burgiss <hal@foobox.net>
- Bump version for 3.0.0 :)

* Fri Aug 23 2002 Karsten Hopp <karsten@redhat.de>
- docu and filter updates

* Sat Aug 10 2002 Karsten Hopp <karsten@redhat.de>
- Update to next release candidate 2.9.20

* Thu Aug 08 2002 Karsten Hopp <karsten@redhat.de>
- Update to next release candidate

* Tue Aug 06 2002 Karsten Hopp <karsten@redhat.de>
- 2.9.18
- autoconf check for pcre.h in subdir

* Tue Aug 06 2002 Hal Burgiss <hal@foobox.net>
- Reset version for 2.9.20.

* Tue Jul 30 2002 Hal Burgiss <hal@foobox.net>
- Reset version for 2.9.18.

* Sat Jul 27 2002 Karsten Hopp <karsten@redhat.de>
- this is a release-candidate for privoxy-3.0

* Sat Jul 27 2002 Hal Burgiss <hal@foobox.net>
- Reset version and release for 2.9.16.

* Fri Jul 12 2002 Karsten Hopp <karsten@redhat.de>
- don't use ghost files for rcX.d/*, using chkconfig is the 
  correct way to do this job (#68619)

* Fri Jul 05 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ privoxy-2.9.15-8
- Changing delete order for groups and users (users should be first)

* Wed Jul 03 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ privoxy-2.9.15-7
- Changing sed expression that removed CR from the end of the lines. This
  new one removes any control caracter, and should work with older versions
  of sed

* Tue Jul 02 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ privoxy-2.9.15-6
- Fixing defattr values. File and directory modes where swapped

* Tue Jul 02 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ privoxy-2.9.15-5
- Bumping Release number (which should be changed every time the specfile
  is)

* Tue Jul 02 2002 Hal Burgiss <hal@foobox.net>
+ privoxy-2.9.15-4
- Fix typo in templates creation.

* Wed Jun 26 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ privoxy-2.9.15-4
- Fixing issues created by specfile sync between branches
  - Correcting the release number (WARNING)
  - Reintroducing text file conversion (dos -> unix)
  - Reconverting hardcoded directories to macros
  - Refixing ownership of privoxy files (now using multiple defattr
    definitions)

* Thu Jun 20 2002 Karsten Hopp <karsten@redhat.de>
- fix several .spec file issues to shut up rpmlint
  - non-standard-dir-perm /var/log/privoxy 0744
  - invalid-vendor Privoxy.Org (This is ok for binaries compiled by privoxy
    members, but not for packages from Red Hat)
  - non-standard-group Networking/Utilities
  - logrotate and init scripts should be noreplace

* Mon May 27 2002 Hal Burgiss <hal@foobox.net>
+ privoxy-2.9.15-1
- Index.html is now privoxy-index.html for doc usage.

* Sat May 25 2002 Hal Burgiss <hal@foobox.net>
+ privoxy-2.9.15-1
- Add html man page so index.html does not 404.

* Fri May 24 2002 Hal Burgiss <hal@foobox.net>
+ privoxy-2.9.15-1
- Add another template and alphabetize these for easier tracking.
- Add doc/images directory.

* Wed May 15 2002 Hal Burgiss <hal@foobox.net>
+ privoxy-2.9.15-1
- Add templates/edit-actions-list-button

* Fri May 03 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ privoxy-2.9.15-1
- Version bump
- Adding noreplace for %%{privoxyconf}/config
- Included a method to verify if the versions declared on the specfile and
  configure.in match. Interrupt the build if they don't.

* Fri Apr 26 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ privoxy-2.9.14-3
- Changing Vendor to Privoxy.Org

* Tue Apr 23 2002 Hal Burgiss <hal@foobox.net>
+ privoxy-2.9.14-2
- Adjust for new *actions files.

* Mon Apr 22 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ privoxy-2.9.14-2
- Removed the redhat hack that prevented the user and group from
  being dealocated. That was a misundestanding of my part regarding
  redhat policy.

* Mon Apr 22 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ privoxy-2.9.14-2
- Using macros to define uid and gid values
- Bumping release

* Mon Apr 22 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ privoxy-2.9.14-1
- Changes to fixate the uid and gid values as (both) 73. This is a 
  value we hope to standarize for all distributions. RedHat already
  uses it, and Conectiva should start as soon as I find where the heck
  I left my cluebat :-)
- Only remove the user and group on uninstall if this is not redhat, once
  redhat likes to have the values allocated even if the package is not 
  installed

* Tue Apr 16 2002 Hal Burgiss <hal@foobox.net>
+ privoxy-2.9.13-6
- Add --disable-dynamic-pcre to configure.

* Wed Apr 10 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ privoxy-2.9.13-5
- Relisting template files on the %%files section

* Tue Apr 09 2002 Hal Burgiss <hal@foobox.net>
+ privoxy-2.9.13-4
- Removed 'make dok'. Docs are all maintained in CVS (and tarball) now.

* Mon Apr 08 2002 Hal Burgiss <hal@foobox.net>
+ privoxy-2.9.13-4
- Add templates/cgi-style.css, faq.txt, p_web.css, LICENSE
- Remove templates/blocked-compact.
- Add more docbook stuff to Builderquires.

* Thu Mar 28 2002 Sarantis Paskalis <sarantis@cnl.di.uoa.gr>
+ privoxy-2.9.13-3
- Include correct documentation file.

* Tue Mar 26 2002 Hal Burgiss <hal@foobox.net>
+ privoxy-2.9.13-3
- Fix typo in Description.

* Tue Mar 26 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ privoxy-2.9.13-3
- Added commentary asking to update the release value on the configure
  script

* Tue Mar 26 2002 Hal Burgiss <hal@foobox.net>
+ privoxy-2.9.13-3
- Added the missing edit-actions-for-url-filter to templates.

* Mon Mar 25 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ privoxy-2.9.13-2
- Fixing Release number

* Sun Mar 24 2002 Hal Burgiss <hal@foobox.net>
+ privoxy-2.9.13-2
- Added faq to docs.

* Sun Mar 24 2002 Rodrigo Barbosa <rodrigob@suespammers.org>
+ privoxy-2.9.13-2
- Fixed the init files entries. Now we use %%ghost
- improved username (and groupname) handling on the %%pre section. By improved
  I mean: we do it by brute force now. Much easier to maintain. Yeah, you
  got it right. No more Mr. Nice Guy.
- Removed the userdel call on %%post. No need, once it's complety handled on
  the %%pre section

* Sun Mar 24 2002 Hal Burgiss <hal@foobox.net>
+ junkbusterng-2.9.13-1
  Added autoheader. Added autoconf to buildrequires.

* Sun Mar 24 2002 Hal Burgiss <hal@foobox.net>
+ junkbusterng-2.9.13-1
- Fixed build problems re: name conflicts with man page and logrotate.
- Commented out rc?d/* configs for time being, which are causing a build 
- failure. /etc/junkbuster is now /etc/privoxy. Stefan did other name 
- changes. Fixed typo ';' should be ':' causing 'rpm -e' to fail.

* Fri Mar 22 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ junkbusterng-2.9.13-1
- References to the expression ijb where changed where possible
- New package name: junkbusterng (all in lower case, acording to
  the LSB recomendation)
- Version changed to: 2.9.13
- Release: 1
- Added: junkbuster to obsoletes and conflicts (Not sure this is
  right. If it obsoletes, why conflict ? Have to check it later)
- Summary changed: Stefan, please check and aprove it
- Changes description to use the new name
- Sed string was NOT changed. Have to wait to the manpage to
  change first
- Keeping the user junkbuster for now. It will require some aditional
  changes on the script (scheduled for the next specfile release)
- Added post entry to move the old logfile to the new log directory
- Removing "chkconfig --add" entry (not good to have it automaticaly
  added to the startup list).
- Added preun section to stop the service with the old name, as well
  as remove it from the startup list
- Removed the chkconfig --del entry from the conditional block on
  the preun scriptlet (now handled on the %%files section)

* Thu Mar 21 2002 Hal Burgiss <hal@foobox.net>
- added ijb_docs.css to docs.

* Mon Mar 11 2002 Hal Burgiss <hal@foobox.net>
+ junkbuster-2.9.11-8 
- Take out --enable-no-gifs, breaks some browsers.

* Sun Mar 10 2002 Hal Burgiss <hal@foobox.net>
+ junkbuster-2.9.11-8 
- Add --enable-no-gifs to configure.

* Fri Mar 08 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ junkbuster-2.9.11-7
- Added BuildRequires to libtool.

* Wed Mar 06 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ junkbuster-2.9.11-6
- Changed the routined that handle the junkbust and junkbuster users on
  %%pre and %%post to work in a smoother manner
- %%files now uses hardcoded usernames, to avoid problems with package
  name changes in the future

* Tue Mar 05 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ junkbuster-2.9.11-5
- Added "make redhat-dok" to the build process
- Added docbook-utils to BuildRequires

* Tue Mar 05 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ junkbuster-2.9.11-4
- Changing man section in the manpage from 1 to 8
- We now require packages, not files, to avoid issues with apt

* Mon Mar 04 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ junkbuster-2.9.11-3
- Fixing permissions of the init script

* Mon Mar 04 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ junkbuster-2.9.11-2
- General specfile fixup, using the best recomended practices, including:
    - Adding -q to %%setup
    - Using macros whereever possible
    - Not using wildchars on %%files section
    - Doubling the percentage char on changelog and comments, to
      avoid rpm expanding them

* Sun Mar 03 2002 Hal Burgiss <hal@foobox.net>
- /bin/false for shell causes init script to fail. Reverting.

* Wed Jan 09 2002 Hal Burgiss <hal@foobox.net>
- Removed UID 73. Included user-manual and developer-manual in docs.
  Include other actions files. Default shell is now /bin/false.
  Userdel user=junkbust. ChangeLog was not zipped. Removed 
  RPM_OPT_FLAGS kludge.

* Fri Dec 28 2001 Thomas Steudten <thomas@steudten.ch>
- add paranoia check for 'rm -rf %%{buildroot}'
- add gzip to 'BuildRequires'

* Sat Dec  1 2001 Hal Burgiss <hal@foobox.net>
- actionsfile is now ijb.action.

* Tue Nov  6 2001 Thomas Steudten <thomas@steudten.ch>
- Compress manpage
- Add more documents for installation
- Add version string to name and source

* Wed Oct 24 2001 Hal Burigss <hal@foobox.net>
- Back to user 'junkbuster' and fix configure macro.

* Wed Oct 10 2001 Hal Burigss <hal@foobox.net>
- More changes for user 'junkbust'. Init script had 'junkbuster'.

* Sun Sep 23 2001 Hal Burgiss <hal@foobox.net>
- Change of $RPM_OPT_FLAGS handling. Added new HTML doc files.
- Changed owner of /etc/junkbuster to shut up PAM/xauth log noise.

* Thu Sep 13 2001 Hal Burgiss <hal@foobox.net>
- Added $RPM_OPT_FLAGS support, renaming of old logfile, and 
- made sure no default shell exists for user junkbust.

* Sun Jun  3 2001 Stefan Waldherr <stefan@waldherr.org>
- rework of RPM

* Mon Sep 25 2000 Stefan Waldherr <stefan@waldherr.org>
- CLF Logging patch by davep@cyw.uklinux.net
- Hal DeVore <haldevore@earthling.net> fix akamaitech in blocklist

* Sun Sep 17 2000 Stefan Waldherr <stefan@waldherr.org>
- Steve Kemp skx@tardis.ed.ac.uk's javascript popup patch.
- Markus Breitenbach breitenb@rbg.informatik.tu-darmstadt.de supplied
  numerous fixes and enhancements for Steve's patch.
- adamlock@netscape.com (Adam Lock) in the windows version:
  - Taskbar activity spinner always spins even when logging is
  turned off (which is the default) - people who don't
  like the spinner can turn it off from a menu option.
  - Taskbar popup menu has a options submenu - people can now
  open the settings files for cookies, blockers etc.
  without opening the JB window.
  - Logging functionality works again
  - Buffer overflow is fixed - new code uses a bigger buffer
  and snprintf so it shouldn't overflow anymore.
- Fixed userid swa, group learning problem while installing.
  root must build RPM.
- Added patch by Benjamin Low <ben@snrc.uow.edu.au> that prevents JB to
  core dump when there is no log file.
- Tweaked SuSE startup with the help of mohataj@gmx.net and Doc.B@gmx.de.
- Fixed man page to include imagefile and popupfile.
- Sanity check for the statistics function added.
- "Patrick D'Cruze" <pdcruze@orac.iinet.net.au>: It seems Microsoft
 are transitioning Hotmail from FreeBSD/Apache to Windows 2000/IIS.
 With IIS/5, it appears to omit the trailing \r\n from http header
 only messages.  eg, when I visit http://www.hotmail.com, IIS/5
 responds with a HTTP 302 redirect header.  However, this header
 message is missing the trailing \r\n.  IIS/5 then closes the
 connection.  Junkbuster, unfortunately, discards the header becomes
 it thinks it is incomplete - and it is.  MS have transmitted an
 incomplete header!
- Added bug reports and patch submission forms in the docs.

* Mon Mar 20 2000 Stefan Waldherr <stefan@waldherr.org>
       Andrew <anw@tirana.freewire.co.uk> extended the JB:
       Display of statistics of the total number of requests and the number
       of requests filtered by junkbuster, also the percentage of requests
       filtered. Suppression of the listing of files on the proxy-args page.
       All stuff optional and configurable.

* Sun Sep 12 1999 Stefan Waldherr <stefan@waldherr.org>
       Jan Willamowius (jan@janhh.shnet.org) fixed a bug in the 
       code which prevented the JB from handling URLs of the form
       user:password@www.foo.com. Fixed.

* Mon Aug  2 1999 Stefan Waldherr <stefan@waldherr.org>
    Blank images are no longer cached, thanks to a hint from Markus 
        Breitenbach <breitenb@rbg.informatik.tu-darmstadt.de>. The user 
        agent is NO longer set by the Junkbuster. Sadly, many sites depend 
        on the correct browser version nowadays. Incorporated many 
    suggestions from Jan "Yenya" Kasprzak <kas@fi.muni.cz> for the
        spec file. Fixed logging problem and since runlevel 2 does not 
        use networking, I replaced /etc/rc.d/rc2.d/S84junkbuster with
        /etc/rc.d/rc2.d/K09junkbuster thanks to Shaw Walker 
        <walker@netgate.net>. You should now be able to build this RPM as 
        a non-root user (mathias@weidner.sem.lipsia.de).

* Sun Jan 31 1999 Stefan Waldherr <stefan@waldherr.org>
    %%{_localstatedir}/log/junkbuster set to nobody. Added /etc/junkbuster/imagelist
    to allow more sophisticated matching of blocked images. Logrotate
    logfile. Added files for auto-updating the blocklist et al.

* Wed Dec 16 1998 Stefan Waldherr <stefan@waldherr.org>
    Configure blank version via config file. No separate blank
    version anymore. Added Roland's <roland@spinnaker.rhein.de>
    patch to show a logo instead of a blank area. Added a suggestion
    from Alex <alex@cocoa.demon.co.uk>: %%{_localstatedir}/lock/subsys/junkbuster.
    More regexps in the blocklist. Prepared the forwardfile for
    squid. Extended image regexp with help from gabriel 
    <somlo@CS.ColoState.EDU>.

* Thu Nov 19 1998 Stefan Waldherr <stefan@waldherr.org>
    All RPMs now identify themselves in the show-proxy-args page.
    Released Windoze version. Run junkbuster as nobody instead of
    root. 

* Fri Oct 30 1998 Stefan Waldherr <stefan@waldherr.org>
    Newest version. First release (hence the little version number
    mixture -- 2.0.2-0 instead of 2.0-7). This version tightens 
    security over 2.0.1; some multi-user sites will need to change 
    the listen-address in the configuration file. The blank version of
        the Internet Junkbuster has a more sophisticated way of replacing
    images. All RPMs identify themselves in the show-proxy-args page.

* Thu Sep 24 1998 Stefan Waldherr <stefan@waldherr.org>
    Modified the blocking feature, so that only GIFs and JPEGs are
    blocked and replaced but not HTML pages. Thanks to 
    "Gerd Flender" <plgerd@informatik.uni-siegen.de> for this nice
    idea. Added numerous stuff to the blocklist. Keep patches in
        seperate files and no longer in diffs (easier to maintain).

* Tue Jun 16 1998 Stefan Waldherr <swa@cs.cmu.edu>
        Moved config files to /etc/junkbuster directory, moved man page,
    added BuildRoot directive (Thanks to Alexey Nogin <ayn2@cornell.edu>)
        Made new version junkbuster-raw (which is only a stripped version of 
        the junkuster rpm, i.e. without my blocklist, etc.)

* Tue Jun 16 1998 (2.0-1)
    Uhm, not that much. Just a new junkbuster version that
    fixes a couple of bugs ... and of course a bigger 
    blocklist with the unique Now-less-ads-than-ever(SM)
    feature.
    Oh, one thing: I changed the default user agent to Linux -- no 
    need anymore to support Apple.

* Tue Jun 16 1998 (2.0-0)
    Now-less-ads-than-ever (SM)
    compiled with gcc instead of cc
    compiled with -O3, thus it should be a little faster
    show-proxy-args now works
    /etc/junkbuster.init wasn't necessary

* Tue Jun 16 1998 (1.4)
    some more config files were put into /etc
    The junkbuster-blank rpm returns a 1x1 pixel image, that gets 
    displayed by Netscape instead of the blocked image.
    Read http://www.waldherr.org/junkbuster/ for
    further info.

* Tue Jun 16 1998 (1.3)
    The program has been moved to /usr/sbin (from /usr/local/bin)
    Init- and stopscripts (/etc/rc.d/rc*) have been added so
    that the junkbuster starts automatically during bootup.
    The /etc/blocklist file is much more sophisticated. Theoretically
    one should e.g. browse all major US and German newspapers without
    seeing one annoying ad.
    junkbuster.init was modified. It now starts junkbuster with an
    additional "-r @" flag.

