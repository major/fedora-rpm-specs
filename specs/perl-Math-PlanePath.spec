Name:           perl-Math-PlanePath
Version:        129
Release:        14%{?dist}
Summary:        Mathematical paths through the 2-D plane
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://user42.tuxfamily.org/math-planepath/index.html
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Math-PlanePath-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.4
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant) >= 1.02
BuildRequires:  perl(constant::defer) >= 5
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::BigRat)
BuildRequires:  perl(Math::Factor::XS)
BuildRequires:  perl(Math::Libm)
BuildRequires:  perl(Math::NumSeq)
BuildRequires:  perl(Math::NumSeq::Base::IterateIth)
BuildRequires:  perl(Math::NumSeq::Modulo)
BuildRequires:  perl(Math::NumSeq::OEIS::Catalogue::Plugin)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(vars)
# Tests only:
BuildRequires:  perl(lib)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(Number::Fraction) >= 1.14
BuildRequires:  perl(Test)
# Optional tests only:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Float)
# Devel::FindRef not yet packaged
BuildRequires:  perl(Devel::StackTrace)
# Math::BigInt::Lite not yet packaged
Requires:       perl(constant::defer) >= 5
Requires:       perl(File::Spec)
Requires:       perl(Math::BigFloat)
Requires:       perl(Math::BigInt)
Requires:       perl(Math::BigRat)
Requires:       perl(Math::Factor::XS)
Requires:       perl(Math::NumSeq::Modulo)
Requires:       perl(Module::Load)
Requires:       perl(Scalar::Util)

# Filtering unversioned provides and requires
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Math::PlanePath::CellularRule::Line\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Math::PlanePath::CellularRule::OddSolid\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Math::PlanePath::CellularRule::OneTwo\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Math::PlanePath::CellularRule::Two\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(constant\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(constant::defer\\)$

%description
This spot of Perl code calculates various mathematical paths through a 2-D X,Y
plane. There's no drawing in Math-PlanePath, just coordinate calculations.

%prep
%setup -q -n Math-PlanePath-%{version}
find examples -type f -exec chmod 0644 -c {} +

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license COPYING
%doc Changes examples debian/copyright
%{perl_vendorlib}/Math*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 129-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 129-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 129-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 129-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 129-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 129-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 129-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 129-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 129-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 129-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 129-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 129-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 129-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Petr Pisar <ppisar@redhat.com> - 129-1
- 129 bump

* Tue Jan 12 2021 Jitka Plesnikova <jplesnik@redhat.com> - 128-2
- Fix failing test

* Mon Oct 05 2020 Jitka Plesnikova <jplesnik@redhat.com> - 128-1
- 128 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 127-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 127-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 127-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 127-1
- 127 bump (#1742906)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 126-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 126-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 126-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 126-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 126-2
- Perl 5.28 rebuild

* Mon Mar 05 2018 Miro Hrončok <mhroncok@redhat.com> - 126-1
- 126 bump (#1551284)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 125-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Jitka Plesnikova <jplesnik@redhat.com> - 125-1
- 125 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 124-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 124-2
- Perl 5.26 rebuild

* Tue Feb 21 2017 Miro Hrončok <mhroncok@redhat.com> - 124-1
- 124 bump (#1421453)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 123-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 123-2
- Perl 5.24 rebuild

* Tue May 03 2016 Jitka Plesnikova <jplesnik@redhat.com> - 123-1
- 123 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 122-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Petr Šabata <contyk@redhat.com> - 122-1
- 122 bump
- Packaging the provided examples
- Packaging the license text with %%license
- Fixes a FTBFS issue (#1296524)
- SPEC cleanup and modernization

* Thu Nov 19 2015 Miro Hrončok <mhroncok@redhat.com> - 121-1
- rebuilt

* Fri Oct 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 120-1
- 120 bump

* Thu Jun 25 2015 Jitka Plesnikova <jplesnik@redhat.com> - 119-1
- 119 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 118-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 118-2
- Perl 5.22 rebuild

* Thu Mar 05 2015 Miro Hrončok <mhroncok@redhat.com> - 118-1
- New version 118 (#1197534)

* Fri Sep 26 2014 Miro Hrončok <mhroncok@redhat.com> - 117-1
- New version 117 (#1145017)
- Add BR perl(Data::Float)

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 116-2
- Perl 5.20 rebuild

* Mon Jun 23 2014 Miro Hrončok <mhroncok@redhat.com> - 116-1
- New version 116 (#1111864)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 115-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Miro Hrončok <mhroncok@redhat.com> - 115-1
- New version 115 (#1087329)

* Fri Feb 14 2014 Miro Hrončok <mhroncok@redhat.com> - 114-2
- Add BR Math::NumSeq for tests

* Fri Feb 14 2014 Miro Hrončok <mhroncok@redhat.com> - 114-1
- New version 114 (#1063019)
- More unversioned provides to filter

* Fri Dec 27 2013 Miro Hrončok <mhroncok@redhat.com> - 113-1
- New version 113 (#1046669)

* Wed Dec 11 2013 Miro Hrončok <mhroncok@redhat.com> - 112-1
- New version 112 (#1039713)

* Tue Nov 26 2013 Miro Hrončok <mhroncok@redhat.com> - 111-1
- New version 111 (#1030912)

* Mon Sep 02 2013 Miro Hrončok <mhroncok@redhat.com> - 110-1
- New upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 105-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 105-2
- Perl 5.18 rebuild

* Mon Jun 24 2013 Miro Hrončok <mhroncok@redhat.com> - 105-1
- New upstream release

* Sat Feb 09 2013 Miro Hrončok <mhroncok@redhat.com> - 98-2
- Using original homepage for URL
- Updated summary and description to suit whole package
- Packaged debian/copyright as documentation
- Quallified BR perl(Math::BigFloat) with >= 1.993
- Build-required perl(constant) >= 1.02
                 perl(Test)
                 perl(Scalar::Util)
                 perl(Carp)
                 perl(File::Spec)
                 perl(Exporter)
                 perl(lib)
- Run-required   perl(Math::Factor::XS)
                 perl(Math::NumSeq::Modulo)
                 perl(Module::Load)
- Removed BR     perl(Math::BigRat)
                 perl >= 0:5.004

* Sat Feb 02 2013 Miro Hrončok <mhroncok@redhat.com> - 98-1
- New release
- Removed perl default filter
- %%{__perl} -> perl
- Replaced obsoleted PERL_INSTALL_ROOT with DESTDIR
- Removed deleting empty dirs
- Replaced BRs with BRs from Michal Ingeli <mi@v3.sk>
- Filter unversioned deps and provides

* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 90-2
- Removed BRs provided by perl package

* Tue Oct 09 2012 Miro Hrončok <miro@hroncok.cz> 90-1
- New release

* Sun Sep 23 2012 Miro Hrončok <miro@hroncok.cz> 88-1
- Specfile autogenerated by cpanspec 1.78 and revised.
