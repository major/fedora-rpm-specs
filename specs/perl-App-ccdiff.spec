Name:           perl-App-ccdiff
Version:        0.34
Release:        1%{?dist}
Summary:        Colored Character diff

License:        Artistic-2.0
URL:            https://metacpan.org/release/App-ccdiff
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/App-ccdiff-%{version}.tgz

BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators

BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  make

BuildRequires:  perl(warnings)
BuildRequires:  perl(charnames)
BuildRequires:  perl(Algorithm::Diff::XS)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Getopt::Long)

BuildRequires:  perl(Test::More)
BuildRequires:  perl(Capture::Tiny)


Requires:       perl(Algorithm::Diff)
Recommends:     perl(Algorithm::Diff::XS)

# For pod2man / nroff
Requires:       perl-podlators
Requires:       groff-base

# For pod2usage
Requires:       perl(Pod::Usage)

%{?perl_default_filter}

%description
All command-line tools that show the difference between two files fall
short in showing minor changes visuably useful. This tool tries to give
the look and feel of `diff --color` or `colordiff`, but extending the
display of colored output from red for deleted lines and green for added
lines to red for deleted characters and green for added characters within
the changed lines.


%prep
%setup -q -n App-ccdiff-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build


%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*


%check
make test


%files
%license LICENSE
%doc ChangeLog CONTRIBUTING.md README.md
%{_bindir}/ccdiff
%{perl_vendorlib}/*
%{_mandir}/man1/ccdiff.1*
%{_mandir}/man3/App::ccdiff.3*


%changelog
* Fri Jan 03 2025 Richard Fearn <richardfearn@gmail.com> - 0.34-1
- Update to 0.34 (#2335268)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Nov 18 2023 Richard Fearn <richardfearn@gmail.com> - 0.33-2
- Add dependencies on Algorithm::Diff / Algorithm::Diff::XS

* Sun Nov 12 2023 Richard Fearn <richardfearn@gmail.com> - 0.33-1
- Update to 0.33 (#2248548)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Richard Fearn <richardfearn@gmail.com> - 0.32-3
- Don't glob everything under shared directories in %%files

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 08 2023 Richard Fearn <richardfearn@gmail.com> - 0.32-1
- Update to 0.32 (#2158460)

* Tue Dec 27 2022 Richard Fearn <richardfearn@gmail.com> - 0.31-5
- Use SPDX license identifier

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-3
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 01 2022 Richard Fearn <richardfearn@gmail.com> 0.31-1
- Update to new version 0.31 (#2036424)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-3
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Richard Fearn <richardfearn@gmail.com> 0.30-1
- Update to new version 0.30 (#1910350)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 04 2019 Richard Fearn <richardfearn@gmail.com> 0.28-1
- Update to new version 0.28 (#1748007)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Richard Fearn <richardfearn@gmail.com> 0.26-5
- Add version constraint to ExtUtils::MakeMaker dependency (due to use of
  NO_PACKLIST)

* Mon Jan 07 2019 Richard Fearn <richardfearn@gmail.com> 0.26-4
- Don't explicitly delete empty directories - it is done automatically

* Mon Jan 07 2019 Richard Fearn <richardfearn@gmail.com> 0.26-3
- Don't create .packlist files at build time

* Mon Jan 07 2019 Richard Fearn <richardfearn@gmail.com> 0.26-2
- Add missing BuildRequires and Requires

* Sat Jan 05 2019 Richard Fearn <richardfearn@gmail.com> 0.26-1
- Initial version for Fedora
