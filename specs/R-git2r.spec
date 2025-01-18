%global packname git2r
%global packver  0.35.0
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          2%{?dist}
Summary:          Provides Access to Git Repositories

License:          GPL-2.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-graphics, R-utils
# Suggests:  R-getPass
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    pkgconfig(libgit2) >= 0.26.0
BuildRequires:    R-graphics
BuildRequires:    R-utils
BuildRequires:    R-getPass

%description
Interface to the 'libgit2' library, which is a pure C implementation of the
'Git' core methods. Provides access to 'Git' repositories to extract data
and running some basic 'Git' commands.


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
%license %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.35.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 15 2025 Pete Walter <pwalter@fedoraproject.org> - 0.35.0-1
- Update to 0.35.0 (rhbz#2251593)
- Drop bundled libgit2 handling as libgit2 is no longer bundled

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.32.0-6
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Pete Walter <pwalter@fedoraproject.org> - 0.32.0-3
- Rebuild for libgit2 1.7.x

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May  1 2023 Tom Callaway <spot@fedoraproject.org> - 0.32.0-1
- update to 0.32.0

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.30.1-6
- R-maint-sig mass rebuild

* Sun Mar 05 2023 Pete Walter <pwalter@fedoraproject.org> - 0.30.1-5
- Rebuild for libgit2 1.6.x

* Sat Jan 28 2023 Pete Walter <pwalter@fedoraproject.org> - 0.30.1-4
- Rebuild for libgit2 1.5.x

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 09 2022 Pete Walter <pwalter@fedoraproject.org> - 0.30.1-2
- Rebuild for libgit2 1.4

* Thu Aug 18 2022 Tom Callaway <spot@fedoraproject.org> - 0.30.1-1
- update to 0.30.1
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 20 2022 Igor Raits <igor.raits@gmail.com> - 0.28.0-7
- Rebuild for libgit2 1.4.x

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 28 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.28.0-5
- Rebuild for libgit2 1.3.x

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun  8 2021 Tom Callaway <spot@fedoraproject.org> - 0.28.0-3
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.28.0-1
- Update to latest version (#1914679)

* Mon Dec 28 19:00:31 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.27.1-4
- Rebuild for libgit2 1.1.x

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 0.27.1-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.27.1-1
- Update to latest version

* Mon Apr 27 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.26.1-5
- Rebuild against libgit2 1.x

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.26.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.26.1-1
- Update to latest version

* Mon Jun 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.25.2-2
- rebuilt for libgit2 0.28

* Wed Mar 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.25.2-1
- Update to latest version

* Sun Mar 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.25.1-1
- Update to latest version

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.24.0-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.23.0-2
- Rebuild for libgit2 0.27.x

* Sun Jul 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.23.0-1
- Update latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 0.21.0-2
- rebuild for R 3.5.0

* Mon Apr 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.21.0-1
- initial package for Fedora
