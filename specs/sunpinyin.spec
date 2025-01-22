# TODO: fixes scons to generate debug information
%global debug_package %{nil}

%define _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/xsunpinyin.conf
%define gitdate 20190805

Name:		sunpinyin
Version:	3.0.0
Release:	0.14.%{gitdate}git%{?dist}
Summary:	A statistical language model based Chinese input method engine
License:	LGPL-2.1-only OR CDDL-1.0
URL:		http://code.google.com/p/sunpinyin/
Source0:	%{name}-%{gitdate}.tar.xz
Source2:	http://downloads.sourceforge.net/project/open-gram/lm_sc.3gm.arpa-20140820.tar.bz2
Source3:	http://downloads.sourceforge.net/project/open-gram/dict.utf8-20131214.tar.bz2
Patch0: 	sunpinyin-use-python3.patch
Patch1: 	sunpinyin-fixes-scons.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:	sqlite-devel
BuildRequires:	gettext	
BuildRequires:	python3-scons
BuildRequires:	perl(Pod::Man)
BuildRequires:	python3-devel

%description
Sunpinyin is an input method engine for Simplified Chinese. It is an SLM based
IM engine, and features full sentence input.

SunPinyin has been ported to various input method platforms and operating 
systems. The 2.0 release currently supports iBus, XIM, and Mac OS X. 

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files that allows user
to write their own front-end for sunpinyin.

%package data
Summary:	Little-endian data files for %{name}
License:	CC-BY-SA-3.0
Obsoletes:	%{name}-data-le
Obsoletes:	%{name}-data-be

%description data
The %{name}-data package contains necessary lexicon data and its index data
files needed by the sunpinyin input methods.

%prep
%autosetup -p1 -n %{name}-%{gitdate}

mkdir -p raw
cp %SOURCE2 raw
cp %SOURCE3 raw
pushd raw
tar xvf lm_sc.3gm.arpa-20140820.tar.bz2
tar xvf dict.utf8-20131214.tar.bz2
popd

%build
# export CFLAGS, CXXFLAGS, LDFLAGS, ...
%configure || :

scons %{?_smp_mflags} --prefix=%{_prefix} --libdir=%{_libdir} --datadir=%{_datadir}
export PATH=`pwd`/src:$PATH
pushd raw
ln -sf ../doc/SLM-inst.mk Makefile
make %{?_smp_mflags} VERBOSE=1
popd

%install
scons %{?_smp_mflags} --prefix=%{_prefix} --libdir=%{_libdir} --datadir=%{_datadir} install --install-sandbox=%{buildroot}
pushd raw
make install DESTDIR=%{buildroot} INSTALL="install -p"
popd

# additional %%doc files to include by path to avoid duplicates/conflicts
# see https://bugzilla.redhat.com/1001266
install -m0644 AUTHORS TODO %{buildroot}%{_docdir}/%{name}


%files
%license COPYING *.LICENSE
%{_libdir}/libsunpinyin*.so.*
%{_docdir}/%{name}/README
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/TODO

%files devel
%{_libdir}/libsunpinyin*.so
%{_libdir}/pkgconfig/sunpinyin*.pc
%{_includedir}/sunpinyin*

%files data
%{_datadir}/%{name}
%{_bindir}/*
%{_mandir}/man1/*.1.gz
%{_docdir}/%{name}/SLM-*.mk

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.14.20190805git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.13.20190805git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.12.20190805git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.11.20190805git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 28 2023 Peng Wu <pwu@redhat.com> - 3.0.0-0.10.20190805git
- Migrate to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.9.20190805git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.8.20190805git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.7.20190805git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.6.20190805git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.5.20190805git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.4.20190805git
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.3.20190805git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.2.20190805git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug  5 2019 Peng Wu <pwu@redhat.com> - 3.0.0-0.1.20190805git
- Update scons and use python3

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-0.26.20160301git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-0.25.20160301git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 Peng Wu <pwu@redhat.com> - 2.0.4-0.24.20160301git%{?dist}
- Use python2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-0.23.20160301git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.4-0.22.20160301git
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-0.21.20160301git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-0.20.20160301git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-0.19.20160301git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-0.18.20160301git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar  1 2016 Peng Wu <pwu@redhat.com> - 2.0.4-0.17.20160301git
- Update to the latest upstream git snapshot

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-0.16.20130710git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-0.15.20130710git
- Rawhide only: Fix pod2man invocation for perl-podlators >= 4.
- Export global compiler flags before building.
- Minor spec cleanup: remove %%defattr usage and %%clean section,
  use %%license, add %%_isa to -devel base package dependency,
  don't mix %%buildroot and $RPM_BUILD_ROOT
- Insert gitdate into release to follow snapshot guidelines.
- Fix duplicated doc files (#1001266).

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-0.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.4-0.13
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-0.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 2.0.4-0.11
- Handle AArch64 as well

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 10 2013 Liang Suilong <liangsuilong@gmail.com> - 2.0.4-0.8
- Upstream to the latest git snapshot

* Sun Feb 24 2013 Liang Suilong <liangsuilong@gmail.com> - 2.0.4-0.7
- Drop ibus-sunpinyin
- Drop xsunpinyin
- Architecture-dependent data file
- Upstream sunpinyin data file

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 28 2012 Liang Suilong <liangsuilong@gmail.com> - 2.0.4-0.5
- Fix the spec file for building fcitx-sunpinyin

* Thu Jul 26 2012 Liang Suilong <liangsuilong@gmail.com> - 2.0.4-0.4
- Upstream to the latest git snapshot

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 03 2012 Liang Suilong <liangsuilong@gmail.com> - 2.0.4-0.2
- Upstream to the latest git snapshot

* Sun May 13 2012 Liang Suilong <liangsuilong@gmail.com> - 2.0.4-0.1
- Upstream to the latest git snapshot
- Add BR: python-devel
- Upgrade to the latest SLM Data
- Drop the patch: sunpinyin-fixes-unistd-compile.patch

* Tue Mar 06 2012  Peng Wu <pwu@redhat.com> - 2.0.3-4
- Rebuilt for ibus-1.4.99

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.0.3-2
- Rebuild for new libpng

* Fri Feb 18 2011 Howard Ning <mrlhwliberty@gmail.com> - 2.0.3-1
- New upstream

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 26 2010  Peng Wu <pwu@redhat.com> - 2.0.2-4
- Fixes build for ibus 1.4

* Thu Aug 19 2010 Chen Lei <supercyper@163.com> - 2.0.2-3
- Rebuild for Rawhide

* Thu Aug 19 2010 Chen Lei <supercyper@163.com> - 2.0.2-2
- Add seperate license field to data files

* Mon Aug 16 2010 Chen Lei <supercyper@163.com> - 2.0.2-1
- Initial Package
