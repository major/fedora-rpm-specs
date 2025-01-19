Name:           licensecheck
Version:        3.3.9
Release:        6%{?dist}
Summary:        Simple license checker for source files

License:        AGPL-3.0-or-later
BuildArch:      noarch
URL:            https://metacpan.org/release/App-Licensecheck
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONASS/App-Licensecheck-v%{version}.tar.gz

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators

BuildRequires:  perl(autodie)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Feature::Compat::Class)
BuildRequires:  perl(Feature::Compat::Try)
BuildRequires:  perl(if)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Log::Any::Test)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::Copyright)
BuildRequires:  perl(String::License)
BuildRequires:  perl(String::License::Naming)
BuildRequires:  perl(String::License::Naming::Custom)
BuildRequires:  perl(String::License::Naming::SPDX)
# BuildRequires:  perl(SVG::Box)
BuildRequires:  perl(Test2::Suite)
BuildRequires:  perl(Test2::Tools::Command)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  make

Requires:       perl(Log::Any::Adapter::Screen)


%description
Licensecheck attempts to determine the license that applies to each file passed
to it, by searching the start of the file for text belonging to various
licenses.


%prep
%autosetup -p1 -n App-Licensecheck-v%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build


%install
make pure_install DESTDIR=%{buildroot}
# Remove .packlist
rm -f %{buildroot}%{perl_vendorarch}/auto/App/Licensecheck/.packlist
# Install bash-completions file
install -Dpm 0644 scripts/licensecheck.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/licensecheck


%check
make test || :


