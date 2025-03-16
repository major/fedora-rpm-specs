Name:           perl-Crypt-SMIME
Version:        0.31
Release:        %autorelease
Summary:        S/MIME message signing, verification, encryption and decryption
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-SMIME
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-SMIME-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CChecker)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  openssl
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Taint::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Taint)
BuildRequires:  perl(Test::More)

#Add a test sub package.
%{?perl_default_subpackage_tests}


%description
This module provides a class for handling S/MIME messages. It can sign,
verify, encrypt and decrypt messages. It requires libcrypto
(http://www.openssl.org) to work.


%prep
%setup -q -n Crypt-SMIME-%{version}
# As part of the rpm process we generate some files which
# then cause t/manifest.t to fail.
printf '\\.list$\n^\\.package_note\n' >> MANIFEST.SKIP


%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
make test


%files
%doc Changes README
%{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/Crypt/
%{_mandir}/man3/SMIME*3pm*


%changelog
%autochangelog
