Name:           perl-eperl
Version:        2.2.14
Release:        64%{?dist}
Summary:        Embedded Perl Language
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://www.ossp.org/pkg/tool/eperl/
Source0:        ftp://ftp.ossp.org/pkg/tool/eperl/eperl-%{version}.tar.gz
Patch0:         http://ftp.debian.org/pool/main/e/eperl/eperl_2.2.14-15.1.diff.gz
Patch1:         perl-eperl-5.16compat.patch
# Fix format-security compiler warnings, bug #1058664
Patch2:         eperl-2.2.14-Fix-format-security-compiler-warnings.patch
Patch3:         perl-eperl-c99.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gdbm-devel
BuildRequires:  gcc
BuildRequires:  libdb-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.3.250
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

%description
ePerl interprets an ASCII file bristled with Perl 5 program statements
by evaluating the Perl 5 code while passing through the plain ASCII
data. It can operate in various ways: As a stand-alone Unix filter or
integrated Perl 5 module for general file generation tasks and as a
powerful Webserver scripting language for dynamic HTML page
programming.

The documentation and latest release can be found on
http://www.ossp.org/pkg/tool/eperl/

Note that this package does not include the Apache::ePerl module,
which is designed for mod_perl 1.x.

%prep
%setup -q -n eperl-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
chmod u+x etc/shtool
find contrib/utils -perm /0100 -type f -exec chmod 644 {} \;

%build
# Use NO_PERLLOCAL to stop generating perllocal.pod
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
    NO_PACKLIST=1 NO_PERLLOCAL=1
#perl -pi -e 's/^\tLD_RUN_PATH=[^\s]+\s*/\t/' Makefile
%{make_build}
make -f Makefile.stand %{?_smp_mflags} eperl \
    prefix=%{_prefix} libdir=%{_datadir}/eperl

%install
# pure_install doesn't work.
%{make_install}
make -f Makefile.stand install \
    prefix=$RPM_BUILD_ROOT%{_prefix} libdir=$RPM_BUILD_ROOT%{_datadir}/eperl

# Remove all of the Apache bits.
find $RPM_BUILD_ROOT -iname '*apache*' -exec rm -rf {} \; || :
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license ARTISTIC COPYING
%doc ANNOUNCE ChangeLog ChangeLog.1x ChangeLog.20 ChangeLog.21
%doc INSTALL.APACHE INSTALL.NSAPI KNOWN.BUGS NEWS README
%doc eperl_logo.gif eperl_powered.gif contrib/utils/
%{perl_vendorarch}/*
%{_bindir}/eperl
%{_datadir}/eperl
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.14-62
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.14-58
- Perl 5.38 rebuild

* Thu Feb 02 2023 Florian Weimer <fweimer@redhat.com> - 2.2.14-57
- Fix C99 compatibility issue

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.14-54
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-52
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.14-51
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.14-48
- Perl 5.32 rebuild

* Fri Feb 28 2020 Petr Pisar <ppisar@redhat.com> - 2.2.14-47
- Modernize a spec file

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.14-44
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.14-41
- Perl 5.28 rebuild

* Mon Feb 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.14-40
- Add build-require gcc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.2.14-38
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.14-35
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.14-33
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.14-30
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.14-29
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Petr Pisar <ppisar@redhat.com> - 2.2.14-26
- Fix format-security compiler warnings (bug #1058664)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.2.14-24
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug  6 2012 Marcela Mašláňová <mmaslano@redhat.com> - 2.2.14-22
- apply Jitka's patch rhbz#839609
- change BR from db4-devel to libdb-devel

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.2.14-20
- Perl 5.16 rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 16 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.2.14-18
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.2.14-16
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.2.14-15
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.2.14-14
- Mass rebuild with perl-5.12.0

* Fri Mar 12 2010 Marcela Mašláňová <mmaslano@redhat.com> - 2.2.14-13
- rebuild with new gdbm

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.2.14-12
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 05 2008 Steven Pritchard <steve@kspei.com> 2.2.14-9
- Update to Debian's eperl_2.2.14-15.1.diff.gz.
- BR ExtUtils::Embed.
- Drop eperl-2.2.14-perl510-noDynaLoader.a.patch.

* Fri Mar 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.14-8
- actually commit patch to cvs

* Fri Mar 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.14-7
- perl 5.10 doesn't have DynaLoader.a

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.14-6
- Rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2.14-5
- Autorebuild for GCC 4.3

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 2.2.14-4
- Fix find option order.
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Mon Aug 28 2006 Steven Pritchard <steve@kspei.com> 2.2.14-3
- Rebuild.

* Thu Jul 13 2006 Steven Pritchard <steve@kspei.com> 2.2.14-2
- Update to Debian's eperl_2.2.14-13.diff.gz.
- Spec cleanup.
- Drop docs that aren't relevant.

* Tue Jul 12 2005 Steven Pritchard <steve@kspei.com> 2.2.14-1
- Specfile autogenerated.
- Add eperl_2.2.14-12.diff.gz from Debian.
- Drop Apache::ePerl (requires mod_perl 1).
