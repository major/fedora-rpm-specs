%global packname  gdata
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.18.0.1
Release:          10%{?dist}
Summary:          Various R Programming Tools for Data Manipulation

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:          GPL-2.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-gtools R-stats R-methods R-utils
# Suggests:  R-RUnit
# LinkingTo:
# Enhances:

BuildArch:        noarch

BuildRequires:    R-devel tex(latex)
BuildRequires:    R-gtools R-stats R-methods R-utils
BuildRequires:    R-RUnit
BuildRequires:    perl-interpreter
BuildRequires:    perl(lib)


%description
Various R programming tools for data manipulation, including:
  - medical unit conversions,
  - combining objects,
  - character vector operations,
  - factor manipulation,
  - obtaining information about R objects,
  - manipulating MS-Excel formatted files,
  - generating fixed-width format files,
  - extricating components of date & time objects,
  - operations on columns of data frames,
  - matrix operations,
  - operations on vectors,
  - operations on data frames,
  - value of last evaluated expression, and
  - wrapper for 'sample' that ensures consistent behavior for both scalar and
    vector arguments.


%prep
%setup -q -c -n %{packname}

# Fix permissions
chmod -x %{packname}/inst/perl/Digest/Perl/MD5.pm
chmod -x %{packname}/inst/perl/Spreadsheet/README-XLS
chmod -x %{packname}/inst/perl/module_tools.pl
chmod -x %{packname}/inst/perl/xls2csv.pl
chmod -x %{packname}/inst/perl/xls2tab.pl
chmod -x %{packname}/inst/perl/xls2tsv.pl
sed -i -e '/^#!\//, 1d' %{packname}/inst/perl/*.pl


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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/bin
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/perl
%{rlibdir}/%{packname}/xls


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.18.0.1-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.18.0.1-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 2.18.0.1-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 2.18.0.1-1
- update to 2.18.0.1
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 2.18.0-12
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 2.18.0-9
- rebuild for R 4

* Sun Mar 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.18.0-8
- Add explicit Perl dependencies

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.18.0-6
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.18.0-2
- Fix permissions on Perl code

* Wed Mar 14 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.18.0-1
- initial package for Fedora
