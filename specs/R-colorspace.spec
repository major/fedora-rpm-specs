%global packname colorspace
%global packver  2.0-3
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((kernlab|rcartocolor|scico|shinyjs|vcd|viridis)\\)

# Not yet available.
%global with_suggests 0

Name:             R-%{packname}
Version:          2.0.3
Release:          10%{?dist}
Summary:          A Toolbox for Manipulating and Assessing Colors and Palettes

# Automatically converted from old format: BSD - review is highly recommended.
License:          LicenseRef-Callaway-BSD
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-graphics, R-grDevices, R-stats
# Suggests:  R-datasets, R-utils, R-KernSmooth, R-MASS, R-kernlab, R-mvtnorm, R-vcd, R-tcltk, R-shiny, R-shinyjs, R-ggplot2, R-dplyr, R-scales, R-grid, R-png, R-jpeg, R-knitr, R-rmarkdown, R-RColorBrewer, R-rcartocolor, R-scico, R-viridis, R-wesanderson
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-graphics
BuildRequires:    R-grDevices
BuildRequires:    R-stats
%if %{with_suggests}
BuildRequires:    R-datasets
BuildRequires:    R-utils
BuildRequires:    R-KernSmooth
BuildRequires:    R-MASS
BuildRequires:    R-kernlab
BuildRequires:    R-mvtnorm
BuildRequires:    R-vcd
BuildRequires:    R-tcltk
BuildRequires:    R-shiny
BuildRequires:    R-shinyjs
BuildRequires:    R-ggplot2
BuildRequires:    R-dplyr
BuildRequires:    R-scales
BuildRequires:    R-grid
BuildRequires:    R-png
BuildRequires:    R-jpeg
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-RColorBrewer
BuildRequires:    R-rcartocolor
BuildRequires:    R-scico
BuildRequires:    R-viridis
BuildRequires:    R-wesanderson
%endif

%description
Carries out mapping between assorted color spaces including RGB, HSV, HLS,
CIEXYZ, CIELUV, HCL (polar CIELUV), CIELAB, and polar CIELAB. Qualitative,
sequential, and diverging color palettes based on HCL colors are provided along
with corresponding ggplot2 color scales. Color palette choice is aided by an
interactive app (with either a Tcl/Tk or a shiny graphical user interface) and
shiny apps with an HCL color picker and a color vision deficiency emulator.
Plotting functions for displaying and assessing palettes include color
swatches, visualizations of the HCL space, and trajectories in HCL and/or RGB
spectrum. Color manipulation functions include: desaturation,
lightening/darkening, mixing, and simulation of color vision deficiencies
(deutanomaly, protanomaly, tritanomaly). Details can be found on the project
web page at <http://colorspace.R-Forge.R-project.org/> and in the accompanying
scientific paper: Zeileis et al. (2020, Journal of Statistical Software,
<doi:10.18637/jss.v096.i01>).


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
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --ignore-vignettes --no-examples
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/CITATION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/cvdemulator
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/hclcolorpicker
%{rlibdir}/%{packname}/hclwizard
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.3-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.0.3-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.0.3-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug  2 2022 Tom Callaway <spot@fedoraproject.org> - 2.0.3-1
- update to 2.0-3
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 7  2021 Tom Callaway <spot@fedoraproject.org> - 2.0.1-1
- update to 2.0.1
- rebuild for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.0-1
- Update to latest version (#1896672)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 1.4.1-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.1-1
- Update to latest version

* Fri Feb 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 1.3.2-2
- rebuild for R 3.5.0

* Wed Apr 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- initial package for Fedora
