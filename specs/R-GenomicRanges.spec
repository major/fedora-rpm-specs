%global packname  GenomicRanges
%global rlibdir %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.48.0
Release:          10%{dist}
Summary:          Representation and manipulation of genomic intervals
License:          Artistic-2.0
URL:              http://www.bioconductor.org/packages/release/bioc/html/GenomicRanges.html
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:    R-devel tex(latex) R-core >= 4.0.0 R-methods R-stats4 R-utils R-stats
BuildRequires:    R-IRanges-devel >= 2.23.9 R-BiocGenerics >= 0.37.0 R-XVector-devel >= 0.29.2 R-GenomeInfoDb >= 1.15.2 R-S4Vectors-devel >= 0.27.12

%description
The ability to efficiently store genomic annotations and alignments is
playing a central role when it comes to analyze high-throughput sequencing
data (a.k.a. NGS data). The package defines general purpose containers for
storing genomic intervals as well as more specialized containers for
storing alignments against a reference genome.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
# Circular dependencies:
# R-BSgenome depends on R-GenomicRanges which
# suggests to have R-BSgenome
#%%{_bindir}/R CMD check %%{packname}

%files
%dir %{rlibdir}/%{packname}/
%doc %{rlibdir}/%{packname}/doc/
%doc %{rlibdir}/%{packname}/html/
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta/
%{rlibdir}/%{packname}/R/
%{rlibdir}/%{packname}/extdata/
%{rlibdir}/%{packname}/help/
%{rlibdir}/%{packname}/unitTests/
%{rlibdir}/%{packname}/scripts/
%{rlibdir}/%{packname}/libs/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.48.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.48.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.48.0-8
- R-maint-sig mass rebuild

* Sat Apr  20 2024 Miroslav Suchý <msuchy@redhat.com> - 1.48.0-7
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.48.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.48.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.48.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.48.0-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.48.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 1.48.0-1
- update to 1.48.0
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 1.44.0-1
- update to 1.44.0
- Rebuilt for R 4.1.0

* Thu Feb  4 2021 Tom Callaway <spot@fedoraproject.org> - 1.42.0-1
- update to 1.42.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 1.40.0-1
- update to 1.40.0
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov  4 2019 Tom Callaway <spot@fedoraproject.org> - 1.38.0-1
- update to 1.38.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.34.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb  6 2019 Tom Callaway <spot@fedoraproject.org> - 1.34.0-1
- update to 1.34.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 1.32.3-1
- update to 1.32.3

* Wed Mar 14 2018 Tom Callaway <spot@fedoraproject.org> - 1.30.3-1
- update to 1.30.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Tom Callaway <spot@fedoraproject.org> - 1.28.3-1
- update to 1.28.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec  7 2015 Tom Callaway <spot@fedoraproject.org> - 1.22.1-1
- update to 1.22.1

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Tom Callaway <spot@fedoraproject.org> - 1.20.3-1
- update to 1.20.3

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun  9 2014 Tom Callaway <spot@fedoraproject.org> - 1.16.3-1
- update to 1.16.3

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 27 2014 pingou <pingou@pingoured.fr> 1.14.4-1
- Update to version 1.14.4

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 pingou <pingou@pingoured.fr> 1.12.4-1
- Update to version 1.12.4

* Sun Apr 07 2013 pingou <pingou@pingoured.fr> 1.12.1-1
- Update to version 1.12.1

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 pingou <pingou@pingoured.fr> 1.10.5-1
- Update to version 1.10.5

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Tom Callaway <spot@fedoraproject.org> 1.6.2-1
- update to 1.6.2

* Sat Jul 02 2011 pingou <pingou@pingoured.fr> 1.4.6-1
- Update to version 1.4.6

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 pingou <pingou@pingoured.fr> 1.2.3-1
- Update to version 1.2.3

* Mon Dec 20 2010 pingou <pingou@pingoured.fr> 1.2.2-1
- Update to version 1.2.2

* Thu Nov 25 2010 pingou <pingou@pingoured.fr> 1.2.1-1
- Update to version 1.2.1

* Tue Oct 26 2010 pingou <pingou@pingoured.fr> 1.2.0-1
- Update to version 1.2.0

* Wed Sep 29 2010 jkeating - 1.0.9-2
- Rebuilt for gcc bug 634757

* Tue Sep 07 2010 pingou <pingou@pingoured.fr> 1.0.9-1
- Update to version 1.0.9

* Tue Aug 17 2010 pingou <pingou@pingoured.fr> 1.0.7-2
- Change Require from R to R-core

* Thu Jul 29 2010 pingou <pingou@pingoured.fr> 1.0.7-1
- Update to 1.0.7
- End directory by / in %%files

* Mon Jul 19 2010 pingou <pingou@pingoured.fr> 1.0.6-1
- Update to 1.0.6
- End directory by / in %%files
- Change URL
- Fix typo in the comment of check (dependencies)
- Add dependencie to R-IRanges-devel

* Tue Jun 29 2010 pingou <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora
