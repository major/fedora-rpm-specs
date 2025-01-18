# asciicast missing
%bcond_with suggests

%global packname callr
%global packver  3.7.3
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          8%{?dist}
Summary:          Call R from R

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-processx >= 3.6.1, R-R6, R-utils
# Suggests:  R-asciicast, R-cli>= 1.1.0, R-covr, R-mockery, R-ps, R-rprojroot, R-spelling, R-testthat >= 3.0.0, R-withr >= 2.3.0
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-processx >= 3.6.1
BuildRequires:    R-R6
BuildRequires:    R-utils
%if %{with suggests}
BuildRequires:    R-asciicast
BuildRequires:    R-cli >= 1.1.0
BuildRequires:    R-mockery
BuildRequires:    R-ps
BuildRequires:    R-rprojroot
BuildRequires:    R-spelling
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-withr >= 2.3.0
%endif

%description
It is sometimes useful to perform a computation in a separate R process,
without affecting the current R process at all. This packages does exactly
that.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with suggests}
%{_bindir}/R CMD check %{packname} --ignore-vignettes
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/developer-notes.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 3.7.3-6
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 3.7.3-2
- R-maint-sig mass rebuild

* Wed Apr 19 2023 Tom Callaway <spot@fedoraproject.org> - 3.7.3-1
- update to 3.7.3
- adjust packaging model to one where suggests are optional (and not enabled by default)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Tom Callaway <spot@fedoraproject.org> - 3.7.1-1
- update to 3.7.1
- rebuild for R 4.2.1
- bootstrap

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 3.7.0-3
- bootstrap off

* Wed Jun  9 2021 Tom Callaway <spot@fedoraproject.org> - 3.7.0-2
- Rebuilt for R 4.1.0
- bootstrap

* Sun Apr 25 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.7.0-1
- Update to latest version (#1951665)
- Rename check conditional to bootstrap

* Sat Apr 03 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.6.0-1
- Update to latest version (#1943902)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.5.1-1
- Update to latest version (#1887921)

* Sat Oct 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.5.0-1
- Update to latest version (#1886598)

* Mon Sep 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.4.4-1
- Update to latest version (#1876681)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 3.4.3-2
- conditionalize check to break testthat loop
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.4.3-1
- Update to latest version

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.4.2-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.4.0-1
- Update to latest version

* Mon Sep 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.3.2-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.3.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.3.1-1
- Update to latest version

* Tue Jul 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.3.0-1
- Update to latest version

* Fri Mar 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.2.0-1
- Update to latest version

* Sun Feb 24 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.1.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0.0-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 2.0.4-1
- update to 2.0.4 (package now noarch)

* Thu Apr 26 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.3-1
- Update to latest version

* Thu Mar 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-2
- Remove extra Requires

* Wed Mar 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-1
- initial package for Fedora
