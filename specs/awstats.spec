Name:       awstats
Version:    7.9
Release:    7%{?dist}
Summary:    Advanced Web Statistics
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:    GPL-3.0-or-later
URL:        https://www.awstats.org/
Source0:    https://downloads.sourceforge.net/project/awstats/AWStats/%{version}/awstats-%{version}.tar.gz
Source1:    %{name}.cron
Patch0:     awstats-awredir.pl-sanitize-parameters.patch

# fix configuration for httpd 2.4 (#871366)
Patch1:     awstats-7.9-httpd-2.4.patch

BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  recode
Requires:   perl-Net-IP, perl-Net-DNS, perl-Geo-IP
Requires:   crontabs  
Requires(post): perl-interpreter

# For systemd.macros
BuildRequires:  systemd
Requires(postun): systemd

## SELinux policy is now included upstream
Obsoletes:  awstats-selinux < 6.8-1
Provides:   awstats-selinux = %{version}-%{release}


%description
Advanced Web Statistics is a powerful and full-featured tool that generates
advanced web server graphical statistics. This server log analyzer works
from the command line or as a CGI and shows all information your log contains,
in graphical web pages. It can analyze a lot of web/wap/proxy servers such as
Apache, IIS, Weblogic, Webstar, Squid, ... but also mail or FTP servers.

This program can measure visits, unique visitors, authenticated users, pages,
domains/countries, OS busiest times, robot visits, type of files, search
engines/keywords used, visit duration, HTTP errors and more...
Statistics can be updated from a browser or your scheduler.
The program also supports virtual servers, plugins and a lot of features.

With the default configuration, the statistics are available at:
http://localhost/awstats/awstats.pl


%prep
%setup -q
%patch -P0 -p 1
%patch -P1 -p 1

