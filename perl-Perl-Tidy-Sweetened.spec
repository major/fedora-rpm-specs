Name:           perl-Perl-Tidy-Sweetened
Version:        1.18
Release:        6%{?dist}
Summary:        Tweaks to Perl::Tidy to support some syntactic sugar
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Perl-Tidy-Sweetened
Source0:        https://cpan.metacpan.org/authors/id/M/MG/MGRIMES/Perl-Tidy-Sweetened-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
There are a number of modules on CPAN that allow users to write their
classes with a more "modern" syntax. These tools eliminate the need to
shift off $self, can support type checking and offer other improvements.
Unfortunately, they can break the support tools that the Perl community has
come to rely on. This module attempts to work around those issues.

%prep
%setup -q -n Perl-Tidy-Sweetened-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README TODO
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-5
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-2
- Perl 5.34 rebuild

* Sun Jan 31 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-1
- 1.18 bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-1
- 1.17 bump

* Thu Oct 22 2020 Petr Pisar <ppisar@redhat.com> - 1.16-4
- Adjust tests to Perl-Tidy-20200907 (bug #1879947)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-2
- Perl 5.32 rebuild

* Tue Apr 14 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-1
- 1.16 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-1
- 1.15 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-2
- Perl 5.28 rebuild

* Thu Mar 29 2018 Petr Pisar <ppisar@redhat.com> - 1.14-1
- 1.14 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 06 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-1
- 1.12 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-2
- Perl 5.24 rebuild

* Mon Apr 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-1
- 1.11 bump

* Mon Mar 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-1
- 1.10 bump

* Fri Mar 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-3
- Fix test to work against perltidy-20160302 (bug #1314800)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-1
- 1.07 bump

* Fri Nov 27 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-1
- Initial release
