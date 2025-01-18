%global packname tinytex
%global packver  0.45
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          8%{?dist}
Summary:          Helper Functions to Install and Maintain TeX Live, and Compile LaTeX Documents

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-xfun >= 0.29
# Suggests:  R-testit, R-rstudioapi
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-xfun >= 0.29
BuildRequires:    R-testit
BuildRequires:    R-rstudioapi

%description
Helper functions to install and maintain the 'LaTeX' distribution named
'TinyTeX' (<https://yihui.org/tinytex/>), a lightweight, cross-platform,
portable, and easy-to-maintain version of 'TeX Live'. This package also
contains helper functions to compile 'LaTeX' documents, and install missing
'LaTeX' packages automatically.


%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%doc %{rlibdir}/%{packname}/CITATION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.45-6
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.45-2
- R-maint-sig mass rebuild

* Wed Apr 19 2023 Tom Callaway <spot@fedoraproject.org> - 0.45-1
- update to 0.45

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 27 2022 Tom Callaway <spot@fedoraproject.org> - 0.42-1
- update to 0.42

* Thu Aug 25 2022 Tom Callaway <spot@fedoraproject.org> - 0.41-1
- update to 0.41
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Tom Callaway <spot@fedoraproject.org> - 0.32-1
- Update to 0.32
- Rebuilt for R 4.1.0

* Sat Apr 03 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.31-1
- Update to latest version (#1944869)

* Fri Mar 05 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.30-1
- Update to latest version (#1935009)

* Sun Feb 07 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.29-1
- Update to latest version (#1918596)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.28-1
- Update to latest version (#1907324)

* Sun Nov 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.27-1
- Update to latest version (#1893509)

* Wed Sep 23 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.26-1
- Update to latest version (#1881355)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.25-1
- Update to latest version

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.24-1
- Update to latest version

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 0.23-1
- update to 0.23
- rebuild for R 4

* Wed Feb 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.20-1
- Update to latest version

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.19-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.18-1
- Update to latest version

* Wed Oct 30 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.17-1
- Update to latest version

* Wed Sep 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.16-1
- Update to latest version

* Sat Aug 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.15-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.14-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.14-1
- Update to latest version

* Tue May 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.13-1
- Update to latest version

* Thu Apr 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.12-1
- Update to latest version

* Tue Mar 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.11-1
- Update to latest version

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.10-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6-1
- Update to latest version

* Sat May 12 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5-1
- initial package for Fedora
