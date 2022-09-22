Name:           perl-CLASS
Summary:        Alias for __PACKAGE__
Version:        1.1.7
Release:        %autorelease
License:        GPL+ or Artistic
Source0:        https://cpan.metacpan.org/authors/id/J/JD/JDEGUEST/CLASS-v%{version}.tar.gz
URL:            https://metacpan.org/release/CLASS
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.4
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Test::More) >= 0.07

%{?perl_default_filter}

%description
This package provides CLASS and $CLASS; both synonyms for __PACKAGE__.
They're easier to type, and $CLASS has the additional benefit of working
in strings.

%prep
%setup -q -n CLASS-v%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
