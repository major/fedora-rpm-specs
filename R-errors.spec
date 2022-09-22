%bcond_with check

%global packname  errors
%global rlibdir   %{_datadir}/R/library

Name:           R-%{packname}
Version:        0.3.6
Release:        7%{?dist}
Summary:        Uncertainty Propagation for R Vectors

License:        MIT
URL:            https://cran.r-project.org/package=%{packname}
Source0:        %{url}&version=%{version}#/%{packname}_%{version}.tar.gz

BuildRequires:  R-devel >= 3.0.0
%if %{with check}
BuildRequires:  R-dplyr >= 1.0.0, R-vctrs >= 0.3.1, R-pillar
BuildRequires:  R-testthat
BuildRequires:  R-knitr, R-rmarkdown
%endif
BuildArch:      noarch

%description
Support for measurement errors in R vectors, matrices and arrays:
automatic uncertainty propagation and reporting.
Documentation about 'errors' is provided in the paper by Ucar,
Pebesma & Azcorra (2018, <doi:10.32614/RJ-2018-075>), included in
this package as a vignette; see 'citation("errors")' for details.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%if %{with check}
export LANG=C.UTF-8
export _R_CHECK_FORCE_SUGGESTS_=0
%{_bindir}/R CMD check --ignore-vignettes %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data

%changelog
* Wed Aug  3 2022 Tom Callaway <spot@fedoraproject.org> - 0.3.6-7
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 0.3.6-3
- Rebuilt for R 4.1.0
- conditionalize check (and BR) and disable

* Sat Feb 27 2021 Iñaki Úcar <iucar@fedoraproject.org> - 0.3.6-2
- Rebuilt for units update

* Sat Feb 27 2021 Iñaki Úcar <iucar@fedoraproject.org> - 0.3.6-1
- Update to 0.3.6

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 0.3.3-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Iñaki Úcar <iucar@fedoraproject.org> - 0.3.3-1
- Update to 0.3.3

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.2-2
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 31 2019 Iñaki Úcar <iucar@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Iñaki Úcar <iucar@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Wed Aug 15 2018 Iñaki Úcar <iucar@fedoraproject.org> - 0.3.0-3
- Bump version to trigger rebuild due to target misconfiguration in f29

* Wed Aug 15 2018 Iñaki Úcar <iucar@fedoraproject.org> - 0.3.0-2
- Bump version to trigger rebuild due to target misconfiguration in f29

* Tue Aug 14 2018 Iñaki Úcar <iucar@fedoraproject.org> - 0.3.0-1
- initial package for Fedora
