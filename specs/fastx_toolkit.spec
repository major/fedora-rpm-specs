Name:		fastx_toolkit
Version:	0.0.14
Release:	37%{?dist}
Summary:	Tools to process short-reads FASTA/FASTQ files

License:	AGPL-3.0-or-later
URL:		http://hannonlab.cshl.edu/%{name}/index.html
Source0:	http://hannonlab.cshl.edu/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-gcc47.patch

BuildRequires:  gcc-c++
BuildRequires:	libgtextutils-devel
BuildRequires:	perl-generators
BuildRequires: make
# FASTX-Barcode-Splitter requires the GNU Sed program.
Requires:	sed
# fasta_clipping_histogram requires PerlIO::gzip and GD::Graph::bars
Requires:	perl-PerlIO-gzip
Requires:	perl-GDGraph

%description

The FASTX-Toolkit is a collection of command line tools for
Short-Reads FASTA/FASTQ files preprocessing.

Next-Generation sequencing machines usually produce FASTA or FASTQ
files, containing multiple short-reads sequences (possibly with
quality information).

The main processing of such FASTA/FASTQ files is mapping (aka
aligning) the sequences to reference genomes or other databases using
specialized programs. Example of such mapping programs are: Blat,
SHRiMP, LastZ, MAQ and many many others.

However, It is sometimes more productive to preprocess the FASTA/FASTQ
files before mapping the sequences to the genome - manipulating the
sequences to produce better mapping results.

The FASTX-Toolkit tools perform some of these preprocessing tasks. 

%package       galaxy
Summary:       Integrate fastx_toolkit with a local Galaxy installation
Requires:      %{name} = %{version}-%{release}


%description   galaxy

These files allow the integration of fastx_toolkit with a local
installation of Galaxy (http://main.g2.bx.psu.edu/), a web-based
platform for analyzing multiple alignments, comparing genomic
annotations, profiling metagenomic samples and much more.


%prep
%setup -q
#Patch to fix compilation with GCC 4.7
%patch -P0 -p1 -b .%{name}-gcc47.patch

%build
%configure
make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"

mkdir %{buildroot}/%{_datadir}/%{name}
cp -a galaxy/ %{buildroot}/%{_datadir}/%{name}

# remove unnecessary m4 files
rm %{buildroot}/%{_datadir}/aclocal/*.m4

# remove autotools Makefile
find %{buildroot}/%{_datadir}/%{name}/galaxy/ -name "Makefile\.*" -delete


%files
%doc AUTHORS COPYING NEWS README THANKS
%{_bindir}/fast*

%files	galaxy
%{_datadir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Apr 21 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.14-35
- convert license to SPDX

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Jeff Law <law@redhat.com> - 0.0.14-26
- No longer force C++11 mode

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Adam Huffman <bloch@verdurin.com> - 0.0.14-21
- Add BR for gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.0.14-13
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Adam Huffman <bloch@verdurin.com> - 0.0.14-1
- Update to upstream 0.0.14 release
- C++11 standard required

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.0.13-9
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.13-6
- Rebuilt for c++ ABI breakage

* Mon Jan  9 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.0.13-5
- fix compilation with GCC 4.7

* Fri May 27 2011 Adam Huffman <bloch@verdurin.com> - 0.0.13-4
- fix ownership of /usr/share/fastx_toolkit

* Tue Nov 16 2010 Adam Huffman <bloch@verdurin.com> - 0.0.13-3
- fix license and remove autotools Makefiles

* Wed Aug 25 2010 Adam Huffman <bloch@verdurin.com> - 0.0.13-2
- fix CFLAGS and CXXFLAGS

* Tue May 11 2010 Adam Huffman <bloch@verdurin.com> - 0.0.13-1
- initial version

