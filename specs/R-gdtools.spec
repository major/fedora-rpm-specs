%global packname gdtools
%global packver  0.2.4
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((fontquiver)\\)

Name:             R-%{packname}
Version:          0.2.4
Release:          10%{?dist}
Summary:          Utilities for Graphical Rendering

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:          GPL-3.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
Patch0:           0001-format-security-fix.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-Rcpp >= 0.12.12, R-systemfonts >= 0.1.1
# Suggests:  R-htmltools, R-testthat, R-fontquiver >= 0.2.0, R-curl
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-Rcpp-devel >= 0.12.12
BuildRequires:    R-systemfonts >= 0.1.1
BuildRequires:    cairo-devel
BuildRequires:    R-htmltools
BuildRequires:    R-testthat

%description
Useful tools for writing vector graphics devices.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}
pushd %{packname}
%patch -P0 -p1
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
# Don't need fontquiver or curl.
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so

%files devel
%{rlibdir}/%{packname}/include


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.4-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.2.4-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.2.4-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 0.2.4-1
- update to 0.2.4
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 0.2.3-3
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.3-1
- Update to latest version (#1913461)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.2.2-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-1
- Update to latest version

* Mon Sep 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.9-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.9-1
- Update to latest version

* Sun Apr 07 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.8-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 0.1.7-3
- rebuild for R 3.5.0

* Sun Mar 18 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.7-2
- Add missing Rcpp Requires.

* Thu Mar 08 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.7-1
- initial package for Fedora
