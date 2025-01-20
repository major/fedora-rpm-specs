# -*- rpm-spec -*-

%define metacpan https://cpan.metacpan.org/authors/id/J/JV/JV
%define FullName Text-Layout

Name: perl-%{FullName}
Summary: Pango style text formatting
License: (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Artistic-2.0
Version: 0.038
Release: 2%{?dist}
Source: %{metacpan}/%{FullName}-%{version}.tar.gz
Url: https://metacpan.org/release/%{FullName}

# It's all plain perl, nothing architecture dependent.
BuildArch: noarch

# This package would provide many (perl) modules, but these are
# not intended for general use.
%global __requires_exclude Text::Layout::Font(Config|Descriptor)
%global __provides_exclude_from /(Testing|Cairo|Pango|PDFAPI2|ImageElement|ElementRole)\\.pm$

Requires: perl(:VERSION) >= 5.26.0

Recommends: perl(PDF::API2) >= 2.036
Recommends: perl(HarfBuzz::Shaper) >= 0.026

BuildRequires: make
BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker) >= 7.24
BuildRequires: perl(Object::Pad) >= 0.78
BuildRequires: perl(File::Basename)
BuildRequires: perl(HarfBuzz::Shaper) >= 0.026
BuildRequires: perl(PDF::API2) >= 2.036
BuildRequires: perl(Test::More)
BuildRequires: perl(constant)
BuildRequires: perl(overload)
BuildRequires: perl(strict)
BuildRequires: perl(utf8)
BuildRequires: perl(warnings)
BuildRequires: perl-generators
BuildRequires: perl-interpreter

%description
Text::Layout provides methods for Pango style text formatting. Where
possible the methods have identical names and (near) identical
behavior as their Pango counterparts.

See https://developer.gnome.org/pango/stable/pango-Layout-Objects.html.

Text::Layout uses backend modules to render the marked up text.
Backends are included for PDF::API2 and PDF::Builder.

The package uses Text::Layout::FontConfig (included) to organize fonts
by description.

If module HarfBuzz::Shaper is installed, Text::Layout can use it for
text shaping.

%prep
%setup -q -n %{FullName}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%check
make test

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.038-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 27 2024 Johan Vromans <jvromans@squirrel.nl> - 0.038-1
- Upgrade to upstream.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.032-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.032-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.032-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov  1 2023 Johan Vromans <jvromans@squirrel.nl> - 0.032-1
- Upgrade to upstream 0.032.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.031-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 29 2023 Johan Vromans <jvromans@squirrel.nl> - 0.031-1
- Upgrade to upstream 0.031.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.030-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 08 2022 Johan Vromans <jvromans@squirrel.nl> - 0.030-3
- Fix provides for Text::Layout::Testing.

* Tue Nov 08 2022 Johan Vromans <jvromans@squirrel.nl> - 0.030-2
- Fix provides for Text::Layout::Markdown.

* Sat Sep 03 2022 Johan Vromans <jvromans@squirrel.nl> - 0.030-1
- Upgrade to upstream 0.030.

* Wed Aug 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.029-1
- 0.029 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.028-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.028-2
- Perl 5.36 rebuild

* Fri Feb 04 2022 Johan Vromans <jvromans@squirrel.nl> - 0.028-1
- Upgrade to upstream 0.028.
- Note that there are incompatible changes in this release.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.021-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 21 2021 Johan Vromans <jvromans@squirrel.nl> - 0.021-1
- Upgrade to upstream 0.021.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.019-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.019-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.019-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 16 2020 Johan Vromans <jvromans@squirrel.nl> - 0.019-1
- Upgrade to upstream 0.019.

* Mon Aug 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.018.3-1
- 0.018.3 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.018.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.018.1-4
- Perl 5.32 rebuild

* Thu Feb 27 2020 Johan Vromans <jvromans@squirrel.nl> - 0.018.1-3
- Incorporate reviewer feedback.
- Upgrade to upstream 0.018.1.
* Wed Feb 26 2020 Johan Vromans <jvromans@squirrel.nl> - 0.018-2
- Incorporate reviewer feedback.
* Tue Feb 25 2020 Johan Vromans <jvromans@squirrel.nl> - 0.018-1
- Incorporate reviewer feedback.
- Upgrade to upstream 0.018.
* Sun Feb 02 2020 Johan Vromans <jvromans@squirrel.nl> - 0.016-1
- Initial Fedora package.
