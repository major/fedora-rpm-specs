%bcond_with check

%global packname fs
%global packver  1.6.2
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          7%{?dist}
Summary:          Cross-Platform File System Operations Based on 'libuv'
# Wasn't this so much nicer when it was just GPLv3?
#
# SPDX is currently missing this one:
# https://scancode-licensedb.aboutcode.org/bsd-credit.html
License:          GPL-3.0-only AND libutil-David-Nugent AND BSD-3-Clause AND BSD-2-Clause AND ISC AND MIT AND LicenseRef-Fedora-Public-Domain AND Beerware
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
# Fedora-specific.
Patch0001:        0001-Use-system-libuv.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-methods
# Suggests:  R-testthat >= 3.0.0, R-covr, R-pillar >= 1.0.0, R-tibble >= 1.1.0, R-crayon, R-rmarkdown, R-knitr, R-withr, R-spelling, R-vctrs >= 0.3.0
# LinkingTo:
# Enhances:

BuildRequires:    pkgconfig(libuv) >= 1.18.0
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
%if %{with check}
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-pillar >= 1.0.0
BuildRequires:    R-tibble >= 1.1.0
BuildRequires:    R-crayon
BuildRequires:    R-rmarkdown
BuildRequires:    R-knitr
BuildRequires:    R-withr
BuildRequires:    R-spelling
%if %{fedora} > 32
BuildRequires:    R-vctrs >= 0.3.0
%endif
%endif

%description
A cross-platform interface to file system operations, built on top of the
'libuv' C library.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
# Remove bundled libuv.
%patch -P0001 -p1
rm -rf src/libuv-*
sed -i -e '/libuv/d' MD5

# Don't need coverage; it's not packaged either.
sed -i 's/, covr//g' DESCRIPTION
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with check}
export LANG=C.UTF-8
%if %{fedora} > 32
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%endif
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/COPYRIGHTS
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.6.2-5
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 28 2023 Tom Callaway <spot@fedoraproject.org> - 1.6.2-1
- update to 1.6.2

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.5.2-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug  4 2022 Tom Callaway <spot@fedoraproject.org> - 1.5.2-1
- update to 1.5.2
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 1.5.0-3
- Rebuilt for R 4.1.0
- disable check via conditional

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.0-1
- Update to latest version

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.2-1
- Update to latest version

* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 1.4.1-1
- update to 1.4.1
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version

* Sun May 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- Update to latest version
- Add workaround for libuv stat bug (https://github.com/libuv/libuv/issues/2262)

* Wed Mar 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.7-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.6-1
- initial package for Fedora
