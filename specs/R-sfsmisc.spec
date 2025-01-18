%global packname sfsmisc
%global packver  1.1
%global packrev  15
%global rlibdir  %{_datadir}/R/library

%bcond_with suggests

Name:             R-%{packname}
Version:          %{packver}.%{packrev}
Release:          7%{?dist}
Summary:          Utilities from 'Seminar fuer Statistik' ETH Zurich

License:          GPL-2.0-or-later
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}-%{packrev}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-grDevices, R-utils, R-stats, R-tools
# Suggests:  R-datasets, R-tcltk, R-cluster, R-lattice, R-MASS, R-Matrix, R-nlme, R-lokern, R-Rmpfr, R-gmp
# LinkingTo:
# Enhances:

BuildArch:        noarch
Suggests:         procps-ng
BuildRequires:    procps-ng
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-grDevices
BuildRequires:    R-utils
BuildRequires:    R-stats
BuildRequires:    R-tools
%if %{with suggests}
BuildRequires:    R-datasets
BuildRequires:    R-tcltk
BuildRequires:    R-cluster
BuildRequires:    R-lattice
BuildRequires:    R-MASS
BuildRequires:    R-Matrix
BuildRequires:    R-nlme
BuildRequires:    R-lokern
BuildRequires:    R-Rmpfr
BuildRequires:    R-gmp
%endif

%description
Useful utilities ['goodies'] from Seminar fuer Statistik ETH Zurich, some
of which were ported from S-plus in the 1990s. For graphics, have pretty
(Log-scale) axes, an enhanced Tukey-Anscombe plot, combining histogram and
boxplot, 2d-residual plots, a 'tachoPlot()', pretty arrows, etc. For
robustness, have a robust F test and robust range(). For system support,
notably on Linux, provides 'Sys.*()' functions with more access to system
and CPU information. Finally, miscellaneous utilities such as simple
efficient prime numbers, integer codes, Duplicated(), toLatex.numeric() and
is.whole().


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
%if %{with suggests}
%{_bindir}/R CMD check --no-examples %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check --no-examples --no-vignettes %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/ChangeLog
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.1.15-5
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May  1 2023 Tom Callaway <spot@fedoraproject.org> - 1.1.15-1
- update to 1.1-15
- make suggests conditional

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.1.13-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 1.1.13-1
- update to 1.1-13
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 1.1.11-3
- bootstrap off

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 1.1.11-2
- Rebuilt for R 4.1.0
- bootstrap

* Sat Apr 24 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.11-1
- Update to latest version (#1948489)

* Sat Apr 03 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.10-1
- Update to latest version (#1944364)

* Fri Mar 26 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.9-1
- Update to latest version (#1942089)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.8-1
- Update to latest version (#1913723)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.7-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.7-1
- Update to latest version

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.5-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.4-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.4-1
- Update to latest version

* Fri Feb 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.3-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.2-1
- initial package for Fedora
