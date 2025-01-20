Name:           perl-Net-FTPServer
Version:        1.125
Release:        32%{?dist}
Summary:        Secure, extensible and configurable Perl FTP server
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Net-FTPServer
Source0:        https://cpan.metacpan.org/authors/id/R/RY/RYOCHIN/Net-FTPServer-%{version}.tar.gz
# Increase default data segment size limit, bug #1381649
Patch0:         Net-FTPServer-1.125-Increase-default-memory-limit.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(Config)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Scalar) >= 1.126
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(Net::FTP)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(vars)
# Optional run-time:
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Authen::PAM)
BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(File::Sync)
# Tests:
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  %{_bindir}/uudecode
BuildRequires:  %{_bindir}/compress
# Optional run-time:
Requires:       perl(Archive::Zip)
Requires:       perl(Authen::PAM)
Requires:       perl(BSD::Resource)
Requires:       perl(Digest::MD5)
Requires:       perl(File::Sync)
Requires:       perl(IO::Scalar) >= 1.126

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(IO::Scalar\\)$

%description
Net::FTPServer is a secure, extensible and configurable FTP server
written in Perl.

This package contains the Perl modules. Install the perl-ftpd package for
the server executables.

%package -n perl-ftpd
Summary:        Secure, extensible and configurable Perl FTP server
Requires:       %{name} = %{version}-%{release}

%description -n perl-ftpd
Net::FTPServer is a secure, extensible and configurable FTP server
written in Perl.

This package contains server executables.

%prep
%setup -q -n Net-FTPServer-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT

# Daemon configuration file
install -m 644 -D etc/ftpd.conf $RPM_BUILD_ROOT%{_sysconfdir}/ftpd.conf

# Want the daemon in sbin rather than bin
[ ! -d $RPM_BUILD_ROOT%{_sbindir} ] \
    && mv -f $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_sbindir}

%check
make test

%files
%doc AUTHORS Changes COPYING README TODO doc/
%{perl_vendorlib}/Net/
%{_mandir}/man3/Net::FTPServer.3pm*
%{_mandir}/man3/Net::FTPServer::DBeg1::DirHandle.3pm*
%{_mandir}/man3/Net::FTPServer::DBeg1::FileHandle.3pm*
%{_mandir}/man3/Net::FTPServer::DBeg1::IOBlob.3pm*
%{_mandir}/man3/Net::FTPServer::DBeg1::Server.3pm*
%{_mandir}/man3/Net::FTPServer::DirHandle.3pm*
%{_mandir}/man3/Net::FTPServer::FileHandle.3pm*
%{_mandir}/man3/Net::FTPServer::Full::DirHandle.3pm*
%{_mandir}/man3/Net::FTPServer::Full::FileHandle.3pm*
%{_mandir}/man3/Net::FTPServer::Full::Server.3pm*
%{_mandir}/man3/Net::FTPServer::Handle.3pm*
%{_mandir}/man3/Net::FTPServer::InMem::DirHandle.3pm*
%{_mandir}/man3/Net::FTPServer::InMem::FileHandle.3pm*
%{_mandir}/man3/Net::FTPServer::InMem::Server.3pm*
%{_mandir}/man3/Net::FTPServer::Proxy::DirHandle.3pm*
%{_mandir}/man3/Net::FTPServer::Proxy::FileHandle.3pm*
%{_mandir}/man3/Net::FTPServer::Proxy::Server.3pm*
%{_mandir}/man3/Net::FTPServer::RO::DirHandle.3pm*
%{_mandir}/man3/Net::FTPServer::RO::FileHandle.3pm*
%{_mandir}/man3/Net::FTPServer::RO::Server.3pm*

