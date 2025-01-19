Name:           perl-Data-Dump-Color
Version:        0.249
Release:        7%{?dist}
Summary:        Like Data::Dump, but with color
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Data-Dump-Color
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Data-Dump-Color-%{version}.tar.gz
BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(blib)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir::Install)
# runtime requirements
BuildRequires:  perl(ColorThemeBase::Static::FromStructColors) >= 0.006
BuildRequires:  perl(ColorThemeUtil::ANSI)
BuildRequires:  perl(Data::Dump::FilterContext)
BuildRequires:  perl(Data::Dump::Filtered)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Load::Util) >= 0.004
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util::LooksLikeNumber)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::NoWarnings)
Requires:       perl(Data::Dump::Filtered)
Requires:       perl(Data::Dump::FilterContext)
Requires:       perl(MIME::Base64)

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Win32::Console::ANSI\\)

%description
This module aims to be a drop-in replacement for Data::Dump. It adds colors
to dumps. For more information, see Data::Dump. This documentation explains
what's different between this module and Data::Dump.

%prep
%setup -q -n Data-Dump-Color-%{version}
/usr/bin/chmod +x share/examples/*.pl
/usr/bin/perl -pi -e 's|^#! ?perl|#!/usr/bin/perl|' share/examples/example2.pl

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man3/*
%{_mandir}/man1/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.249-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 0.249-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.249-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.249-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.249-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.249-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 05 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 0.249-1
- Update to 0.249
- Reorder build requirements

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.248-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.248-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.248-4
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.248-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.248-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 27 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 0.248-1
- Update to 0.248

* Sun Jun 06 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 0.245-1
- Update to 0.245

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.243-2
- Perl 5.34 rebuild

* Sun Feb 14 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 0.243-1
- Update to 0.243
- Use %%{make_install} instead of "make pure_install"
- Use %%{make_build} instead of make
- Replace calls to %%{__perl} with /usr/bin/perl
- Pass NO_PERLLOCAL to Makefile.PL

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.241-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.241-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.241-7
- Perl 5.32 rebuild

* Tue Mar 03 2020 Petr Pisar <ppisar@redhat.com> - 0.241-6
- Build-require blib module for the tests

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.241-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.241-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.241-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.241-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.241-1
- Update to 0.241
- Drop Group tag

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.240-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.240-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.240-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.240-1
- 0.240 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-2
- Perl 5.22 rebuild

* Mon Nov 03 2014 Petr Šabata <contyk@redhat.com> - 0.23-1
- 0.23 bugfix bump

* Tue Oct 21 2014 Petr Pisar <ppisar@redhat.com> - 0.22-1
- 0.22 bump

* Mon Sep 15 2014 Petr Šabata <contyk@redhat.com> - 0.21-2
- Correct the dep list

* Wed Sep 10 2014 Petr Šabata <contyk@redhat.com> 0.21-1
- Initial packaging
