%global packname odbc
%global packver  1.3.3
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          9%{?dist}
Summary:          Connect to ODBC Compatible Databases (using the DBI Interface)

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-bit64, R-blob >= 1.2.0, R-DBI >= 1.0.0, R-hms, R-methods, R-rlang, R-Rcpp >= 0.12.11
# Suggests:  R-covr, R-DBItest, R-magrittr, R-RSQLite, R-testthat, R-tibble
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-bit64
BuildRequires:    R-blob >= 1.2.0
BuildRequires:    R-DBI >= 1.0.0
BuildRequires:    R-hms
BuildRequires:    R-methods
BuildRequires:    R-rlang
BuildRequires:    R-Rcpp-devel >= 0.12.11
BuildRequires:    R-DBItest
BuildRequires:    R-magrittr
BuildRequires:    R-RSQLite
BuildRequires:    R-testthat
BuildRequires:    R-tibble
BuildRequires:    cctz-devel
BuildRequires:    pkgconfig(odbc)

%description
A DBI-compatible interface to ODBC databases.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION

# Remove bundled cctz.
rm -r %{packname}/src/cctz

# Link against system cctz.
sed -i \
    -e '/PKG_CXXFLAGS/s!-Icctz/include!-I/usr/include/cctz!' \
    -e '/PKG_LIBS/s!-Lcctz !!' \
    -e '/$(OBJECTS):/s!cctz/libcctz.a!!' \
    %{packname}/src/Makevars.in


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
%license %{rlibdir}/%{packname}/COPYING
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/icons
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.3.3-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.3.3-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 03 2022 Iñaki Úcar <iucar@fedoraproject.org> - 1.3.3-1
- R 4.2.1, update to 1.3.3

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 1.3.2-2
- Rebuilt for R 4.1.0

* Sat Apr 03 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- Update to latest version (#1946026)

* Sun Mar 21 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version (#1939634)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 29 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- Update to latest version (#1891997)

* Fri Aug 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.3-2
- Unbundle cctz

* Sun Aug 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.3-1
- initial package for Fedora
