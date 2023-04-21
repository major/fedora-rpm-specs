%bcond_with bootstrap

%global packname processx
%global packver  3.8.1
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          1%{?dist}
Summary:          Execute and Control System Processes

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-ps >= 1.2.0, R-R6, R-utils
# Suggests:  R-callr >= 3.7.3, R-cli >= 3.3.0, R-codetools, R-covr, R-curl, R-debugme, R-parallel, R-rlang >= 1.0.2, R-testthat >= 3.0.0, R-webfakes, R-withr
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-ps >= 1.2.0
BuildRequires:    R-R6
BuildRequires:    R-utils
%if %{without bootstrap}
BuildRequires:    R-callr >= 3.7.3
BuildRequires:    R-cli >= 3.3.0
BuildRequires:    R-codetools
BuildRequires:    R-curl
BuildRequires:    R-debugme
BuildRequires:    R-parallel
BuildRequires:    R-rlang >= 1.0.2
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-webfakes
BuildRequires:    R-withr
%endif

%description
Tools to run system processes in the background. It can check if a
background process is running; wait on a background process to finish; get
the exit status of finished processes; kill background processes. It can
read the standard output and error of the processes, using non-blocking
connections. 'processx' can poll a process for standard output or error,
with a timeout. It can also poll several processes at once.


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

# FIXME: Why does this not install?
install -pm 0644 %{packname}/README.md %{buildroot}%{rlibdir}/%{packname}/


%check
%if %{without bootstrap}
%{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/README.md
%doc %{rlibdir}/%{packname}/CODE_OF_CONDUCT.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/bin
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/libs/client.so


%changelog
* Wed Apr 19 2023 Tom Callaway <spot@fedoraproject.org> - 3.8.1-1
- update to 3.8.1

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Tom Callaway <spot@fedoraproject.org> - 3.7.0-1
- update to 3.7.0
- rebuild for R 4.2.1
- bootstrap on

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun  9 2021 Tom Callaway <spot@fedoraproject.org> - 3.5.2-1
- Update to 3.5.2
- bootstrap
- Rebuilt for R 4.1.0

* Mon Apr 05 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.5.1-1
- Update to latest version (#1946117)

* Fri Mar 26 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.5.0-1
- Update to latest version (#1942163)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 04 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.4.5-1
- Update to latest version (#1902707)
- Rename check conditional to bootstrap

* Sat Sep 05 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.4.4-1
- Update to latest version (#1875519)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.4.3-1
- Update to latest version

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 3.4.2-2
- rebuild for R 4
- conditionalize check to break testthat loop

* Wed Feb 12 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.4.2-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.4.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.4.1-1
- Update to latest version

* Tue Jul 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.4.0-1
- Update to latest version

* Wed May 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.3.1-1
- Update to latest version

* Fri Mar 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.3.0-1
- Update to latest version

* Wed Mar 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.2.1-2
- Enable more tests

* Thu Feb 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.2.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.2.0-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 3.1.0-1
- update to 3.1.0

* Mon May 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0.3-1
- Update to latest version

* Wed Mar 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.0.1-1
- initial package for Fedora
