Name:           perl-Data-Integer
Version:        0.006
Release:        %autorelease
Summary:        Details of the native integer data type
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Data-Integer
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Data-Integer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(integer)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(warnings)

%description
This module is about the native integer numerical data type. A native
integer is one of the types of datum that can appear in the numeric part
of a Perl scalar. This module supplies constants describing the native
integer type.

%prep
%autosetup -n Data-Integer-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
