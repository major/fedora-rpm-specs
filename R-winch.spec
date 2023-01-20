%global packname winch
%global packver  0.0.9
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          2%{?dist}
Summary:          Portable Native and Joint Stack Traces

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
Patch0: %{name}-gcc11.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-procmaps >= 0.0.2
# Suggests:  R-DBI, R-knitr, R-magrittr, R-purrr, R-rlang >= 0.4.8, R-rmarkdown, R-RSQLite, R-testthat >= 3.0.0, R-vctrs
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-procmaps >= 0.0.2
BuildRequires:    R-DBI
BuildRequires:    R-knitr
BuildRequires:    R-magrittr
BuildRequires:    R-purrr
BuildRequires:    R-rlang >= 0.4.8
BuildRequires:    R-rmarkdown
BuildRequires:    R-RSQLite
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-vctrs

# libbacktrace has never made any other releases, so it may or may not be 1.0.
Provides: bundled(libbacktrace) = 1.0

%description
Obtain the native stack trace and fuse it with R's stack trace for easier
debugging of R packages with native code.


%prep
%setup -q -c -n %{packname}
%patch0 -p1


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
export LANG=C.UTF-8
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 0.0.9-1
- update to 0.0.9
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 0.0.6-4
- Rebuilt for R 4.1.0

* Thu Feb 25 2021 Jeff Law <law@redhat.com> - 0.0.6-3
- Completely sync libbacktrace/dwarf.c with upstream
  Update MD5 as well

* Wed Feb 24 2021 Jeff Law <law@redhat.com> - 0.0.6-3
- Backport upstream libbacktrace fix for dwarf-5 

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 17 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.0.6-1
- Update to latest version (#1898085)

* Mon Nov 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.0.5-1
- Update to latest version (#1896203)

* Sat Oct 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.0.1-1
- initial package for Fedora
