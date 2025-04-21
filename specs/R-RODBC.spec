%global packname  RODBC
%global packver   1.3
%global packrel   26

Name:             R-%{packname}
Version:          %{packver}.%{packrel}
Release:          %autorelease
Summary:          An ODBC database interface for R
# Automatically converted from old format: GPLv2 or GPLv3 - review is highly recommended.
License:          GPL-2.0-only OR GPL-3.0-only
URL:              http://cran.r-project.org/web/packages/RODBC/
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{packver}-%{packrel}.tar.gz
BuildRequires:    R-devel >= 3.0.0, tetex-latex, unixODBC-devel, texinfo-tex

%description
An ODBC database interface for R.

%prep
%setup -c -q -n %{packname}
%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
%{_bindir}/R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library 
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css
rm -rf %{buildroot}%{_libdir}/R/library/RODBC/doc/Makefile

%check
%{_bindir}/R CMD check --ignore-vignettes --no-manual %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%dir %{_libdir}/R/library/%{packname}/doc/
%doc %{_libdir}/R/library/%{packname}/doc/index.html
%doc %{_libdir}/R/library/%{packname}/doc/RODBC.*
%dir %{_libdir}/R/library/%{packname}/po/
%lang(da) %{_libdir}/R/library/%{packname}/po/da/
%lang(de) %{_libdir}/R/library/%{packname}/po/de/
%lang(en) %{_libdir}/R/library/%{packname}/po/en*/
%lang(pl) %{_libdir}/R/library/%{packname}/po/pl/
%lang(it) %{_libdir}/R/library/%{packname}/po/it/
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/tests.R

%changelog
%autochangelog
