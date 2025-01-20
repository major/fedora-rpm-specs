Name:           perl-Wiki-Toolkit
Version:        0.87
Release:        14%{?dist}
Summary:        Toolkit for building Wikis
# Wiki/Toolkit pod
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://metacpan.org/release/Wiki-Toolkit
Source0:        http://cpan.metacpan.org/authors/id/B/BO/BOB/Wiki-Toolkit-%{version}.tar.gz

BuildArch:      noarch
# build deps
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(DBD::SQLite) >= 0.25
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Lingua::Stem)
BuildRequires:  perl(lib)
# runtime deps
BuildRequires:  perl(CGI)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::PullParser)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Text::WikiFormat)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Time::Seconds)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# test deps
BuildRequires:  perl(Hook::LexWrap)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(warnings)

%{?perl_default_filter}

# There are several search backends provided by Wiki-Toolkit. Because we
# don't want to force one on our users, we filter all their requires out.
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Apache2::
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBIx::FullTextSearch\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Lucy::
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Plucene::
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Search::

# Wiki-Toolkit can store configuration from previous tests runs. We
# don't want this so we exclude it from the requires
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Wiki::Toolkit::TestConfig\\)$

%description
Helps you develop Wikis quickly by taking care of the boring bits for you.
You will still need to write some code - this isn't an instant Wiki.

%prep
%setup -q -n Wiki-Toolkit-%{version}
chmod -x lib/Wiki/Toolkit/Feed/{Atom,RSS}.pm


%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/Wiki*
%{_bindir}/wiki-toolkit-*
%{_mandir}/man1/wiki-toolkit*
%{_mandir}/man3/Wiki*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.87-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.87-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.87-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.87-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.87-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.87-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.87-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.87-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.87-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.87-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.87-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.87-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.87-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 0.87-1
- Update to 0.87

* Sun Dec 27 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.86-1
- Update to 0.86
- Replace calls to %%{__perl} with /usr/bin/perl
- Use %%{make_install} instead of "make pure_install"
- Use %%{make_build} instead of "make"

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.85-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.85-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.85-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.85-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.85-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.85-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.85-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.

