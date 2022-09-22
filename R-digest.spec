%bcond_with check

%global packname digest
%global packver 0.6.29

Name:             R-%{packname}
Version:          %{packver}
Release:          1%{?dist}
Source0:          ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{packver}.tar.gz
License:          GPLv2+ and BSD and MIT and zlib
URL:              http://cran.r-project.org/web/packages/digest/index.html
Summary:          Create Cryptographic Hash Digest of R Objects
BuildRequires:    R-devel >= 3.4.0, tetex-latex, R-utils
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
* Wed Aug  3 2022 Tom Callaway <spot@fedoraproject.org> - 0.6.29-1
- update to 0.6.29
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 0.6.27-2
- Rebuilt for R 4.1.0

* Wed Feb  3 2021 Tom Callaway <spot@fedoraproject.org> - 0.6.27-1
- update to 0.6.27

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 0.6.25-1
- conditionalize tests
- update to 0.6.25
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov  5 2019 Tom Callaway <spot@fedoraproject.org> - 0.6.22-1
- update to 0.6.22

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.15-6
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 0.6.15-2
- rebuild for R 3.5.0

* Fri Mar 23 2018 Tom Callaway <spot@fedoraproject.org> - 0.6.15-1
- update to 0.6.15

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Tom Callaway <spot@fedoraproject.org> - 0.6.12-1
- update to 0.6.12, rebuild for R 3.4.0
- disable check due to missing deps

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Tom Callaway <spot@fedoraproject.org> - 0.6.8-2
- fix license tag
- fix define to be global
- add bundled provide for xxhash

* Wed Nov 4 2015 Tom Callaway <spot@fedoraproject.org> - 0.6.8-1
- Initial package
