Name:           perl-String-Copyright
Version:        0.003014
Release:        8%{?dist}
Summary:        Representation of text-based copyright statements
License:        GPL-3.0-or-later

URL:            https://metacpan.org/release/String-Copyright
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONASS/String-Copyright-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Number::Range)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(Set::IntSpan)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)


%description
String::Copyright Parses common styles of copyright statements and serializes
in normalized format.


%prep
%autosetup -n String-Copyright-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
make test


%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/String::Copyright*.*


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.003014-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.003014-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.003014-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.003014-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.003014-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.003014-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.003014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 17 2022 Sandro Mani <manisandro@gmail.com> - 0.003014-1
- Update to 0.003014

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.003013-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.003013-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.003013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Sandro Mani <manisandro@gmail.com> - 0.003013-1
- Update to 0.003013

* Thu Dec 16 2021 Sandro Mani <manisandro@gmail.com> - 0.003012-1
- Update to 0.003012

* Tue Sep 07 2021 Sandro Mani <manisandro@gmail.com> - 0.003011-1
- Update to 0.003011

* Sat Aug 28 2021 Sandro Mani <manisandro@gmail.com> - 0.003010-1
- Update to 0.003010

* Thu Aug 19 2021 Sandro Mani <manisandro@gmail.com> - 0.003008-1
- Update to 0.003008

* Mon Aug 16 2021 Sandro Mani <manisandro@gmail.com> - 0.003007-1
- Update to 0.003007

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.003006-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.003006-9
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.003006-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.003006-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.003006-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.003006-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.003006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.003006-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.003006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 28 2018 Sandro Mani <manisandro@gmail.com> - 0.003006-1
- Update to 0.003006

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.003005-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.003005-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.003005-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.003005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.003005-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.003005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 01 2016 Sandro Mani <manisandro@gmail.com> - 0.003005-1
- Update to 0.003005

* Wed Sep 28 2016 Sandro Mani <manisandro@gmail.com> - 0.003004-1
- Update to 0.003004

* Fri Sep 09 2016 Sandro Mani <manisandro@gmail.com> - 0.003003-1
- Update to 0.003003

* Wed Sep 07 2016 Sandro Mani <manisandro@gmail.com> - 0.003002-1
- Update to 0.003002

* Mon Sep 05 2016 Sandro Mani <manisandro@gmail.com> - 0.003001-1
- Update to 0.003001

* Fri Aug 12 2016 Sandro Mani <manisandro@gmail.com> - 0.002001-2
- Add missing BRs

* Fri Aug 12 2016 Sandro Mani <manisandro@gmail.com> - 0.002001-1
- Initial package
