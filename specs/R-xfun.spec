%bcond_with suggests

%global packname xfun
%global packver  0.41
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          6%{?dist}
Summary:          Miscellaneous Functions to Support Packages Maintained by 'Yihui Xie'

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          %{url}&version=%{version}#/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-stats, R-tools
# Suggests:  R-testit, R-parallel, R-codetools, R-rstudioapi, R-tinytex >= 0.30, R-mime, R-markdown >= 1.5, R-knitr >= 1.42, R-htmltools, R-remotes, R-pak, R-rhub, R-renv, R-curl, R-jsonlite, R-magick, R-yaml, R-rmarkdown
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-stats
BuildRequires:    R-tools
BuildRequires:    R-testit
%if %{with suggests}
BuildRequires:    R-parallel
BuildRequires:    R-codetools
BuildRequires:    R-rstudioapi
BuildRequires:    R-tinytex >= 0.30
BuildRequires:    R-mime
BuildRequires:    R-markdown >= 1.5
BuildRequires:    R-knitr >= 1.42
BuildRequires:    R-htmltools
BuildRequires:    R-remotes
BuildRequires:    R-pak
BuildRequires:    R-renv
BuildRequires:    R-rhub
BuildRequires:    R-curl
BuildRequires:    R-jsonlite
BuildRequires:    R-magick
BuildRequires:    R-yaml
BuildRequires:    R-rmarkdown
%endif

%description
Miscellaneous functions commonly used in other packages maintained by
'Yihui Xie'.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-vignettes --no-examples
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
%{rlibdir}/%{packname}/scripts
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.41-4
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 21 2023 Tom Callaway <spot@fedoraproject.org> - 0.41-1
- update to 0.41

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May  1 2023 Tom Callaway <spot@fedoraproject.org> - 0.39-1
- update to 0.39
- conditionalize suggests

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.36-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 30 2022 Tom Callaway <spot@fedoraproject.org> - 0.36-1
- update to 0.36

* Sat Sep 17 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 0.33-1
- Update to 0.33 (RHBZ #2126255)

* Thu Aug 18 2022 Tom Callaway <spot@fedoraproject.org> - 0.32-1
- update to 0.32
- rebuild for R 4.2.1
- bootstrap on

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun  9 2021 Tom Callaway <spot@fedoraproject.org> - 0.23-1
- Update to 0.23
- Rebuilt for R 4.1.0
- bootstrap

* Sun Mar 14 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.22-1
- Update to latest version (#1937702)

* Tue Feb 23 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.21-1
- Update to latest version (#1927507)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.20-1
- Update to latest version (#1913445)

* Sat Oct 31 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.19-1
- Update to latest version

* Wed Sep 30 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.18-1
- Update to latest version (#1877265)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.16-1
- Update to latest version

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.15-1
- Update to latest version

* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 0.14-2
- conditionalize check to break knitr loop
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.14-1
- Update to latest version

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.12-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.11-1
- Update to latest version

* Wed Oct 02 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.10-1
- Update to latest version

* Sun Aug 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7-1
- Update to latest version

* Mon Apr 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6-1
- Update to latest version

* Sun Feb 24 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5-1
- Update to latest version

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3-1
- Update to latest version

* Fri Jun 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2-1
- Update to latest version

* Sun Mar 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1-1
- initial package for Fedora
