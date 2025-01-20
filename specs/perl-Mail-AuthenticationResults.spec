Name:           perl-Mail-AuthenticationResults
Version:        2.20231031
Release:        5%{?dist}
Summary:        Object Oriented Authentication-Results Headers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-AuthenticationResults/
Source0:        https://cpan.metacpan.org/modules/by-module/Mail/Mail-AuthenticationResults-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl >= 0:5.008
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)


%description
Object Oriented Authentication-Results email headers.


%prep
%setup -q -n Mail-AuthenticationResults-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*


%check
%make_build test


%files
%license LICENSE
%doc Changes dist.ini README README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.20231031-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.20231031-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.20231031-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.20231031-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 01 2023 Xavier Bachelot <xavier@bachelot.org> 2.20231031-1
- Update to 2.20231031 (RHBZ#2247355)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.20230112-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 07 2023 Michal Josef Špaček <mspacek@redhat.com> - 2.20230112-2
- Update license to SPDX format

* Tue Mar 07 2023 Xavier Bachelot <xavier@bachelot.org> 2.20230112-1
- Update to 2.20230112 (RHBZ#2160586)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.20210915-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.20210915-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.20210915-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.20210915-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 14 2021 Xavier Bachelot <xavier@bachelot.org> 2.20210915
- Update to 2.20210915 (RHBZ#2003898)

* Tue Sep 14 2021 Xavier Bachelot <xavier@bachelot.org> 2.20210914
- Update to 2.20210914 (RHBZ#2003898)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.20210112-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.20210112-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.20210112-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Xavier Bachelot <xavier@bachelot.org> 2.20210112
- Update to 2.20210112 (RHBZ#1915573)

* Tue Aug 25 2020 Xavier Bachelot <xavier@bachelot.org> 1.20200824.1
- Update to 1.20200824.1 (RHBZ#1871904)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20200331.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.20200331.1-2
- Perl 5.32 rebuild

* Mon Apr 20 2020 Xavier Bachelot <xavier@bachelot.org> 1.20200331.1
- Update to 1.20200331.1 (RHBZ#1825822)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20200108-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Xavier Bachelot <xavier@bachelot.org> 1.20200108-1
- Update to 1.20200108 (RHBZ#1789387).

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20180923-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.20180923-3
- Perl 5.30 rebuild

* Mon Apr 15 2019 Xavier Bachelot <xavier@bachelot.org> 1.20180923-2
- Review fixes.

* Thu Apr 11 2019 Xavier Bachelot <xavier@bachelot.org> 1.20180923-1
- Initial package.
