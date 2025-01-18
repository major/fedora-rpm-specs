# Tests requires processx which requires this package.
%bcond_with bootstrap

%global packname ps
%global packver  1.7.5
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          8%{?dist}
Summary:          List, Query, Manipulate System Processes

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
# No network on builders.
Patch0001:        0001-Don-t-run-example-that-uses-the-network.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-utils
# Suggests:  R-callr, R-covr, R-curl, R-pillar, R-pingr, R-processx >= 3.1.0, R-R6, R-rlang, R-testthat >= 3.0.0, R-webfakes
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-utils
%if %{without bootstrap}
BuildRequires:    R-callr
BuildRequires:    R-curl
BuildRequires:    R-pillar
BuildRequires:    R-pingr
BuildRequires:    R-processx >= 3.1.0
BuildRequires:    R-R6
BuildRequires:    R-rlang
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-webfakes
%endif

%description
List, query and manipulate all system processes, on 'Windows', 'Linux' and
'macOS'.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch -P0001 -p1

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' DESCRIPTION
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Only used to run ./configure on Windows.
rm %{buildroot}%{rlibdir}/%{packname}/tools/winver.R


%check
%if %{without bootstrap}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-examples --no-tests
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/internals.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/bin
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/tools
%{rlibdir}/%{packname}/WORDLIST


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.7.5-6
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.7.5-2
- R-maint-sig mass rebuild

* Wed Apr 19 2023 Tom Callaway <spot@fedoraproject.org> - 1.7.5-1
- update to 1.7.5

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Tom Callaway <spot@fedoraproject.org> - 1.7.1-1
- update to 1.7.1
- bootstrap
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 1.6.0-3
- bootstrap off

* Wed Jun  9 2021 Tom Callaway <spot@fedoraproject.org> - 1.6.0-2
- bootstrap
- Rebuilt for R 4.1.0

* Sun Feb 28 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.0-1
- Update to latest version (#1933522)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 05 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.0-1
- Update to latest version (#1904711)

* Thu Oct 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-1
- Update to latest version (#1886009)

* Thu Aug 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.4-1
- Update to latest version (#1868090)
- Rename with_test to bootstrap conditional

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 1.3.3-2
- expand with_test to cover all BR, then disable to break testthat loop
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.3-1
- Update to latest version

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- Update to latest version
- Patch to work on non-x86 systems

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 05 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-3
- Improve process checking on 32-bit systems

* Mon Aug 20 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-2
- Add option to disable tests due to dependency loop

* Sun Aug 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- initial package for Fedora
