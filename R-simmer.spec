%global packname simmer
%global rlibdir %{_libdir}/R/library

%global __suggests_exclude ^R\\((rticles|simmer\\.plot)\\)

Name:           R-%{packname}
Version:        4.4.6.1
Release:        2%{?dist}
Summary:        Discrete-Event Simulation for R

License:        GPL-2.0-or-later
URL:            https://cran.r-project.org/package=%{packname}
Source0:        %{url}&version=%{version}#/%{packname}_%{version}.tar.gz

BuildRequires:  R-devel >= 3.1.2
BuildRequires:  R-Rcpp-devel >= 0.12.9
BuildRequires:  R-magrittr, R-testthat
# BuildRequires:  R-knitr, R-rmarkdown, R-rticles, R-simmer.plot

%description
A process-oriented and trajectory-based Discrete-Event Simulation (DES)
package for R. It is designed as a generic yet powerful framework. The
architecture encloses a robust and fast simulation core written in 'C++'
with automatic monitoring capabilities. It provides a rich and flexible R
API that revolves around the concept of trajectory, a common path in the
simulation model for entities of the same type.
Documentation about 'simmer' is provided by several vignettes included in
this package, via the paper by Ucar, Smeets & Azcorra (2019,
<doi:10.18637/jss.v090.i02>), and the paper by Ucar, Hernández, Serrano &
Azcorra (2018, <doi:10.1109/MCOM.2018.1700960>); see 'citation("simmer")'
for details.

%package devel
Summary:        Development Files for R-%{packname}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       R-core-devel%{?_isa}

%description devel
Header files for %{packname}.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
export LANG=C.UTF-8
export _R_CHECK_FORCE_SUGGESTS_=0
%{_bindir}/R CMD check --no-manual --ignore-vignettes %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

%files devel
%{rlibdir}/%{packname}/include

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Iñaki Úcar <iucar@fedoraproject.org> - 4.4.6.1-1
- Update to 4.4.6.1, switch to SPDX

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 4.4.5-5
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 4.4.5-3
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 25 2022 Iñaki Úcar <iucar@fedoraproject.org> - 4.4.5-1
- Update to 4.4.5

* Mon Feb 07 2022 Iñaki Úcar <iucar@fedoraproject.org> - 4.4.4-1
- Update to 4.4.4

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 12 2021 Iñaki Úcar <iucar@fedoraproject.org> - 4.4.3-1
- Update to 4.4.3

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 4.4.2-6
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 4.4.2-2
- rebuild for R 4

* Sat Jun 06 2020 Iñaki Úcar <iucar@fedoraproject.org> - 4.4.2-1
- Update to 4.4.2

* Sat Apr 11 2020 Iñaki Úcar <iucar@fedoraproject.org> - 4.4.1-1
- Update to 4.4.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Iñaki Úcar <iucar@fedoraproject.org> - 4.4.0-1
- Update to 4.4.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.3.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.3.0-2
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 31 2019 Iñaki Úcar <iucar@fedoraproject.org> - 4.3.0-1
- Update to 4.3.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Iñaki Úcar <iucar@fedoraproject.org> - 4.2.2-1
- Update to 4.2.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Iñaki Úcar <iucar@fedoraproject.org> - 4.2.1-1
- Update to 4.2.1

* Fri Nov 09 2018 Iñaki Úcar <iucar@fedoraproject.org> - 4.1.0-1
- Update to 4.1.0

* Wed Sep 19 2018 Iñaki Úcar <iucar@fedoraproject.org> - 4.0.1-1
- Update to 4.0.1
- Reflow indentations

* Mon Jul 30 2018 Iñaki Úcar <i.ucar86@gmail.com> - 4.0.0-2
- Capitalize summary
- Remove 'Group', not used in Fedora
- Remove rm of buildroot, not needed

* Mon Jul 30 2018 Iñaki Úcar <i.ucar86@gmail.com> - 4.0.0-1
- Initial package creation
