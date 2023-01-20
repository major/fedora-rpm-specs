%global packname gss
%global packver  2.2-3
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.2.3
Release:          2%{?dist}
Summary:          General Smoothing Splines

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-stats
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-stats

%description
A comprehensive package for structural multivariate function estimation
using smoothing splines.


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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Tom Callaway <spot@fedoraproject.org> - 2.2.3-1
- update to 2.2.3
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun  8 2021 Tom Callaway <spot@fedoraproject.org> - 2.2.2-6
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Tom Callaway <spot@fedoraproject.org> - 2.2.2-4
- rebuild for FlexiBLAS R

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 2.2.2-2
- rebuild for R 4

* Sun May 31 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.2-1
- Update to latest version

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.1-1
- Update to latest version

* Sat Feb 29 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.12-1
- Update to latest version

* Sat Feb 29 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.11-1
- Update to latest version

* Tue Feb 18 2020 Tom Callaway <spot@fedoraproject.org> - 2.1.10-5
- rebuild against R without libRlapack.so

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.10-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.10-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 2.1.9-2
- rebuild for R 3.5.0

* Mon May 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.9-1
- Update to latest version

* Wed Apr 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.8-1
- Update to latest version

* Sun Mar 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.7-1
- initial package for Fedora
