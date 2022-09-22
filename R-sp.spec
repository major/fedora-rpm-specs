%global packname sp
%global packver  1.5-0
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((gstat|maptools)\\)

# Limit loops and extra dependencies.
%global with_suggests 0
# rgeos requires sp; this only suggests it.
%global with_loop 0

Name:             R-%{packname}
Version:          1.5.0
Release:          1%{?dist}
Summary:          Classes and Methods for Spatial Data

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-utils, R-stats, R-graphics, R-grDevices, R-lattice, R-grid
# Suggests:  R-RColorBrewer, R-rgdal >= 1.2-3, R-rgeos >= 0.3-13, R-gstat, R-maptools, R-deldir
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-utils
BuildRequires:    R-stats
BuildRequires:    R-graphics
BuildRequires:    R-grDevices
BuildRequires:    R-lattice
BuildRequires:    R-grid
%if 0%{with_suggests}
BuildRequires:    R-RColorBrewer
BuildRequires:    R-rgdal >= 1.2.3
BuildRequires:    R-gstat
BuildRequires:    R-maptools
BuildRequires:    R-deldir
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-sf
%if 0%{with_loop}
BuildRequires:    R-rgeos >= 0.3.13
%endif
%endif

%description
Classes and methods for spatial data; the classes document where the spatial
location information resides, for 2D or 3D data. Utility functions are
provided, e.g. for plotting data as maps, spatial selection, as well as methods
for retrieving coordinates, for subsetting, print, summary, etc.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with_suggests}
%if %{with_loop}
%{_bindir}/R CMD check %{packname}
%else
rm %{packname}/tests/agg.R* %{packname}/tests/over2.R*  # whole file requires rgeos
%{_bindir}/R CMD check %{packname} --no-examples --no-vignettes
%endif
%else
rm %{packname}/tests/agg.R* %{packname}/tests/over2.R*  # whole file requires rgeos
_R_CHECK_FORCE_SUGGESTS_=0 \
    %{_bindir}/R CMD check %{packname} --no-examples --no-vignettes
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/external
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so

%files devel
%{rlibdir}/%{packname}/include


%changelog
* Fri Aug 19 2022 Tom Callaway <spot@fedoraproject.org> - 1.5.0-1
- update to 1.5-0
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 1.4.5-3
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.5-1
- Update to latest version (#1914654)

* Thu Oct 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.4-1
- Update to latest version (#1886138)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 1.4.2-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.2-1
- Update to latest version

* Fri Feb 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.1-1
- Update to latest version

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 1.2.7-2
- rebuild for R 3.5.0

* Mon Mar 26 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.7-1
- Update to latest version.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.5-4
- Move some Requires to Suggests.

* Fri Sep 01 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.5-3
- Split headers into -devel package.

* Fri Sep 01 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.5-2
- new package built with tito

* Fri Sep 01 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.5-1
- initial package for Fedora
