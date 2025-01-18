%global packname igraph
%global packver  2.0.3
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((graph|igraphdata|rgl)\\)

# Some loops; some unavailable yet.
%global with_suggests 0
# Examples use the network.
%bcond_with network

Name:             R-%{packname}
Version:          %{packver}
Release:          3%{?dist}
Summary:          Network Analysis and Visualization

# Main: GPLv2+; html_library.tcl: TCL
License:          GPL-2.0-or-later AND TCL
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
# Unbundle some things:
Patch0002:        0002-Unbundle-uuid.patch
Patch0003:        0003-Unbundle-arpack.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-graphics, R-grDevices, R-magrittr, R-Matrix, R-pkgconfig >= 2.0.0, R-rlang, R-stats, R-utils
# Suggests:  R-ape, R-digest, R-graph, R-igraphdata, R-rgl, R-scales, R-stats4, R-tcltk, R-testthat, R-withr, R-vdiffr, R-knitr, R-rmarkdown
# LinkingTo: R-cpp11
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cpp11-devel >= 0.4.7
BuildRequires:    gcc-c++
BuildRequires:    R-methods
BuildRequires:    R-cli
BuildRequires:    R-graphics
BuildRequires:    R-grDevices
BuildRequires:    R-lifecycle
BuildRequires:    R-magrittr
BuildRequires:    R-Matrix
BuildRequires:    R-pkgconfig >= 2.0.0
BuildRequires:    R-rlang
BuildRequires:    R-stats
BuildRequires:    R-utils
BuildRequires:    R-vctrs
BuildRequires:    R-callr
BuildRequires:    R-digest
BuildRequires:    R-stats4
BuildRequires:    R-tcltk
BuildRequires:    R-testthat
BuildRequires:    R-withr
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
%if %{with_suggests}
BuildRequires:    R-ape
BuildRequires:    R-decor
BuildRequires:    R-graph
BuildRequires:    R-igraphdata
BuildRequires:    R-rgl
BuildRequires:    R-scales
# As of 1.4.0, we cannot run the tests without this...
BuildRequires:    R-vdiffr
%endif
BuildRequires:    arpack-devel
BuildRequires:    glpk-devel
BuildRequires:    gmp-devel
BuildRequires:    libuuid-devel
BuildRequires:    libxml2-devel
BuildRequires:    flexiblas-devel

# https://github.com/igraph/rigraph/issues/268
# Not a released version.
Provides: bundled(igraph) = 857a125069c226f266562b3781b82833fe1d59d9

%description
Routines for simple graphs and network analysis. It can handle large graphs
very well and provides functions for generating random and regular graphs,
graph visualization, centrality methods and much more.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch -P0002 -p1
%patch -P0003 -p1

# Fix executable files.
chmod -x src/vendor/simpleraytracer/*.*
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if !%{with network}
ARGS=--no-examples
%endif
%if %{with_suggests}
%{_bindir}/R CMD check %{packname} $ARGS
%else
# _R_CHECK_FORCE_SUGGESTS_=0 %%{_bindir}/R CMD check %%{packname} $ARGS
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/benchmarks
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/html_library.tcl
%license %{rlibdir}/%{packname}/html_library.license.terms
%{rlibdir}/%{packname}/igraph.gif
%{rlibdir}/%{packname}/igraph2.gif
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/lifecycle
%{rlibdir}/%{packname}/my_html_library.tcl
%{rlibdir}/%{packname}/tkigraph_help


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 26 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.0.3-1
- Update to latest version

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.3-5
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 22 2023 Tom Callaway <spot@fedoraproject.org> - 1.4.3-1
- update to 1.4.3

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.1-2
- R-maint-sig mass rebuild

* Fri Mar  3 2023 Tom Callaway <spot@fedoraproject.org> - 1.4.1-1
- update to 1.4.1

* Mon Feb 13 2023 Tom Callaway <spot@fedoraproject.org> - 1.4.0-1
- update to 1.4.0
- disable tests until R-vdiffr makes it into Fedora (if ever)

* Sun Jan 22 2023 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.5-3
- Drop support for i686
- Switch to SPDX licenses

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 22 2022 Tom Callaway <spot@fedoraproject.org> - 1.3.5-1
- update to 1.3.5

* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 1.3.4-1
- update to 1.3.4
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 1.2.6-3
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.6-1
- Update to latest version (#1885643)

* Mon Aug 10 2020 Tom Callaway <spot@fedoraproject.org> - 1.2.5-4
- rebuild for FlexiBLAS R

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 1.2.5-2
- move ape within the with_suggests conditional to break the loop
- rebuild for R 4

* Fri Mar 20 2020 Tom Callaway <spot@fedoraproject.org> - 1.2.5-1
- update to 1.2.5
- use bundled arpack for now

* Tue Feb 18 2020 Tom Callaway <spot@fedoraproject.org> - 1.2.4.2-3
- rebuild to remove dep on libRlapack.so

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.4.2-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.4.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.4.1-1
- Update to latest version

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.4-1
- Update to latest version

* Sun Feb 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.3-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.2-1
- Update to latest version

* Tue Jul 24 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.1-2
- Fix build on older Fedora

* Mon Jul 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.1-1
- initial package for Fedora
