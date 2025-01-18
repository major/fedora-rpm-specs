%global packname BiocFileCache
%global packver 2.4.0

%global with_suggests 0
%global with_network 0

%if ! %{with_suggests}
%global __suggests_exclude ^R\\((BiocStyle)\\)
%endif

Name:             R-%{packname}
Version:          %{packver}
Release:          10%{?dist}
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{packver}.tar.gz
License:          Artistic-2.0
BuildArch:        noarch
URL:              http://www.bioconductor.org/packages/release/bioc/html/%{packname}.html
Summary:          Manage Files Across Sessions
BuildRequires:    R-devel >= 3.4.0, tetex-latex, R-dbplyr >= 1.0.0
BuildRequires:    R-methods, R-stats, R-utils, R-dplyr, R-RSQLite, R-DBI, R-rappdirs, R-filelock, R-curl, R-httr
# Suggests
BuildRequires:    R-rtracklayer, R-testthat, R-knitr, R-rmarkdown
%if %{with_suggests}
BuildRequires:    R-BiocStyle
%endif

%description
This package creates a persistent on-disk cache of files that the user can
add, update, and retrieve. It is useful for managing resources (such as custom
Txdb objects) that are costly or difficult to create, web resources, and data
files used across sessions.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{_datadir}/R/library
R CMD INSTALL %{packname} -l %{buildroot}%{_datadir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%check
# Some of the tests (and examples use the network)
# With no network, no check.
%if %{with_network}
export LANG=C.UTF-8
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-vignettes
%endif
%endif

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/html
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%doc %{_datadir}/R/library/%{packname}/NEWS
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/help
%doc %{_datadir}/R/library/%{packname}/doc
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/schema

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.4.0-8
- R-maint-sig mass rebuild

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.0-7
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.4.0-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 04 2022 Iñaki Úcar <iucar@fedoraproject.org> - 2.4.0-1
- R 4.2.1, update to 2.4.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 2.0.0-1
- update to 2.0.0
- Rebuilt for R 4.1.0

* Wed Feb  3 2021 Tom Callaway <spot@fedoraproject.org> - 1.14.0-1
- update to 1.14.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 16 2020 Tom Callaway <spot@fedoraproject.org> - 1.12.0-2
- fix doc files

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 1.12.0-1
- initial package

