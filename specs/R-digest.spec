%bcond_with check

%global packname digest
%global packver 0.6.37

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          %{url}&version=%{version}#/%{packname}_%{version}.tar.gz
# Automatically converted from old format: GPLv2+ and BSD and MIT and zlib - review is highly recommended.
License:          GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND Zlib
Summary:          Create Cryptographic Hash Digest of R Objects
BuildRequires:    R-devel >= 3.4.0, tex(latex), R-utils
%if %{with check}
# Test requires:
BuildRequires:    R-simplermarkdown, R-tinytest
%endif
Provides:         bundled(xxhash)

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

%package devel
Requires:         %{name}%{?_isa} = %{version}-%{release}
Summary:          Header files for compiling against digest

%description devel
Header files for compiling against digest.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/R.css

%check
%if %{with check}
# s390x fails this check in spooky ways
%ifnarch s390x
%{_bindir}/R CMD check %{packname}
%endif
%endif

%files
%license %{_libdir}/R/library/%{packname}/GPL-2
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/doc/
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/demo
%{_libdir}/R/library/%{packname}/tinytest

%files devel
%{_libdir}/R/library/%{packname}/include/

%changelog
%autochangelog
