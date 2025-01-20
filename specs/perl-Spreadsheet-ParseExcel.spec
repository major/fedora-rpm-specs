# Perform optional tests
%bcond_without perl_Spreadsheet_ParseExcel_enables_optional_test

# Perform automated tests
%bcond_without perl_Spreadsheet_ParseExcel_enables_extra_test

# The debuginfo package is empty. Full-arch package because of
# %%{perl_vendorarch}/Unicode/Map/MS/WIN/CP932Excel.map.
%global debug_package %{nil}

Name:           perl-Spreadsheet-ParseExcel
Epoch:          1
Version:        0.66
Release:        4%{?dist}
Summary:        Extract information from an Excel file
# sample/xls2csv.pl:    Artistic-1.0-Perl
#                       TODO: Clarify with an upstream
#                       <https://github.com/jmcnamara/spreadsheet-parseexcel/issues/10>
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Spreadsheet-ParseExcel
Source0:        https://cpan.metacpan.org/modules/by-module/Spreadsheet/Spreadsheet-ParseExcel-%{version}.tar.gz
# Test Test95.xls from t/excel_files. Required to have the tests relocatable
# without a duplicating Test95.xls. In upstream after 0.66,
# <https://github.com/jmcnamara/spreadsheet-parseexcel/pull/11>.
Patch0:         Spreadsheet-ParseExcel-0.66-Test-Test95.xls-from-t-excel_files.patch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Crypt::RC4)
BuildRequires:  perl(Digest::Perl::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(IO::File)
# IO::Scalar not used, we have perl built with PerlIO
BuildRequires:  perl(Jcode)
BuildRequires:  perl(OLE::Storage_Lite) >= 0.19
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Spreadsheet::WriteExcel)
# Text::CSV_XS not used at tests
BuildRequires:  perl(Unicode::Map)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
%if %{with perl_Spreadsheet_ParseExcel_enables_optional_test}
# Optional tests
BuildRequires:  perl(IO::Scalar)
%endif
%if %{with perl_Spreadsheet_ParseExcel_enables_extra_test}
# Extra tests
BuildRequires:  perl(Perl::MinimumVersion) >= 1.20
BuildRequires:  perl(Pod::Simple) >= 3.07
BuildRequires:  perl(Test::CPAN::Meta) >= 0.12
BuildRequires:  perl(Test::MinimumVersion) >= 0.008
BuildRequires:  perl(Test::Pod) >= 1.26
%endif
Requires:       perl(Carp)
Requires:       perl(OLE::Storage_Lite) >= 0.19
Requires:       perl(Text::CSV_XS)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(OLE::Storage_Lite\\)$

%description
The Spreadsheet::ParseExcel module can be used to read information from
Excel 95-2003 binary files.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
%if %{with perl_Spreadsheet_ParseExcel_enables_optional_test}
# Optional tests
Requires:       perl(IO::Scalar)
%endif
%if %{with perl_Spreadsheet_ParseExcel_enables_extra_test}
# Extra tests
Requires:       perl(Perl::MinimumVersion) >= 1.20
Requires:       perl(Test::CPAN::Meta) >= 0.12
Requires:       perl(Test::MinimumVersion) >= 0.008
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Spreadsheet-ParseExcel-%{version}
%if %{without perl_Spreadsheet_ParseExcel_enables_extra_test}
for T in t/90_pod.t t/91_minimumversion.t t/92_meta.t; do
    rm "$T"
    perl -i -ne 'print $_ unless m{^\Q'"$T"'\E}' MANIFEST
