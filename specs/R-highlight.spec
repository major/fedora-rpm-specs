%global packname highlight

Name:		R-%{packname}
Version:	0.5.1
Release:	9%{?dist}
Summary:	R Syntax Highlighter
License:	GPL-3.0-or-later
URL:		https://cran.r-project.org/package=%{packname}
Source0:	%{url}&version=%{version}#/%{packname}_%{version}.tar.gz
#		Don't create std::string from NULL (gcc 12 error)
Patch0:		%{name}-no-std-string-from-null.patch
BuildRequires:	R-core-devel
BuildRequires:	tex(latex)
%if %{?fedora}%{!?fedora:0} >= 38
BuildRequires:	tex(inconsolata.sty)
%endif

%if %{?fedora}%{!?fedora:0} >= 31 || %{?rhel}%{!?rhel:0} >= 8
BuildRequires:	R-rpm-macros
%else
Requires:	R-core%{?_isa}
%endif

%description
Syntax highlighter for R code based on the results of the R parser.
Rendering in HTML and latex markup. Custom Sweave driver performing
syntax highlighting of R code chunks.

%prep
%setup -q -c
%patch -P 0 -p0

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l %{buildroot}%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{_libdir}/R/library/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/NEWS
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/NEWS.md
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/highlight
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/R/library/%{packname}/stylesheet

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.5.1-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jul 23 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.5.1-4
- Fix build requires

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.5.1-2
- R-maint-sig mass rebuild

* Mon Mar 27 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.5.1-1
- Update to 0.5.1

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Tom Callaway <spot@fedoraproject.org> - 0.5.0-10
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.5.0-7
- Don't create std::string from NULL (gcc 12 error)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 09 2021 Tom Callaway <spot@fedoraproject.org> - 0.5.0-5
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Tom Callaway <spot@fedoraproject.org> - 0.5.0-2
- rebuild for R 4

* Fri Mar 20 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.5.0-1
- Update to 0.5.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.7.2-6
- Remove explicit dependencies provided by automatic dependency generator

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.7.2-5
- Rebuild with automatic Provides

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 0.4.7.2-1
- update to 0.4.7.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Tom Callaway <spot@fedoraproject.org> - 0.4.7.1-2
- rebuild for R 3.4.0

* Fri Mar 31 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.7.1-1
- Update to 0.4.7.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.4.7-1
- Initial package creation
