%global packname rgeos
%global packver  0.6
%global packrev  2
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((maptools)\\)

# Suggests loops with maps and maptools.
%bcond_with suggests

Name:             R-%{packname}
Version:          %{packver}.%{packrev}
Release:          1%{?dist}
Summary:          Interface to Geometry Engine - Open Source ('GEOS')

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}-%{packrev}.tar.gz
# Not yet sure why this is necessary.
Patch0001:        %{packname}-Be-explicit-about-sp.patch

# Here's the R view of the dependencies world:
# Depends:   R-methods, R-sp >= 1.1-0
# Imports:   R-utils, R-stats, R-graphics
# Suggests:  R-maptools >= 0.8-5, R-testthat, R-XML, R-maps, R-rgdal
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    geos-devel >= 3.2.0
BuildRequires:    R-methods
BuildRequires:    R-sp-devel >= 1.1.0
BuildRequires:    R-utils
BuildRequires:    R-stats
BuildRequires:    R-graphics
BuildRequires:    R-testthat
BuildRequires:    R-XML
BuildRequires:    R-rgdal
%if %{with suggests}
BuildRequires:    R-maptools >= 0.8.5
BuildRequires:    R-maps
%endif

%description
Interface to Geometry Engine - Open Source ('GEOS') using the C 'API' for
topology operations on geometries.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch0001 -p1
popd

# Not important.
rm %{packname}/inst/SVN_VERSION


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
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/README
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/poly-ex-gpc
%{rlibdir}/%{packname}/test_cases
%{rlibdir}/%{packname}/wkts


%changelog
* Fri Mar  3 2023 Tom Callaway <spot@fedoraproject.org> - 0.6.2-1
- update to 0.6-2

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 0.5.9-1
- update to 0.5-9
- bootstrap on
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 21 2021 Sandro Mani <manisandro@gmail.com> - 0.5.8-1
- Update to 0.5.8 for geos 3.10 support

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 0.5.5-4
- Rebuilt for R 4.1.0

* Sat Feb 13 2021 Sandro Mani <manisandro@gmail.com> - 0.5.5-3
- Rebuild (geos)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.5-1
- Update to latest version (#1876574)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.5.3-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.3-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.2-1
- Update to latest version

* Sat Aug 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.1-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.3-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.3-1
- Update to latest version

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.2-1
- Update to latest version

* Tue Feb 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.28-4
- Rebuilt for updated Proj

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.28-1
- Update to latest version

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 0.3.26-2
- rebuild for R 3.5.0

* Mon Mar 26 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.26-1
- initial package for Fedora
