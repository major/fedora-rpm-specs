%global packname rgdal
%global packver  1.5
%global packrev  32
%global rlibdir  %{_libdir}/R/library
%global with_suggests 0

Name:             R-%{packname}
Version:          %{packver}.%{packrev}
Release:          10%{?dist}
Summary:          Bindings for the 'Geospatial' Data Abstraction Library

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}-%{packrev}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods, R-sp >= 1.1-0
# Imports:   R-grDevices, R-graphics, R-stats, R-utils
# Suggests:  R-knitr, R-DBI, R-RSQLite, R-maptools, R-mapview, R-rmarkdown, R-curl, R-rgeos
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-sp-devel >= 1.1.0
BuildRequires:    R-grDevices
BuildRequires:    R-graphics
BuildRequires:    R-stats
BuildRequires:    R-utils
%if %{with_suggests}
BuildRequires:    R-knitr
BuildRequires:    R-DBI
BuildRequires:    R-RSQLite
BuildRequires:    R-maptools
BuildRequires:    R-mapview
BuildRequires:    R-rmarkdown
BuildRequires:    R-curl
BuildRequires:    R-rgeos
%endif
BuildRequires:    gdal-devel >= 1.11.4
BuildRequires:    proj-devel >= 4.8.0
BuildRequires:    sqlite-devel

%description
Provides bindings to the 'Geospatial' Data Abstraction Library ('GDAL') and
access to projection/transformation operations from the 'PROJ' library. Use is
made of classes defined in the 'sp' package. Raster and vector map data can be
imported into R, and raster and vector 'sp' objects exported. From 'rgdal'
1.5-8, installed with to 'GDAL' >=3, 'PROJ' >=6 and 'sp' >= 1.4, coordinate
reference systems use 'WKT2_2019' strings, not 'PROJ' strings.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
# Bundled projects.h from proj; not needed.
rm inst/include/projects.h
rmdir inst/include
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Remove unnecessary documentation.
rm %{buildroot}%{rlibdir}/%{packname}/README.windows
rm %{buildroot}%{rlibdir}/%{packname}/SVN_VERSION
# Remove unnecessary autoconf macros.
rm -r %{buildroot}%{rlibdir}/%{packname}/m4


%check
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --ignore-vignettes
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/README
%license %{rlibdir}/%{packname}/LICENSE.TXT
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/OSGeo4W_test
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/misc
%{rlibdir}/%{packname}/pictures
%{rlibdir}/%{packname}/vectors


%changelog
* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 1.5.32-1
- update to 1.5-32
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 1.5.23-9
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Thu Mar 10 2022 Sandro Mani <manisandro@gmail.com> - 1.5.23-8
- Rebuild for proj-9.0.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 1.5.23-6
- Rebuild (gdal)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 1.5.23-4
- Rebuilt for R 4.1.0

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 1.5.23-3
- Rebuild (gdal)

* Sun Mar 07 2021 Sandro Mani <manisandro@gmail.com> - 1.5.23-2
- Rebuild (proj)

* Sun Feb 07 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.23-1
- Update to latest version (#1921085)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.19-1
- Update to latest version (#1912680)

* Wed Nov 11 13:10:29 CET 2020 Sandro Mani <manisandro@gmail.com> - 1.5.18-2
- Rebuild (proj, gdal)

* Wed Oct 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.18-1
- Update to latest version (#1887906)

* Sat Oct 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.17-1
- Update to latest version (#1886385)

* Sat Aug 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.16-1
- Update to latest version
- rhbz#1867002

* Tue Aug 04 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.15-1
- Update to latest version
- rhbz#1841144

* Sun Aug 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.12-3
- Backport fix for CXXFLAGS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.12-1
- Update to latest version

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.5.8-1
- update to 1.5-8
- rebuild for R 4

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 1.4.8-4
- Rebuild (gdal)

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 1.4.8-3
- Rebuild (gdal)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.8-1
- Update to latest version

* Mon Oct 28 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.7-1
- Update to latest version

* Wed Oct 02 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.6-1
- Update to latest version

* Wed Sep 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.4-4
- Remove old proj subpackage dependencies

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.4-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.4-1
- Update to latest version

* Thu Mar 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.3-1
- Update to latest version

* Mon Mar 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.2-1
- Update to latest version

* Thu Feb 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.9-1
- Update to latest version

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.6-1
- Update to latest version

* Tue Feb 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.4-3
- Rebuilt for updated Proj

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 06 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.4-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.3-1
- Update to latest version

* Sat Jun 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- Update to latest version

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 1.2.20-2
- rebuild for R 3.5.0

* Mon May 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.20-1
- Update to latest version

* Tue Mar 20 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.18-1
- initial package for Fedora
