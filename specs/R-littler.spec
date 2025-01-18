%global packname littler

%global __suggests_exclude ^R\\(.*\\)

Name:		R-%{packname}
Version:	0.3.19
Release:	6%{?dist}
Summary:	littler: R at the Command-Line via 'r'

License:	GPL-2.0-or-later
URL:		https://cran.r-project.org/package=%{packname}
Source0:	%{url}&version=%{version}#/%{packname}_%{version}.tar.gz

BuildRequires:	R-core-devel
BuildRequires:	tex(latex)
%if %{?fedora}%{!?fedora:0} >= 38
BuildRequires:	tex(inconsolata.sty)
%endif
%if %{?fedora}%{!?fedora:0}
BuildRequires:	R-knitr
%endif

%if %{?fedora}%{!?fedora:0} >= 31 || %{?rhel}%{!?rhel:0} >= 8
BuildRequires:	R-rpm-macros
%else
Requires:	R-core%{?_isa}
%endif

%description
A scripting and command-line front-end is provided by 'r' (aka 'littler')
as a lightweight binary wrapper around the GNU R language and environment
for statistical computing and graphics. While R can be used in batch
mode, the r binary adds full support for both 'shebang'-style scripting
(i.e. using a hash-mark-exclamation-path expression as the first line in
scripts) as well as command-line use in standard Unix pipelines. In other
words, r provides the R language without the environment.

%package examples
Summary:	R-littler Examples
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description examples
Examples for using R-littler.

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l %{buildroot}%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm %{packname}/inst/bin/r %{packname}/src/r
rm %{packname}/src/Makevars
rm -rf %{buildroot}%{_libdir}/R/library/R.css
rm -rf %{buildroot}%{_libdir}/R/library/%{packname}/script-tests

mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{_libdir}/R/library/%{packname}/bin/r \
   %{buildroot}%{_bindir}
rmdir %{buildroot}%{_libdir}/R/library/%{packname}/bin
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_libdir}/R/library/%{packname}/man-page/r.1 \
   %{buildroot}%{_mandir}/man1
rmdir %{buildroot}%{_libdir}/R/library/%{packname}/man-page

for f in %{buildroot}%{_libdir}/R/library/%{packname}/examples/* ; do
    grep -q '/usr/bin/env r' $f && sed 's!/usr/bin/env r!/usr/bin/r!' -i $f
done

%check
%if %{?fedora}%{!?fedora:0}
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%else
# R-knitr is not available in EPEL - use --ignore-vignettes
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check --ignore-vignettes %{packname}
%endif

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/NEWS.Rd
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_bindir}/r
%{_mandir}/man1/r.1*

%files examples
%{_libdir}/R/library/%{packname}/examples

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.3.19-4
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 19 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.19-1
- New upstream release 0.3.19

* Sun Jul 23 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.18-4
- Fix build requires

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.3.18-2
- R-maint-sig mass rebuild

* Mon Mar 27 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.18-1
- New upstream release 0.3.18

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 07 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.17-1
- New upstream release 0.3.17

* Wed Oct 12 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.16-1
- New upstream release 0.3.16

* Fri Aug 19 2022 Tom Callaway <spot@fedoraproject.org> - 0.3.15-4
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 04 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.15-1
- New upstream release 0.3.15

* Thu Oct 07 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.14-1
- New upstream release 0.3.14

* Sun Jul 25 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.13-1
- New upstream release 0.3.13

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.12-3
- Rebuild for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.12-1
- New upstream release 0.3.12

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.11-1
- New upstream release 0.3.11

* Sat Jul 04 2020 José Abílio Matos <jamatos@fc.up.pt> - 0.3.10-2
- bump version to ensure upgrade path (due to a F32 rebuild)

* Mon Jun 08 2020 Tom Callaway <spot@fedoraproject.org> - 0.3.10-1
- update to 0.3.10
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.9-2
- Exclude Suggests for unavailable packages

* Thu Oct 31 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.9-1
- New upstream release 0.3.9

* Thu Sep 19 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.8-5
- Unify specfile

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.8-4
- Remove explicit dependencies provided by automatic dependency generator

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.8-3
- Rebuild with automatic Provides

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.8-1
- New upstream release 0.3.8

* Mon Mar 25 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.7-1
- New upstream release 0.3.7

* Fri Feb 01 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.6-1
- New upstream release 0.3.6

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 22 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.5-1
- New upstream release 0.3.5

* Fri Aug 31 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.4-1
- New upstream release 0.3.4

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 0.3.3-5
- Rebuild for ICU 62

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 0.3.3-4.1
- actually rebuild against R 3.5.0

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 0.3.3-4
- rebuild for R 3.5.0

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 0.3.3-3
- Rebuild for ICU 61.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.3-1
- New upstream release

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 0.3.2-5
- Rebuild for ICU 60.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Tom Callaway <spot@fedoraproject.org> - 0.3.2-2
- rebuild for R 3.4.0

* Thu Feb 16 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.2-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 30 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.1-1
- New upstream release
- Drop accepted patches: R-littler-ExcludeVars.patch, R-littler-ldflags.patch

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 0.3.0-2
- rebuild for ICU 57.1

* Sat Feb 20 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.3.0-1
- Initial package creation
