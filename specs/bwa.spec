Name:           bwa
Version:        0.7.17
Release:        15%{?dist}
Summary:        Burrows-Wheeler Alignment tool

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://bio-bwa.sourceforge.net/
Source0:        http://downloads.sourceforge.net/bio-%{name}/%{name}-%{version}.tar.bz2
# Fix building against GCC 10.
# https://github.com/lh3/bwa/commit/2a1ae7b6f34a96ea25be007ac9d91e57e9d32284
Patch0:         bwa-fix-build-gcc10.patch
# Enable non-x86_64 CPU architectures with simde.
# https://github.com/lh3/bwa/pull/283
Patch1:         bwa-simde.patch
BuildRequires:  gcc
BuildRequires:  perl-generators
%ifnarch x86_64
BuildRequires:  simde-devel
%endif
BuildRequires:  zlib-devel
BuildRequires: make

%description

BWA is a program for aligning sequencing reads against a large
reference genome (e.g. human genome). It has two major components, one
for read shorter than 150bp and the other for longer reads.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1


%build
# Set -O3 for the better performance.
# https://github.com/lh3/bwa/pull/278
CFLAGS="%{optflags} -O3"
%ifnarch x86_64
# See Makefile in the pull request.
# https://github.com/lh3/bwa/pull/283
CFLAGS="${CFLAGS} -DUSE_SIMDE -DSIMDE_ENABLE_NATIVE_ALIASES -fopenmp-simd -DSIMDE_ENABLE_OPENMP"
%endif
%make_build CFLAGS="${CFLAGS}"


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}/bwakit
mkdir -p %{buildroot}/%{_mandir}/man1

install -m 0755 bwa %{buildroot}/%{_bindir}
install -m 0755 qualfa2fq.pl %{buildroot}/%{_bindir}
install -m 0755 xa2multi.pl %{buildroot}/%{_bindir}
install -m 0755 bwakit/* %{buildroot}/%{_datadir}/%{name}/bwakit
install -m 0644 bwa.1 %{buildroot}/%{_mandir}/man1/bwa.1


%check
./bwa 2>&1 | grep '^Version: %{version}'


%files
%doc COPYING NEWS.md README.md README-alt.md
%{_bindir}/bwa
%{_bindir}/qualfa2fq.pl
%{_bindir}/xa2multi.pl
%{_datadir}/%{name}/*
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.17-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.17-14
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Tom Stellard <tstellar@redhat.com> - 0.7.17-3
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Fri May 22 2020 Jun Aruga <jaruga@redhat.com> - 0.7.17-2
- Enable non-x86_64 CPU architectures with simde.
- Set -O3 for the better performance.

* Thu Apr 16 2020 Jun Aruga <jaruga@redhat.com> - 0.7.17-1
- Update to upstream release 0.7.17
- Move bwakit files to data directory to avoid conflicts.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Adam Huffman <bloch@verdurin.com> - 0.7.15-7
- Add BR for gcc

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 02 2016 Adam Huffman <bloch@verdurin.com> - 0.7.15-1
- Update to upstream release 0.7.15

* Thu Mar 24 2016 Adam Huffman <bloch@verdurin.com> - 0.7.13-1
- Update to upstream release 0.7.13

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 03 2015 Adam Huffman <bloch@verdurin.com> - 0.7.12-1
- Update to upstream 0.7.12

* Sat Dec 27 2014 Adam Huffman <bloch@verdurin.com> - 0.7.11-1
- Update to upstream 0.7.11
- First attempt to include new bwakit packaging

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 20 2014 Adam Huffman <bloch@verdurin.com> - 0.7.10-1
- Update to upstream 0.7.10

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Adam Huffman <bloch@verdurin.com> - 0.7.9a-1
- Update to upstream 0.7.9a
- Docs now in Markdown format, including new README.md

* Sun Oct 27 2013 Adam Huffman <bloch@verdurin.com> - 0.7.5a-2
- Remove nosse2 patch because 0.7+ versions only build on x86_64

* Sat Oct 26 2013 Adam Huffman <bloch@verdurin.com> - 0.7.5a-1
- Update to upstream 0.7.5a

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.6.1-6
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 28 2012 Dan Horák <dan[at]danny.cz> - 0.6.1-3
- enable SSE2 on x86_64 only, fixes build on secondary arches

* Sun May 13 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.6.1-2
- add patch to avoid SSE2 on i386

* Wed Jan 11 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.6.1-1
- update to 0.6.1

* Thu Feb 17 2011 Adam Huffman <bloch@verdurin.com> - 0.5.9-1
- new upstream release 0.5.9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan  5 2011 Adam Huffman <bloch@verdurin.com> - 0.5.8c-1
- upstream bugfix release

* Tue Jul 20 2010 Adam Huffman <bloch@verdurin.com> - 0.5.8a-1
- new upstream release

* Sat May 29 2010 Adam Huffman <bloch@verdurin.com> - 0.5.7-2
- fix source URL
- install manpage
- fix cflags

* Fri May 28 2010 Adam Huffman <bloch@verdurin.com> - 0.5.7-1
- initial version

