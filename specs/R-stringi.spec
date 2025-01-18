%global packname stringi
%global packver  1.8.3
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          5%{?dist}
Summary:          Character String Processing Facilities

# Automatically converted from old format: BSD - review is highly recommended.
License:          LicenseRef-Callaway-BSD
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-tools, R-utils, R-stats
# Suggests:
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-stats
BuildRequires:    libicu-devel >= 61

%description
A multitude of character string/text/natural language processing tools: pattern
searching (e.g., with 'Java'-like regular expressions or the 'Unicode'
collation algorithm), random string generation, case mapping, string
transliteration, concatenation, sorting, padding, wrapping, Unicode
normalisation, date-time formatting and parsing, and many more. They are fast,
consistent, convenient, and - owing to the use of the 'ICU' (International
Components for Unicode) library - portable across all locales and platforms.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}

# Remove bundled code.
rm -r %{packname}/src/icu74
sed -i -e '/src\/icu74\//d' %{packname}/MD5


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname} \
    --configure-args="--disable-icu-bundle"
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/CITATION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%files devel
%{rlibdir}/%{packname}/include


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 1.8.3-4
- Rebuild for ICU 76

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.3-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 26 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.8.3-1
- Update to latest version

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.8.1-5
- R-maint-sig mass rebuild

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 1.8.1-4
- Rebuild for ICU 74

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 21 2023 Tom Callaway <spot@fedoraproject.org> - 1.8.1-1
- update to 1.8.1

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 1.7.8-5
- Rebuilt for ICU 73.2

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.7.8-4
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 1.7.8-2
- Rebuild for ICU 72

* Fri Aug 19 2022 Tom Callaway <spot@fedoraproject.org> - 1.7.8-1
- update to 1.7.8
- rebuild for R 4.2.1

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.6.2-5
- Rebuilt for ICU 71.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun  9 2021 Tom Callaway <spot@fedoraproject.org> - 1.6.2-1
- update to 1.6.2
- Rebuilt for R 4.1.0

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 1.5.3-3
- Rebuild for ICU 69

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.3-1
- Update to latest version (#1877263)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Dennis Gilmore <dennis@ausil.us> - 1.4.6-4
- rebuild for R 4.0.1

* Mon Jun 15 2020 Pete Walter <pwalter@fedoraproject.org> - 1.4.6-3
- Rebuild for ICU 67

* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 1.4.6-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.6-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.4-1
- Update to latest version

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 1.4.3-4
- Rebuild for ICU 65

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.3-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.3-1
- Update to latest version

* Wed Feb 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.4-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 1.2.3-2
- Rebuild for ICU 62

* Fri Jun 15 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.3-1
- Update to latest version

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 1.2.2-1
- update to 1.2.2, rebuild for R 3.5.0

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 1.1.7-2
- Rebuild for ICU 61.1

* Wed Apr 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.7-1
- Update to latest version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 1.1.6-2
- Rebuild for ICU 60.1

* Sat Nov 18 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.1.6-1
- Update to latest release.

* Thu Aug 24 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.1.5-1
- initial package for Fedora
