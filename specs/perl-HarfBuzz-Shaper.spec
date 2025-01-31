# -*- rpm-spec -*-

%define metacpan https://cpan.metacpan.org/authors/id/J/JV/JV
%define FullName HarfBuzz-Shaper

Name: perl-%{FullName}
Summary: Access to a small subset of the native HarfBuzz library
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License: GPL-1.0-or-later OR Artistic-1.0-Perl
Version: 0.028
Release: 1%{?dist}
Source: %{metacpan}/%{FullName}-%{version}.tar.gz
Url: https://metacpan.org/release/%{FullName}


BuildRequires: coreutils findutils gcc make perl-devel
BuildRequires: harfbuzz-devel >= 1.7.7
BuildRequires: make
BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(Devel::CheckLib)
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(Test::More)
BuildRequires: perl(XSLoader)
BuildRequires: perl(charnames)
BuildRequires: perl(lib)
BuildRequires: perl(strict)
BuildRequires: perl(utf8)
BuildRequires: perl(warnings)
BuildRequires: perl-generators
BuildRequires: perl-interpreter

%description
HarfBuzz::Shaper is a perl module that provides access to a small
subset of the native HarfBuzz library.

The subset is suitable for typesetting programs that need to deal with
complex languages like Devanagari.

This module is intended to be used with module L<Text::Layout>.

%prep
%setup -q -n %{FullName}-%{version}

# Make sure the included sources for harfbuzz are not used.
rm -fr ./hb_src
# Same for Devel::CheckLib.
rm -fr ./inc
# And adjust the MANIFEST.
perl -i -ne 'print $_ unless m{^(hb_src|inc)/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test VERBOSE=1

%files
%doc Changes README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/HarfBuzz/Shaper.pm
%{_mandir}/man3/*

%changelog
* Wed Jan 29 2025 Johan Vromans <jvromans@squirrel.nl> - 0.028-1
- Upgrade to new upstream version.

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.026-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.026-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.026-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.026-10
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.026-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.026-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.026-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.026-6
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.026-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.026-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.026-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.026-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Johan Vromans <jvromans@squirrel.nl> - 0.026-1
- Upgrade to new upstream version.

* Fri Dec 24 2021 Johan Vromans <jvromans@squirrel.nl> - 0.025-1
- Upgrade to new upstream version.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.024-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.024-2
- Perl 5.34 rebuild

* Mon Apr 19 2021 Johan Vromans <jvromans@squirrel.nl> - 0.024-1
- Upgrade to new upstream version.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.023-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.023-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Johan Vromans <jvromans@squirrel.nl> - 0.023-7
- Upgrade to new upstream version.

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.022-6
- Perl 5.32 rebuild

* Fri Jun 05 2020 Johan Vromans <jvromans@squirrel.nl> - 0.022-5
- Upgrade to new upstream version.

* Tue Mar 03 2020 Johan Vromans <jvromans@squirrel.nl> - 0.021-4
- Upgrade to new upstream version.

* Wed Feb 26 2020 Johan Vromans <jvromans@squirrel.nl> - 0.018.4-3
- Incorporate reviewer feedback.

* Tue Feb 25 2020 Johan Vromans <jvromans@squirrel.nl> - 0.018.4-2
- Incorporate reviewer feedback.

* Sun Feb 02 2020 Johan Vromans <jvromans@squirrel.nl> - 0.018.4-1
- Initial Fedora package.
