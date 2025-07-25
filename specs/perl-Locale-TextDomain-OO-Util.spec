# Provide Locale::TextDomain::OO implementation in JavaScript
%bcond_without perl_Locale_TextDomain_OO_Util_enables_javascript

Name:           perl-Locale-TextDomain-OO-Util
Version:        4.002
Release:        19%{?dist}
Summary:        Lexical Utils for Locale::TextDomain::OO
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Locale-TextDomain-OO-Util
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STEFFENW/Locale-TextDomain-OO-Util-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(charnames)
BuildRequires:  perl(English)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Test::Differences) >= 0.60
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

%description
This module provides methods for lexicon constants, to join and split
lexicon keys and to extract the gettext file header.

%if %{with perl_Locale_TextDomain_OO_Util_enables_javascript}
%package -n js-Locale-TextDomain-OO-Util
Summary:        Lexical Utils for Locale::TextDomain::OO in JavaScript
BuildRequires:  web-assets-devel
Requires:       js-jquery
Requires:       web-assets-filesystem

%description -n js-Locale-TextDomain-OO-Util
This package contains the Locale::TextDomain::OO utils as JavaScript.
%endif

%prep
%setup -q -n Locale-TextDomain-OO-Util-%{version}
sed -i -e 's/\r//' README Changes example/*
sed -i -e '1s|#!.*perl|%(perl -MConfig -e 'print $Config{startperl}')|' example/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%if %{with perl_Locale_TextDomain_OO_Util_enables_javascript}
mkdir -p $RPM_BUILD_ROOT%{_jsdir}/js-Locale-TextDomain-OO-Util
cp -pr javascript/* $RPM_BUILD_ROOT%{_jsdir}/js-Locale-TextDomain-OO-Util
%endif

%check
make test

%files
%doc Changes example README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%exclude %{perl_vendorlib}/Locale/TextDomain/OO/Util/JavaScript.pm
%exclude %{_mandir}/man3/Locale::TextDomain::OO::Util::JavaScript.3*


%if %{with perl_Locale_TextDomain_OO_Util_enables_javascript}
%files -n js-Locale-TextDomain-OO-Util
%{perl_vendorlib}/Locale/TextDomain/OO/Util/JavaScript.pm
%{_mandir}/man3/Locale::TextDomain::OO::Util::JavaScript.3*
%{_jsdir}/js-Locale-TextDomain-OO-Util
%endif

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.002-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.002-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.002-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.002-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.002-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.002-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.002-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.002-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.002-11
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.002-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.002-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.002-8
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.002-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.002-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.002-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.002-2
- Perl 5.30 rebuild

* Mon Mar 18 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.002-1
- 4.002 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.001-2
- Perl 5.28 rebuild

* Tue Jun 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.001-1
- 4.001 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.008-1
- 3.008 bump

* Mon Jul 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.007-1
- 3.007 bump

* Mon Jul 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.006-1
- Initial release
