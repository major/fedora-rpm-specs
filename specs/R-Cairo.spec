%global packname Cairo
%global packver  1.6-0
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.6.0
Release:          14%{?dist}
Summary:          Use Cairo for high-quality bitmap, vector, and display output

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:          GPL-2.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-grDevices, R-graphics
# Suggests:  R-png
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-grDevices
BuildRequires:    R-graphics
BuildRequires:    R-png
BuildRequires:    cairo-devel >= 1.2
BuildRequires:    libXt-devel

%description
R graphics device using cairographics library that can be used to create
high-quality vector (PDF, PostScript and SVG) and bitmap output (PNG, JPEG,
TIFF), and high-quality rendering in displays (X11 and Win32).  Since it uses
the same back-end for all output, copying across formats is WYSIWYG. Files are
created without the dependence on X11 or other external programs. This device
supports alpha channel (semi-transparent drawing) and resulting images can
contain transparent and semi-transparent regions. It is ideal for use in server
environments (file output) and as a replacement for other devices that don't
have Cairo's capabilities such as alpha support or anti-aliasing. Backends are
modular such that any subset of backends is supported.


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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 1.6.0-13
- Rebuild for ICU 76

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.0-12
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.6.0-10
- R-maint-sig mass rebuild

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 1.6.0-9
- Rebuild for ICU 74

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 1.6.0-5
- Rebuilt for ICU 73.2

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.6.0-4
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 1.6.0-2
- Rebuild for ICU 72

* Wed Aug 24 2022 Tom Callaway <spot@fedoraproject.org> - 1.6.0-1
- update to 1.6-0
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 1.5.12.2-4
- rebuild for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.12.2-1
- Update to latest version

* Thu Jun 25 2020 José Abílio Matos <jamatos@fc.up.pt> - 1.5.12-3
- bump version to ensure upgrade path (due to a F32 rebuild)

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 1.5.12-2
- Rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.12-1
- Update to latest version

* Sat Mar 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.11-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.10-4
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.10-2
- Cleanup summary and description

* Mon Apr 01 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.10-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 1.5.9-4
- rebuild for R 3.5.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.5.9-2
- Cleanup metadata a bit.

* Fri Feb 17 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.5.9-1
- initial package for Fedora
