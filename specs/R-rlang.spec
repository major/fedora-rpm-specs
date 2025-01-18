%bcond_with suggests

%global packname rlang
%global packver  1.1.3
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          3%{?dist}
Summary:          Functions for Base Types and Core R and 'Tidyverse' Features

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          %{url}&version=%{version}#/%{packname}_%{version}.tar.gz

Patch0001:        0001-Unbundle-libxxhash.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-utils
# Suggests:  R-cli >= 3.1.0, R-covr, R-crayon, R-fs, R-glue, R-knitr, R-magrittr, R-methods, R-pillar, R-rmarkdown, R-stats, R-testthat >= 3.0.0, R-tibble, R-usethis, R-vctrs >= 0.2.3, R-withr
# LinkingTo:
# Enhances:

BuildRequires:    pkgconfig(libxxhash)
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-utils
BuildRequires:    R-testthat >= 3.0.0
%if %{with suggests}
BuildRequires:    R-cli >= 3.1.0
BuildRequires:    R-crayon
BuildRequires:    R-fs
BuildRequires:    R-glue
BuildRequires:    R-knitr
BuildRequires:    R-magrittr
BuildRequires:    R-methods
BuildRequires:    R-pillar
BuildRequires:    R-rmarkdown
BuildRequires:    R-stats
BuildRequires:    R-tibble
BuildRequires:    R-usethis
BuildRequires:    R-vctrs >= 0.2.3
BuildRequires:    R-withr
%endif

%description
A toolbox for working with base types, core R features like the condition
system, and core 'Tidyverse' features like tidy evaluation.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch -P0001 -p1

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' DESCRIPTION
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
export LANG=C.UTF-8
%if %{with suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --ignore-vignettes
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
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/backtrace-ver


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 26 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.1.3-1
- Update to latest version

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.1.2-4
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov  5 2023 Tom Callaway <spot@fedoraproject.org> - 1.1.2-1
- update to 1.1.2

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 29 2023 Tom Callaway <spot@fedoraproject.org> - 1.1.1-1
- update to 1.1.1

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.1.0-2
- R-maint-sig mass rebuild

* Tue Mar 14 2023 Tom Callaway <spot@fedoraproject.org> - 1.1.0-1
- update to 1.1.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 24 2022 Tom Callaway <spot@fedoraproject.org> - 1.0.6-1
- update to 1.0.6

* Sat Sep 17 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5 (RHBZ #2015338)

* Thu Aug 18 2022 Tom Callaway <spot@fedoraproject.org> - 1.0.4-1
- update to 1.0.4
- rebuild for R 4.2.1
- bootstrap on

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 0.4.11-2
- bootstrap off

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 0.4.11-1
- Rebuilt for R 4.1.0
- update to 0.4.11

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.10-1
- Update to latest version (#1911718)

* Sat Nov 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.9-1
- Update to latest version (#1901765)

* Sat Oct 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.8-1
- Update to latest version (#1886418)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.7-1
- Update to latest version

* Fri Jul  3 2020 José Matos <jamatos@fedoraproject.org> - 0.4.6-4
- skip check on bootstrap (testthat is required for tests)

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.4.6-3
- bootstrap off

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 0.4.6-2
- bootstrap on
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.6-1
- Update to latest version

* Mon Mar 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.5-1
- Update to latest version

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.4-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.2-1
- Update to latest version

* Fri Oct 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.1-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.0-1
- Update to latest version

* Sun Apr 07 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.4-1
- Update to latest version

* Mon Apr 01 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.3-1
- Update to latest version

* Fri Mar 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.2-1
- Update to latest version

* Fri Feb 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-1
- Update to latest version
- Enable tests

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-1
- Update to latest version

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 0.2.0-2
- rebuild for R 3.5.0

* Sun Mar 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0-1
- initial package for Fedora
