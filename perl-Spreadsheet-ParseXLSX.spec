Name:           perl-Spreadsheet-ParseXLSX
Version:        0.27
Release:        11%{?dist}
Summary:        Parse XLSX files
License:        MIT
URL:            https://github.com/doy/spreadsheet-parsexlsx
Source:         https://cpan.metacpan.org/authors/id/D/DO/DOY/Spreadsheet-ParseXLSX-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Crypt::Mode::CBC)
BuildRequires:  perl(Crypt::Mode::ECB)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Graphics::ColorUtils)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(OLE::Storage_Lite)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Spreadsheet::ParseExcel) >= 0.61
BuildRequires:  perl(XML::Twig)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Makefile:
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(blib) >= 1.01

%description
This module is an adaptor for <Spreadsheet::ParseExcel> that reads XLSX files.
For documentation about the various data that you can retrieve from these
classes, please see <Spreadsheet::ParseExcel>,
<Spreadsheet::ParseExcel::Workbook>, <Spreadsheet::ParseExcel::Worksheet>, and
<Spreadsheet::ParseExcel::Cell>.


%prep
%setup -q -n Spreadsheet-ParseXLSX-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
make %{?_smp_mflags}


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
make test


%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/Spreadsheet::ParseXLSX*.3*


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-10
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.27-1
- initial package release.
