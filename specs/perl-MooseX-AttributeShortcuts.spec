# Run optional test
%{bcond_without perl_MooseX_AttributeShortcuts_enables_optional_test}

Name:           perl-MooseX-AttributeShortcuts
Version:        0.037
Release:        23%{?dist}
Summary:        Shorthand for common Moose attribute options
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://metacpan.org/release/MooseX-AttributeShortcuts/
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/MooseX-AttributeShortcuts-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(aliased)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Moose) >= 1.14
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Meta::TypeConstraint)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Meta::TypeConstraint::Mooish)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(MooseX::Types::Common::String)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Util)
BuildRequires:  perl(namespace::autoclean) >= 0.24
# Tests only:
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::CheckDeps) >= 0.010
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::Moose::More) >= 0.049
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Requires)
%if %{with perl_MooseX_AttributeShortcuts_enables_optional_test}
# Optional tests:
BuildRequires:  perl(MooseX::SemiAffordanceAccessor)
%endif

%description
Ever find yourself repeatedly specifying writers and builders, because there's
no good shortcut to specify them? Sometimes you want an attribute to have
a read-only public interface, but a private writer. And wouldn't it be easier
to just say "builder => 1" and have the attribute construct the canonical
"_build_$name" builder name for you?

This package causes an attribute trait to be applied to all attributes defined
to the using class. This trait extends the attribute option processing to
handle the above variations.


%prep
%setup -q -n MooseX-AttributeShortcuts-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.037-22
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.037-15
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.037-12
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.037-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.037-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.037-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 21 2017 Petr Pisar <ppisar@redhat.com> - 0.037-1
- 0.037 bump

* Mon Nov 06 2017 Petr Pisar <ppisar@redhat.com> - 0.036-1
- 0.036 bump

* Mon Sep 25 2017 Petr Pisar <ppisar@redhat.com> - 0.035-1
- 0.035 bump

* Fri Aug 11 2017 Petr Pisar <ppisar@redhat.com> - 0.034-2
- Rebuild to deal with a clash after merging f27-rebuild tag

* Thu Jul 27 2017 Petr Pisar <ppisar@redhat.com> - 0.034-1
- 0.34 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.033-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Petr Pisar <ppisar@redhat.com> - 0.033-1
- 0.033 bump

* Wed Jun 14 2017 Petr Pisar <ppisar@redhat.com> - 0.032-1
- 0.032 bump

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.031-2
- Perl 5.26 rebuild

* Thu Jun 01 2017 Petr Pisar <ppisar@redhat.com> - 0.031-1
- 0.031 bump

* Tue May 09 2017 Petr Pisar <ppisar@redhat.com> - 0.029-1
- 0.029 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.028-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.028-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.028-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.028-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.028-2
- Perl 5.22 rebuild

* Wed Apr 08 2015 Petr Pisar <ppisar@redhat.com> - 0.028-1
- 0.028 bump

* Thu Mar 12 2015 Petr Pisar <ppisar@redhat.com> - 0.027-1
- 0.027 bump

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.024-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.024-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 Petr Pisar <ppisar@redhat.com> - 0.024-1
- 0.024 bump

* Mon Apr 14 2014 Petr Pisar <ppisar@redhat.com> - 0.023-1
- 0.023 bump

* Tue Oct 01 2013 Petr Pisar <ppisar@redhat.com> - 0.022-1
- 0.022 bump

* Tue Sep 10 2013 Petr Pisar <ppisar@redhat.com> - 0.021-1
- 0.021 bump

* Tue Aug 27 2013 Petr Pisar <ppisar@redhat.com> - 0.020-1
- 0.020 bump

* Wed Aug 07 2013 Petr Pisar <ppisar@redhat.com> - 0.019-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.019-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Petr Pisar <ppisar@redhat.com> - 0.019-1
- 0.19 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 Petr Pisar <ppisar@redhat.com> - 0.017-1
- 0.017 bump

* Mon Aug 27 2012 Petr Pisar <ppisar@redhat.com> - 0.015-1
- 0.015 bump

* Fri Aug 17 2012 Petr Pisar <ppisar@redhat.com> - 0.014-1
- 0.014 bump

* Mon Jul 23 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-1
- 0.013 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.010-2
- Perl 5.16 rebuild

* Tue Apr 10 2012 Petr Pisar <ppisar@redhat.com> - 0.010-1
- 0.010 bump

* Mon Jan 23 2012 Petr Pisar <ppisar@redhat.com> - 0.008-1
- 0.008 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 01 2011 Petr Pisar <ppisar@redhat.com> - 0.006-1
- 0.006 bump

* Thu Sep 29 2011 Petr Pisar <ppisar@redhat.com> 0.005-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot and defattr spec code
