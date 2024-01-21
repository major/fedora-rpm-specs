%global packname lubridate
%global packver  1.9.2
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          5%{?dist}
Summary:          Make dealing with dates a little easier
License:          GPL-2.0-or-later-version
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-generics, R-timechange >= 0.1.1
# Suggests:  R-covr, R-knitr, R-rmarkdown, R-testthat >= 2.1.0, R-vctrs >= 0.5.0
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-generics
BuildRequires:    R-timechange >= 0.1.1
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat >= 2.1.0
BuildRequires:    R-vctrs >= 0.5.0

%description
Functions to work with date-times and time-spans: fast and user friendly
parsing of date-time data, extraction and updating of components of a date-time
(years, months, days, hours, minutes, and seconds), algebraic manipulation on
date-time and time-span objects. The 'lubridate' package has a consistent and
memorable syntax that makes working with dates easy and fun.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Used to update sources; don't need to package it.
rm %{buildroot}%{rlibdir}/%{packname}/cctz.sh


%check
%{_bindir}/R CMD check --ignore-vignettes %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/pkgdown


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 12 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.9.2-3
- Ignore vignettes

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.9.2-2
- R-maint-sig mass rebuild

* Fri Mar  3 2023 Tom Callaway <spot@fedoraproject.org> - 1.9.2-1
- update to 1.9.2

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 1.8.0-1
- update to 1.8.0
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 1.7.10-2
- Rebuilt for R 4.1.0

* Sat Feb 27 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.10-1
- Update to latest version (#1933314)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.9.2-1
- Update to latest version (#1897632)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.9-1
- Update to latest version

* Sat Jun  6 2020 Tom Callaway <spot@fedoraproject.org>  - 1.7.8-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.8-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.4-6
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 1.7.4-2
- rebuild for R 3.5.0

* Thu Apr 26 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.4-1
- Update to latest release

* Sun Mar 18 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.3-4
- Add missing Rcpp Requires.
- Make library name explicit.

* Sat Mar 17 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.3-3
- Unbundle cctz.

* Mon Mar 05 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.3-2
- Enable doc build.

* Sun Mar 04 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.3-1
- initial package for Fedora
