%global packname systemfonts
%global packver  1.0.4
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          5%{?dist}
Summary:          System Native Font Finding

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-testthat >= 2.1.0, R-covr, R-knitr, R-rmarkdown, R-tools
# LinkingTo: R-cpp11 >= 0.2.1
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cpp11-devel >= 0.2.1
BuildRequires:    R-testthat >= 2.1.0
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-tools
BuildRequires:    pkgconfig(fontconfig)

%description
Provides system native access to the font catalogue. As font handling
varies between systems it is difficult to correctly locate installed fonts
across different operating systems. The 'systemfonts' package provides
bindings to the native libraries on Windows, macOS and Linux for finding
font files that can then be used further by e.g. graphic devices. The main
use is intended to be from compiled code but 'systemfonts' also provides
access from R.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' DESCRIPTION

chmod -x src/*.* src/unix/*.*
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check --ignore-vignettes %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
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
%{rlibdir}/%{packname}/unfont.ttf

%files devel
%{rlibdir}/%{packname}/include


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.0.4-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 1.0.4-1
- update to 1.0.4
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 1.0.2-1
- update to 1.0.2
- Rebuilt for R 4.1.0

* Tue Feb 23 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-1
- Update to latest version (#1923756)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.2-1
- Update to latest version (#1883682)

* Wed Sep 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-1
- Update to latest version (#1876947)

* Thu Sep 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-1
- Update to latest version (#1874447)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 0.2.2-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.1-1
- initial package for Fedora
