%bcond_with bootstrap

%global packname waldo
%global packver  0.4.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          3%{?dist}
Summary:          Find Differences Between R Objects

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-cli, R-diffobj, R-fansi, R-glue, R-methods, R-rematch2, R-rlang >= 0.4.10, R-tibble
# Suggests:  R-testthat >= 3.0.0, R-covr, R-R6
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cli
BuildRequires:    R-diffobj >= 0.3.4
BuildRequires:    R-fansi
BuildRequires:    R-glue
BuildRequires:    R-methods
BuildRequires:    R-rematch2
BuildRequires:    R-rlang >= 0.4.10
BuildRequires:    R-tibble
%if %{without bootstrap}
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-R6
BuildRequires:    R-withr
BuildRequires:    R-xml2
%endif

%description
Compare complex R objects and reveal the key differences.  Designed
particularly for use in testing packages where being able to quickly
isolate key differences makes understanding test failures much easier.


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
%if %{without bootstrap}
%{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.4.0-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Tom Callaway <spot@fedoraproject.org> - 0.4.0-1
- update to 0.4.0
- rebuild for R 4.2.1
- bootstrap on

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 0.2.5-3
- bootstrap off

* Thu Jun 10 2021 Tom Callaway <spot@fedoraproject.org> - 0.2.5-2
- Rebuilt for R 4.1.0
- bootstrap

* Wed Mar 10 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.5-1
- Update to latest version (#1936608)

* Mon Feb 15 2021 Tom Callaway <spot@fedoraproject.org> - 0.2.4-1
- update to 0.2.4

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.3-1
- Update to latest version (#1896126)

* Fri Oct 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-1
- Update to latest version (#1888855)

* Sat Oct 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-1
- Update to latest version (#1886503)

* Fri Aug 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0-1
- initial package for Fedora
