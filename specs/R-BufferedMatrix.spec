%global packname   BufferedMatrix
%global Rvers      3.4.0

Name:              R-%{packname}
Version:           1.60.0
Release:           11%{dist}
Summary:           A matrix data storage object method from bioconductor
Summary(fr):       Stockage des données d'un matrice dans un fichier temporaire
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:           LicenseRef-Callaway-LGPLv2+
URL:               http://bioconductor.org/packages/release/bioc/html/BufferedMatrix.html
Source0:           http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:     R-devel >= %{Rvers} tex(latex) R-methods

%package           devel
Summary:           Development files for %{name}
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description
A tabular style data object where most data is stored outside main memory.
A buffer is used to speed up access to data.

This library is part of the bioconductor (bioconductor.org) project.

%description -l fr
Une table de données dans laquelle la plus part des données sont stocké,
en dehors de la mémoire principale. Une mémoire tampon est utilisé pour
accélérer l'accès aux données.

%description    devel
The %{name}-devel  package contains Header and libraries files for
developing applications that use %{name}

%prep
%setup -c -q -n %{packname}

%build

%install
rm -rf %{buildroot}i
sed -i -e 's/\r$//' %{packname}/inst/doc/BufferedMatrix.Rnw

mkdir -p %{buildroot}%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

## Change the header of place for the -devel --> Removed
## see: https://www.redhat.com/archives/fedora-r-devel-list/2009-March/msg00001.html

#mkdir -p  $RPM_BUILD_ROOT%{_datadir}/R/library/%{packname}/include/
#install -D %{packname}/inst/include/*  $RPM_BUILD_ROOT%{_datadir}/R/library/%{packname}/include/
#chmod -x $RPM_BUILD_ROOT%{_datadir}/R/library/%{packname}/include/*
#rm -rf %{buildroot}%{_libdir}/R/library/%{packname}/include/

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/NAMESPACE
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html

%files		devel
%{_libdir}/R/library/%{packname}/include/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.60.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 1.60.0-10
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.60.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.60.0-8
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.60.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.60.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.60.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.60.0-4
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.60.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug  2 2022 Tom Callaway <spot@fedoraproject.org> - 1.60.0-2
- actually build against R 4.2.1

* Tue Aug  2 2022 Tom Callaway <spot@fedoraproject.org> - 1.60.0-1
- update to 1.60.0
- R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.56.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.56.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.56.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 1.56.0-1
- update to 1.56.0
- rebuild for R 4.1.0

* Wed Feb  3 2021 Tom Callaway <spot@fedoraproject.org> - 1.54.0-1
- update to 1.54.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.52.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.52.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 1.52.0-1
- update to 1.52.0
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.50.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov  7 2019 Tom Callaway <spot@fedoraproject.org> - 1.50.0-1
- update to 1.50.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.44.0-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 1.44.0-1
- update to 1.44.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Tom Callaway <spot@fedoraproject.org> - 1.40.0-1
- update to 1.40.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 02 2014 pingou <pingou@pingoured.fr> 1.28.0-1
- Update to version 1.28.0

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 27 2014 pingou <pingou@pingoured.fr> 1.26.0-1
- Update to version 1.26.0

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 07 2013 pingou <pingou@pingoured.fr> 1.24.0-1
- Update to version 1.24.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 pingou <pingou@pingoured.fr> 1.22.0-1
- Update to version 1.22.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 26 2012 pingou <pingou@pingoured.fr> 1.20.0-1
- Update to version 1.20.0

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Tom Callaway <spot@fedoraproject.org> 1.18.0-2
- rebuild for R 2.14.0

* Thu Nov 03 2011 pingou <pingou@pingoured.fr> 1.18.0-1
- Update to version 1.18.0

* Wed Jun 22 2011 pingou <pingou@pingoured.fr> 1.16.0-1
- Update to version 1.16.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 pingou <pingou@pingoured.fr> 1.14.0-1
- Update to version 1.14.0

* Tue May 11 2010 pingou <pingou@pingoured.fr> 1.12.0-1
- Update to version 1.12.0
- Fix R and BR (R-core tex(latex))
- Remove R for post/postun

* Sat Nov 21 2009 pingou <pingou@pingoured.fr> 1.10.0-1
- Update to 1.10.0
- Remove %%post and %%postun
- Adapt %%files to R-2.10.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 28 2009 pingou <pingou@pingoured.fr> 1.8.0-1
- Update to Bioconductor 2.4 and R-2.9.0

* Sun Mar 22 2009 pingou <pingou@pingoured.fr> - 1.6.0-2
- -devel should contain only the folder include  !

* Sat Mar 21 2009 pingou <pingou@pingoured.fr> - 1.6.0-1
- Update to Biocondutor 2.3
- Put back the headers to libdir instead of moving them to datadir

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Pingou <pingoufc4@yahoo.fr> 1.4.0-2
- Change own directory -- #473617

* Fri May 02 2008 Pingou <pingoufc4@yahoo.fr> 1.4.0-1
- Update to bioconductor 2.2

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.0-5
- Autorebuild for GCC 4.3

* Sat Feb 09 2008 Pingou <pingoufc4@yahoo.fr> 1.2.0-4
- Typo error on the changelog

* Sat Feb 09 2008 Pingou <pingoufc4@yahoo.fr> 1.2.0-3
- Change the URL

* Tue Jan 08 2008 Pingou <pingoufc4@yahoo.fr> 1.2.0-2
- Change on the BR

* Tue Nov 27 2007 Pingou <pingoufc4@yahoo.fr> 1.2.0-1
- Update to version 1.2.0

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.0.1-6
- Rebuild for selinux ppc32 issue.

* Wed Jul 11 2007 Pingou <pingoufc4@yahoo.fr> 1.0.1-5
- Change in the files section to fit the guidelines

* Wed Jul 11 2007 Pingou <pingoufc4@yahoo.fr> 1.0.1-4
- Change in the spec to remove the %%{__**} form in the macro

* Tue Jul 10 2007 Pingou <pingoufc4@yahoo.fr> 1.0.1-3
- Change in post and postun to fit the packaging guidelines
- Change in the prep section to fit the guidelines

* Thu Jul 05 2007 Pingou <pingoufc4@yahoo.fr> 1.0.1-2
- Fix install include

* Mon Jul 02 2007 Pingou <pingoufc4@yahoo.fr> 1.0.1-1
- initial package for Fedora

