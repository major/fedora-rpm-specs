# -*- rpm-spec -*-

%define metacpan https://cpan.metacpan.org/authors/id/J/JV/JV
%define FullName File-LoadLines

Name: perl-%{FullName}
Summary: Loads the contents of a text file into an array of lines
License: GPL+ or Artistic
Version: 1.021
Release: 4%{?dist}
Source: %{metacpan}/%{FullName}-%{version}.tar.gz
Url: https://metacpan.org/release/%{FullName}

# It's all plain perl, nothing architecture dependent.
BuildArch: noarch

Requires: perl(:VERSION) >= 5.10.1
Requires: perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

BuildRequires: make
BuildRequires: perl(Carp)
BuildRequires: perl(Encode)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(base)
BuildRequires: perl(strict)
BuildRequires: perl(utf8)
BuildRequires: perl(warnings)
BuildRequires: perl-generators
BuildRequires: perl-interpreter

%description
File-LoadLines provides an easy way to load the contents of a text
file into an array of lines.

It automatically handles ASCII, Latin and UTF-8 text.
When the file has a BOM, it handles UTF-8, UTF-16 LE and BE, and
UTF-32 LE and BE.

Recognized line terminators are NL (Unix, Linux), CRLF (DOS, Windows)
and CR (Mac).

%prep
%setup -q -n %{FullName}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%check
make test VERBOSE=1

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.021-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.021-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.021-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 16 2021 Johan Vromans <jvromans@squirrel.nl> - 1.021-1
- Upgrade to new upstream version.

* Mon Aug 16 2021 Johan Vromans <jvromans@squirrel.nl> - 1.02-1
- Upgrade to new upstream version.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.020.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.020.2-2
- Perl 5.34 rebuild

* Thu May 13 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.020.2
- 1.020.2 bump

* Thu Jan 14 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-1
- 1.01 bump

* Fri Dec 04 2020 Johan Vromans <jvromans@squirrel.nl> - 1.00-1
- Upgrade to new upstream version.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-5
- Perl 5.32 rebuild

* Fri Feb 28 2020 Johan Vromans <jvromans@squirrel.nl> - 0.02-4
- Incorporate reviewer feedback.
* Wed Feb 26 2020 Johan Vromans <jvromans@squirrel.nl> - 0.02-3
- Incorporate reviewer feedback.
* Tue Feb 25 2020 Johan Vromans <jvromans@squirrel.nl> - 0.02-2
- Incorporate reviewer feedback.
* Sun Feb 02 2020 Johan Vromans <jvromans@squirrel.nl> - 0.02-1
- Initial Fedora package.
