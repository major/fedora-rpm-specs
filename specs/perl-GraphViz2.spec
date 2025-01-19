Name:           perl-GraphViz2
Version:        2.67
Release:        8%{?dist}
Summary:        GraphViz2 Perl module
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/GraphViz2
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/GraphViz2-%{version}.tar.gz

BuildArch:      noarch
# build deps
BuildRequires:  graphviz
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl
# runtime deps
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(Data::Section::Simple)
BuildRequires:  perl(Date::Simple)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Text::Xslate)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test deps
BuildRequires:  perl(Graph::Directed)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Snapshot)
BuildRequires:  perl(utf8)

%{?perl_default_filter}

%description
This module provides a Perl interface to the amazing Graphviz, an open
source graph visualization tool from AT&T. It is called GraphViz2 so
that preexisting code using (the Perl module) GraphViz continues to work.

%prep
%setup -q -n GraphViz2-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/GraphViz2*
%{_mandir}/man3/GraphViz2*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.67-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 2.67-7
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.67-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.67-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.67-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.67-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jul 31 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 2.67-1
- Update to 2.67

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.66-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.66-5
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.66-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.66-2
- Perl 5.34 rebuild

* Sun Feb 28 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 2.66-1
- Update to 2.66

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 2.65-1
- Update to 2.65

* Sun Jan 03 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 2.64-1
- Update to 2.64

* Sun Nov 22 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.62-1
- Update to 2.62

* Sun Nov 08 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.61-1
- Update to 2.61

* Sun Nov 08 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.60-1
- Update to 2.60

* Sun Nov 01 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.59-1
- Update to 2.59

* Sun Oct 25 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.58-1
- Update to 2.58

* Sun Oct 18 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.57-1
- Update to 2.57

* Sun Oct 04 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.50-1
- Update to 2.50

* Sun Sep 20 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.48-1
- Update to 2.48
- Use /usr/bin/perl instead of %%{__perl}
- Use %%{make_install} instead of "make pure_install"
- Use %%{make_build} instead of make
- Pass NO_PERLLOCAL=1 to Makefile.PL

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.47-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.47-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.47-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.47-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.47-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.47-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.47-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.47-3
- Perl 5.28 rebuild

* Tue Jun 19 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.47-2
- Take into account review comments (#1592136)

* Thu Apr 12 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.47-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.
