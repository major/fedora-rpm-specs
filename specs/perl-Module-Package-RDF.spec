Name:           perl-Module-Package-RDF
Version:        0.014
Release:        17%{?dist}
Summary:        Drive your distribution with RDF
# CONTRIBUTING: CC-BY-SA
# other files:  GPL+ or Artistic
# Automatically converted from old format: (GPL+ or Artistic) and CC-BY-SA - review is highly recommended.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-CC-BY-SA
URL:            https://metacpan.org/release/Module-Package-RDF
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Module-Package-RDF-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Package)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(Getopt::ArgvFile)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::All)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::AutoLicense) >= 0.08
BuildRequires:  perl(Module::Install::AutoManifest)
# 1.04 version from Module::Install in META.yml
BuildRequires:  perl(Module::Install::Base) >= 1.04
BuildRequires:  perl(Module::Install::Copyright) >= 0.009
BuildRequires:  perl(Module::Install::Credits) >= 0.009
BuildRequires:  perl(Module::Install::DOAP) >= 0.006
BuildRequires:  perl(Module::Install::DOAPChangeSets) >= 0.206
BuildRequires:  perl(Module::Install::RDF) >= 0.009
BuildRequires:  perl(Module::Install::ReadmeFromPod) >= 0.12
BuildRequires:  perl(Module::Install::TrustMetaYml) >= 0.003
BuildRequires:  perl(Module::Package) >= 0.30
BuildRequires:  perl(Module::Package::Plugin)
BuildRequires:  perl(Moo)
BuildRequires:  perl(RDF::TriN3) >= 0.201
BuildRequires:  perl(RDF::Trine) >= 0.135
BuildRequires:  perl(Software::License)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Template)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More) >= 0.96
# 1.04 version from Module::Install in META.yml
Requires:       perl(Module::Install::Base) >= 1.04
Requires:       perl(Module::Package::Plugin)
Requires:       perl(RDF::TriN3) >= 0.201
Requires:       perl(warnings)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Module::Install::Base|RDF::TriN3)\\)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(:VERSION\\) >= 5\\.(5|8)\\.

%description
This is a build system for Perl modules defined by RDF.

%prep
%setup -q -n Module-Package-RDF-%{version}
rm -rf inc
perl -i -lne 'print $_ unless m{^inc/}' MANIFEST

%build
# bootstrap dies on CPAN RT#71565 because it cannot normalize '5.010' string.
perl -Ilib Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 \
    --skipdeps # avoid installing unused dependencies from CPAN
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README TODO
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.014-16
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-9
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-6
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon May 06 2019 Petr Pisar <ppisar@redhat.com> - 0.014-1
- Specfile autogenerated by cpanspec 1.78.
