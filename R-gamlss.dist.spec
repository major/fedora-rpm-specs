%global packname gamlss.dist
%global packver  6.0-3
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          6.0.3
Release:          1%{?dist}
Summary:          Distributions for Generalized Additive Models for Location Scale and Shape

License:          GPLv2 or GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-MASS, R-graphics, R-stats, R-methods, R-grDevices
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildRequires:    R-devel >= 3.5.0
BuildRequires:    tex(latex)
BuildRequires:    R-MASS
BuildRequires:    R-graphics
BuildRequires:    R-stats
BuildRequires:    R-methods
BuildRequires:    R-grDevices

%description
A set of distributions which can be used for modelling the response variables
in Generalized Additive Models for Location Scale and Shape, Rigby and
Stasinopoulos (2005), <doi:10.1111/j.1467-9876.2005.00510.x>. The distributions
can be continuous, discrete or mixed distributions. Extra distributions can be
created, by transforming, any continuous distribution defined on the real line,
to a distribution defined on ranges 0 to infinity or 0 to 1, by using a "log"
or a "logit" transformation respectively.


%prep
%setup -q -c -n %{packname}

# Fix permissions.
chmod -x \
    %{packname}/NAMESPACE %{packname}/R/*.R \
    %{packname}/man/*.Rd %{packname}/src/ST3.?


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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%doc %{rlibdir}/%{packname}/Distributions-2010.pdf


%changelog
* Thu Aug  4 2022 Tom Callaway <spot@fedoraproject.org> - 6.0.3-1
- update to 6.0-3
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun  8 2021 Tom Callaway <spot@fedoraproject.org> - 5.3.2-2
- Rebuilt for R 4.1.0

* Wed Mar 10 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.3.2-1
- Update to latest version (#1936954)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.1.7-1
- Update to latest version

* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 5.1.6-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.1.6-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.1.5-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.1.4-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.1.4-1
- Update to latest version

* Wed Mar 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.1.3-1
- Update to latest version

* Fri Feb 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.1.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 14 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.1.0-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.0.6-1
- Update to latest version

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 5.0.5-2
- rebuild for R 3.5.0

* Tue May 01 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.0.5-1
- Update to latest version

* Sun Mar 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.0.4-1
- initial package for Fedora
