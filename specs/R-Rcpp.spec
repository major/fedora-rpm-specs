%global packname Rcpp

%global __suggests_exclude ^R\\((pkgKitten|rbenchmark|tinytest)\\)

Name:		R-%{packname}
Version:	1.0.14
Release:	1%{?dist}
Summary:	Seamless R and C++ Integration

#		The following three files uses the Boost Software License:
#		- Rcpp/inst/include/Rcpp/utils/tinyformat/tinyformat.h
#		- Rcpp/inst/include/Rcpp/macros/config.hpp
#		- Rcpp/inst/include/Rcpp/macros/cat.hpp
License:	GPL-2.0-or-later AND BSL-1.0
URL:		https://cran.r-project.org/package=%{packname}
Source0:	%{url}&version=%{version}#/%{packname}_%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	R-core-devel
BuildRequires:	R-inline
BuildRequires:	dos2unix
BuildRequires:	tex(latex)
%if %{?fedora}%{!?fedora:0} >= 38
BuildRequires:	tex(inconsolata.sty)
%endif
BuildRequires:	R-rpm-macros

%description
The Rcpp package provides R functions as well as C++ classes which
offer a seamless integration of R and C++. Many R data types and
objects can be mapped back and forth to C++ equivalents which
facilitates both writing of new code as well as easier integration of
third-party libraries.
Documentation about Rcpp is provided by several vignettes included in
this package, via the Rcpp Gallery site at http://gallery.rcpp.org,
the paper by Eddelbuettel and Francois (2011, JSS), and the book by
Eddelbuettel (2013, Springer).
See citation("Rcpp") for details on the last two.

%package devel
Summary:	Rcpp Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	R-core-devel%{?_isa}

%description devel
Header files for Rcpp.

%package examples
Summary:	Rcpp Examples
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description examples
Examples for using Rcpp.

%prep
%setup -q -c

dos2unix -k \
    %{packname}/inst/tinytest/cpp/InternalFunction.cpp \
    %{packname}/inst/tinytest/cpp/InternalFunctionCPP11.cpp

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l %{buildroot}%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css
rm -rf %{buildroot}%{_libdir}/R/library/%{packname}/tinytest

sed 's!/bin/env Rscript!/usr/bin/Rscript!' \
    -i %{buildroot}%{_libdir}/R/library/%{packname}/discovery/cxx0x.R
chmod 755 %{buildroot}%{_libdir}/R/library/%{packname}/discovery/cxx0x.R

for f in ConvolveBenchmarks/overhead.r ConvolveBenchmarks/overhead.sh \
	 Misc/ifelseLooped.r Misc/newFib.r OpenMP/OpenMPandInline.r ; do
    chmod 755 %{buildroot}%{_libdir}/R/library/%{packname}/examples/$f
done

for f in `find %{buildroot}%{_libdir}/R/library/%{packname}/examples -type f` ; do
    grep -q '/usr/bin/env r' $f && sed 's!/usr/bin/env r!/usr/bin/r!' -i $f
done

%check
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/NEWS.Rd
%doc %{_libdir}/R/library/%{packname}/announce
%doc %{_libdir}/R/library/%{packname}/bib
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/CITATION
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/discovery
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/R/library/%{packname}/prompt
%{_libdir}/R/library/%{packname}/skeleton

%files devel
%{_libdir}/R/library/%{packname}/include

%files examples
%{_libdir}/R/library/%{packname}/examples

%changelog
* Wed Jan 22 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0.14-1
- Update to 1.0.14

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 08 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0.13-2
- Require R >= 4.5.0 for new APIs (backport from upstream)

* Thu Jul 18 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0.13-1
- Update to 1.0.13

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.0.12-4
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0.12-1
- Update to 1.0.12

* Sun Jul 23 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0.11-3
- Fix build requires

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.0.11-1
- Update to 1.0.11, switch to SPDX

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.0.10-2
- R-maint-sig mass rebuild

* Tue Jan 24 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0.10-1
- Update to 1.0.10

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 24 2022 Tom Callaway <spot@fedoraproject.org> - 1.0.9-3
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0.9-1
- Update to 1.0.9

* Wed Apr 06 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0.8.3-1
- Update to 1.0.8.3

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0.8-1
- Update to 1.0.8

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 21 2021 Tom Callaway <spot@fedoraproject.org> - 1.0.7-2
- rebuild for R 4.1.0 (epel8)

* Thu Jul 08 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0.7-1
- Update to 1.0.7

* Mon Jun 07 2021 Tom Callaway <spot@fedoraproject.org> - 1.0.6-3
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0.6-1
- Update to 1.0.6

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0.5-1
- Update to 1.0.5

* Wed Jun 03 2020 Tom Callaway <spot@fedoraproject.org> - 1.0.4.6-1
- update to 1.0.4.6, rebuild for R 4

* Sat Mar 21 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0.4-2
- Fix for linking error seen when using root's R interface:
  "You are probably missing the definition of Rcpp::demangler_one(char const*)"

* Fri Mar 20 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0.4-1
- Update to 1.0.4
- The package no longer uses knitr for vignettes, drop --ignore-vignettes

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-2
- Exclude Suggests for unavailable packages

* Mon Nov 11 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0.3-1
- Update to 1.0.3

* Tue Aug 13 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0.2-1
- Update to 1.0.2

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-5
- rebuilt

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-4
- Remove explicit dependencies provided by automatic dependency generator

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-3
- Rebuild with automatic Provides

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0.1-1
- Update to 1.0.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0.0-1
- Update to 1.0.0

* Mon Oct 22 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.12.19-1
- Update to 0.12.19

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.12.18-2
- Rebuild with fixed binutils

* Sat Jul 28 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.12.18-1
- Update to 0.12.18

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 22 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.12.17-1
- Update to 0.12.17

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 0.12.16-2.1
- actually build against R 3.5.0

* Wed May 16 2018 TOm Callaway <spot@fedoraproject.org> - 0.12.16-2
- rebuild for R 3.5.0

* Wed Mar 14 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.12.16-1
- Update to 0.12.16

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.12.15-1
- Update to 0.12.15

* Sat Nov 25 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.12.14-1
- Update to 0.12.14

* Thu Oct 05 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.12.13-1
- Update to 0.12.13
- The package has changed vignette builder from "highlight" to "knitr"
- The R-knitr package is not available in Fedora, so --ignore-vignettes was
  added to the R CMD check command
- Removed the build requires used only by the vignette checks

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.12.12-1
- Update to 0.12.12

* Mon May 22 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.12.11-1
- Update to 0.12.11

* Mon Mar 20 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.12.10-1
- Update to 0.12.10
- Add tex BuildRequires for EPEL 7 (now provided by texlive-extension package)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.12.9-1
- Update to 0.12.9

* Fri Dec 02 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.12.8-1
- Update to 0.12.8

* Tue Sep 06 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.12.7-1
- Update to 0.12.7

* Fri Jul 22 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.12.6-1
- Update to 0.12.6

* Tue May 24 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.12.5-1
- Update to 0.12.5

* Sun Apr 10 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.12.4-1
- Update to 0.12.4

* Tue Feb 23 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.12.3-3
- Adjust BuildRequires for EPEL
- Replace /usr/bin/env shebang
- Set executable permission on script with shebang

* Thu Feb 18 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.12.3-2
- Fix license tag (add Boost)

* Fri Feb 05 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.12.3-1
- Initial package creation
