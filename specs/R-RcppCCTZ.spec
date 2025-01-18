%global packname RcppCCTZ
%global packver  0.2.11
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          10%{?dist}
Summary:          'Rcpp' Bindings for the 'CCTZ' Library

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-Rcpp >= 0.11.0
# Suggests:  R-tinytest
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-Rcpp-devel >= 0.11.0
BuildRequires:    R-tinytest
BuildRequires:    cctz-devel

%description
'Rcpp' Access to the 'CCTZ' timezone library is provided. 'CCTZ' is a C++
library for translating between absolute and civil times using the rules of a
time zone.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}
Requires:         cctz-devel

%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}

# Remove bundled cctz.
rm -r %{packname}/inst/include/cctz
rm %{packname}/src/time_zone_*.{cc,h}
rm %{packname}/src/{civil_time_detail,time_tool,zone_info_source}.cc

# Link against system cctz.
sed -i '/PKG_CXXFLAGS/d' %{packname}/src/Makevars
echo "PKG_LIBS = -lcctz" >> %{packname}/src/Makevars


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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/tinytest
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so

%files devel
%{rlibdir}/%{packname}/include


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.11-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.2.11-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.2.11-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 0.2.11-1
- update to 0.2.11
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 0.2.9-3
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 30 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.9-1
- Update to latest version (#1873902)

* Fri Aug 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.8-2
- Add proper devel subpackage

* Tue Aug 04 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.8-1
- Update to latest version
- rhbz#1866140

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 0.2.7-2
- rebuild for R 4

* Sat Mar 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.7-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.6-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.5-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.5-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 0.2.3-3
- rebuild for R 3.5.0

* Mon Mar 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.3-2
- Add missing Rcpp Requires

* Sat Mar 17 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.3-1
- initial package for Fedora
