%global packname  gsl
%global packvers  2.1-7.1
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.1.7.1
Release:          4%{?dist}
Summary:          Wrapper for the Gnu Scientific Library

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packvers}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    gsl-devel >= 2.1

%description
An R wrapper for some of the functionality of the Gnu Scientific Library.


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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/gsl_stickermaker.R
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 04 2022 Iñaki Úcar <iucar@fedoraproject.org> - 2.1.7.1-3
- Rebuild for gsl-2.7.1

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.7.1-2
- Rebuild for gsl-2.7.1

* Thu Aug 18 2022 Tom Callaway <spot@fedoraproject.org> - 2.1.7.1-1
- update to 2.1-7.1
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun  8 2021 Tom Callaway <spot@fedoraproject.org> - 2.1.6-8
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 2.1.6-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.6-3
- Rebuilt for GSL 2.6.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.6-1
- Update to latest version

* Sat Mar 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.5-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.9.10.3-1
- initial package for Fedora