# Fix style sheets.
perl -pi -e 's,/icon,/awstatsicons,g' wwwroot/css/*
# Fix some bad file permissions here for convenience.
chmod -x tools/httpd_conf
find tools/xslt -type f | xargs chmod -x
# Remove \r in conf file (file written on MS Windows)
perl -pi -e 's/\r//g' docs/COPYING.TXT docs/LICENSE.TXT docs/pad_awstats.xml docs/awstats_changelog.txt docs/styles.css tools/httpd_conf tools/logresolvemerge.pl tools/awstats_exportlib.pl tools/awstats_buildstaticpages.pl tools/maillogconvert.pl tools/urlaliasbuilder.pl wwwroot/cgi-bin/awredir.pl
# Encoding
recode ISO-8859-1..UTF-8 docs/awstats_changelog.txt
# Stray version control file
rm -f tools/webmin/.gitignore

%install
rm -rf $RPM_BUILD_ROOT

### Create folders
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/{httpd/conf.d,%{name},cron.hourly}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}

### Install files
cp -pr tools $RPM_BUILD_ROOT%{_datadir}/%{name}
chmod 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/tools/*.pl
chmod 644 $RPM_BUILD_ROOT%{_datadir}/%{name}/tools/httpd_conf
cp -pr wwwroot $RPM_BUILD_ROOT%{_datadir}/%{name}
chmod 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/wwwroot/cgi-bin/*.pl
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/wwwroot/classes/src
### We want these outside CGI path.
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/wwwroot/cgi-bin/{lang,lib,plugins}
cp -pr wwwroot/cgi-bin/{lang,lib,plugins} $RPM_BUILD_ROOT%{_datadir}/%{name}

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/wwwroot/cgi-bin/awstats.model.conf

### Commit permanent changes to default configuration
install -p -m 644 wwwroot/cgi-bin/awstats.model.conf \
    $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/%{name}.model.conf
perl -pi -e '
                s|^LogFile=.*$|LogFile="%{_localstatedir}/log/httpd/access_log"|;
                s|^DirData=.*$|DirData="%{_localstatedir}/lib/awstats"|;
                s|^DirCgi=.*$|DirCgi="/awstats"|;
                s|^DirIcons=.*$|DirIcons="/awstatsicons"|;
                s|^SiteDomain=.*$|SiteDomain="localhost.localdomain"|;
                s|^HostAliases=.*$|HostAliases="localhost 127.0.0.1"|;
                s|^EnableLockForUpdate=.*$|EnableLockForUpdate=1|;
                s|^SaveDatabaseFilesWithPermissionsForEveryone=.*$|SaveDatabaseFilesWithPermissionsForEveryone=0|;
                s|^SkipHosts=.*$|SkipHosts="127.0.0.1"|;
                s|^Expires=.*$|Expires=3600|;
            ' $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/%{name}.model.conf
install -p -m 644 $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/%{name}.{model,localhost.localdomain}.conf 

# Fix AWStats path in scripts
perl -pi -e 's|/usr/local/awstats|%{_datadir}/awstats|g' \
             $RPM_BUILD_ROOT%{_datadir}/%{name}/tools/*.pl

# Apache configuration
install -p -m 644 tools/httpd_conf $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/%{name}.conf

# Cron job
install -m 0750 -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly/%{name}

# replace logos with Copyright and Trademark problem by unknown.png
# https://bugzilla.redhat.com/show_bug.cgi?id=1196549
cd $RPM_BUILD_ROOT%{_datadir}/%{name}/wwwroot/icon
for i in browser/adobe.png browser/seamonkey.png os/win*.png os/macos*.png cpu/intel.png cpu/ibm.png; do
  cp -v os/unknown.png $i
done
cd -


%post
if [ $1 -eq 1 ]; then
  if [ ! -f %{_sysconfdir}/%{name}/%{name}.`hostname`.conf ]; then
    %{__cat} %{_sysconfdir}/%{name}/%{name}.model.conf | \
      %{__perl} -p -e 's|^SiteDomain=.*$|SiteDomain="'`hostname`'"|;
                       s|^HostAliases=.*$|HostAliases="REGEX[^.*'${HOSTNAME//./\\\\.}'\$]"|;
                      ' > %{_sysconfdir}/%{name}/%{name}.`hostname`.conf || :
  fi
fi

%postun
%systemd_postun_with_restart httpd.service


%files
# Apache configuration file
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%config(noreplace) %attr(750,root,root) %{_sysconfdir}/cron.hourly/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/
%{_localstatedir}/lib/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/wwwroot
%{_datadir}/%{name}/tools
%{_datadir}/%{name}/wwwroot/cgi-bin
# Different defattr to fix lots of files which should not be +x.
%defattr(644,root,root,755)
%doc README.md docs/*
%{_datadir}/%{name}/lang
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/plugins
%{_datadir}/%{name}/wwwroot/classes
%{_datadir}/%{name}/wwwroot/css
%{_datadir}/%{name}/wwwroot/icon
%{_datadir}/%{name}/wwwroot/js


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 7.9-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Tim Jackson <rpm@timj.co.uk> - 7.9-1
- Version 7.9

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Tim Jackson <rpm@timj.co.uk> - 7.8-9
- Fix CVE-2022-46391 (rhbz #2150632)
- Clean up spec file, removing conditionals for now-obsolete releases

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 7.8-7
- Perl 5.36 rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 7.8-4
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Tim Jackson <rpm@timj.co.uk> - 7.8-2
- Fix CVE-2020-35176

* Fri Aug 07 2020 Tim Jackson <rpm@timj.co.uk> - 7.8-1
- Version 7.8

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 7.7-10
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 7.7-9
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 7.7-6
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 7.7-3
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Petr Lautrbach <plautrba@redhat.com> - 7.7-1
- Version 7.7

* Tue Jan 02 2018 Petr Lautrbach <plautrba@redhat.com> - 7.6-8
- Fix two path traversal issues in awstat.pl - CVE-2017-1000501 (#1529349)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Petr Pisar <ppisar@redhat.com> - 7.6-6
- perl dependency renamed to perl-interpreter manually
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 7.6-5
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 7.6-4
- Perl 5.26 rebuild

* Tue May 30 2017 Petr Lautrbach <plautrba@redhat.com> - 7.6-3
- Revert "Move cron file to awstats-cron"

* Tue May 23 2017 Petr Lautrbach <plautrba@redhat.com> - 7.6-2
- Move cron file to awstats-cron
- Update default path to be more compatible with Linux distro

* Wed Apr 12 2017 Petr Lautrbach <plautrba@redhat.com> - 7.6-1
- version 7.6

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 7.4-5
- Fix FTBFS when perl is not in the SRPM build root

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 7.4-4
- Perl 5.24 rebuild

* Thu Feb 25 2016 Petr Lautrbach <plautrba@redhat.com> 7.4-3
- replace logos with Copyright and Trademark problem by unknown.png (#1196549)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Petr Lautrbach <plautrba@redhat.com> 7.4-1
- version 7.4

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 7.3-3
- Perl 5.22 rebuild

* Fri Sep 05 2014 Jitka Plesnikova <jplesnik@redhat.com> - 7.3-2
- Perl 5.20 rebuild

* Wed Sep 03 2014 Petr Lautrbach <plautrba@redhat.com> 7.3-1
- version 7.3

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 7.2-2
- Perl 5.20 rebuild

* Mon Jun 09 2014 Petr Lautrbach <plautrba@redhat.com> 7.2-1
- version 7.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 10 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 7.1.1-5
- Add BR: systemd for systemd.macros (RHBZ #1017665).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 7.1.1-3
- Perl 5.18 rebuild

* Tue Apr 02 2013 Petr Lautrbach <plautrba@redhat.com> 7.1.1-2
- add a missing requirement on crontab and fix (#947040)
- add missing requirements (#908981)
- spec file and patches cleanup

* Mon Mar 18 2013 Petr Lautrbach <plautrba@redhat.com> 7.1.1-1
- version 7.1.1

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Petr Lautrbach <plautrba@redhat.com> 7.1-1
- version 7.1

* Fri Nov 16 2012 Petr Lautrbach <plautrba@redhat.com> 7.0-11
- fix configuration for httpd 2.4 (#871366)
- fix potential XSS attacks - CVE-2012-4547 (#871159)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 7.0-9
- Perl 5.16 rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan 02 2012 Petr Lautrbach <plautrba@redhat.com> 7.0-7
- fix for perl-5.14 (#768443,#768982,#771031)

* Fri Oct 07 2011 Petr Lautrbach <plautrba@redhat.com> 7.0-6
- fix CRLF Injection flaw (#740926)

* Mon Oct 03 2011 Petr Lautrbach <plautrba@redhat.com> 7.0-5
- fix multiple XSS and sql injection flaws (#740926)

* Wed Aug 10 2011 Petr Lautrbach <plautrba@redhat.com> 7.0-4
- don't use Switch module

* Tue Feb 15 2011 Petr Lautrbach <plautrba@redhat.com> 7.0-3
- update to upstream 7.0 version

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 13 2010 Aurelien Bompard <abompard@fedoraproject.org> -  7.0-1
- version 7.0

* Thu Nov 26 2009 Aurelien Bompard <abompard@fedoraproject.org> -  6.95-1
- version 6.95 (security fix)
- drop patch0

* Fri Aug 21 2009 Aurelien Bompard <abompard@fedoraproject.org> -  6.9-4
- don't backup the cgi when patching (#518168)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 31 2008 Aurelien Bompard <abompard@fedoraproject.org> 6.9-1
- version 6.9
- use Debian's version of the CVE-2008-3714 fix

* Sat Dec 06 2008 Aurelien Bompard <abompard@fedoraproject.org> 6.8-3
- Use Debian's patch for CVE-2008-3714 (rh#474396)

* Sat Aug 23 2008 Aurelien Bompard <abompard@fedoraproject.org> 6.8-2
- Add upstream patch for CVE-2008-3714

* Mon Jul 21 2008 Aurelien Bompard <abompard@fedoraproject.org> 6.8-1
- version 6.8

* Fri Mar 14 2008 Aurelien Bompard <abompard@fedoraproject.org> 6.7-3
- SELinux policy is included upstream
- Fix cron job (bug 435101)

* Sun Dec 02 2007 Aurelien Bompard <abompard@fedoraproject.org> 6.7-2
- awstats does not actually require httpd (bug 406901)

* Mon Aug 13 2007 Aurelien Bompard <abompard@fedoraproject.org> 6.7-1
- split SElinux bits in the -selinux package (bug 250637)
- use an SElinux module instead of semanage
- update to version 6.7

* Sun Jan 07 2007 Aurelien Bompard <abompard@fedoraproject.org> 6.6-1
- version 6.6 final

* Fri Nov 03 2006 Aurelien Bompard <abompard@fedoraproject.org> 6.6-0.4.beta
- fix typo in the cron job (bug 213803)

* Mon Oct 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 6.6-0.3.beta
- fix DOS encoding on logresolvemerge.pl

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 6.6-0.2.beta
- rebuild

* Sun May 07 2006 Aurelien Bompard <gauret[AT]free.fr> 6.6-0.1.beta
- version 6.6 (beta), fixes CVE-2005-2732 (bug 190921, 190922, and 190923)

* Sun Apr 09 2006 Aurelien Bompard <gauret[AT]free.fr> 6.5-3
- SELinux support: use semanage to label the cgi and the database files
- Only allow access from localhost by default (this app has a security history)

* Thu Feb 23 2006 Aurelien Bompard <gauret[AT]free.fr> 6.5-2
- rebuild for FC5

* Wed Jan 11 2006 Aurelien Bompard <gauret[AT]free.fr> 6.5-1
- version 6.5 final

* Mon Aug 22 2005 Aurelien Bompard <gauret[AT]free.fr> 6.5-1
- version 6.5 (beta), fixes CAN-2005-1527

* Mon Mar 21 2005 Aurelien Bompard <gauret[AT]free.fr> 6.4-1
- version 6.4 final
- change release tag (following Owen's scheme)
- convert tabs into spaces

* Tue Feb 15 2005 Aurelien Bompard <gauret[AT]free.fr> 6.4-0.1.pre
- update to 6.4pre to fix a vulnerability

* Thu Feb 10 2005 Aurelien Bompard <gauret[AT]free.fr> 6.3-1
- version 6.3 final

* Thu Jan 27 2005 Aurelien Bompard <gauret[AT]free.fr> 6.3-0.1.20050122
- update to 6.3pre to fix vulnerability

* Sun Nov 28 2004 Aurelien Bompard <gauret[AT]free.fr> 6.2-0.fdr.1
- version 6.2

* Thu May 20 2004 Aurelien Bompard <gauret[AT]free.fr> 6.1-0.fdr.6
- remove redundant substitution

* Thu May 20 2004 Aurelien Bompard <gauret[AT]free.fr> 6.1-0.fdr.5
- be closer to upstream default configuration
- use the included apache conf file
- merge changes from Michael Schwendt (bug 1608)

* Wed May 19 2004 Aurelien Bompard <gauret[AT]free.fr> 6.1-0.fdr.4
- fix cron job for relocated tools

* Wed May 19 2004 Aurelien Bompard <gauret[AT]free.fr> 6.1-0.fdr.3
- keep the tools in the tools subdirectory

* Wed May 19 2004 Aurelien Bompard <gauret[AT]free.fr> 6.1-0.fdr.2
- fix scripts in /usr/bin
- rename configure.pl to awstats_configure.pl

* Sun May 16 2004 Aurelien Bompard <gauret[AT]free.fr> 6.1-0.fdr.1
- version 6.1

* Wed Mar 03 2004 Aurelien Bompard <gauret[AT]free.fr> 6.0.0.fdr.2
- requires perl without version to fix build on rh9

* Thu Feb 19 2004 Aurelien Bompard <gauret[AT]free.fr> 6.0-0.fdr.1
- version 6.0

* Mon Dec 22 2003 Aurelien Bompard <gauret[AT]free.fr> 5.9-0.fdr.5
- solve stupid bug in %%install
- only create the preconfigured config file on install, not on upgrade

* Mon Dec 22 2003 Aurelien Bompard <gauret[AT]free.fr> 5.9-0.fdr.4
- post scriptlet doesn't overwrite user configuration now
  be careful if you upgrade from 5.9-0.fdr.3
- replace _DATADIR in apache configuration in the install stage
  (was in the post scriptlet before)
- remove 'noreplace' tag from the apache config file
- various cleanups in the %%install stage
- Thanks to Mickael Schwendt.

* Sun Dec 07 2003 Aurelien Bompard <gauret[AT]free.fr> 5.9-0.fdr.3
- %%post et %%postun now use condrestart instead of restart
- only restart apache if we are upgrading
- install and cp use the "-p" switch
- use %%_datadir in /etc/httpd/conf.d/awstats.conf
- improve cron job 
- don't brutally recode HTML pages
- the scan is now done hourly instead of daily
- *.pm files are not executable any more
- tools are in %%bindir
- various other improvements
- many thanks to Michael Schwendt and Dag Wieers.

* Sat Nov 29 2003 Aurelien Bompard <gauret[AT]free.fr> 5.9-0.fdr.2
- Set the hostname in %%post (thanks to Michael Koziarski)
- Improved customization in %%post

* Sun Nov 16 2003 Aurelien Bompard <gauret[AT]free.fr> 5.9-0.fdr.1
- fix /etc/cron.daily/awstats permissions
- fix log name in conf file
- port to fedora (from Mandrake)