done
%endif
# Fix line-endings
for file in sample/* t/0[0-5]_*.t; do
    [ -f "$file" ] && perl -pi -e 's/\r\n/\n/' "$file"
done
# Normalize shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}
# For Spreadsheet::ParseExcel::FmtJapan2; see README for details
install -D -m 644 -p CP932Excel.map \
    %{buildroot}%{perl_vendorarch}/Unicode/Map/MS/WIN/CP932Excel.map
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_Spreadsheet_ParseExcel_enables_extra_test}
cp -a META.yml t %{buildroot}%{_libexecdir}/%{name}
%endif
# Remove tests that expect modules in a current working directory
rm %{buildroot}%{_libexecdir}/%{name}/t/90_pod.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/46_save_parser.t writed into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset RELEASE_TESTING
export AUTOMATED_TESTING=1
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset RELEASE_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test AUTOMATED_TESTING=1

%files
%doc Changes README README_Japan.htm examples/ sample/
%dir %{perl_vendorarch}/Unicode
%dir %{perl_vendorarch}/Unicode/Map
%dir %{perl_vendorarch}/Unicode/Map/MS
%dir %{perl_vendorarch}/Unicode/Map/MS/WIN
%{perl_vendorarch}/Unicode/Map/MS/WIN/CP932Excel.map
%dir %{perl_vendorlib}/Spreadsheet
%{perl_vendorlib}/Spreadsheet/ParseExcel
%{perl_vendorlib}/Spreadsheet/ParseExcel.pm
%{_mandir}/man3/Spreadsheet::ParseExcel.3*
%{_mandir}/man3/Spreadsheet::ParseExcel::*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.66-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 20 2024 Petr Pisar <ppisar@redhat.com> - 1:0.66-2
- Fix declaring dependencies for extra tests

* Tue Feb 20 2024 Petr Pisar <ppisar@redhat.com> - 1:0.66-1
- Return to CPAN versioning
- Package the tests

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6600-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6600-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 30 2023 Paul Howarth <paul@city-fan.org> - 0.6600-1
- Update to 0.66
  - Fix for CVE-2023-7101 (unvalidated input can lead to arbitrary code
    execution vulnerability)
    https://github.com/runrig/spreadsheet-parseexcel/issues/33
- Use author-independent source URL
- Use SPDX-format license tag
- No longer need to fix document file permissions
- Fix permissions verbosely
- Don't assume "pm" suffix on manpage files

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6500-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6500-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6500-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.6500-32
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6500-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6500-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.6500-29
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6500-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6500-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.6500-26
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6500-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6500-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.6500-23
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6500-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6500-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.6500-20
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6500-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6500-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6500-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.6500-16
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6500-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.6500-14
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6500-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6500-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.6500-11
- Perl 5.22 rebuild

* Mon Dec 08 2014 Petr Šabata <contyk@redhat.com> - 0.6500-10
- 0.65 bump

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.5900-10
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5900-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5900-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5900-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 0.5900-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5900-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5900-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 0.5900-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5900-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 Paul Howarth <paul@city-fan.org> - 0.5900-1
- Update to 0.59 (#731907)
  - Patch for decryption of default encrypted workbooks from Alexey Mazurin
  - Fix for invalid formatting of text cells that are numeric (CPAN RT#62073)
- BR: perl(Crypt::RC4) and perl(Digest::Perl::MD5)
- Drop conditionals for EPEL-5 support since Crypt::RC4 isn't available there

* Mon Aug 22 2011 Paul Howarth <paul@city-fan.org> - 0.5800-1
- Update to 0.58
  - Fix for text cells formatted with a leading apostrophe (CPAN RT#61299)
  - Documentation fixes (CPAN RT#61320)
  - Fix for currency locales in format strings (CPAN RT#60547)
  - Fix for incomplete SETUP records

* Mon Aug 22 2011 Paul Howarth <paul@city-fan.org> - 0.5700-1
- Update to 0.57
  - Added fix for reading formatted data from Excel 4 files
  - Added example programs, a_simple_parser.pl and display_text_table.pl
  - Removed Build.PL from README (CPAN RT#52670)
- Package examples as %%doc
- Drop note about sample files not being UTF-8 encoded; no longer applicable

* Mon Aug 22 2011 Paul Howarth <paul@city-fan.org> - 0.5600-1
- Update to 0.56
  - Added error() and error_code() error handling routines, which allows
    encrypted files to be ignored; added t/10_error_codes.t for these methods
    (CPAN RT#47978, CPAN RT#51033)
  - Made version 0.19 of OLE::Storage_Lite a prerequisite to avoid issues when
    writing OLE header in SaveParser
  - Changed Parse() method name to parse() for consistency with the rest of the
    API; the older method name is still supported but not documented
- Bump version requirement for perl(OLE::Storage_Lite) to 0.19
- No longer need to fix line-endings of Changes file

* Mon Aug 22 2011 Paul Howarth <paul@city-fan.org> - 0.5500-1
- Update to 0.55
  - Refactored Worksheet interface and documentation, adding 04_regression.t
    and 05_regression.t to test changes
  - Fixed column units conversion, adding 24_row_col_sizes.t as check
  - Fixed RK number conversion, which was the source of several RT bugs and
    portability issues; added 25_decode_rk_numbers.t test case
  - Added fix for incorrectly skipped charts (CPAN RT#44009)
  - Added fix for locale [$-ddd] strings in number formats (CPAN RT#43638)
  - Added fix for multiple dots in number formats (CPAN RT#45502)
  - Added fix to make half way rounding behave like Excel (CPAN RT#45626)
  - Added checks for valid dates in Utility::ExcelFmt (CPAN RT#48831)
  - Added new FmtJapan module and tests written by Goro Fuji
  - Fixed bug in ExcelFmt() date handling where conversion to weekday and month
    names wasn't handled correctly, adding extra tests to
    21_number_format_user.t
  - Fixed bug when checking $Config{useperlio} (CPAN RT#28861)
  - Fixed bug where CellHandler variables weren't scoped to package
    (CPAN RT#43250)
  - Added tests for ExcelLocaltime() and LocaltimeExcel(),
    26_localtime2excel.t and 27_localtime2excel.t
  - Refactored SaveParser docs
  - Made perl 5.8.0 a requirement for proper Unicode handling
  - Fixed minor int2col() bug, adding 28_int2col.t test (CPAN RT#48967)
  - Refactored Workbook API and docs
  - Fix for height/width of hidden rows/columns with additional tests in
    05_regression.t (CPAN RT#48450)
  - Fix for malformed Print_Title Name block
  - Refactored Cell.pm documentation and method names and added regression
    suite, t/06_regression.t
  - Added float comparison test to avoid false failing tests on 64-bit systems
- Drop perl(Test::More) and perl(Test::Pod) version requirements
- BR: perl(Test::CPAN::Meta) and perl(Test::MinimumVersion), and enable
  AUTOMATED_TESTING
- Fix line-endings of Changes file

* Mon Aug 22 2011 Paul Howarth <paul@city-fan.org> - 0.4900-10
- Revert to ExtUtils::MakeMaker flow preferred by upstream
- Make %%files list more explicit
- Add note about encoding of sample files

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.4900-9
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.4900-8
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4900-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.4900-6
- Rebuild to fix problems with vendorarch/lib (#661697)

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.4900-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.4900-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4900-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4900-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 02 2009 Steven Pritchard <steve@kspei.com> 0.4900-1
- Update to 0.49.

* Thu Jan 22 2009 Steven Pritchard <steve@kspei.com> 0.4700-1
- Update to 0.47.

* Sat Jan 17 2009 Steven Pritchard <steve@kspei.com> 0.4500-1
- Update to 0.45.
- s/Get/Extract/ in Summary.
- Update Source0 URL.
- Update description.
- Fix line endings in README and samples.

* Thu Dec 11 2008 Steven Pritchard <steve@kspei.com> 0.3300-1
- Update to 0.33.
- Make Test::More dep versioned.
- BR Test::Pod.

* Mon Mar  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3200-5
- rebuild for new perl (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3200-4
- Autorebuild for GCC 4.3

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.3200-3
- rebuild for new perl

* Thu Jan 10 2008 Ralf Corsépius <rc040203@freenet.de> 0.3200-2
- Update License-tag.
- BR perl(Test::More) (BZ 419631).
- Let package own %%{perl_vendorarch}/Unicode.

* Sat May 19 2007 Steven Pritchard <steve@kspei.com> 0.3200-1
- Update to 0.32.

* Fri Apr 06 2007 Steven Pritchard <steve@kspei.com> 0.3000-1
- Update to 0.30.
- BR Proc::ProcessTable for better test coverage.

* Wed Jan 17 2007 Steven Pritchard <steve@kspei.com> 0.2800-1
- Update to 0.28.
- Drop typo fix.
- BR: Spreadsheet::WriteExcel (for tests).

* Wed Jan 17 2007 Steven Pritchard <steve@kspei.com> 0.2700-2
- Fix typo in Spreadsheet::ParseExcel::FmtUnicode.

* Tue Jan 16 2007 Steven Pritchard <steve@kspei.com> 0.2700-1
- Update to 0.27.
- Cleanup to more closely match cpanspec output.
- Switch to Module::Build-based build.
- BR: IO::Scalar, Unicode::Map, and Jcode.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.2603-3
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Steven Pritchard <steve@kspei.com> 0.2603-2
- Fix find option order.

* Sun May 14 2006 Michael A. Peters <mpeters@mac.com> - 0.2603-1
- Install the CP932Excel.map file
- makes package arch dependent

* Wed May 10 2006 Michael A. Peters <mpeters@mac.com> - 0.2603-0.2
- Changed license to GPL or Artistic per the ParseExcel.pm file

* Wed May 10 2006 Michael A. Peters <mpeters@mac.com> - 0.2603-0.1
- Initial packaging
