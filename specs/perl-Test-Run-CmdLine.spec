Name:           perl-Test-Run-CmdLine
Version:        0.0132
Release:        14%{?dist}
Summary:        Run TAP tests from command line using the Test::Run module
# lib and other code:   MIT
# bin/runprove:         GPL+ or Artistic
## sub-packaged:
# examples:             BSD
# Automatically converted from old format: (GPL+ or Artistic) and MIT - review is highly recommended.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-MIT
URL:            https://metacpan.org/release/Test-Run-CmdLine
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Test-Run-CmdLine-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
# Prefer Module::Build over ExtUtils::Maker because the Test::Run::Builder
# uses Module::Build too
BuildRequires:  perl(Module::Build) >= 0.36
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Moose)
# MooseX::Getopt::Basic version from unused MooseX::Getopt in META
BuildRequires:  perl(MooseX::Getopt::Basic) >= 0.26
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Usage) >= 1.12
BuildRequires:  perl(Test::Run::Base)
BuildRequires:  perl(Test::Run::Iface)
# Test::Run::Obj version taken from unused Test::Run::Core specified in META
BuildRequires:  perl(Test::Run::Obj) >= 0.0126
BuildRequires:  perl(Test::Run::Trap::Obj)
BuildRequires:  perl(Test::Trap)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(YAML::XS)
# Test:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(mro)
BuildRequires:  perl(Test::More)
# MooseX::Getopt::Basic version from unused MooseX::Getopt in META
Requires:       perl(MooseX::Getopt::Basic) >= 0.26
Requires:       perl(Test::Run::Obj) >= 0.0126

# Ignore dependencies in documentation
%{?perl_default_filter}

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::Run::Obj\\)$

%description
These Perl modules allow one to run TAP tests and analyze them from the
command line using the Test::Run module. It provides runprove tool with
command line facilities similar to Test::Harness' prove tool.

%package examples
Summary:        Examples for Test::Run::CmdLine Perl module
# lib and other code:   MIT
# bin/runprove:         GPL+ or Artistic
# examples:             BSD
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description examples
BSD-licensed and quite large examples for %{name} package.

%prep
%setup -q -n Test-Run-CmdLine-%{version}
find lib -type f -exec chmod 0644 {} +
# Remove unwanted files
rm --interactive=never examples/eumm-and-test-manifest/MyModule/.cvsignore
perl -i -ne 'print $_ unless m{^examples/eumm-and-test-manifest/MyModule/.cvsignore}' MANIFEST
# Correct shellbangs in examples
perl -MConfig -pi -e 's|^#!perl |$Config{startperl} |' \
    examples/eumm-and-test-manifest/MyModule/t/*.t

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes docs README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files examples
%doc examples

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0132-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0132-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0132-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0132-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0132-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0132-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0132-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0132-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.0132-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0132-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0132-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.0132-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0132-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.0132-1
- 0.0132 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0131-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.0131-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0131-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0131-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.0131-11
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0131-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0131-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.0131-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0131-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0131-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.0131-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0131-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.0131-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0131-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Petr Pisar <ppisar@redhat.com> - 0.0131-1
- 0.0131 bump

* Wed Jan 06 2016 Petr Pisar <ppisar@redhat.com> - 0.0130-1
- 0.0130 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0128-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.0128-2
- Perl 5.22 rebuild

* Fri Jun 05 2015 Petr Pisar <ppisar@redhat.com> - 0.0128-1
- 0.0128 bump

* Wed Jun 03 2015 Petr Pisar <ppisar@redhat.com> - 0.0127-1
- 0.0127 bump

* Fri Feb 27 2015 Petr Pisar <ppisar@redhat.com> 0.0126-1
- Specfile autogenerated by cpanspec 1.78.
