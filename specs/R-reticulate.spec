%global packname reticulate
%global packver  1.20
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          15%{?dist}
Summary:          R Interface to 'Python'

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:          Apache-2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
Patch0001:        0001-Skip-network-tests.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-Matrix, R-Rcpp >= 0.12.7, R-graphics, R-jsonlite, R-methods, R-png, R-rappdirs, R-utils, R-withr
# Suggests:  R-callr, R-knitr, R-rmarkdown, R-testthat
# LinkingTo:
# Enhances:

Requires:         python3
BuildRequires:    python3-devel
BuildRequires:    python3-docutils
BuildRequires:    python3-numpy
%ifnarch %{ix86}
# https://bugzilla.redhat.com/show_bug.cgi?id=2263999
BuildRequires:    python3-pandas
%endif
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-Matrix
BuildRequires:    R-Rcpp-devel >= 0.12.7
BuildRequires:    R-graphics
BuildRequires:    R-jsonlite
BuildRequires:    R-methods
BuildRequires:    R-png
BuildRequires:    R-rappdirs
BuildRequires:    R-utils
BuildRequires:    R-withr
BuildRequires:    R-callr
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat
# Test modules:
BuildRequires:   python3dist(docutils)
BuildRequires:   python3dist(matplotlib)
BuildRequires:   python3dist(numpy)
%ifnarch %{ix86}
BuildRequires:   python3dist(pandas)
%endif
BuildRequires:   python3dist(scipy)

%description
Interface to Python modules, classes, and functions. When calling into Python,
R data types are automatically converted to their equivalent Python types. When
values are returned from Python to R they are converted back to R types.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch -P0001 -p1
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%py_byte_compile %{python3} %{buildroot}%{rlibdir}/%{packname}/python/rpytools


%check
%{_bindir}/R CMD check --ignore-vignettes %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/config
%{rlibdir}/%{packname}/python


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul  24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.20-14
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.20-12
- R-maint-sig mass rebuild

* Fri Feb 16 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 1.20-11
- Do not test with Pandas on i686

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.20-7
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 1.20-5
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 1.20-1
- update to 1.20
- Rebuilt for R 4.1.0

* Sat Apr 24 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.19-1
- Update to latest version (#1951995)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.18-1
- Update to latest version (#1890309)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.16-2
- rebuild for R 4

* Sun May 31 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.16-1
- Update to latest version

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.15-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.14-1
- Update to latest version

* Sat Aug 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.13-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12-1
- Update to latest version

* Sat Mar 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.11.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 06 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.10-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.9-1
- Update to latest version

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.8-2
- Rebuilt for Python 3.7

* Sat Jun 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8-1
- Update to latest version

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 1.7-2
- rebuild for R 3.5.0

* Sun Apr 29 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7-1
- Update to latest version

* Sun Apr 29 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6-1
- initial package for Fedora
