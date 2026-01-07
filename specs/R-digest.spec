Name:           R-digest
Version:        %R_rpm_version 0.6.39
Release:        %autorelease
Summary:        Create Cryptographic Hash Digest of R Objects

# Automatically converted from old format: GPLv2+ and BSD and MIT and zlib - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND Zlib
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 0.6.39

Provides:       bundled(xxhash)

%description
Implementation of a function 'digest()' for the creation of hash digests of
arbitrary R objects (using the md5, sha-1, sha-256, crc32, xxhash and
murmurhash algorithms) permitting easy comparison of R language objects, as
well as a function 'hmac()' to create hash-based message authentication code.
The md5 algorithm by Ron Rivest is specified in RFC 1321, the sha-1 and
sha-256 algorithms are specified in FIPS-180-1 and FIPS-180-2, and the crc32
algorithm is described in
ftp://ftp.rocksoft.com/cliens/rocksoft/papers/crc_v3.txt. For md5, sha-1,
sha-256 and aes, this package uses small standalone implementations that were
provided by Christophe Devine. For crc32, code from the zlib library is used.
For sha-512, an implementation by Aaron D. Gifford is used. For xxHash, the
implementation by Yann Collet is used. For murmurhash, an implementation by
Shane Day is used. Please note that this package is not meant to be deployed
for cryptographic purposes for which more comprehensive (and widely tested)
libraries such as OpenSSL should be used.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
