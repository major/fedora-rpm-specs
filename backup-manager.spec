%global commit b710665c784fad8e805a3e8cea4ebe2016615ca6
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           backup-manager
Version:        0.7.10
Release:        37%{?dist}
Summary:        A command line backup tool for GNU/Linux

License:        GPLv2+
URL:            https://github.com/sukria/Backup-Manager
Source0:        https://github.com/sukria/Backup-Manager/archive/%{commit}/Backup-Manager-%{commit}.tar.gz
Source1:        %{name}.cron.daily
# Change default directory and add cron.daily support
Patch0:         %{name}-configtpl.patch
# Strict pod2man does not tolerate mistakes
Patch1:         %{name}-0.7.10-Fix-POD-syntax.patch
# Fix #1208596 - backup-manager package uses /share/locale/ while every other package use /usr/share/locale/
Patch2:         %{name}-0.7.10-destdir.patch
BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
BuildRequires: make

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       /bin/bash
Requires:       /usr/bin/cdrecord
Requires:       /usr/bin/logger
Requires:       /usr/bin/mkisofs
Requires:       bc
Requires:       bzip2
Requires:       coreutils
Requires:       crontabs
Requires:       dar
Requires:       diffutils
Requires:       dvd+rw-tools
Requires:       less
Requires:       ftp
Requires:       gettext
Requires:       gnupg
Requires:       gzip
Requires:       openssh-clients
Requires:       rsync
Requires:       sed
Requires:       tar
Requires:       which


%description
Backup Manager is a command line backup tool for GNU/Linux, designed to help
you make daily archives of your file system. Written in bash and Perl, it can
make archives in lots of open formats (tar, gzip, bzip2, lzma, dar, zip) and
provides lots of interesting features (such as network exports or CD/DVD
automated-burning).

The program is designed to be as easy to use as possible and is popular with
desktop users and sysadmins. The whole backup process is defined in one
full-documented configuration file which needs no more than 5 minutes to tune
for your needs.


%prep
%setup -qn Backup-Manager-%{commit}
%patch0 -p1 -b .configtpl
%patch1 -p1 -b .pod
%patch2 -p1 -b .destdir

# Clean Makefile
sed -i -e "s@install -o root -g 0 @install @" Makefile

# rpmlint W: file-not-utf8
for file in  ChangeLog THANKS; do
    iconv -f ISO_8859-1 -t UTF-8 -o ${file}{.utf8,}
    mv ${file}{.utf8,}
done;


%build
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install \
    DESTDIR=%{buildroot} \
    PERL5DIR=%{buildroot}%{perl_vendorlib} \
    INSTALL="install -p"
%find_lang %{name}

# Create backup directory
install -d %{buildroot}%{_localstatedir}/%{name}

# Copy configuration
install -p -D -m 0644 %{buildroot}%{_datadir}/%{name}/%{name}.conf.tpl \
    %{buildroot}%{_sysconfdir}/%{name}.conf

# Add cron.daily
install -p -D -m 0755 %{SOURCE1} %{buildroot}%{_sysconfdir}/cron.daily/%{name}.cron

# rpmlint : sanitize.sh is a non-executable-script
chmod 755 %{buildroot}%{_datadir}/%{name}/sanitize.sh



%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README THANKS
%{_bindir}/%{name}-purge
%{_bindir}/%{name}-upload
%{_sbindir}/%{name}
%{perl_vendorlib}/BackupManager
%{_datadir}/%{name}
%{_mandir}/man8/%{name}*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_sysconfdir}/cron.daily/%{name}.cron
%{_localstatedir}/%{name}


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.10-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.7.10-36
- Perl 5.36 rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.10-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.10-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.7.10-33
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.10-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.10-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.7.10-30
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.10-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.7.10-27
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.10-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.7.10-24
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.7.10-21
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.7.10-19
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Petr Šabata <contyk@redhat.com> - 0.7.10-17
- Prevent FTBFS by adding a build time dependency on podlators, providing pod2man

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.7.10-15
- Perl 5.22 rebuild

* Sun May 24 2015 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.7.10-14
- Path for issue #1208596: backup-manager package uses /share/locale/ while every other package use /usr/share/locale/

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.7.10-13
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 21 2013 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.7.10-11
- Add a missing requirement on crontabs for the cron job to the spec file (#947045)
- Readability improvement
- Change URL and Source0 according https://github.com/sukria/Backup-Manager/issues/24

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.7.10-9
- Perl 5.18 rebuild
- Fix POD syntax

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.7.10-6
- Perl 5.16 rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.7.10-4
- Perl mass rebuild

* Fri Jun 10 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.7.10-3
- Perl 5.14 mass rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 26 2010 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.7.10-1
- Upstream 0.7.10
- Remove old sed in SPEC file
- Remove version from path0
- Add French translation

* Wed Jul 14 2010 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.7.9-1
- Upstream 0.7.9

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.7.8-7
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.7.8-6
- rebuild against perl 5.10.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 12 2009 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.7.8-4
- Bump release

* Thu Jun 25 2009 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.7.8-3
- Add dar in requierement

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 07 2009 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.7.8-1
- Upstream 0.7.8
- Remove genisoimage requirement

* Thu Jan 15 2009 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.7.7-7
- Replace some sed by a patch
- Replace /bin/sh by /bin/bash

* Tue Jan 13 2009 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.7.7-6
- Fix Requires
- Fix use %%{_localstatedir} insted %%{_var}/lib

* Sat Jan 10 2009 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.7.7-5
- Fix Requires
- Add  %%{_var}/lib/backup-manager directory
- Use %%{buildroot} insted $RPM_BUILD_ROOT

* Sat Jan 10 2009 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.7.7-4
- Fix license
- Fix timestamp in install

* Fri Oct 10 2008 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.7.7-3
- Add a daily cron (backup-manager.cron.daily)

* Wed Aug 20 2008 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.7.7-2
- utf-8 correction with Iconv
- Configuration file correction

* Sun Aug 17 2008 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.7.7-1
- Initial packaging
