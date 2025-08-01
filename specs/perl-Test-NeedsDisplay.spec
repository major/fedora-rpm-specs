Name:           perl-Test-NeedsDisplay
Version:        1.07
Release:        40%{?dist}
Summary:        Ensure that tests needing a display have one
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-NeedsDisplay
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Test-NeedsDisplay-%{version}.tar.gz
# Prevent from races by using free display numbers, bug #1248968,
# CPAN RT#106699
Patch0:         Test-NeedsDisplay-1.07-Use-non-conflicting-display-numbers.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install) >= 0.77
BuildRequires:  perl(Module::Install::External)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# xorg-x11-server-Xvfb for xvfb-run program required by Makefile.PL
BuildRequires:  xorg-x11-server-Xvfb
# Run-time:
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(warnings)
# Optional tests:
# Pod::Simple 3.07 not used
# Test::CPAN::Meta 0.12 not used
# Test::MinimumVersion 0.008 not used
# Test::Pod 1.26 not used
# xeyes for xeyes (will pull in xorg-x11-apps on older distros)
BuildRequires:  xeyes
Requires:       perl(File::Spec) >= 0.80
Requires:       perl(Test::More) >= 0.47

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Spec|Test::More)\\)$

%description
When testing GUI applications, sometimes applications or modules absolutely
insist on a display, even just to load a module without actually showing
any objects.

%prep
%setup -q -n Test-NeedsDisplay-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -rf ./inc
sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-32
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-29
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 1.07-27
- Requires xeyes, not xorg-x11-apps

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-26
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-23
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-20
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-17
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-15
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Petr Pisar <ppisar@redhat.com> - 1.07-13
- Prevent from races by using free display numbers (bug #1248968)

* Fri Jul 31 2015 Petr Pisar <ppisar@redhat.com> - 1.07-12
- Specify all dependencies

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-10
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.07-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.07-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct  2 2011 Tom Callaway <spot@fedoraproject.org> - 1.07-1
- update to 1.07

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.05-8
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.05-6
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.05-5
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.05-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 16 2008 Marcela Mašláňová <mmaslano@redhat.com> 1.05-1
- Specfile autogenerated by cpanspec 1.77.
