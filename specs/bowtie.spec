Name:		bowtie
Version:	1.3.1
Release:	7%{?dist}
Summary:	An ultrafast, memory-efficient short read aligner

# bowite: Artistic 2.0
# tinythread.{h,cpp}: zlib
# Automatically converted from old format: Artistic 2.0 and zlib - review is highly recommended.
License:	Artistic-2.0 AND Zlib
URL:		http://bowtie-bio.sourceforge.net/index.shtml
Source0:	http://downloads.sourceforge.net/%{name}-bio/%{name}-%{version}-src.zip
# git clone https://github.com/BenLangmead/bowtie.git
# cd bowtie
# git checkout v1.3.1
# tar czvf bowtie-1.3.1-tests.tgz scripts/test/
Source1:	bowtie-%{version}-tests.tgz
# Remove perl-Sys-Info module depenency, as it does not exist on Fedora.
Patch1:		bowtie-test-remove-perl-Sys-Info-dep.patch
Requires:	python3
BuildRequires:	gcc-c++
BuildRequires:	hostname
BuildRequires:	perl-interpreter
BuildRequires:	perl(Clone)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(lib)
BuildRequires:	python3
BuildRequires:	tbb-devel
BuildRequires:	zlib-devel
BuildRequires: make
# 32-bit CPU architectures are not supported for bowtie version >= 1.1.0.
# https://github.com/BenLangmead/bowtie/commit/5f90d3fdad97a8181ddaa96c64faeef1f2b6edf9
ExcludeArch: i686 armv7hl

# Bundled libraries
# https://fedoraproject.org/wiki/Bundled_Libraries?rd=Packaging:Bundled_Libraries#Requirement_if_you_bundle
# TinyThread++
# https://tinythreadpp.bitsnbites.eu/
# https://gitorious.org/tinythread/tinythreadpp
Provides: bundled(tiny-thread) = 1.1


%description

Bowtie, an ultrafast, memory-efficient short read aligner for short
DNA sequences (reads) from next-gen sequencers. Please cite: Langmead
B, et al. Ultrafast and memory-efficient alignment of short DNA
sequences to the human genome. Genome Biol 10:R25.

%prep
%setup -q -n %{name}-%{version}-src

# Remove the directory to avoid building bowtie with bundled libraries.
rm -rf third_party/

# Fix shebang to use system python3.
for file in $(find . -name "*.py") bowtie bowtie-*; do
  sed -E -i '1s|/usr/bin/env python[3]?|%{__python3}|' "${file}"
done


%build
# Set flags considering bowtie2's testing cases for each architecture.
# https://github.com/BenLangmead/bowtie2/blob/master/.travis.yml
# https://github.com/BenLangmead/bowtie/pull/102
%ifnarch x86_64
export POPCNT_CAPABILITY=0
%endif

# A workaround to pass the tests.
# Cline paired 2 (fw:1, sam:1) test aborted with -Wp,-D_GLIBCXX_ASSERTIONS
# https://github.com/BenLangmead/bowtie/issues/136
CFLAGS=$(echo "${CFLAGS}" | sed -e 's/-Wp,-D_GLIBCXX_ASSERTIONS//')
export CFLAGS
CXXFLAGS=$(echo "${CXXFLAGS}" | sed -e 's/-Wp,-D_GLIBCXX_ASSERTIONS//')
export CXXFLAGS

# Set debug flag "-g" to prevent the error
# "Empty %%files file debugsourcefiles.list".
%make_build allall EXTRA_FLAGS="-g"


%install
%make_install prefix="%{_prefix}"

mkdir -p %{buildroot}/%{_datadir}/bowtie
cp -a reads %{buildroot}/%{_datadir}/bowtie/
cp -a indexes %{buildroot}/%{_datadir}/bowtie/
cp -a genomes %{buildroot}/%{_datadir}/bowtie/
cp -a scripts %{buildroot}/%{_datadir}/bowtie/

# Install bowtie-*-debug commands used by `bowtie --debug`.
for cmd in bowtie-*-debug; do
  cp -p "${cmd}" %{buildroot}/%{_bindir}/
done

%check
for cmd in bowtie bowtie-build bowtie-inspect; do
  ./"${cmd}" --version | grep 'version %{version}'
done

tar xzvf %{SOURCE1}
cat %{PATCH1} | patch -p1

# See Makefile simple-test target.
scripts/test/simple_tests.pl --bowtie=./bowtie --bowtie-build=./bowtie-build


%files
%license LICENSE
%doc MANUAL NEWS VERSION AUTHORS TUTORIAL doc/{manual.html,style.css}
%dir %{_datadir}/bowtie
%{_bindir}/bowtie
%{_bindir}/bowtie-align-l
%{_bindir}/bowtie-align-l-debug
%{_bindir}/bowtie-align-s
%{_bindir}/bowtie-align-s-debug
%{_bindir}/bowtie-build
%{_bindir}/bowtie-build-l
%{_bindir}/bowtie-build-l-debug
%{_bindir}/bowtie-build-s
%{_bindir}/bowtie-build-s-debug
%{_bindir}/bowtie-inspect
%{_bindir}/bowtie-inspect-l
%{_bindir}/bowtie-inspect-l-debug
%{_bindir}/bowtie-inspect-s
%{_bindir}/bowtie-inspect-s-debug
%{_datadir}/bowtie/genomes
%{_datadir}/bowtie/indexes
%{_datadir}/bowtie/reads
%{_datadir}/bowtie/scripts


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.1-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb 17 2023 Jun Aruga <jaruga@redhat.com> - 1.3.1-1
- Update to upstream release 1.3.1
  Resolves: rhbz#2003918

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Jun Aruga <jaruga@redhat.com> - 1.3.0-1
- Update to upstream release 1.3.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 17 2020 Jun Aruga <jaruga@redhat.com> - 1.2.3-2
- Fix the build failure adding perl(FindBin) and perl(lib) build dependencies.

* Fri Feb 28 2020 Jun Aruga <jaruga@redhat.com> - 1.2.3-1
- Update to upstream release 1.2.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.1-4
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Adam Huffman <bloch@verdurin.com> - 1.0.1-1
- Update to upstream release 1.0.1

* Wed Dec 04 2013 Adam Huffman <bloch@verdurin.com> - 1.0.0-2
- Correct licence information (thanks to Dave Love)
- Reorganise documentation (thanks to Dave Love)
- Fix compilation on ARM


* Wed Aug 07 2013 Adam Huffman <bloch@verdurin.com> - 1.0.0-1
- Update to stable upstream release 1.0.0
- Remove unnecessary script patch


* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.12.7-7
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.7-4
- Rebuilt for c++ ABI breakage

* Mon Jan  9 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.12.7-3
- add patch to fix compilation with GCC 4.7

* Mon Jun 27 2011 Adam Huffman <bloch@verdurin.com> - 0.12.7-2
- add missing doc/ 
- add patch to fix Perl script without shebang

* Mon Sep 13 2010 Adam Huffman <bloch@verdurin.com> - 0.12.7-1
- new upstream release 0.12.7
- changelog at http://bowtie-bio.sourceforge.net/index.shtml

* Tue Aug 31 2010 Adam Huffman <bloch@verdurin.com> - 0.12.5-3
- really fix compilation flags

* Wed Aug 25 2010 Adam Huffman <bloch@verdurin.com> - 0.12.5-2
- fix compilation flags

* Mon Aug  2 2010 Adam Huffman <bloch@verdurin.com> - 0.12.5-1
- initial version

