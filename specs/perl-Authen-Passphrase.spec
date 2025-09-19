%if 0%{?fedora} >= 43
ExcludeArch: %{ix86}
%endif

Name:           perl-Authen-Passphrase
Version:        0.008
Release:        %autorelease
Summary:        Hashed passwords/passphrases as objects

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Authen-Passphrase
Source:         https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Authen-Passphrase-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Authen::DecHpwd) >= 2.003
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::DES)
BuildRequires:  perl(Crypt::Eksblowfish::Bcrypt) >= 0.008
BuildRequires:  perl(Crypt::Eksblowfish::Uklblowfish) >= 0.008
BuildRequires:  perl(Crypt::MySQL) >= 0.03
BuildRequires:  perl(Crypt::PasswdMD5) >= 1.0
BuildRequires:  perl(Crypt::UnixCrypt_XS) >= 0.08
BuildRequires:  perl(Data::Entropy::Algorithms)
BuildRequires:  perl(Digest) >= 1.00
BuildRequires:  perl(Digest::MD4) >= 1.2
BuildRequires:  perl(Digest::MD5) >= 1.9953
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(MIME::Base64) >= 2.21
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Runtime) >= 0.011
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(warnings)

%description
These Perl modules provide a passphrase recognizer. Its job is
to recognize whether an offered passphrase is the right one. Various
passphrase encoding schemes are supported.

%prep
%autosetup -n Authen-Passphrase-%{version}

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
