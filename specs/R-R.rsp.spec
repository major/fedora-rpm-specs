%global packname R.rsp
%global packver  0.45.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          10%{?dist}
Summary:          Dynamic Generation of Scientific Reports

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:          LicenseRef-Callaway-LGPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-methods, R-stats, R-tools, R-utils, R-R.methodsS3 >= 1.7.1, R-R.oo >= 1.23.0, R-R.utils, R-R.cache, R-digest >= 0.6.13
# Suggests:  R-tcltk, R-markdown >= 0.8, R-knitr >= 1.9, R-R.devices >= 2.16.1, R-base64enc >= 0.1-2
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-stats
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-R.methodsS3 >= 1.8.0
BuildRequires:    R-R.oo >= 1.23.0
BuildRequires:    R-R.utils
BuildRequires:    R-R.cache
BuildRequires:    R-digest
BuildRequires:    R-tcltk
BuildRequires:    R-markdown >= 0.8
BuildRequires:    R-knitr
BuildRequires:    R-R.devices
BuildRequires:    R-base64enc
BuildRequires:    R-ascii

%description
The RSP markup language makes any text-based document come alive.  RSP provides
a powerful markup for controlling the content and output of LaTeX, HTML,
Markdown, AsciiDoc, Sweave and knitr documents (and more), e.g. 'Today's date
is <%=Sys.Date()%>'.  Contrary to many other literate programming languages,
with RSP it is straightforward to loop over mixtures of code and text sections,
e.g. in month-by-month summaries.  RSP has also several preprocessing
directives for incorporating static and dynamic contents of external files
(local or online) among other things.  Functions rstring() and rcat() make it
easy to process RSP strings, rsource() sources an RSP file as it was an R
script, while rfile() compiles it (even online) into its final output format,
e.g. rfile('report.tex.rsp') generates 'report.pdf' and rfile('report.md.rsp')
generates 'report.html'.  RSP is ideal for self-contained scientific reports
and R package vignettes.  It's easy to use - if you know how to write an R
script, you'll be up and running within minutes.


%prep
%setup -q -c -n %{packname}

# Fix line endings.
for file in \
%{packname}/inst/doc/R_packages-Static_PDF_and_HTML_vignettes.pdf.asis \
%{packname}/inst/tcl/r-httpd.tcl \
; do
    sed "s|\r||g" ${file} > ${file}.new
    touch -r ${file} ${file}.new
    mv ${file}.new ${file}
done


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
%{rlibdir}/%{packname}/exData
%{rlibdir}/%{packname}/exec
%{rlibdir}/%{packname}/rsp
%{rlibdir}/%{packname}/rsp_LoremIpsum
%{rlibdir}/%{packname}/rsp_encodings
%{rlibdir}/%{packname}/rsp_examples
%{rlibdir}/%{packname}/rsp_tests
%{rlibdir}/%{packname}/rsp_tests_experimental
%{rlibdir}/%{packname}/rsp_tests_online
%{rlibdir}/%{packname}/tcl


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.45.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.45.0-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.45.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.45.0-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.45.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.45.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.45.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.45.0-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.45.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 24 2022 Tom Callaway <spot@fedoraproject.org> - 0.45.0-1
- update to 0.45.0
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.44.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.44.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.44.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 0.44.0-3
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.44.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.44.0-1
- Update to latest version (rhbz#1855381)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.43.2-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.43.2-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.43.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.43.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.43.0-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.42.0-1
- initial package for Fedora
