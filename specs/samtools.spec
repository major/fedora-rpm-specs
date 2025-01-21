Name:		samtools
Version:	1.15.1
Release:	6%{?dist}
Summary:	Tools for nucleotide sequence alignments in the SAM format

License:	MIT
URL:		http://www.htslib.org/
Source0:	https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	gcc
BuildRequires:	htslib-devel
BuildRequires:	htslib-tools
BuildRequires:	make
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
# It's used in make test.
BuildRequires:	perl-interpreter
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(lib)

%description
SAM (Sequence Alignment/Map) is a flexible generic format for storing
nucleotide sequence alignment.
SAM Tools provide various utilities for manipulating alignments in the
SAM format, including sorting, merging, indexing and generating
alignments in a per-position format.


%prep
%setup -q

# Remove INSTALL file to suppress rpmlint warning.
rm -f INSTALL


%build
%configure CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" \
  --prefix=%{_prefix} \
  --with-htslib=system
%make_build


%install
%make_install

# Replace shebang for /usr/lib/rpm/redhat/brp-mangle-shebangs check.
for file in $(grep -l '^#!/usr/bin/env perl' %{buildroot}%{_bindir}/*); do
  sed -i '1 s|/usr/bin/env perl|/usr/bin/perl|' "${file}"
done


%check
# Check if samtools is built with system htslib.
ldd samtools | grep -E '/lib(64)?/libhts\.so\.'

make test


%files
%doc AUTHORS ChangeLog.old NEWS examples/
%license LICENSE
# We do not use a wildcard to list bin files, because this often leads
# to problems when the name changes or something additional is installed.
%{_bindir}/ace2sam
%{_bindir}/blast2sam.pl
%{_bindir}/bowtie2sam.pl
%{_bindir}/export2sam.pl
%{_bindir}/fasta-sanitize.pl
%{_bindir}/interpolate_sam.pl
%{_bindir}/maq2sam-long
%{_bindir}/maq2sam-short
%{_bindir}/md5fa
%{_bindir}/md5sum-lite
%{_bindir}/novo2sam.pl
%{_bindir}/plot-ampliconstats
%{_bindir}/plot-bamstats
%{_bindir}/psl2sam.pl
%{_bindir}/sam2vcf.pl
%{_bindir}/samtools
%{_bindir}/samtools.pl
%{_bindir}/seq_cache_populate.pl
%{_bindir}/soap2sam.pl
%{_bindir}/wgsim
%{_bindir}/wgsim_eval.pl
%{_bindir}/zoom2sam.pl
%{_mandir}/man1/samtools.1*
%{_mandir}/man1/samtools-*.1*
%{_mandir}/man1/wgsim.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 Jun Aruga <jaruga@redhat.com> - 1.15.1-1
- Update to samtools version 1.15.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 John Marshall <jmarshall@hey.com> - 1.13-1
- Update to samtools version 1.13
- Upstream now includes individual man pages for each samtools subcommand
- misc/varfilter.py has been removed upstream, and other scripts added

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 17 2020 Jun Aruga <jaruga@redhat.com> - 1.9-3
- Fix the build failure adding perl(FindBin) and perl(lib) build dependencies.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Jun Aruga <jaruga@redhat.com> - 1.9-1
- Update to 1.9
- Remove devel and libs sub packges, as "make dylib" was removed.

* Fri Nov 01 2019 Jun Aruga <jaruga@redhat.com> - 0.1.19-20
- Remove Python 2 dependency (rhbz#1738176).

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Petr Pisar <ppisar@redhat.com> - 0.1.19-18
- varfilter.py is a Python 2 code (bug #1675976)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Adam Huffman <bloch@verdurin.com> - 0.1.19-16
- Add BR for python2

* Fri Jul 20 2018 Adam Huffman <bloch@verdurin.com> - 0.1.19-15
- Add BR for gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Tom Callaway <spot@fedoraproject.org> - 0.1.19-7
- add fixes from Rsamtools

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun  9 2014 Tom Callaway <spot@fedoraproject.org> - 0.1.19-5
- add faidx_fetch_seq2 function from rsamtools

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.1.19-2
- Perl 5.18 rebuild

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 0.1.19-1
- update to 0.1.19

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Adam Huffman <verdurin@fedoraproject.org> - 0.1.18-2
- make sure new seqtk tool included

* Tue Sep  6 2011 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.18-1
- Updated to 0.1.18

* Tue May 10 2011 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.16-1
- Updated to 0.1.16

* Mon Apr 11 2011 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.15-1
- Updated to 0.1.15

* Wed Mar 23 2011 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.14-1
- Updated to 0.1.14
- Build shared library instead of static

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec  6 2010 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.12a-2
- Fixed header files directory ownership
- Added missing header files

* Mon Dec  6 2010 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.12a-1
- Updated to 0.1.12a

* Tue Nov 23 2010 Adam Huffman <bloch@verdurin.com> - 0.1.8-4
- cleanup man page handling

* Sun Oct 10 2010 Adam Huffman <bloch@verdurin.com> - 0.1.8-4
- fix attributes for devel subpackage
- fix library location

* Sun Sep 26 2010 Adam Huffman <bloch@verdurin.com> - 0.1.8-3
- put headers and library in standard locations

* Mon Sep 6 2010 Adam Huffman <bloch@verdurin.com> - 0.1.8-2
- merge Rasmus' latest changes (0.1.8 update)
- include bam.h and libbam.a for Bio-SamTools compilation
- move bam.h and libbam.a to single directory
- put bgzf.h, khash.h and faidx.h in the same place
- add -fPIC to CFLAGS to make Bio-SamTools happy
- add virtual Provide as per guidelines

* Tue Aug 17 2010 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.8-1
- Updated to 0.1.8.

* Mon Nov 30 2009 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.7a-1
- Updated to 0.1.7a.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 12 2009 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.5c-3
- Specfile cleanup.

* Sat Jul 11 2009 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.5c-2
- Fixed manpage location.
- Make sure optflags is passed to the makefiles.

* Sat Jul 11 2009 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.5c-1
- Initial build.
