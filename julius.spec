%global dkcommit 1ceb4de

Name:		julius
Version:	4.5
Release:	9%{?dist}
Summary:	Large vocabulary continuous speech recognition (LVCSR) decoder software
License:	Julius
URL:		https://github.com/julius-speech/julius
Source0:	https://github.com/julius-speech/julius/archive/v%{version}.tar.gz
# Source1:	http://julius.sourceforge.jp/archive/japanese-models.tar.gz
# Need to generate from git
# BE SURE YOU HAVE git-lfs installed before doing a clone
# git clone https://github.com/julius-speech/dictation-kit.git
# cd dictation-kit
# rm -rf bin src
# cd ..
# tar --exclude-vcs -cJf dictation-kit-%%{dkcommit}.tar.xz dictation-kit
Source1:	dictation-kit-%{dkcommit}.tar.xz
Patch0:		julius-4.5-DESTDIR.patch
Patch1:		julius-4.5-sharedlibs.patch
Patch2:		julius-4.5-cpuidfix.patch
Patch3:		julius-ldflags.patch

BuildRequires:	perl-generators
BuildRequires:	perl(Jcode), alsa-lib-devel, libsndfile-devel, pulseaudio-libs-devel, zlib-devel, readline-devel
BuildRequires:	SDL2-devel
BuildRequires:	bison, flex, nkf
BuildRequires:  autoconf, automake, libtool
BuildRequires: make
# Requires:	

%description
"Julius" is a high-performance, two-pass large vocabulary continuous speech 
recognition (LVCSR) decoder software for speech-related researchers and 
developers. Based on word N-gram and context-dependent HMM, it can perform 
almost real-time decoding on most current PCs in 60k word dictation task. 
Major search techniques are fully incorporated such as tree lexicon, N-gram 
factoring, cross-word context dependency handling, enveloped beam search, 
Gaussian pruning, Gaussian selection, etc. Besides search efficiency, it is 
also modularized carefully to be independent from model structures, and 
various HMM types are supported such as shared-state triphones and 
tied-mixture models, with any number of mixtures, states, or phones. 
Standard formats are adopted to cope with other free modeling toolkit such 
as HTK, CMU-Cam SLM toolkit, etc. 

%package devel
Requires:	julius = %{version}-%{release}
Summary:	Development files and libraries for libjulius and libsent

%description devel
Development files and libraries	for libjulius and libsent.

%package japanese-models
BuildArch:	noarch
Requires:	julius = %{version}-%{release}
Summary:	Julius Japanese language model and acoustic models
License:	Julius

%description japanese-models
A Japanese language model (20k-word trained by newspaper article) and acoustic 
models (Phonetic tied-mixture triphone / monophone) for use with Julius.

%prep
%setup -q -a 1
%patch0 -p1 -b .DESTDIR
%patch1 -p1 -b .shared
%patch2 -p1 -b .cpuidfix
%patch3 -p1
# Fix end-of-line encoding
sed -i 's/\r//' Release.txt
autoreconf -ifv || :

%build
%configure
# this fails
# make %{?_smp_mflags}
make

%install
mkdir -p %{buildroot}%{_libdir}/pkgconfig/
make install DESTDIR=%{buildroot}
chmod +x %{buildroot}%{_libdir}/*.so.*

mkdir -p %{buildroot}%{_datadir}/julius/
cp -a Sample.jconf %{buildroot}%{_datadir}/julius/
pushd dictation-kit
cp *conf %{buildroot}%{_datadir}/julius/
cp -a model/ %{buildroot}%{_datadir}/julius/
popd

# rename to avoid conflict with Oracle Java
mv %{buildroot}%{_bindir}/jcontrol %{buildroot}%{_bindir}/julius-jcontrol

%ldconfig_scriptlets

%files
%doc ChangeLog Release.txt Release-ja.txt
%license LICENSE.txt
%{_bindir}/accept_check
%{_bindir}/adinrec
%{_bindir}/adintool
%{_bindir}/adintool-gui
%{_bindir}/binlm2arpa
%{_bindir}/dfa_determinize
%{_bindir}/dfa_minimize
%{_bindir}/generate
%{_bindir}/generate-ngram
%{_bindir}/gram2sapixml.pl
%{_bindir}/jclient.pl
%{_bindir}/julius-jcontrol
%{_bindir}/julius
%{_bindir}/mkbingram
%{_bindir}/mkbinhmm
%{_bindir}/mkbinhmmlist
%{_bindir}/mkdfa.pl
%{_bindir}/mkfa
%{_bindir}/mkgshmm
%{_bindir}/mkss
%{_bindir}/nextword
%{_bindir}/yomi2voca.pl
%{_libdir}/libjulius.so.*
%{_libdir}/libsent.so.*
# %%lang(ja) %%{_mandir}/ja/man1/*
# %%{_mandir}/man1/*
%dir %{_datadir}/julius/
%{_datadir}/julius/*conf

%files devel
%{_bindir}/libjulius-config
%{_bindir}/libsent-config
%{_includedir}/julius/
%{_includedir}/sent/
%{_libdir}/libjulius.so
%{_libdir}/libsent.so
%{_libdir}/pkgconfig/*.pc

%files japanese-models
%{_datadir}/julius/model/

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb  8 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.5-8
- Drop link and optimization flags from pkgconf files (avoids issues with
  https://fedoraproject.org/wiki/Changes/Package_information_on_ELF_objects)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Tom Callaway <spot@fedoraproject.org> - 4.5-1
- update to 4.5

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.4.2.1-6
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov  8 2017 Tom Callaway <spot@fedoraproject.org> - 4.4.2.1-2
- fix cpuid.h conditionalization to be more complete

* Tue Nov  7 2017 Tom Callaway <spot@fedoraproject.org> - 4.4.2.1-1
- update to 4.4.2.1
- rename jcontrol to julius-jcontrol to avoid conflict with oracle java

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 4.2.2-10
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep  3 2014 Tom Callaway <spot@fedoraproject.org> - 4.2.2-7
- fix DESTDIR patch so that mkfa and mkdfa.pl get installed

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 4.2.2-3
- Perl 5.18 rebuild

* Tue Aug 28 2012 Tom Callaway <spot@fedoraproject.org> - 4.2.2-2
- fix Source0 URL

* Mon Aug 13 2012 Tom Callaway <spot@fedoraproject.org> - 4.2.2-1
- initial package
