Name:           R-openssl
Version:        %R_rpm_version 2.4.2
Release:        %autorelease
Summary:        Toolkit for Encryption, Signatures and Certificates Based on OpenSSL

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(openssl)

%description
Bindings to OpenSSL libssl and libcrypto, plus custom SSH key parsers.
Supports RSA, DSA and EC curves P-256, P-384, P-521, and curve25519.
Cryptographic signatures can either be created and verified manually or via
x509 certificates. AES can be used in cbc, ctr or gcm mode for symmetric
encryption; RSA for asymmetric (public key) encryption or EC for Diffie
Hellman. High-level envelope functions combine RSA and AES for encrypting
arbitrary sized data. Other utilities include key generators, hash functions
(md5, sha1, sha256, etc), base64 encoder, a secure random number generator, and
'bignum' math methods for manually performing crypto calculations on large
multibyte integers.

%prep
%autosetup -c
rm -f openssl/tests/testthat/test_google.R # network

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
