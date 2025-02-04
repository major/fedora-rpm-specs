Name:		mmseq
Version:	1.0.11
Release:	23%{?dist}
Summary:	Haplotype and isoform specific expression estimation for RNA-seq

%if 0%{?fedora} >= 33
%bcond_without flexiblas
%endif

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/eturro/%{name}
Source0:	https://github.com/eturro/%{name}/archive/%{version}.zip
#Patch1:		mmseq-flags.patch
Patch2:		mmseq-zlib.patch

BuildRequires:  gcc-c++
BuildRequires:	make
BuildRequires:	boost-devel
BuildRequires:	perl-generators
BuildRequires:	htslib-devel
BuildRequires:	gsl-devel
BuildRequires:	zlib-devel
BuildRequires:	armadillo-devel
%if %{with flexiblas}
BuildRequires:	flexiblas-devel
%endif

Requires:	ruby
Requires:	samtools
Requires:	perl-interpreter

%description
Software for fast, scalable haplotype and isoform expression
estimation using multi-mapping RNA-seq reads.  Example scripts are included.

%prep
%setup -q -n %{name}-%{version}
#Use Fedora compilation headers
#%%patch1 -p1 -b .mmseq-flags.patch
#Fix zlib linking
%patch -P2 -p1 -b .mmseq-zlib.patch

