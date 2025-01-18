%global packname  readxl
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.4.3
Release:          3%{?dist}
Summary:          Read Excel Files

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-cellranger, R-tibble >= 2.0.1, R-utils
# Suggests:  R-knitr, R-rmarkdown, R-testthat >= 3.1.6, R-withr
# LinkingTo: R-progress, R-cpp11 >= 0.4.0
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    libxls-devel >= 1.6.2
#BuildRequires:    rapidxml-devel
BuildRequires:    R-cellranger
BuildRequires:    R-covr
BuildRequires:    R-cpp11-devel >= 0.4.0
BuildRequires:    R-tibble >= 2.0.1
BuildRequires:    R-utils
BuildRequires:    R-progress-devel
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat >= 3.1.6
BuildRequires:    R-withr

# Patched-in functionality, so not removeable.
Provides: bundled(rapidxml-devel) = 1.13

%description
Import excel files into R. Supports '.xls' via the 'libxls' C library
<https://github.com/libxls/libxls> and '.xlsx' via the embedded
'RapidXML' C++ library <http://rapidxml.sourceforge.net>.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
# Remove bundled libxls.
rm -rf src/Makevars.win src/libxls src/unix src/windows
sed -i '5,$d' src/Makevars
echo "PKG_LIBS=-lxlsreader" >> src/Makevars
find src -type f -exec sed -i 's@include "libxls/xls.h"@include <xls.h>@g' {} \;

# Patched-in functionality, so not removeable.
## Remove bundled rapidxml.
#rm src/rapidxml*
chmod -x src/rapidxml/*
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check --ignore-vignettes %{packname}


%files
%dir %{rlibdir}/%{packname}
%license %{rlibdir}/%{packname}/LICENSE
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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/WORDLIST


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 26 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.3-1
- Update to latest version

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.2-6
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.2-2
- R-maint-sig mass rebuild

* Thu Feb  9 2023 Tom Callaway <spot@fedoraproject.org> - 1.4.2-1
- update to 1.4.2

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 04 2022 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.1-1
- R 4.2.1, update to 1.4.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 1.3.1-10
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-8
- rebuilt for libxls

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.3.1-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version

* Sun Mar 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- initial package for Fedora
