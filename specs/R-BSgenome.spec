%global packname  BSgenome
%global Rvers     3.0.0

Name:             R-%{packname}
Version:          1.64.0
Release:          10%{dist}
Summary:          Infrastructure for Biostrings-based genome data packages
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/BSgenome.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
BuildRequires:    R-devel >= %{Rvers} tex(latex)
BuildRequires:    R-BiocGenerics >= 0.13.8 R-S4Vectors-devel >= 0.17.28 R-IRanges-devel >= 2.13.16
BuildRequires:    R-GenomeInfoDb >= 1.25.6 R-GenomicRanges >= 1.31.10 R-Biostrings-devel >= 2.47.6
BuildRequires:    R-rtracklayer >= 1.39.7
BuildRequires:    R-methods R-utils R-stats R-matrixStats R-XVector-devel >= 0.29.3 R-Rsamtools

%description
Infrastructure shared by all the Biostrings-based genome data packages

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}

# architecture independant package
mkdir -p %{buildroot}%{_datadir}/R/library
R CMD INSTALL %{packname} -l %{buildroot}%{_datadir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_datadir}/R/library/R.css

%check
# The dependencies asked are:
# 1- only 'suggests'
# 2- really big
# 3- contain only 'metadata' no code
#%{_bindir}/R CMD check %{packname}


%files
%dir %{_datadir}/R/library/%{packname}/
%doc %{_datadir}/R/library/%{packname}/doc
%doc %{_datadir}/R/library/%{packname}/DESCRIPTION
%doc %{_datadir}/R/library/%{packname}/html
%doc %{_datadir}/R/library/%{packname}/NEWS
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/extdata
%{_datadir}/R/library/%{packname}/help
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/pkgtemplates

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.64.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.64.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.64.0-8
- R-maint-sig mass rebuild

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 1.64.0-7
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.64.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.64.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.64.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.64.0-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.64.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 04 2022 Iñaki Úcar <iucar@fedoraproject.org> - 1.64.0-1
- R 4.2.1, update to 1.64.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.60.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.60.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.60.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 1.60.0-1
- update to 1.60.0
- Rebuilt for R 4.1.0

* Wed Feb  3 2021 Tom Callaway <spot@fedoraproject.org> - 1.58.0-1
- update to 1.58.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.56.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.56.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 1.56.0-1
- update to 1.56.0
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.54.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov  7 2019 Tom Callaway <spot@fedoraproject.org> - 1.54.0-1
- update to 1.54.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.48.0-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.48.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.48.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.48.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.48.0-1
- Update toi 1.48.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 11 2016 pingou <pingou@pingoured.fr> 1.38.0-1
- Update to version 1.38.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.36.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 03 2015 pingou <pingou@pingoured.fr> 1.36.2-1
- Update to version 1.36.2
- Add R-rtracklayer as BR and R

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul 02 2014 pingou <pingou@pingoured.fr> 1.32.0-1
- Update to version 1.32.0
- Add R-Rsamtools and R-bitops as R and BR

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 27 2014 pingou <pingou@pingoured.fr> 1.30.0-1
- Update to version 1.30.0

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 07 2013 pingou <pingou@pingoured.fr> 1.28.0-1
- Update to version 1.28.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 pingou <pingou@pingoured.fr> 1.26.1-1
- Update to version 1.26.1

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Tom Callaway <spot@fedoraproject.org> 1.22.0-1
- update to 1.22.0

* Sat Jul 02 2011 pingou <pingou@pingoured.fr> 1.20.0-1
- Update to version 1.20.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 pingou <pingou@pingoured.fr> 1.18.3-1
- Update to version 1.18.3

* Mon Dec 20 2010 pingou <pingou@pingoured.fr> 1.18.2-1
- Update to version 1.18.2

* Tue Oct 26 2010 pingou <pingou@pingoured.fr> 1.18.0-1
- Update to version 1.18.0

* Sat Sep 11 2010 pingou <pingou@pingoured.fr> 1.16.5-2
- Add R-GenomicRanges in R and BR

* Sat Sep 11 2010 pingou <pingou@pingoured.fr> 1.16.5-1
- Update to version 1.16.5

* Sat Jun 05 2010 pingou <pingou@pingoured.fr> 1.16.1-1
- Update to version 1.16.1
- Update to R-2.11.0
- Remove post/postun
- Update R and BR to R-core and R-devel
- Change source0 and URL to a more stable form

* Sat Nov 21 2009 pingou <pingou@pingoured.fr> 1.14.2-1
- Update to 1.14.2
- Remove %%post and %%postun
- Adapt %%files to R-2.10.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 pingou <pingou@pingoured.fr> 1.12.3-1
- Update to 1.12.3

* Fri Jun 12 2009 pingou <pingou@pingoured.fr> 1.12.2-1
- Update to 1.12.2

* Wed May 20 2009 pingou <pingou@pingoured.fr> 1.12.0-2
- The NAMESPACE file is not a doc

* Mon May 18 2009 pingou <pingou@pingoured.fr> 1.12.0-1
- Update to 1.12.0 for Bioconductor 2.4 and R 2.9.0
- Remove the dependency on R-Biobase which is not needed

* Wed Apr 01 2009 pingou <pingou@pingoured.fr> 1.10.5-2
- Add R-Biostrings-devel as BR
- Define and use the macro BioC for the bioconductor release

* Fri Mar 13 2009 pingou <pingou -AT- pingoured.fr> 1.10.5-1
- initial package for Fedora
