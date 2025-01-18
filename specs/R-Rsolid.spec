%global packname  Rsolid

Name:		  R-%{packname}
Version:	  0.9.31
Release:	  51%{?dist}
Summary:	  Quantile normalization and base calling for second generation sequencing data

License:	  Artistic-2.0
URL:		  http://rafalab.jhsph.edu/Rsolid/
Source0:	  http://rafalab.jhsph.edu/Rsolid/Rsolid_0.9-31.tar.gz
Patch0:           R-Rsolid-R3.patch
Patch1:           R-Rsolid-configure-c99.patch
BuildRequires:	  R-devel >= 3.4.0 tex(latex) hdf5-devel 

%package	  devel
Summary:	  Development files for %{name}
Requires:	  %{name}%{?_isa} = %{version}-%{release}

%description

Rsolid is an R package for normalizing fluorescent intensity data from
ABI/SOLiD second generation sequencing platform. It has been observed
that the color-calls provided by factory software contain technical
artifacts, where the proportions of colors called are extremely
variable across sequencing cycles. Under the random DNA fragmentation
assumption, these proportions should be equal across sequencing cycles
and proportional to the dinucleotide frequencies of the sample.

Rsolid implements a version of the quantile normalization algorithm
that transforms the intensity values before calling colors. Results
show that after normalization, the total number of mappable reads
increases by around 5%, and number of perfectly mapped reads increases
by 10%. Moreover a 2-5% reduction in overall error rates is observed,
with a 2-6% reduction in the rate of valid adjacent color
mis-matches. The latter is important, since it leads to a decrease in
false-positive SNP calls.

The normalization algorithm is computationally efficient. In a test we
are able to process 300 million reads in 2 hours using 10 computer
cluster nodes. The engine functions of the package are written in C
for better performance.

%description	devel

The %{name}-devel  package contains header and library files for
developing applications that use %{name}

%prep
%setup -q -c -n %{packname}
%patch -P0 -p1 -b .fixed
%patch -P1 -p1 -b .configure-c99

%build

%install
# x86/x86_64 -> Architecture dependent package
mkdir -p %{buildroot}%{_libdir}/R/library 
R CMD INSTALL %{packname} --configure-args="--with-hdf5=%{_prefix}" -l %{buildroot}%{_libdir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

#Remove executable files to pass check
rm -rf %{packname}/src/hdf5-1.8.3
rm -rf %{packname}/config.status
rm -rf %{packname}/configure

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs

%files	devel
%{_libdir}/R/library/%{packname}/include


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 0.9.31-50
- Rebuild for hdf5 1.14.5

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.9.31-48
- R-maint-sig mass rebuild

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.31-47
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 26 2023 Florian Weimer <fweimer@redhat.com> - 0.9.31-43
- Port configure script to c99

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.9.31-42
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 03 2022 Iñaki Úcar <iucar@fedoraproject.org> - 0.9.31-40
- R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Orion Poplawski <orion@nwra.com> - 0.9.31-37
- Rebuild for hdf5 1.12.1

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 0.9.31-36
- Rebuild for hdf5 1.10.7

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 0.9.31-32
- Rebuild for hdf5 1.10.6

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 0.9.31-31
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.31-29
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 0.9.31-27
- Rebuild for hdf5 1.10.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 0.9.31-24
- rebuild for R 3.5.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 0.9.31-20
- rebuild for R 3.4.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.31-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.31-17
- Rebuild for hdf5 1.8.16

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.31-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 0.9.31-15
- Rebuild for hdf5 1.8.15

* Wed Jan 07 2015 Orion Poplawski <orion@cora.nwra.com> - 0.9.31-14
- Rebuild for hdf5 1.8.14

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.31-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.31-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.31-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.31-10
- Rebuild for hdf5 1.8.11

* Fri Apr 12 2013 Tom Callaway <spot@fedoraproject.org> - 0.9.31-9
- rebuild for R3

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.31-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Tom Callaway <spot@fedoraproject.org> - 0.9.31-5
- rebuild for R 2.14.0

* Thu May 19 2011 Adam Huffman <bloch@verdurin.com> - 0.9.31-4
- remove executable files to pass check

* Tue May 17 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9.31-3
- Rebuild for hdf5 1.8.7

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 23 2010 Adam Huffman <bloch@verdurin.com> - 0.9.31-1
- another upstream bugfix release

* Thu Aug  5 2010 Adam Huffman <bloch@verdurin.com> - 0.9.3-1
- New upstream bugfix release

* Fri Jul 16 2010 Adam Huffman <bloch@verdurin.com> - 0.9.2-4
- fix duplicated files entries

* Fri Jul 16 2010 Adam Huffman <bloch@verdurin.com> - 0.9.2-3
- new upstream release with licensing clarification
- specfile cleanups to address reviewer comments:
  - directory ownership
  - requires

* Mon Jul 12 2010 Adam Huffman <bloch@verdurin.com> - 0.9.2-2
- spec formatting cleanups

* Tue Jul  6 2010 Adam Huffman <bloch@verdurin.com> - 0.9.2-1
- new release with ability to disable bundled HDF5
- fix files section
- -devel subpackage

* Thu Jun 03 2010 Adam Huffman <bloch@verdurin.com> - 0.9.1-1
- initial package for Fedora
