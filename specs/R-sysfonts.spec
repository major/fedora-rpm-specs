%global packname sysfonts
%global packver  0.8.8
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          11%{?dist}
Summary:          Loading Fonts into R

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:          GPL-2.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-curl, R-jsonlite
# LinkingTo:
# Enhances:

Requires:         liberation-mono-fonts
Requires:         liberation-sans-fonts
Requires:         liberation-serif-fonts
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    pkgconfig(freetype2)
BuildRequires:    pkgconfig(libpng)
BuildRequires:    pkgconfig(zlib)
BuildRequires:    liberation-mono-fonts
BuildRequires:    liberation-sans-fonts
BuildRequires:    liberation-serif-fonts
BuildRequires:    R-curl
BuildRequires:    R-jsonlite

%description
Loading system fonts and Google Fonts <https://fonts.google.com/> into R,
in order to support other packages such as 'R2SWF' and 'showtext'.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Replace fonts by system fonts (note that this cannot be done in prep because
# R CMD INSTALL copies symlink targets.)
pushd %{buildroot}%{rlibdir}/%{packname}/fonts
rm AUTHORS License.txt
for family in Mono Sans Serif; do
    family_lower="${family,,}"
    for style in Regular Bold Italic BoldItalic; do
        rm Liberation${family}-${style}.ttf
%if 0%{?fedora} > 40
        ln -s /usr/share/fonts/liberation-${family_lower}-fonts/Liberation${family}-${style}.ttf
%else
        ln -s /usr/share/fonts/liberation-${family_lower}/Liberation${family}-${style}.ttf
%endif
    done
done
popd


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/fonts
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.8-10
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 21 2024 Parag Nemade <pnemade@fedoraproject.org> - 0.8.8-8
- Fix to use the new Liberation fonts installation path for F41+

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.8.8-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.8.8-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 0.8.8-1
- update to 0.8.8
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 0.8.3-3
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.3-1
- Update to latest version (#1914617)

* Tue Nov 17 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.2-1
- Update to latest version (#1898348)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 0.8.1-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.1-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8-4
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8-2
- Update Liberation font paths to newest locations

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.2-5
- Fix unbundling of fonts

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.2-3
- Really rebuild for R 3.5.0

* Fri Jun 08 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.2-2
- Rebuild for R 3.5.0

* Thu May 31 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.2-1
- initial package for Fedora
