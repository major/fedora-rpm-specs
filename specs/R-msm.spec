%global packname msm

%global __suggests_exclude ^R\\((flexsurv|minqa|mstate|numDeriv)\\)

Name:             R-%{packname}
Version:          1.6.9
Release:          10%{?dist}
Source0:          ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{version}.tar.gz
# Automatically converted from old format: GPLv2+ and GPLv3+ - review is highly recommended.
License:          GPL-2.0-or-later AND GPL-3.0-or-later
URL:              http://cran.r-project.org/web/packages/msm/
Summary:          Multi-state Markov and hidden Markov models in continuous time
BuildRequires:    R-devel >= 3.4.0, tetex-latex, R-mvtnorm-devel, R-survival, R-expm

%description
Functions for fitting general continuous-time Markov and hidden Markov
multi-state models to longitudinal data.  Both Markov transition rates
and the hidden Markov output process can be modeled in terms of
covariates.  A variety of observation schemes are supported, including
processes observed at arbitrary times, completely-observed processes,
and censored states.

%prep
%setup -q -c -n %{packname}
# Fix some permissions and formats
# find . -type f -perm 755 -exec chmod 644 {} \;
find . -type f -name '*.[hc]' -exec chmod 644 {} \;

# Fix the encoding of the NEWS file
chmod 644 %{packname}/inst/NEWS
iconv -f ISO88591 -t UTF8 -o NEWS %{packname}/inst/NEWS
mv -f NEWS %{packname}/inst

%build

%install
# Specific installation procedure for R
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

# Remove the temporary object files
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)

# Remove the generic cascading style sheet for R
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/R.css


%check
# check needs a lot.
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/CITATION
%doc %{_libdir}/R/library/%{packname}/data
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs/%{packname}.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  7 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.9-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.6.9-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.6.9-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 1.6.9-1
- update to 1.6.9
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 1.6.8-8
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Tom Callaway <spot@fedoraproject.org> - 1.6.8-6
- rebuild for FlexiBLAS R

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.6.8-3
- rebuild for R 4

* Tue Feb 18 2020 Tom Callaway <spot@fedoraproject.org> - 1.6.8-2
- rebuild against R without libRlapack.so

* Thu Feb 06 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> 1.6.8-1
- Upgrade to 1.6.8

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.6-6
- Exclude Suggests for unavailable packages

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.6-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 1.6.6-1
- Update to 1.6.6

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Tom Callaway <spot@fedoraproject.org> - 1.6.4-1
- update to 1.6.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May  8 2014 Tom Callaway <spot@fedoraproject.org> - 1.3-1
- update to 1.3

* Sun Dec 29 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> 1.2-1
- Update to 1.2

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 1.1.4-1
- update to 1.1.4

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov  8 2011 Tom Callaway <spot@fedoraproject.org> - 1.1-1
- update to 1.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 21 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.5-2
- fix tag mistake

* Thu Jan 21 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.5-1
- update to 0.9.5
- cleanup package to fix FTBFS

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.9.1-2
- Suppressed the unused definition of the packrel variable

* Fri Jun 12 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.9.1-1
- Integrated the new upstream (0.9.1) version

* Sat Jun 06 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.8.2-2
- Altered the license so as to reflect upstream, after clarification with them

* Sun May 03 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.8.2-1
- Initial package creation
