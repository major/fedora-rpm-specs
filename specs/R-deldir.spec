%global packname deldir
%global packver  1.0-6
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0.6
Release:          10%{?dist}
Summary:          Delaunay Triangulation and Dirichlet (Voronoi) Tessellation

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-graphics, R-grDevices
# Suggests:  R-polyclip
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-graphics
BuildRequires:    R-grDevices
BuildRequires:    R-polyclip

%description
Calculates the Delaunay triangulation and the Dirichlet or Voronoi
tessellation (with respect to the entire plane) of a planar point set.
Plots triangulations and tessellations in various ways.  Clips
tessellations to sub-windows. Calculates perimeters of tessellations.
Summarises information about the tiles of the tessellation.


%prep
%setup -q -c -n %{packname}

# Remove extraneous source code.
rm -r %{packname}/inst/code.discarded
rm -r %{packname}/inst/ratfor
rm -r %{packname}/inst/SavedRatfor


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/READ_ME
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/data


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.6-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.0.6-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.0.6-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug  3 2022 Tom Callaway <spot@fedoraproject.org> - 1.0.6-1
- update to 1.0-6
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 0.2.10-2
- Rebuilt for R 4.1.0

* Tue Feb 23 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.10-1
- Update to latest version (#1916988)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.3-1
- Update to latest version (#1895987)

* Fri Nov 06 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-1
- Update to latest version (#1894843)

* Tue Sep 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.29-1
- Update to latest version (#1878510)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.28-1
- Update to latest version

* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 0.1.25-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.25-1
- Update to latest version

* Sun Feb 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.23-3
- Fix rank mismatch build errors

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.23-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.22-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.22-1
- Update to latest version

* Sat Jun 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.21-1
- Update to latest version

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.16-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 0.1.15-2
- rebuild for R 3.5.0

* Wed Apr 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.15-1
- Update to latest version

* Wed Mar 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.14-1
- initial package for Fedora
