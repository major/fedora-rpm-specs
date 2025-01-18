%global packname  S4Vectors
%global rlibdir %{_libdir}/R/library

%global __suggests_exclude ^R\\((BiocStyle|ShortRead|graph)\\)

Name:             R-%{packname}
Version:          0.40.2
Release:          3%{dist}
Summary:          S4 implementation of vectors and lists
License:          Artistic-2.0
URL:              http://www.bioconductor.org/packages/release/bioc/html/S4Vectors.html
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Patch0:           0001-format-security-fix.patch
BuildRequires:    R-devel >= 4.0.0 tex(latex) R-methods R-utils R-stats R-stats4
BuildRequires:    R-BiocGenerics >= 0.37.0

%description
The S4Vectors package defines the Vector and List virtual classes and a set of
generic functions that extend the semantic of ordinary vectors and lists in R.
Package developers can easily implement vector-like or list-like objects as
concrete subclasses of Vector or List. In addition, a few low-level concrete
subclasses of general interest (e.g. DataFrame, Rle, and Hits) are implemented
in the S4Vectors package itself (many more are implemented in the IRanges
package and in other Bioconductor infrastructure packages).

%package devel
Summary:          Development files for R-S4Vectors
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for R-S4Vectors.

%prep
%setup -q -c -n %{packname}
pushd %{packname}
%patch -P0 -p1
popd

%build

%install
mkdir -p %{buildroot}%{rlibdir}
R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
# Testing tests optional deps we don't package
# _R_CHECK_FORCE_SUGGESTS_=false %%{_bindir}/R CMD check %%{packname}

%files
%dir %{rlibdir}/%{packname}/
%doc %{rlibdir}/%{packname}/html/
%doc %{rlibdir}/%{packname}/doc/
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/Meta/
%{rlibdir}/%{packname}/R/
%{rlibdir}/%{packname}/help/
%{rlibdir}/%{packname}/unitTests/
%{rlibdir}/%{packname}/libs/

%files devel
%{rlibdir}/%{packname}/include/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 26 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.40.2-1
- Update to latest version

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.34.0-8
- R-maint-sig mass rebuild

* Sat Apr  20 2024 Miroslav Suchý <msuchy@redhat.com> - 0.34.0-7
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.34.0-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 0.34.0-1
- update to 0.34.0
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 0.30.0-1
- Update to 0.30.0
- Rebuilt for R 4.1.0

* Wed Feb  3 2021 Tom Callaway <spot@fedoraproject.org> - 0.28.1-1
- update to 0.28.1

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 0.26.1-1
- rebuild for R 4
- update to 0.26.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Tom Callaway <spot@fedoraproject.org> - 0.24.1-1
- update to 0.24.1

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.24.0-2
- Exclude Suggests for unavailable packages

* Mon Nov  4 2019 Tom Callaway <spot@fedoraproject.org> - 0.24.0-1
- update to 0.24.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.22.0-2
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 31 2019 Tom Callaway <spot@fedoraproject.org> - 0.22.0-1
- update to 0.22.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb  6 2019 Tom Callaway <spot@fedoraproject.org> - 0.20.1-1
- update to 0.20.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 0.18.2-1
- update to 0.18.2

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 0.18.1-1
- update to 0.18.1, rebuild for R 3.5.0

* Wed Mar 14 2018 Tom Callaway <spot@fedoraproject.org> - 0.16.0-1
- update to 0.16.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun  7 2017 Tom Callaway <spot@fedoraproject.org> - 0.14.3-1
- update to 0.14.3

* Wed May 24 2017 Tom Callaway <spot@fedoraproject.org> - 0.14.1-1
- update to 0.14.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec  7 2015 Tom Callaway <spot@fedoraproject.org> - 0.8.3-1
- update to 0.8.3

* Fri Jul 03 2015 pingou <pingou@pingoured.fr> 0.6.1-1
- Update to version 0.6.1

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Tom Callaway <spot@fedoraproject.org> - 0.6.0-1
- initial package