%files -n perl-ftpd
%config(noreplace) %{_sysconfdir}/ftpd.conf
%{_sbindir}/dbeg1-ftpd.pl
%{_sbindir}/ftpd.pl
%{_sbindir}/inmem-ftpd.pl
%{_sbindir}/proxy-ftpd.pl
%{_sbindir}/ro-ftpd.pl

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.125-25
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.125-22
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.125-19
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.125-16
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.125-13
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.125-10
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Petr Pisar <ppisar@redhat.com> - 1.125-8
- Increase default data segment size limit (bug #1381649)

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.125-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.125-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.125-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.125-4
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.125-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.125-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct  8 2013 Paul Howarth <paul@city-fan.org> - 1.125-1
- Update to 1.125
  - Maintainer changed
  - Organized document and package files
  - Fixed pod format errors
  - New repository: https://github.com/ryochin/p5-net-ftpserver
  - Added a workaround to make sure to cause abort by SIGURG in t/240abort.t
    (CPAN RT#21261)
  - Fixed a bug that MLST command treated DirHandle as FileHandle
    (CPAN RT#27640)
  - Fixed a bug that ls -l command doesn't show a directory named '0'
    (CPAN RT#29503)
  - Fixed a problem that extra large file sizes were not displayed correctly
    because of integer digit overflow (CPAN RT#35332)
  - Fixed a problem caused by a Constant.pm internal change, affecting
    Archive::Zip (CPAN RT#35698)
  - Fixed a problem that Archive::Zip::Member::setLastModFileDateTimeFromUnix()
    doesn't accept 0 (CPAN RT#35698)
  - Addressed an issue that ftpd.conf had been installed despite lack of write
    permission to sysconfdir (CPAN RT#81130)
  - Added a message that Win32 platform is not supported (CPAN RT#81136)
  - Switched to Test::More for better installation process
  - Supported cpantesters and added other small changes
  - Tweaked t/240abort.t to skip when BSD::Resource is not installed, to avoid
    test errors on OpenBSD/Solaris at cpantesters
  - Improved an error message when using chroot feature by non-root users with
    Full personality
- This release by RYOCHIN -> update source URL
- Drop upstreamed patch and hacks for CPAN RT#35698
- Drop %%defattr, redundant since rpm 4.4
- Simplify %%install
- Run the test suite
- Make %%files list more explicit
- Don't use macros for commands
- Drop redundant recoding of documentation

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.122-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.122-20
- Perl 5.18 rebuild
- Specify all dependencies

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.122-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug  6 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.122-18
- applied patch from RT#35698. Tests were fixed by this change.
- switch off tests. Sometimes they passed in scratch build, sometimes failed.
  One reason could be old bug RT#21261.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.122-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 1.122-16
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.122-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 13 2011 Petr Pisar <ppisar@redhat.com> - 1.122-14
- Build-require Carp because Carp dual-lives now (bug #736768)

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.122-13
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.122-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.122-11
- Rebuild to fix problems with vendorarch/lib (#661697_

* Tue Dec 14 2010 Steven Pritchard <steve@kspei.com> 1.122-10
- Rebuild.

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.122-9
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.122-8
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.122-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.122-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat May 17 2008 Steven Pritchard <steve@kspei.com> 1.122-5
- Improve descriptions.
- Mark ftpd.conf config(noreplace).
- Drop bin/ and ftpd.conf from main package docs.
- Set permissions on ftpd.conf properly.

* Fri May 09 2008 Steven Pritchard <steve@kspei.com> 1.122-4
- Add perl-ftpd subpackage.
- License is really GPLv2+.

* Fri May 09 2008 Steven Pritchard <steve@kspei.com> 1.122-3
- Convert README to UTF-8.

* Wed May 07 2008 Steven Pritchard <steve@kspei.com> 1.122-2
- Update License tag.
- BR uudecode, compress.
- Fix a problem with using constants from Archive::Zip
  (http://rt.cpan.org/Ticket/Display.html?id=35698).
- Remove both _bindir and _sbindir to be safe.

* Mon Jul 16 2007 Steven Pritchard <steve@kspei.com> 1.122-1
- Specfile autogenerated by cpanspec 1.73.
- Fix License and doc list.
- Package scripts as examples.
- BR Archive::Zip, Authen::PAM, Compress::Zlib, DBI, and File::Sync.
- Require Authen::PAM and File::Sync.
- Remove .cvsignore files.
