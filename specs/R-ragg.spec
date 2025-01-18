%global packname ragg
%global packver  1.2.4
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          9%{?dist}
Summary:          Graphic Devices Based on AGG

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-systemfonts >= 1.0.3, R-textshaping >= 0.3.0
# Suggests:  R-covr, R-testthat, R-grid, R-graphics
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-systemfonts-devel >= 1.0.3
BuildRequires:    R-textshaping-devel >= 0.3.0
BuildRequires:    R-testthat
BuildRequires:    R-grid
BuildRequires:    R-graphics

BuildRequires:    gcc-c++
BuildRequires:    pkgconfig(freetype2)
BuildRequires:    pkgconfig(libpng)
BuildRequires:    pkgconfig(libtiff-4)
BuildRequires:    libjpeg-devel

%description
Anti-Grain Geometry (AGG) is a high-quality and high-performance 2D drawing
library. The 'ragg' package provides a set of graphic devices based on AGG
to use as alternative to the raster devices provided through the
'grDevices' package.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


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
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.4-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.4-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 24 2022 Tom Callaway <spot@fedoraproject.org> - 1.2.4-1
- update to 1.2.4

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 1.2.2-1
- update to 1.2.2
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 1.1.3-1
- update to 1.1.3
- Rebuilt for R 4.1.0

* Sun Mar 21 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.2-1
- Update to latest version (#1940017)

* Sat Feb 27 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- Update to latest version (#1933092)

* Tue Feb 23 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest version (#1915004)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.0-1
- Update to latest version (#1885208)

* Fri Aug 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-2
- Rebuild to fix dist tag

* Mon Aug 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-1
- initial package for Fedora
