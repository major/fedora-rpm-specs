Name:           perl-Business-ISMN
Version:        1.205
Release:        %autorelease
Summary:        Perl library for International Standard Music Numbers
License:        Artistic-2.0
URL:            https://metacpan.org/release/Business-ISMN
Source0:        https://cpan.metacpan.org/modules/by-module/Business/Business-ISMN-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More) >= 1.00
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Tie::Cycle) >= 1.21
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Recommends:     perl(GD::Barcode::EAN13)

%description
%{summary}.

%prep
%setup -q -n Business-ISMN-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README.pod
%{perl_vendorlib}/Business*
%{_mandir}/man3/Business::ISMN*

%changelog
%autochangelog
