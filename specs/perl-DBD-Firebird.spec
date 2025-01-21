# Filter the Perl extension module
%{?perl_default_filter}

%global pkgname DBD-Firebird

Summary:        Firebird interface for perl
Name:           perl-DBD-Firebird
Version:        1.39
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{pkgname}
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAM/%{pkgname}-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  libfbclient2-devel >= 2.5.1
BuildRequires:  libicu-devel
BuildRequires:  gcc
%if 0%{?rhel} == 8
# https://github.com/mariuz/perl-dbd-firebird/issues/58
BuildRequires:  gcc-toolset-12
%endif
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBI) >= 1.43
BuildRequires:  perl(DBI::DBD)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(Math::BigFloat) >= 1.55
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::CheckDeps) >= 0.007
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%description
DBD::Firebird is a Perl module that works with the DBI module to provide
access to Firebird databases.

%prep
%autosetup -p1 -n %{pkgname}-%{version}

%build
%if 0%{?rhel} == 8
. /opt/rh/gcc-toolset-12/enable
%endif

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%make_build

%install
%make_install
chmod -R u+w $RPM_BUILD_ROOT/*

%check
# Test for ib_set_tx_param() seems to be buggy (thus disable for now)
rm -f t/embed-62-timeout.t

# Disable thread-based test of ib_wait_event, as this test cannot be
# guaranteed to succeed with overloaded host, see:
# - https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=719582
# - https://bugzilla.redhat.com/show_bug.cgi?id=1228642
# - https://bugzilla.redhat.com/show_bug.cgi?id=1161469
export AUTOMATED_TESTING=1

# Full test coverage requires a live Firebird database (see the README file)
make test

%files
%doc Changes README
%{perl_vendorarch}/DBD/
%{perl_vendorarch}/auto/DBD/
%{_mandir}/man3/*.3*

%changelog
* Sun Jan 19 2025 Robert Scheck <robert@fedoraproject.org> 1.39-1
- Upgrade to 1.39 (#2338811)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.38-2
- Perl 5.40 rebuild

* Tue May 21 2024 Robert Scheck <robert@fedoraproject.org> 1.38-1
- Upgrade to 1.38 (#2282101)

* Mon May 20 2024 Robert Scheck <robert@fedoraproject.org> 1.37-1
- Upgrade to 1.37 (#2281617)

* Mon May 20 2024 Robert Scheck <robert@fedoraproject.org> 1.36-1
- Upgrade to 1.36 (#2281509)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.34-7
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Robert Scheck <robert@fedoraproject.org> 1.34-4
- Buildrequire libfbclient2-devel (or firebird-devel) to avoid
  Koschei build failures caused by libfbclient.so (#2102191)

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.34-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 05 2021 Robert Scheck <robert@fedoraproject.org> 1.34-1
- Upgrade to 1.34 (#2029130)

* Wed Nov 10 2021 Robert Scheck <robert@fedoraproject.org> 1.33-1
- Upgrade to 1.33 (#2021689)

* Sat Aug 21 2021 Robert Scheck <robert@fedoraproject.org> 1.32-8
- Re-enabled s390x build since firebird 4.x is fixed (#1969393)

* Mon Jul 26 2021 Robert Scheck <robert@fedoraproject.org> 1.32-7
- Disabled s390x build until firebird 4.x is fixed (#1969393)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.32-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.32-2
- Perl 5.32 rebuild

* Sun Apr 26 2020 Robert Scheck <robert@fedoraproject.org> 1.32-1
- Upgrade to 1.32 (#1812799)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.31-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.31-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Robert Scheck <robert@fedoraproject.org> 1.31-1
- Upgrade to 1.31 (#1522691)

* Mon Dec 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.29-1
- 1.29 bump

* Wed Oct 11 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-1
- 1.25 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-1
- 1.24 bump

* Fri Oct 14 2016 Robert Scheck <robert@fedoraproject.org> 1.22-3
- Buildrequire libfbclient.so rather firebird-devel to cover
  building with firebird 2.5.x and 3.0.x without conditionals

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-2
- Perl 5.24 rebuild

* Wed Mar 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-1
- 1.22 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 29 2015 Robert Scheck <robert@fedoraproject.org> 1.21-1
- Upgrade to 1.21 (#1267292)

* Mon Jun 22 2015 Robert Scheck <robert@fedoraproject.org> 1.20-1
- Upgrade to 1.20

* Mon Jun 22 2015 Robert Scheck <robert@fedoraproject.org> 1.19-4
- Disable failed test with overloaded host (#1161469, #1228642)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-2
- Perl 5.22 rebuild

* Fri Apr 03 2015 Robert Scheck <robert@fedoraproject.org> 1.19-1
- Upgrade to 1.19 (#1207216)

* Sun Oct 12 2014 Robert Scheck <robert@fedoraproject.org> 1.18-1
- Upgrade to 1.18

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-7
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.11-3
- Perl 5.18 rebuild

* Fri Apr 19 2013 Robert Scheck <robert@fedoraproject.org> 1.11-2
- Changes to match with Fedora Packaging Guidelines (#951874)

* Sun Apr 14 2013 Robert Scheck <robert@fedoraproject.org> 1.11-1
- Upgrade to 1.11
- Initial spec file for Fedora and Red Hat Enterprise Linux
