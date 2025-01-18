%bcond_with check

%global packname vctrs
%global packver  0.6.5
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          3%{?dist}
Summary:          Vector Helpers

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
# https://github.com/r-lib/vctrs/issues/1353
Patch0001:        0001-Skip-some-tests-on-big-endian-machines.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-cli >= 3.4.0, R-glue, R-lifecycle >= 1.0.3, R-rlang >= 1.0.6
# Suggests:  R-bit64, R-covr, R-crayon, R-dplyr >= 0.8.5, R-generics, R-knitr, R-pillar >= 1.4.4, R-pkgdown >= 2.0.1, R-rmarkdown, R-testthat >= 3.0.0, R-tibble >= 3.1.3, R-withr, R-xml2, R-waldo >= 0.2.0, R-zeallot
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cli >= 3.4.0
BuildRequires:    R-glue
BuildRequires:    R-lifecycle >= 1.0.3
BuildRequires:    R-rlang >= 1.0.6
%if %{with check}
BuildRequires:    R-bit64
BuildRequires:    R-crayon
BuildRequires:    R-dplyr >= 0.8.5
BuildRequires:    R-generics
BuildRequires:    R-knitr
BuildRequires:    R-pillar >= 1.4.4
BuildRequires:    R-pkgdown >= 2.0.1
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-tibble >= 3.1.3
BuildRequires:    R-withr
BuildRequires:    R-xml2
BuildRequires:    R-waldo >= 0.2.0
BuildRequires:    R-zeallot
%endif

%description
Defines new notions of prototype and size that are used to provide tools for
consistent and well-founded type-coercion and size-recycling, and are in turn
connected to ideas of type- and size-stability useful for analysing function
interfaces.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' DESCRIPTION
# pkgdown appears to only be a maintenance thing.
sed -i 's/pkgdown, //g' DESCRIPTION
# Skip big-endian problems.
%patch -P0001 -p1
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with check}
export LANG=C.UTF-8
%{_bindir}/R CMD check %{packname}
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
%{rlibdir}/%{packname}/WORDLIST
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so

%files devel
%{rlibdir}/%{packname}/include


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.6.5-1
- Update to newest version

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.6.2-5
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.6.2-1
- R-maint-sig mass rebuild
- Update to the latest version

* Mon Feb 20 2023 Tom Callaway <spot@fedoraproject.org> - 0.5.2-1
- update to 0.5.2

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 30 2022 Tom Callaway <spot@fedoraproject.org> - 0.5.1-1
- update to 0.5.1

* Thu Aug 18 2022 Tom Callaway <spot@fedoraproject.org> - 0.4.1-1
- update to 0.4.1
- rebuild for R 4.2.1
- disable check

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 20 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.8-3
- Re-enable tests

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Tom Callaway <spot@fedoraproject.org> - 0.3.8-1
- Update to 0.3.8
- Rebuilt for R 4.1.0
- disable check

* Sat Apr 03 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.7-1
- Update to latest version (#1944173)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.6-1
- Update to latest version (#1908729)

* Thu Nov 19 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.5-1
- Update to latest version (#1898577)

* Thu Sep 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.4-1
- Update to latest version (#1873347)

* Thu Sep 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.3-1
- Update to latest version

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.2-2
- Re-enable checks

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.2-1
- Update to latest version

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 0.3.0-2
- conditionalize check to break loops
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-1
- Update to latest version

* Sun Mar 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.4-1
- Update to latest version

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.3-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0-1
- Update to latest version

* Thu May 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.0-1
- initial package for Fedora

