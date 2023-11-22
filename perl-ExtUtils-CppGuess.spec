Name:           perl-ExtUtils-CppGuess
Version:        0.27
Release:        1%{?dist}
Summary:        Guess C++ compiler and flags
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ExtUtils-CppGuess
Source:         https://cpan.metacpan.org/modules/by-module/ExtUtils/ExtUtils-CppGuess-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.35
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(blib)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.280231
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(XSLoader)
# Dependencies
Requires:       perl(ExtUtils::ParseXS) >= 3.35

%description
ExtUtils::CppGuess attempts to guess the system's C++ compiler that is
compatible with the C compiler that your perl was built with.

%prep
%autosetup -p1 -n ExtUtils-CppGuess-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
%make_build test

%files
%doc Changes README
%dir %{perl_vendorlib}/ExtUtils/
%{perl_vendorlib}/ExtUtils/CppGuess.pm
%{_mandir}/man3/ExtUtils::CppGuess.3*

%changelog
* Mon Nov 20 2023 Paul Howarth <paul@city-fan.org> - 0.27-1
- Update to 0.27 (rhbz#2250558)
- Use author-independent source URL
- Use SPDX-format license tag
- Classify buildreqs by usage
- Fix permissions verbosely

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-2
- Perl 5.36 rebuild

* Thu Apr 21 2022 Miro Hrončok <mhroncok@redhat.com> - 0.26-1
- Update to 0.26
- Fixes rhbz#2077427

* Thu Apr 21 2022 Miro Hrončok <mhroncok@redhat.com> - 0.25-1
- Update to 0.25
- Fixes rhbz#2077156

* Tue Apr 19 2022 Miro Hrončok <mhroncok@redhat.com> - 0.24-1
- Update to 0.24
- Fixes rhbz#2076721

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Miro Hrončok <mhroncok@redhat.com> - 0.23-1
- Update to 0.23
- Fixes rhbz#1965763

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-6
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-3
- Perl 5.32 rebuild

* Fri Mar 06 2020 Petr Pisar <ppisar@redhat.com> - 0.21-2
- Build-require blib for tests

* Mon Feb 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-1
- Update to 0.21 (#1794452)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-1
- Update to 0.20 (#1747714)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-2
- Perl 5.30 rebuild

* Tue Apr 02 2019 Miro Hrončok <mhroncok@redhat.com> - 0.19-1
- Update to 0.19 (#1692229)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-4
- Perl 5.28 rebuild

* Mon Mar 05 2018 Petr Pisar <ppisar@redhat.com> - 0.12-3
- Adapt to removing GCC from a build root (bug #1547165)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 23 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-1
- 0.12 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Miro Hrončok <mhroncok@redhat.com> - 0.11-1
- Update to 0.11 (#1261473)
- Update source URL

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-2
- Perl 5.22 rebuild

* Wed Apr 15 2015 Miro Hrončok <mhroncok@redhat.com> - 0.09-1
- New version 0.09 (#1210999)
- Use ExtUtils::MakeMaker
- Sort BRs alphabetically

* Mon Jan 26 2015 Miro Hrončok <mhroncok@redhat.com> - 0.08-1
- New version 0.08 (#1183574)
- Updated download URL

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 0.07-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 04 2012 Miro Hrončok <miro@hroncok.cz> - 0.07-3
- Removed deleting empty dirs
- Added BRs for t/lib/TestUtils.pm

* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 0.07-2
- Removed useless BRs
- Removed perl autofilter

* Mon Oct 01 2012 Miro Hrončok <miro@hroncok.cz> 0.07-1
- Specfile autogenerated by cpanspec 1.78 and revised.