%files
%doc Changes README
%license LICENSE
%{_bindir}/licensecheck
%{_datadir}/bash-completion/
%{perl_vendorlib}/*
%{_mandir}/man1/licensecheck.1*
%{_mandir}/man3/App::Licensecheck.*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 05 2023 Sandro Mani <manisandro@gmail.com> - 3.3.9-1
- Update to 3.3.9

* Sun Jan 29 2023 Sandro Mani <manisandro@gmail.com> - 3.3.8-1
- Update to 3.3.8

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Sandro Mani <manisandro@gmail.com> - 3.3.6-1
- Update to 3.3.6

* Tue Jan 10 2023 Sandro Mani <manisandro@gmail.com> - 3.3.3-1
- Update to 3.3.3

* Sun Jan 08 2023 Sandro Mani <manisandro@gmail.com> - 3.3.2-1
- Update to 3.3.2

* Thu Jan 05 2023 Sandro Mani <manisandro@gmail.com> - 3.3.1-1
- Update to 3.3.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.3.0-3
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Sandro Mani <manisandro@gmail.com> - 3.3.0-1
- Update to 3.3.0

* Tue Nov 23 2021 Sandro Mani <manisandro@gmail.com> - 3.2.14-1
- Update to 3.2.14

* Wed Oct 13 2021 Sandro Mani <manisandro@gmail.com> - 3.2.13-1
- Update to 3.2.13

* Mon Aug 30 2021 Sandro Mani <manisandro@gmail.com> - 3.2.12-1
- Update to 3.2.12

* Thu Aug 19 2021 Sandro Mani <manisandro@gmail.com> - 3.2.11-1
- Update to 3.2.11

* Tue Aug 17 2021 Sandro Mani <manisandro@gmail.com> - 3.2.9-1
- Update to 3.2.9

* Sun Aug 15 2021 Sandro Mani <manisandro@gmail.com> - 3.2.8-1
- Update to 3.2.8

* Mon Aug 09 2021 Sandro Mani <manisandro@gmail.com> - 3.2.6-1
- Update to 3.2.6

* Sat Jul 24 2021 Sandro Mani <manisandro@gmail.com> - 3.2.5-1
- Update to 3.2.5

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Sandro Mani <manisandro@gmail.com> - 3.2.2-1
- Update to 3.2.2

* Tue Jun 22 2021 Sandro Mani <manisandro@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.1.1-5
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.1.1-2
- Perl 5.32 rebuild

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 3.1.1-1
- Update to 3.1.1

* Mon May 18 2020 Sandro Mani <manisandro@gmail.com> - 3.0.47-1
- Update to 3.0.47

* Mon Apr 06 2020 Sandro Mani <manisandro@gmail.com> - 3.0.46-1
- Update to 3.0.46

* Mon Feb 24 2020 Sandro Mani <manisandro@gmail.com> - 3.0.45-1
- Update to 3.0.45
- Add patch to avoid dependency on non-free perl-Array-IntSpan
- Note: this patch results in some deficiencies compared to vanilla upstream
  See https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=951186

* Tue Jan 28 2020 Sandro Mani <manisandro@gmail.com> - 3.0.39-1
- Update to 3.0.39

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Sandro Mani <manisandro@gmail.com> - 3.0.37-1
- Update to 3.0.37

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.0.36-7
- Perl 5.30 rebuild

* Tue Feb 12 2019 Pete Walter <pwalter@fedoraproject.org> - 3.0.36-6
- Obsolete devscripts-compat

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Sandro Mani <manisandro@gmail.com> - 3.0.36-4
- Fix: Use of uninitialized value $3 in concatenation (.) or string (#1595880)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.0.36-2
- Perl 5.28 rebuild

* Fri Apr 06 2018 Sandro Mani <manisandro@gmail.com> - 3.0.36-1
- Update to 3.0.36

* Thu Apr 05 2018 Sandro Mani <manisandro@gmail.com> - 3.0.35-1
- Update to 3.0.35

* Thu Mar 29 2018 Sandro Mani <manisandro@gmail.com> - 3.0.34-1
- Update to 3.0.34

* Fri Feb 16 2018 Sandro Mani <manisandro@gmail.com> - 3.0.33-1
- Update to 3.0.33

* Sat Feb 10 2018 Sandro Mani <manisandro@gmail.com> - 3.0.32-1
- Update to 3.0.32

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 23 2017 Sandro Mani <manisandro@gmail.com> - 3.0.31-2
- Rebuild for perl-Regexp-Pattern-License

* Thu Aug 17 2017 Sandro Mani <manisandro@gmail.com> - 3.0.31-1
- Update to 3.0.31

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 06 2017 Sandro Mani <manisandro@gmail.com> - 3.0.30-1
- Update to 3.0.30

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.0.29-3
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Sandro Mani <manisandro@gmail.com> - 3.0.29-1
- Update to 3.0.29

* Sun Nov 27 2016 Sandro Mani <manisandro@gmail.com> - 3.0.28-1
- Update to 3.0.28

* Thu Nov 24 2016 Sandro Mani <manisandro@gmail.com> - 3.0.27-1
- Update to 3.0.27

* Wed Sep 28 2016 Sandro Mani <manisandro@gmail.com> - 3.0.26-1
- Update to 3.0.26

* Thu Sep 22 2016 Sandro Mani <manisandro@gmail.com> - 3.0.25-1
- Update to 3.0.25

* Fri Sep 09 2016 Sandro Mani <manisandro@gmail.com> - 3.0.24-1
- Update to 3.0.24

* Fri Aug 19 2016 Sandro Mani <manisandro@gmail.com> - 3.0.19-1
- Update to 3.0.19

* Mon Aug 15 2016 Sandro Mani <manisandro@gmail.com> - 3.0.17-1
- Update to 3.0.17

* Fri Jul 22 2016 Sandro Mani <manisandro@gmail.com> - 3.0.7-1
- Update to 3.0.7
- BR: perl-generators
- Use CPAN URL

* Sun Jul 17 2016 Sandro Mani <manisandro@gmail.com> - 3.0.2-1
- Update to 3.0.2

* Mon Jul 04 2016 Sandro Mani <manisandro@gmail.com> - 3.0.1-1
- Initial package
