Name:           perl-Type-Tie
Version:        0.015
Release:        9%{?dist}
Summary:        Tie a variable to a type constraint
# cf. README
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Type-Tie
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tie-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-interpreter >= 0:5.008005
BuildRequires:  perl-generators

BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter::Tiny) >= 0.026
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Hash::FieldHash)
# Optional alternative to perl(Hash::FieldHash)
# BuildRequires:  perl(Hash::Util::FieldHash::Compat)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Tests:
%if !%{defined perl_bootstrap}
# Build-cycle: perl-Type-Tiny → perl-Type-Tie
BuildRequires:  perl(Types::Standard)
%endif
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(constant)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# perl-generators fails to detect this
Requires:       perl(Data::Dumper)

%description
This module exports a single function: ttie. ttie ties a variable to a
type constraint, ensuring that whatever values stored in the variable
will conform to the type constraint. If the type constraint has
coercions, these will be used if necessary to ensure values assigned to
the variable conform.

%prep
%setup -q -n Type-Tie-%{version}

# Remove bundled stuff
%{__rm} -r inc/
sed -i -e '/^inc\/.*$/d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install DESTDIR=$RPM_BUILD_ROOT

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%license COPYRIGHT LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.015-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-8
- Perl 5.36 re-rebuild of bootstrapped packages

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-7
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.015-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.015-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-4
- Perl 5.34 re-rebuild of bootstrapped packages

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.015-1
- Upstream update.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-7
- Perl 5.32 re-rebuild of bootstrapped packages

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-3
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-2
- Perl 5.30 rebuild

* Tue Mar 05 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.014-1
- Upstream update.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.013-1
- Upstream update.
- Add BR: perl(Moo).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.011-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.011-1
- Upstream update.

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-8
- Perl 5.28 re-rebuild of bootstrapped packages

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-7
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-4
- Perl 5.26 re-rebuild of bootstrapped packages

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-3
- Perl 5.26 rebuild

* Fri Feb 03 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.009-2
- Reflect feedback from package review.

* Fri Feb 03 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.009-1
- Initial Fedora package.
