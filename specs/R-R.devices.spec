%global packname R.devices
%global packver  2.17.1
%global rlibdir  %{_datadir}/R/library

# R.rsp is a Suggests loop.
%global with_loop 0

Name:             R-%{packname}
Version:          %{packver}
Release:          10%{?dist}
Summary:          Unified Handling of Graphics Devices

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:          LicenseRef-Callaway-LGPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-grDevices, R-R.methodsS3 >= 1.8.1, R-R.oo >= 1.24.0, R-R.utils >= 2.10.1, R-base64enc >= 0.1-2
# Suggests:  R-digest >= 0.6.13, R-Cairo >= 1.5-9, R-R.rsp
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-grDevices
BuildRequires:    R-R.methodsS3 >= 1.8.1
BuildRequires:    R-R.oo >= 1.24.0
BuildRequires:    R-R.utils >= 2.10.1
BuildRequires:    R-base64enc >= 0.1.2
BuildRequires:    R-digest >= 0.6.13
BuildRequires:    R-Cairo >= 1.5.9
%if %{with_loop}
BuildRequires:    R-R.rsp
%endif

%description
Functions for creating plots and image files in a unified way regardless of
output format (EPS, PDF, PNG, SVG, TIFF, WMF, etc.). Default device options
as well as scales and aspect ratios are controlled in a uniform way across
all device types. Switching output format requires minimal changes in code.
This package is ideal for large-scale batch processing, because it will
never leave open graphics devices or incomplete image files behind, even on
errors or user interrupts.


%prep
%setup -q -c -n %{packname}

for file in %{packname}/inst/doc/R.devices-overview.tex.rsp; do
    sed "s|\r||g" ${file} > ${file}.new
    touch -r ${file} ${file}.new
    mv ${file}.new ${file}
done


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with_loop}
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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/exdata


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.17.1-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.17.1-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.17.1-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 24 2022 Tom Callaway <spot@fedoraproject.org> - 2.17.1-1
- update to 2.17.1
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 2.17.0-2
- Rebuilt for R 4.1.0

* Sun Feb 07 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.17.0-1
- Update to latest version (#1918023)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 2.16.1-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.16.1-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.16.0-4
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.16.0-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.15.1-2
- Fix some file line endings

* Sun Apr 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.15.1-1
- initial package for Fedora