# Remove bundled binaries
# Only 2 bin/*-linux files are included in Source0 archive.
rm -f bin/*-linux

%if %{with flexiblas}
sed -e 's/-lblas/-lflexiblas/g' -e 's/-llapack/-lflexiblas/g' -i src/Makefile
%endif

%build
cd src
make %{?_smp_mflags} CXXFLAGS="%{optflags}"

%check
# Check src/VERSION is correctly set.
test "$(bin/mmseq --version 2>&1 || true)" = "%{name}-%{version}"

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 bin/bam2hits %{buildroot}%{_bindir}
install -p -m 0755 bin/extract_transcripts %{buildroot}%{_bindir}
install -p -m 0755 bin/hitstools %{buildroot}%{_bindir}
install -p -m 0755 bin/mmcollapse %{buildroot}%{_bindir}
install -p -m 0755 bin/mmdiff %{buildroot}%{_bindir}
install -p -m 0755 bin/mmseq %{buildroot}%{_bindir}
install -p -m 0755 bin/offsetGTF %{buildroot}%{_bindir}
install -p -m 0755 bin/t2g_hits %{buildroot}%{_bindir}
install -p -m 0755 bin/*.sh %{buildroot}%{_bindir}
install -p -m 0755 bin/*.rb %{buildroot}%{_bindir}
install -p -m 0755 bin/ensembl_gtf_to_gff.pl %{buildroot}%{_bindir}



%files
%doc README.md COPYING doc/
%{_bindir}/bam2hits
%{_bindir}/extract_transcripts
%{_bindir}/hitstools
%{_bindir}/mmcollapse
%{_bindir}/mmdiff
%{_bindir}/mmseq
%{_bindir}/offsetGTF
%{_bindir}/t2g_hits
%{_bindir}/fastagrep.sh
%{_bindir}/mouse_strain_transcriptome.sh
%{_bindir}/usage.sh
%{_bindir}/filterGTF.rb
%{_bindir}/haploref.rb
%{_bindir}/testregexp.rb
%{_bindir}/ensembl_gtf_to_gff.pl


%changelog
* Sun Feb 02 2025 Orion Poplawski <orion@nwra.com> - 1.0.11-23
- Rebuild with gsl 2.8

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.11-21
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 1.0.11-17
- Rebuilt for Boost 1.83

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.0.11-15
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.11-13
- Rebuild for gsl-2.7.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.0.11-11
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 1.0.11-9
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.0.11-6
- Rebuilt for Boost 1.75

* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.0.11-5
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 1.0.11-3
- Rebuilt for Boost 1.73

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Jun Aruga <jaruga@redhat.com> - 1.0.11-1
- Update to new Github-based upstream release 1.0.11.

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.0.8a-31
- Rebuilt for GSL 2.6.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8a-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8a-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.0.8a-28
- Rebuilt for Boost 1.69

* Fri Aug 17 2018 José Abílio Matos <jamatos@fc.up.pt> - 1.0.8a-27
- rebuild for armadillo soname bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8a-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8a-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.0.8a-24
- Rebuilt for Boost 1.66

* Fri Sep 22 2017 Adam Huffman <bloch@verdurin.com> - 1.0.8a-23
- rebuilt for armadillo

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8a-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8a-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8a-20
- Rebuilt for Boost 1.64

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1.0.8a-19
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8a-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8a-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.0.8a-16
- Rebuilt for Boost 1.63

* Thu Jun 30 2016 José Matos <jamatos@fedoraproject.org> - 1.0.8a-15
- Rebuild for armadillo 7.x and remove BR SuperLU because armadillo takes care of that

* Sat Jun  4 2016 José Matos <jamatos@fedoraproject.org> - 1.0.8a-14
- Rebuild for armadillo 7.x

* Mon May 23 2016 Jonathan Wakely <jwakely@redhat.com> - 1.0.8a-13
- Add missing BuildRequires (#1337966)

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 1.0.8a-13
- Rebuilt for linker errors in boost (#1331983)

* Thu Feb 25 2016 José Matos <jamatos@fedoraproject.org> - 1.0.8a-12
- Apply the c++11 patches only to Fedora >= 24 (where g++ implements gnu++14)

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.8a-11
- Rebuild for gsl 2.1

* Fri Feb 12 2016 Adam Huffman <bloch@verdurin.com> - 1.0.8a-10
- patch to add compatibility with C++11 iostream
- patch to add compatibility with C++11 static data member initialization

* Wed Feb 10 2016 Adam Huffman <bloch@verdurin.com> - 1.0.8a-9
- rebuilt to pick up new armadillo

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8a-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.0.8a-7
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.0.8a-6
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8a-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.0.8a-4
- rebuild for Boost 1.58

* Sun Jul 05 2015 Adam Huffman <bloch@verdurin.com> - 1.0.8a-3
- Update binaries and docs to install and package
- Fix changelog

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 01 2015 Adam Huffman <bloch@verdurin.com> - 1.0.8a-1
- Update to new Github-based upstream release
- Add armadillo BR

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.9.18-14
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.9.18-11
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0.9.18-10
- rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.9.18-8
- Rebuild for boost 1.54.0

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.9.18-7
- Perl 5.18 rebuild

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.9.18-6
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.9.18-5
- Rebuild for Boost-1.53.0

* Sun Aug 12 2012 Kevin Fenzi <kevin@scrye.com> - 0.9.18-4
- Rebuild for new boost

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-2
- Rebuilt for c++ ABI breakage

* Wed Jan 11 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.9.18-1
- update to 0.9.18
- remove pileup.sh and get_isize.rb, discarded upstream
- update patches and remove flags patch

* Sun Nov 20 2011 Adam Huffman <adam@vaioz.verdurin.salon> - 0.9.14-2
- rebuild for new Boost in Rawhide

* Fri Oct  7 2011 Adam Huffman <bloch@verdurin.com> - 0.9.14-1
- new upstream bugfix release

* Wed Aug 17 2011 Adam Huffman <bloch@verdurin.com> - 0.9.12-1
- upstream release 0.9.12 fixing a possible segfault

* Thu Jul 21 2011 Adam Huffman <bloch@verdurin.com> - 0.9.11-2
- rebuild for new Boost in Rawhide

* Sat May 28 2011 Adam Huffman <bloch@verdurin.com> - 0.9.11-1
- new upstream release
- add routeB.sh script
- sam2hits.rb removed

* Fri May 27 2011 Adam Huffman <bloch@verdurin.com> - 0.9.10b-3
- patch to deal with zlib better

* Sun May 15 2011 Adam Huffman <bloch@verdurin.com> - 0.9.10b-2
- remove bundled binaries
- remove VERSION
- explicit naming for included scripts

* Sun May  8 2011 Adam Huffman <bloch@verdurin.com> - 0.9.10b-1
- new upstream version
- patch descriptions

* Sun May  8 2011 Adam Huffman <bloch@verdurin.com> - 0.9.9-3
- fix permissions for installed files
- include missing Perl script
- improve description

* Sat Apr  9 2011 Adam Huffman <bloch@verdurin.com> - 0.9.9-2
- fix compilation flags for debuginfo
- include shell and Ruby scripts

* Mon Apr  4 2011 Adam Huffman <bloch@verdurin.com> - 0.9.9-1
- initial version
