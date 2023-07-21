Name:		bfast
Version:	0.7.0a
Release:	32%{?dist}
Summary:	Blat-like Fast Accurate Search Tool

License:	GPLv2 and MIT
URL:		https://github.com/nh13/BFAST
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-pthread-new.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	perl-generators
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel
BuildRequires: make


%description

BFAST facilitates the fast and accurate mapping of short reads to
reference sequences.  Some advantages of BFAST include:

Speed: enables billions of short reads to be mapped quickly.

Accuracy: A priori probabilities for mapping reads with defined set of variants.

An easy way to measurably tune accuracy at the expense of speed.

Specifically, BFAST was designed to facilitate whole-genome
resequencing, where mapping billions of short reads with variants is
of utmost importance.

BFAST supports both Illumina and ABI SOLiD data, as well as any other
Next-Generation Sequencing Technology (454, Helicos), with particular
emphasis on sensitivity towards errors, SNPs and especially
indels. Other algorithms take short-cuts by ignoring errors, certain
types of variants (indels), and even require further alignment, all to
be the "fastest" (but still not complete). BFAST is able to be tuned
to find variants regardless of the error-rate, polymorphism rate, or
other factors.


%prep
%setup -q
%patch0 -p1 

# Let configure honor CFLAGS
sed -i -e 's,^\(CFLAGS="${default_CFLAGS} ${extended_CFLAGS}"\),# \1,' configure.ac
# Regenerate butil/Makefile.in to retain
# balignmentscoredistribution_LDADD=-lpthread, otherwise the build fails with
# --as-needed in LDFLAGS, bug #1674691
autoreconf -fi

%build
# Package expects gnu89 inline semantics
%configure "CFLAGS=${CFLAGS} -fgnu89-inline"
%make_build


%install
%make_install

rm %{buildroot}/%{_docdir}/%{name}/LICENSE
rm %{buildroot}/%{_docdir}/%{name}/bfast-book.pdf


%files
%doc AUTHORS ChangeLog NEWS README
%doc manual/bfast-book.pdf
%license LICENSE
%{_bindir}/balignmentscoredistribution
%{_bindir}/balignsim
%{_bindir}/bevalsim
%{_bindir}/bfast
%{_bindir}/bfast.resubmit.pl
%{_bindir}/bfast.submit.pl
%{_bindir}/bgeneratereads
%{_bindir}/bindexdist
%{_bindir}/bindexhist
%{_bindir}/bmfmerge
%{_bindir}/brepeat
%{_bindir}/btestindexes
%{_bindir}/ill2fastq.pl
%{_bindir}/solid2fastq


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0a-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0a-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0a-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0a-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0a-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0a-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Filipe Rosset <rosset.filipe@gmail.com> - 0.7.0a-26
- Fix FTBFS rhbz#1863246

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0a-25
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0a-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0a-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0a-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Petr Pisar <ppisar@redhat.com> - 0.7.0a-21
- Regenerate a build script (bug #1674691)
- Upstream moved to <https://github.com/nh13/BFAST>

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0a-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0a-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0a-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0a-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0a-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0a-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 19 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.7.0a-14
- Let configure honor CFLAGS (F24FTBFS, RHBZ#1307345).
- Append -fgnu89-inline to CFLAGS.
- Re-enable hardening.
- Add %%license.
- Modernize spec.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0a-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 05 2015 Adam Huffman <bloch@verdurin.com> - 0.7.0a-12
- Disable hardened build temporarily to work around configure problem

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0a-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0a-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Adam Huffman <bloch@verdurin.com> - 0.7.0a-9
- More aarch64 build fixes
- Update pthread patch

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0a-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Adam Huffman <bloch@verdurin.com> - 0.7.0a-7
- Fix for building on aarch64

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0a-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.7.0a-5
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov  1 2011 Adam Huffman <bloch@verdurin.com> - 0.7.0a-1
- new upstream release 0.7.0a including paired end and mate pair improvements

* Fri May 27 2011 Adam Huffman <bloch@verdurin.com> - 0.6.5a-1
- new upstream release
- remove obsolete file deletion

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4e-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Adam Huffman <bloch@verdurin.com> - 0.6.4e-1
- new upstream bugfix release
- solid2fastq.pl removed upstream

* Wed Jun 23 2010 Adam Huffman <bloch@verdurin.com> - 0.6.4d-5
- add MIT licence for kseq.h
- improve description
- clean up URL

* Tue Jun 22 2010 Adam Huffman <bloch@verdurin.com> - 0.6.4d-4
- add temporary fix for problem with 32-bit build

* Wed Jun 16 2010 Adam Huffman <bloch@verdurin.com> - 0.6.4d-3
- temporary release with solid2fastq.pl removed, to avoid conflict with bwa

* Mon Jun  7 2010 Adam Huffman <bloch@verdurin.com> - 0.6.4d-2
- add BR for zlib and bz2
- patch to add pthread to linking stage
- remove two docs installed by upstream Makefile, to avoid clash with docs

* Thu Jun  3 2010 Adam Huffman <bloch@verdurin.com> - 0.6.4d-1
- initial version

