Name:           perl-DBD-ODBC
Version:        1.61
Release:        9%{?dist}
Summary:        ODBC Driver for DBI
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/DBD-ODBC
Source0:        https://cpan.metacpan.org/modules/by-module/DBD/DBD-ODBC-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(DBI::DBD)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  unixODBC-devel
# Run-time:
BuildRequires:  perl(constant)
BuildRequires:  perl(DBI) >= 1.609
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
# Tests:
BuildRequires:  perl(B)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBI::Const::GetInfoType)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
# Win32::API::More not used
# Optional tests:
# Test::Pod 1.00 not used
BuildRequires:  perl(Test::NoWarnings)
# Test::Pod::Coverage 1.04 not useful
Requires:       perl(DBI) >= 1.609
Requires:       unixODBC
Patch0:         Changes.patch

# Remove under-specfied dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DBI\\)$

%description
This module is needed to access ODBC databases from within Perl. The
module uses the unixODBC manager to connect to the database.

%prep
%setup -q -n DBD-ODBC-%{version}
%patch0 -p1

%build
PERL_MM_USE_DEFAULT=1 %{__perl} Makefile.PL -u INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
    NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes FAQ README TO_DO
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/DBD*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.61-8
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.61-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.61-2
- Perl 5.32 rebuild

* Mon Feb 10 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.61-1
- 1.61 bump
- Use make_build and make_install macros

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.60-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.60-1
- 1.60 bump

* Mon Aug 13 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.59-1
- 1.59 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.58-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.58-2
- Perl 5.28 rebuild

* Thu Apr 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.58-1
- 1.58 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.56-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.56-1
- 1.56 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.52-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Petr Pisar <ppisar@redhat.com> - 1.52-4
- Specify all dependencies (bug #1234347)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.52-2
- Perl 5.22 rebuild

* Mon Apr 20 2015 Jan Holcapek <holcapek@gmail.com> - 1.52-1
- Updated to upstream version 1.52.

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.50-5
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 4 2014 Jan Holcapek <holcapek@gmail.com> 1.50-3
- Enabled Unicode support.
- Fixed release in changelog.

* Mon Jul 28 2014 Jan Holcapek <holcapek@gmail.com> 1.50-1
- Updated to upstream version 1.50.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 6 2014 Jan Holcapek <holcapek@gmail.com> 1.48-1
- Updated to upstream version 1.48.

* Mon Feb 24 2014 Jan Holcapek <holcapek@gmail.com> 1.47-2
- Fix formatting of Changes, which confused RPM dependency
  solver find-requires.sh so that it made the RPM require 'perl(the)'

* Fri Feb 21 2014 Jan Holcapek <holcapek@gmail.com> 1.47-1
- Updated to upstream version 1.47.

* Fri Nov 22 2013 Jan Holcapek <holcapek@gmail.com> 1.45-1
- Initial import (#1028521).

* Fri Nov 08 2013 Jan Holcapek <holcapek@gmail.com> 1.45-1
- Specfile autogenerated by cpanspec 1.78.
