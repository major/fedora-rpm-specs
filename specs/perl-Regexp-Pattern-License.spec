Name:           perl-Regexp-Pattern-License
Version:        3.11.2
Release:        2%{?dist}
Summary:        Regular expressions for legal licenses
License:        GPL-3.0-or-later

BuildArch:      noarch
URL:            https://metacpan.org/release/Regexp-Pattern-License
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONASS/Regexp-Pattern-License-v%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(open)
BuildRequires:  perl(Regexp::Pattern)
BuildRequires:  perl(re::engine::RE2)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Regexp::Pattern)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)


%description
Regexp::Pattern::License provides a hash of regular expression patterns related
to legal software licenses.


%prep
%autosetup -p1 -n Regexp-Pattern-License-v%{version}


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
%{_mandir}/man3/Regexp::Pattern::License*.*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 22 2024 Sandro Mani <manisandro@gmail.com> - 3.11.2-1
- Update to 3.11.2

* Thu Aug 15 2024 Sandro Mani <manisandro@gmail.com> - 3.11.1-6
- Add only-import-reenginere2-when-available.patch

* Thu Aug 15 2024 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 3.11.1-5
- Rebuild for re2-2024-07-02

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 09 2023 Sandro Mani <manisandro@gmail.com> - 3.11.1-1
- Update to 3.11.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Sandro Mani <manisandro@gmail.com> - 3.11.0-1
- Update to 3.11.0

* Mon Apr 03 2023 Sandro Mani <manisandro@gmail.com> - 3.10.1-1
- Update to 3.10.1

* Thu Jan 19 2023 Sandro Mani <manisandro@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.9.4-2
- Perl 5.36 rebuild

* Mon Feb 14 2022 Sandro Mani <manisandro@gmail.com> - 3.9.4-1
- Update to 3.9.4

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 19 2021 Sandro Mani <manisandro@gmail.com> - 3.9.3-1
- Update to 3.9.3

* Sun Aug 15 2021 Sandro Mani <manisandro@gmail.com> - 3.9.0-1
- Update to 3.9.0

* Sat Aug 07 2021 Sandro Mani <manisandro@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Wed Jul 28 2021 Sandro Mani <manisandro@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Sat Jul 24 2021 Sandro Mani <manisandro@gmail.com> - 3.7.1-1
- Update to 3.7.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Sandro Mani <manisandro@gmail.com> - 3.5.1-1
- Update to 3.5.1

* Tue Jun 22 2021 Sandro Mani <manisandro@gmail.com> - 3.5.0-1
- Update to 3.5.0

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.0-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.0-2
- Perl 5.32 rebuild

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Mon May 18 2020 Sandro Mani <manisandro@gmail.com> - 3.3.1-1
- Update to 3.3.1

* Mon Apr 06 2020 Sandro Mani <manisandro@gmail.com> - 3.3.0-1
- Update to 3.3.0

* Sun Feb 23 2020 Sandro Mani <manisandro@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Mon Feb 10 2020 Sandro Mani <manisandro@gmail.com> - 3.1.102-1
- Update to 3.1.102

* Fri Jan 31 2020 Sandro Mani <manisandro@gmail.com> - 3.1.101-1
- Update to 3.1.101

* Tue Jan 28 2020 Sandro Mani <manisandro@gmail.com> - 3.1.100-1
- Update to 3.1.100

* Mon Jan 13 2020 Sandro Mani <manisandro@gmail.com> - 3.1.99-1
- Update to 3.1.99

* Fri Jan 03 2020 Sandro Mani <manisandro@gmail.com> - 3.1.95-1
- Update to 3.1.95

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Sandro Mani <manisandro@gmail.com> - 3.1.94-1
- Update to 3.1.94

* Sun Jun 09 2019 Sandro Mani <manisandro@gmail.com> - 3.1.93-1
- Update to 3.1.93

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.1.92-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.1.92-2
- Perl 5.28 rebuild

* Fri Apr 06 2018 Sandro Mani <manisandro@gmail.com> - 3.1.92-1
- Update to 3.1.92

* Thu Apr 05 2018 Sandro Mani <manisandro@gmail.com> - 3.1.91-1
- Update to 3.1.91

* Sat Feb 10 2018 Sandro Mani <manisandro@gmail.com> - 3.1.0-1
- Update to 3.1.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 18 2017 Sandro Mani <manisandro@gmail.com> - 3.0.31-1
- Initial package
