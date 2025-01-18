%global packname servr
%global packver  0.24
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          10%{?dist}
Summary:          Simple HTTP Server to Serve Static Files or Dynamic Documents

License:          GPL-1.0-or-later
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-mime >= 0.2, R-httpuv >= 1.5.2, R-xfun, R-jsonlite
# Suggests:  R-tools, R-later, R-rstudioapi, R-knitr >= 1.9, R-rmarkdown
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-mime >= 0.2
BuildRequires:    R-httpuv >= 1.5.2
BuildRequires:    R-xfun
BuildRequires:    R-jsonlite
BuildRequires:    R-tools
BuildRequires:    R-later
BuildRequires:    R-rstudioapi
BuildRequires:    R-knitr >= 1.9
BuildRequires:    R-rmarkdown

%description
Start an HTTP server in R to serve static files, or dynamic documents that
can be converted to HTML files (e.g., R Markdown) under a given directory.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/bin
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/resources


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun  17 2024 Miroslav Suchý <msuchy@redhat.com> - 0.24-8
- convert license to SPDX

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.24-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.24-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 0.24-1
- update to 0.24
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 0.22-2
- Rebuilt for R 4.1.0

* Sat Apr 17 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.22-1
- Update to latest version (#1949647)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.21-1
- Update to latest version (#1907321)

* Tue Oct 20 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.20-1
- Update to latest version (#1889245)

* Thu Oct 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.19-1
- Update to latest version (#1885787)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.17-2
- Rebuild for R 4

* Thu Jun 25 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.17-1
- Update to 0.17

* Sun May 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.16-1
- initial package for Fedora
