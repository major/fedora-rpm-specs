Name:           perl-Module-Install-Copyright
Version:        0.009
Release:        30%{?dist}
Summary:        Package a COPYRIGHT file with a distribution
# CONTRIBUTING: CC-BY-SA-2.0-UK
# COPYRIGHT:    LicenseRef-Fedora-Public-Domain
# Other file:   GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND CC-BY-SA-2.0-UK AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/Module-Install-Copyright
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Module-Install-Copyright-%{version}.tar.gz
# To boostrap this package without bundling
Patch0:         Module-Install-Copyright-0.009-Build-without-bundled-Module-Package-modules.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Package)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8.0
BuildRequires:  perl(base)
# constant not used at tests
# List::MoreUtils not used at tests
# Module::Install::Admin::RDF 0.003 not used at tests
BuildRequires:  perl(Module::Install::Base)
# Module::Install::Contributors 0.001 not used at tests
# Module::Manifest not used at tests
# MooX::Struct not used at tests
# Path::Class not used at tests
# RDF::Trine not used at tests
# RDF::Trine::Namespace not used at tests
# Software::License not used at tests
# Software::LicenseUtils not used at tests
BuildRequires:  perl(strict)
# Tests:
BuildRequires:  perl(Test::More) >= 0.61

%description
This Module::Install plug-in extracts copyright and licensing information from
embedded POD and/or RDF meta-data included in the distribution, and outputs it
as a text file called COPYRIGHT which should roughly conform to the Debian
copyright file format.

%prep
%setup -q -n Module-Install-Copyright-%{version}
%patch -P0 -p1
# Remove bundled modules.
# And remove inc/Module/Package/Dist/RDF.pm because it's
# a Module::Package::RDF plug-in that depends on this package. Fortunatelly,
# the inc/Module/Package/Dist/RDF.pm is not good for anything so the patch
# makes not to load it.
rm -rf ./inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README
%doc examples
%dir %{perl_vendorlib}/Module
%dir %{perl_vendorlib}/Module/Install
%dir %{perl_vendorlib}/Module/Install/Admin
%{perl_vendorlib}/Module/Install/Admin/Copyright.pm
%{perl_vendorlib}/Module/Install/Admin/Credits.pm
%{perl_vendorlib}/Module/Install/Copyright.pm
%{perl_vendorlib}/Module/Install/Credits.pm
%{_mandir}/man3/Module::Install::Admin::Copyright.*
%{_mandir}/man3/Module::Install::Admin::Credits.*
%{_mandir}/man3/Module::Install::Copyright.*
%{_mandir}/man3/Module::Install::Credits.*

%changelog
* Wed Oct 14 2026 Petr Pisar <ppisar@redhat.com> - 0.009-30
- Remove unused build-time dependencies

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.009-25
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-18
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-15
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 16 2016 Petr Pisar <ppisar@redhat.com> 0.009-1
- Specfile autogenerated by cpanspec 1.78.
