%global packname data.table
%global packver  1.15.4
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((xts)\\)

# Some dependency loops.
%global with_loop 0

Name:             R-%{packname}
Version:          %{packver}
Release:          3%{?dist}
Summary:          Extension of `data.frame`

License:          MPL-2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-methods
# Suggests:  R-bit64 >= 4.0.0, R-bit >= 4.0.4, R-curl, R-R.utils, R-xts, R-nanotime, R-zoo >= 1.8-1, R-yaml, R-knitr, R-rmarkdown
# LinkingTo:
# Enhances:

BuildRequires:    pkgconfig(zlib)
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-bit64 >= 4.0.0
BuildRequires:    R-bit >= 4.0.4
BuildRequires:    R-curl
BuildRequires:    R-R.utils
BuildRequires:    R-zoo >= 1.8.1
BuildRequires:    R-yaml
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
%if %{with_loop}
BuildRequires:    R-xts
BuildRequires:    R-nanotime
%endif

%description
Fast aggregation of large data (e.g. 100GB in RAM), fast ordered joins,
fast add/modify/delete of columns by group using no copies at all, list
columns, friendly and fast character-separated-value read/write. Offers a
natural and flexible syntax, for faster development.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Useless.
rm %{buildroot}%{rlibdir}/%{packname}/cc


%check
# Segfaults?
%ifnarch aarch64 i686
# Workaround /etc/localtime not being a symlink in koji.
export TZ=Etc/UTC
%if %{with_loop}
%{_bindir}/R CMD check --ignore-vignettes %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check --ignore-vignettes %{packname}
%endif
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/data_table.so
%{rlibdir}/%{packname}/tests
%dir %{rlibdir}/%{packname}/po
%dir %{rlibdir}/%{packname}/po/en@quot
%dir %{rlibdir}/%{packname}/po/en@quot/LC_MESSAGES
%lang(en@quot) %{rlibdir}/%{packname}/po/en@quot/LC_MESSAGES/*.mo
%dir %{rlibdir}/%{packname}/po/zh_CN
%dir %{rlibdir}/%{packname}/po/zh_CN/LC_MESSAGES
%lang(zh_CN) %{rlibdir}/%{packname}/po/zh_CN/LC_MESSAGES/*.mo

%files devel
%{rlibdir}/%{packname}/include


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.15.4-1
- Update to latest version

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.14.8-6
- R-maint-sig mass rebuild

* Sat Apr  13 2024 Miroslav Suchý <msuchy@redhat.com> - 1.14.8-5
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.14.8-1
- R-maint-sig mass rebuild
- Update to latest version

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 1.14.2-1
- update to 1.14.2
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 1.14.0-2
- Rebuilt for R 4.1.0

* Tue Feb 23 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.14.0-1
- Update to latest version (#1931171)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.13.6-1
- Update to latest version (#1911715)

* Sat Dec 12 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.13.4-1
- Update to latest version (#1905468)

* Tue Oct 20 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.13.2-1
- Update to latest version (#1889519)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.13.0-1
- Update to latest version

* Sat Jul  4 2020 José Matos <jamatos@fedoraproject.org> - 1.12.8-4
- disable checks that are failing in R 4.0 (bug in R)

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.12.8-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12.8-1
- Update to latest version

* Mon Oct 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12.6-1
- Update to latest version

* Thu Oct 03 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12.4-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12.2-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 07 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12.2-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12.0-1
- Update to latest version

* Sat Sep 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.11.6-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.11.4-2
- Rebuild for R 3.5.0

* Sat Jun 02 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.11.4-1
- initial package for Fedora
