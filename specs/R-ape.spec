%global packname ape
%global packver  5.7
%global packrev  1
%global rlibdir  %{_libdir}/R/library

# Cannot enable until phangorn is added
%global with_suggests 0

%bcond_with bootstrap

Name:             R-%{packname}
Version:          %{packver}.%{packrev}
Release:          8%{?dist}
Summary:          Analyses of Phylogenetics and Evolution

License:          GPL-2.0-only OR GPL-3.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}-%{packrev}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-nlme, R-lattice, R-graphics, R-methods, R-stats, R-utils, R-parallel, R-Rcpp >= 0.12.0, R-digest
# Suggests:  R-gee, R-expm, R-igraph, R-phangorn
# LinkingTo: R-Rcpp
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-nlme
BuildRequires:    R-lattice
BuildRequires:    R-graphics
BuildRequires:    R-methods
BuildRequires:    R-stats
BuildRequires:    R-utils
BuildRequires:    R-parallel
BuildRequires:    R-Rcpp-devel >= 0.12.0
BuildRequires:    R-digest
%if %{without bootstrap}
BuildRequires:    R-gee
BuildRequires:    R-expm
BuildRequires:    R-igraph
%if %{with_suggests}
BuildRequires:    R-phangorn
%endif
%endif

%description
Functions for reading, writing, plotting, and manipulating phylogenetic
trees, analyses of comparative data in a phylogenetic framework, ancestral
character analyses, analyses of diversification and macroevolution,
computing distances from DNA sequences, reading and writing nucleotide
sequences as well as importing from BioConductor, and several tools such as
Mantel's test, generalized skyline plots, graphical exploration of
phylogenetic data (alex, trex, kronoviz), estimation of absolute
evolutionary rates and clock-like trees using mean path lengths and
penalized likelihood, dating trees with non-contemporaneous sequences,
translating DNA into AA sequences, and assessing sequence alignments.
Phylogeny estimation can be done with the NJ, BIONJ, ME, MVR, SDM, and
triangle methods, and several methods handling incomplete distance matrices
(NJ*, BIONJ*, MVR*, and the corresponding triangle method). Some functions call
external applications (PhyML, Clustal, T-Coffee, Muscle) whose results are
returned into R.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{without bootstrap}
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-examples
%endif
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/data


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 5.7.1-6
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 5.7.1-2
- R-maint-sig mass rebuild

* Mon Mar 13 2023 Tom Callaway <spot@fedoraproject.org> - 5.7.1-1
- update to 5.7-1

* Sun Jan 22 2023 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.6.2-3
- Drop support for i686
- Switch to SPDX licenses

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 5.6.2-1
- update to 5.6-2
- rebuild for R 4.2.1
- bootstrap on

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 5.5-2
- bootstrap off, but rework check logic around missing phangorn

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 5.5-1
- update to 5.5
- bootstrap
- Rebuilt for R 4.1.0

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 5.4.1-3
- rebuild for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.4.1-1
- Update to latest version (#1868589)

* Mon Aug 10 2020 Tom Callaway <spot@fedoraproject.org> - 5.4-3
- rebuild for FlexiBLAS R

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.4-1
- Update to latest version

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 5.3-7
- rebuild for R 4
- turnoff bootstrap

* Sun Feb 23 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.3-6
- Add bootstrap setup to build without igraph

* Tue Feb 18 2020 Tom Callaway <spot@fedoraproject.org> - 5.3-5
- rebuild against R without libRlapack.so

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.3-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.3-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.2-1
- Update to latest version
- Re-enable build checks
- Re-arrange to match latest template

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 5.1-1
- update to 5.1, rebuild for R 3.5.0

* Fri Mar 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.0-1
- initial package for Fedora
