%global packname showtextdb
%global packver  3.0
%global rlibdir  %{_datadir}/R/library

# Examples use the network.
%bcond_with network

Name:             R-%{packname}
Version:          %{packver}
Release:          18%{?dist}
Summary:          Font Files for the 'showtext' Package

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:          Apache-2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
Patch0001:        0001-Load-existing-font-file.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-sysfonts >= 0.7, R-utils
# Suggests:  R-curl
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         wqy-microhei-fonts
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    wqy-microhei-fonts
BuildRequires:    R-sysfonts >= 0.7
BuildRequires:    R-utils
BuildRequires:    R-curl

%description
Providing font files that can be used by the 'showtext' package.


%prep
%setup -q -c -n %{packname}

# Remove bundled font references.
pushd %{packname}
rm inst/AUTHORS inst/COPYRIGHTS
%patch -P0001 -p1
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Replace fonts by system fonts (note that this cannot be done in prep because
# R CMD INSTALL copies symlink targets.)
pushd %{buildroot}%{rlibdir}/%{packname}
rm fonts/*
%if 0%{?fedora} >= 39
ln -s /usr/share/fonts/wqy-microhei-fonts/wqy-microhei.ttc fonts/wqy-microhei.ttc
%else
ln -s /usr/share/fonts/wqy-microhei/wqy-microhei.ttc fonts/wqy-microhei.ttc
%endif
popd


%check
%if %{with network}
%{_bindir}/R CMD check %{packname}
%else
%{_bindir}/R CMD check %{packname} --no-examples
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/fonts


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul  24 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0-17
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 3.0-15
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 12 2023 Iñaki Úcar <iucar@fedoraproject.org> - 3.0-11
- Fix font path

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 3.0-10
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 3.0-8
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 3.0-4
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0-1
- Update to latest version

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 2.0-8
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0-6
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0-3
- Fix unbundling of fonts

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 02 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0-1
- initial package for Fedora
