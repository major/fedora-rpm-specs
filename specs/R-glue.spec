%global packname glue
%global packver  1.6.2
%global rlibdir  %{_libdir}/R/library

# When we are bootstrapping, we drop some dependencies, and/or build time tests.
%bcond_with bootstrap

Name:             R-%{packname}
Version:          %{packver}
Release:          9%{?dist}
Summary:          Interpreted String Literals

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-methods
# Suggests:  R-testthat, R-covr, R-magrittr, R-crayon, R-knitr, R-rmarkdown, R-DBI, R-RSQLite, R-R.utils, R-forcats, R-microbenchmark, R-rprintf, R-stringr, R-ggplot2, R-dplyr, R-withr, R-vctrs >= 0.3.0, R-waldo >= 0.3.0
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
%if %{without bootstrap}
BuildRequires:    R-crayon
BuildRequires:    R-DBI
BuildRequires:    R-dplyr
BuildRequires:    R-forcats
BuildRequires:    R-ggplot2
BuildRequires:    R-knitr
BuildRequires:    R-magrittr
BuildRequires:    R-microbenchmark
BuildRequires:    R-R.utils
BuildRequires:    R-rmarkdown
BuildRequires:    R-rprintf
BuildRequires:    R-RSQLite
BuildRequires:    R-stringr
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-vctrs >= 0.3.0
BuildRequires:    R-waldo >= 0.3.0
BuildRequires:    R-withr
%endif

%description
An implementation of interpreted string literals, inspired by Python's
Literal String Interpolation <https://www.python.org/dev/peps/pep-0498/>
and Docstrings <https://www.python.org/dev/peps/pep-0257/> and Julia's
Triple-Quoted String Literals
<https://docs.julialang.org/en/v1.3/manual/strings/#Triple-Quoted-String-Literals-1>.


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


%check
export LANG=C.UTF-8
%if %{without bootstrap}
%{_bindir}/R CMD check --ignore-vignettes %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.6.2-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.6.2-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Tom Callaway <spot@fedoraproject.org> - 1.6.2-1
- update to 1.6.2
- rebuild for R 4.2.1
- bootstrap

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 1.4.2-4
- bootstrap off

* Wed Jun  9 2021 Tom Callaway <spot@fedoraproject.org> - 1.4.2-3
- Rebuilt for R 4.1.0
- bootstrap

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.2-1
- Update to latest version (#1820713)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul  3 2020 José Matos <jamatos@fedoraproject.org> - 1.4.1-2
- replace "with_suggests" by "bcond_with bootstrap" since that is really its purpose

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 1.4.1-1
- break testthat loop by broadening "with_suggests"
- update to 1.4.1
- rebuild for R 4

* Sat Mar 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-4
- Exclude Suggests for unavailable packages

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- initial package for Fedora
