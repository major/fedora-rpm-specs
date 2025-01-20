Name:           perl-Locale-TextDomain-OO
Version:        1.036
Release:        18%{?dist}
Summary:        Perl object-oriented Interface to Uniforum Message Translation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Locale-TextDomain-OO
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STEFFENW/Locale-TextDomain-OO-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load) >= 0.19
BuildRequires:  perl(Clone)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Locale::MO::File) >= 0.09
BuildRequires:  perl(Locale::PO) >= 0.24
BuildRequires:  perl(Locale::TextDomain::OO::Util::ExtractHeader) >= 3.006
BuildRequires:  perl(Locale::TextDomain::OO::Util::JoinSplitLexiconKeys) >= 2.002
BuildRequires:  perl(Locale::Utils::PlaceholderBabelFish) >= 0.001
BuildRequires:  perl(Locale::Utils::PlaceholderMaketext) >= 1.000
BuildRequires:  perl(Locale::Utils::PlaceholderNamed) >= 1.000
BuildRequires:  perl(Moo) >= 1.003001
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::Singleton)
BuildRequires:  perl(MooX::StrictConstructor)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Path::Tiny) >= 0.052
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tie::Sub) >= 0.09
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(JSON) >= 2.50
BuildRequires:  perl(Test::Differences) >= 0.60
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(utf8)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

Requires:       perl(Class::Load) >= 0.19
Requires:       perl(Locale::MO::File) >= 0.09
Requires:       perl(Locale::PO) >= 0.24
Requires:       perl(Locale::TextDomain::OO::Util::ExtractHeader) >= 3.006
Requires:       perl(Locale::TextDomain::OO::Util::JoinSplitLexiconKeys) >= 2.002
Requires:       perl(Locale::Utils::PlaceholderBabelFish) >= 0.001
Requires:       perl(Locale::Utils::PlaceholderMaketext) >= 1.000
Requires:       perl(Locale::Utils::PlaceholderNamed) >= 1.000
Requires:       perl(Moo) >= 1.003001
Requires:       perl(MooX::Singleton)
Requires:       perl(Path::Tiny) >= 0.052
Requires:       perl(Tie::Sub) >= 0.09


%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Locale::(MO::File|PO)\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Locale::TextDomain::OO::Util::(ExtractHeader|JoinSplitLexiconKeys)\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Locale::Utils::Placeholder(BabelFish|Maketext|Named)\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\((Class::Load|Path::Tiny|Tie::Sub)\\)\\s*$
%global __requires_exclude_from .*%{_docdir}
%global __provides_exclude_from .*%{_docdir}

%description
These modules provide a high-level interface to Perl message translation.

%prep
%setup -q -n Locale-TextDomain-OO-%{version}
for i in `find javascript -type f` README Changes; do
    sed -i -e 's/\r//' $i
done
for i in `find example -type f` ; do
    sed -i -e 's/\r//' $i
    sed -i -e '1s|#!.*perl|%(perl -MConfig -e 'print $Config{startperl}')|' $i
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes example javascript  README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.036-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.036-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.036-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.036-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.036-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.036-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.036-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.036-11
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.036-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.036-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.036-8
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.036-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.036-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.036-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.036-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.036-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.036-2
- Perl 5.30 rebuild

* Mon Mar 18 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.036-1
- 1.036 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.035-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.035-1
- 1.035 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.033-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.033-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.033-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.033-1
- 1.033 bump

* Thu Sep 28 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.031-1
- 1.031 bump

* Wed Aug 30 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.030-1
- 1.030 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.029-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.029-1
- 1.029 bump

* Thu Jun 29 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.028-1
- Initial release
