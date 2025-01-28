Name:           perl-Spreadsheet-ParseXLSX
Version:        0.36
Release:        %autorelease
Summary:        Parse XLSX files
License:        MIT
URL:            https://github.com/MichaelDaum/spreadsheet-parsexlsx
Source:         https://cpan.metacpan.org/authors/id/N/NU/NUDDLEGG/Spreadsheet-ParseXLSX-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Archive::Zip) >= 1.34
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
%autochangelog
