%bcond bootstrap 0

%global packname openssl
%global rlibdir  %{_libdir}/R/library

# Skip examples or tests that use the network.
%bcond network 0

# jose depends on this package.
%bcond doc 0

Name:             R-%{packname}
Version:          2.3.3
Release:          %autorelease
Summary:          Toolkit for Encryption, Signatures and Certificates Based on OpenSSL

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          %{url}&version=%{version}#/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-askpass
# Suggests:  R-curl, R-testthat >= 2.1.0, R-digest, R-knitr, R-rmarkdown, R-jsonlite, R-jose, R-sodium
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    pkgconfig(openssl)
%if 0%{?fedora} >= 41
BuildRequires:    openssl-devel-engine
%endif
BuildRequires:    R-askpass
%if %{without bootstrap}
BuildRequires:    R-curl
BuildRequires:    R-testthat >= 2.1.0
BuildRequires:    R-sodium
%if %{with doc}
BuildRequires:    R-digest
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-jsonlite
BuildRequires:    R-jose
BuildRequires:    glyphicons-halflings-fonts
%endif
%endif

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
%setup -q -c -n %{packname}

%if %{without network}
rm %{packname}/tests/testthat/test_google.R
%endif


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{without bootstrap}
%if %{without network}
args="--no-examples"
%endif
%if %{without doc}
args="${args} --ignore-vignettes"
export _R_CHECK_FORCE_SUGGESTS_=0
%endif
# Allow tests with SHA1 signatures to pass.
# https://github.com/jeroen/openssl/issues/125
export OPENSSL_ENABLE_SHA1_SIGNATURES=1
%{_bindir}/R CMD check %{packname} $args
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/cacert.pem
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
%autochangelog
