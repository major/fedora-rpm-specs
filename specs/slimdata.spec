Name:           slimdata
Version:        2.7.1
Release:        12%{?dist}
Summary:        Tools and library for reading and writing slim compressed data

License:        GPL-3.0-or-later
URL:            http://slimdata.sourceforge.net/
Source0:        http://dl.sf.net/sourceforge/%{name}/slim_v2_7_1.tgz

Patch0:         slimdata-name-change.diff

BuildRequires: make
BuildRequires:     gcc-c++
#BuildRequires:     python3-numpy
BuildRequires:     texlive-latex doxygen texlive-metafont texlive-mfware texlive-geometry

#The current slim algorithm assumes little-endian.  Upstream is (slowly) working on this.
ExcludeArch: ppc64 ppc sparcv9 sparc64

%description
Slim is a data compression system for scientific data sets, both a binary and a
library with C linkage. Slim works with integer data from one or more channels
in a file, which it can compress more rapidly than general tools like gzip.

%package devel
Summary: Headers required when building programs against getdata
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Headers required when building projects that use the slimdata library.

%prep
%setup -q -n slim_v2_7_1
#%patch0 -p1

#Remove included 64-bit biniary
rm -f test/generate_random_data

%build
CPPFLAGS="$RPM_OPT_FLAGS $CPPFLAGS -std=c++98"
export CPPFLAGS

%configure
make %{?_smp_mflags}
make doc

#Rebuild above binary.
#pushd test
#make
#popd

#%check
#make test

%install
mkdir -p %{buildroot}
make DESTDIR=%{buildroot} SUID_ROOT="" install

#delete static lib
rm -f %{buildroot}/%{_libdir}/libslim.a
chmod a+x %{buildroot}/%{_libdir}/libslim.so.0.0

#Rename binary to slimdata; upstream will follow in subsequent releases.
mv %{buildroot}/%{_bindir}/slim %{buildroot}/%{_bindir}/slimdata
rm %{buildroot}/%{_bindir}/unslim %{buildroot}/%{_bindir}/slimcat
#Don't forget the man page: BZ 506141
mv %{buildroot}/%{_mandir}/man1/slim.1 %{buildroot}/%{_mandir}/man1/slimdata.1
pushd .
cd %{buildroot}/%{_bindir}
ln -s slimdata unslim
ln -s slimdata slimcat
popd

%ldconfig_scriptlets

%files
%license COPYING
%doc README AUTHORS TODO VERSIONS
%{_bindir}/*slim*
%{_libdir}/libslim.so.0*
%{_mandir}/man1/*slim*

%files devel
%doc doc/slim_format.pdf doc/html/*
%{_includedir}/version.h
%{_includedir}/slim*.h
%{_libdir}/libslim.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.7.1-8
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.7.1-1
- 2.7.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 24 2016 Jon Ciesla <limburgher@gmail.com> - 2.6.4-12
- Fix FTBFS, BZ 1308136.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.6.4-9
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-3
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 01 2011 Jon Ciesla <limb@jcomserv.net> - 2.6.4-1
- New upstream. 
- Dropping check section as it fails in RPM build.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 7 2009 Matthew Truch <matt at truch.net> - 2.6.3-7
- Excluearch sparcv9 and sparc64 as slimdata doesn't work on bigendian machines

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Matthew Truch <matt at truch.net> - 2.6.3-5
- Change name of man page to slimdata as well (BZ 506141).

* Tue May 5 2009 Matthew Truch <matt at truch.net> - 2.6.3-4
- Change binary name to slimdata.
- Use symlinks for binaries unslim and slimcat

* Tue Apr 21 2009 Matthew Truch <matt at truch.net> - 2.6.3-3
- Correct license tag.
- Make tests run.
- Set exec bit on /usr/lib/libslim.so.0.0

* Sat Apr 4 2009 Matthew Truch <matt at truch.net> - 2.6.3-2
- Don't run tests since they don't seem to work.

* Sun Mar 22 2009 Matthew Truch <matt at truch.net> - 2.6.3-1
- Upstream 2.6.3.  Includes proper licensing.  

* Tue Feb 24 2009 Matthew Truch <matt at truch.net> - 2.6.1b-4
- Include patch to fix gcc-4.4 compilation from Lucian.

* Mon Feb 16 2009 Matthew Truch <matt at truch.net> - 2.6.1b-3
- Fix shared library generation.

* Sun Jan 18 2009 Matthew Truch <matt at truch.net> - 2.6.1b-2
- Properly include BR for building docs and include those docs
- Use better soname for shared library.

* Sat Jan 10 2009 Matthew Truch <matt at truch.net> - 2.6.1b-1
- Update to upstream 2.6.1b.
- Apply fixes to build to better follow Fedora guidelines.

* Tue Oct 28 2008 Matthew Truch <matt at truch.net> - 2.6.1a-1
- Update to upstream 2.6.1a release which includes fixes pushed upstream.

* Fri Oct 24 2008 Matthew Truch <matt at truch.net> - 2.6.1-1
- Initial Fedora build.

