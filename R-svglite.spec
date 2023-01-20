%global packname svglite
%global packver  2.1.0
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((fontquiver)\\)

%global with_suggests 0

Name:             R-%{packname}
Version:          %{packver}
Release:          2%{?dist}
Summary:          An 'SVG' Graphics Device

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-systemfonts >= 1.0.0
# Suggests:  R-htmltools, R-testthat, R-xml2 >= 1.0.0, R-covr, R-fontquiver >= 0.2.0, R-knitr, R-rmarkdown
# LinkingTo: R-cpp11, R-systemfonts
# Enhances:

BuildRequires:    libpng-devel
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-systemfonts-devel >= 1.0.0
BuildRequires:    R-cpp11-devel
BuildRequires:    R-htmltools
BuildRequires:    R-testthat
BuildRequires:    R-xml2 >= 1.0.0
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
%if %{with_suggests}
BuildRequires:    R-fontquiver >= 0.2.0
%endif

%description
A graphics device for R that produces 'Scalable Vector Graphics'. 'svglite'
is a fork of the older 'RSvgDevice' package.


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
export LANG=C.UTF-8
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-tests
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 2.1.0-1
- update to 2.1.0
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 2.0.0-2
- Rebuilt for R 4.1.0

* Tue Feb 23 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.0-1
- Update to latest version (#1931003)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.3.2-1
- Update to latest version

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.2.3-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.3-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.2-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.2-1
- Update to latest version

* Wed Mar 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.1-1
- initial package for Fedora
