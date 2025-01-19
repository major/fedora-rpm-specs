Name:           perl-Excel-Writer-XLSX
Version:        1.14
Release:        2%{?dist}
Summary:        Create a new file in the Excel 2007+ XLSX format
# LICENSE_Artistic_Perl:    Artistic-1.0-Perl text
# LICENSE_GPL_1.0:          GPL-1.0 text
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Excel-Writer-XLSX
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMCNAMARA/Excel-Writer-XLSX-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.2
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Archive::Zip) >= 1.3
BuildRequires:  perl(autouse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp) >= 0.19
# Getopt::Long not used at tests
BuildRequires:  perl(IO::File) >= 1.14
BuildRequires:  perl(List::Util)
# Pod::Usage not used at tests
BuildRequires:  perl(utf8)
# Optinal run-time:
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(Date::Manip)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
# Test::Differences not helpful, a fallback exists
Requires:       perl(Archive::Zip) >= 1.3
Recommends:     perl(Date::Calc)
Recommends:     perl(Date::Manip)
Requires:       perl(File::Temp) >= 0.19
Requires:       perl(IO::File) >= 1.14

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Archive::Zip\\)$
%global __requires_exclude %__requires_exclude|^perl\\(File::Temp\\)$
%global __requires_exclude %__requires_exclude|^perl\\(IO::File\\)$
# Remove private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(TestFunctions\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(TestFunctions\\)

%description
The Excel::Writer::XLSX Perl module can be used to create an Excel file in the
2007+ XLSX format. Multiple worksheets can be added to a workbook and
formatting can be applied to cells. Text, numbers, and formulas can be written
to the cells.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Date::Calc)
Requires:       perl(Date::Manip)
Requires:       perl(utf8)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Excel-Writer-XLSX-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
# Regenerate lib/Excel/Writer/XLSX/Examples.pm
%{make_build} mydocs
%{make_build} all

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Many tests, e.g. t/regression/chart_axis25.t, create files under CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE_Artistic_Perl LICENSE_GPL_1.0
# ./examples is compiled and packaged as Excel::Writer::XLSX::Examples
%doc Changes CONTRIBUTING.md README
%dir %{perl_vendorlib}/Excel
%dir %{perl_vendorlib}/Excel/Writer
%{perl_vendorlib}/Excel/Writer/XLSX
%{perl_vendorlib}/Excel/Writer/XLSX.pm
%{_mandir}/man3/Excel::Writer::XLSX.*
%{_mandir}/man3/Excel::Writer::XLSX::*
%{_mandir}/man1/extract_vba.*
%{_bindir}/extract_vba

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 22 2024 Petr Pisar <ppisar@redhat.com> - 1.14-1
- 1.14 bump

* Fri Oct 18 2024 Petr Pisar <ppisar@redhat.com> - 1.13-1
- 1.13 bump

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Petr Pisar <ppisar@redhat.com> - 1.12-1
- 1.12 bump

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 27 2023 Petr Pisar <ppisar@redhat.com> - 1.11-2
- Package a license grant for Excel::Writer::XLSX

* Wed Apr 26 2023 Petr Pisar <ppisar@redhat.com> - 1.11-1
- 1.11 bump
- Package the tests

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-2
- Perl 5.36 rebuild

* Fri Apr 29 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-1
- 1.09 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-1
- 1.07 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-1
- 1.03 bump

* Fri Nov 15 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-1
- 1.02 bump

* Wed Oct 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-1
- 1.01 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-2
- Perl 5.30 rebuild

* Mon Apr 08 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.00
- 1.00 bump

* Thu Feb 28 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.99-1
- 0.99 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.98-2
- Perl 5.28 rebuild

* Fri Apr 20 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.98-1
- 0.98 bump

* Fri Apr 13 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.97-1
- 0.97 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 18 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.96-1
- 0.96 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.95-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.95-1
- 0.95 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.88-2
- Perl 5.24 rebuild

* Tue Mar 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.88-1
- 0.88 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.86-1
- 0.86 bump

* Mon Oct 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.85-1
- 0.85 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.84-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.84-2
- Perl 5.22 rebuild

* Tue Apr 28 2015 David Dick <ddick@cpan.org> - 0.84-1
- Update to 0.84

* Thu Mar 19 2015 David Dick <ddick@cpan.org> - 0.83-1
- Update to 0.83

* Sat Nov 08 2014 David Dick <ddick@cpan.org> - 0.81-1
- Update to 0.81

* Sat Oct 18 2014 David Dick <ddick@cpan.org> - 0.79-1
- Update to 0.79

* Tue Sep 30 2014 David Dick <ddick@cpan.org> - 0.78-1
- Update to 0.78

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.77-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 David Dick <ddick@cpan.org> - 0.77-1
- Update to 0.77

* Sat Feb 01 2014 David Dick <ddick@cpan.org> - 0.76-1
- Initial release
