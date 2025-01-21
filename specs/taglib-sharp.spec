%global debug_package %{nil}

Name:    taglib-sharp
Version: 2.1.0.0
Release: 26%{?dist}
Summary: Provides tag reading and writing for Banshee and other Mono apps

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     http://download.banshee-project.org/taglib-sharp/
Source0: http://download.banshee-project.org/taglib-sharp/%{version}/%{name}-%{version}.tar.bz2
# These files are missing from the 2.1.0.0 tarball for some reason.
# Downloaded into Fedora packages git on 2016-01-19
Source1: https://raw.githubusercontent.com/mono/taglib-sharp/master/examples/extractKey.cpp 
Source2: https://raw.githubusercontent.com/mono/taglib-sharp/master/examples/listData.cpp

# Mono only available on these:
ExclusiveArch: %{mono_arches}

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires: mono-devel, monodoc-devel, gnome-sharp-devel, exiv2-devel

%description
TagLib# is a FREE and Open Source library for the .NET 2.0 and Mono frameworks 
which will let you tag your software with as much or as little detail as you 
like without slowing you down. It supports a large variety of movie and music 
formats which abstract away the work, handling all the different cases, so all 
you have to do is access file.Tag.Title, file.Tag.Lyrics, or my personal 
favorite file.Tag.Pictures. But don't think all this abstraction is gonna keep 
you from tagging's greatest gems. You can still get to a specific tag type's 
features with just a few lines of code. 

%package devel
Summary: Provides tag reading and writing for Banshee and other Mono apps
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Development files for taglib-sharp.

%prep
%setup -q
cp %{SOURCE1} %{SOURCE2} examples/
sed -i "s#gmcs#mcs#g" configure
sed -i "s#gmcs#mcs#g" configure.ac

%build
# building examples is broken
sed -i "s/SUBDIRS = src examples docs/SUBDIRS = src docs/" Makefile.in
# Docs are broken.
%configure --disable-docs
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p %{buildroot}%{_libdir}/pkgconfig
mv %{buildroot}%{_datadir}/pkgconfig/*.pc %{buildroot}%{_libdir}/pkgconfig/

%files
%doc COPYING
%{_prefix}/lib/mono/gac/*/
%{_prefix}/lib/mono/taglib-sharp/

%files devel
# %%doc %%{_libdir}/monodoc/sources/taglib-sharp-docs*
%{_libdir}/pkgconfig/taglib-sharp.pc

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.0.0-25
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.0.0-23
- Rebuilt for exiv2 0.28.2

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 31 2019 Tom Callaway <spot@fedoraproject.org> - 2.1.0.0-13
- rebuild for auto-provides/requires

* Mon Jul 29 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.1.0.0-12
- fix build with Mono 5

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0.0-4
- mono rebuild for aarch64 support

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Tom Callaway <spot@fedoraproject.org> - 2.1.0.0-2
- use global instead of define

* Tue Jan 19 2016 Tom Callaway <spot@fedoraproject.org> - 2.1.0.0-1
- update to 2.1.0.0

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.0.3.7-13
- Build with mono 4

* Thu Nov 27 2014 Dan Horák <dan[at]danny.cz> - 2.0.3.7-12
- switch to mono_arches

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Brent Baude <baude@us.ibm.com> - 2.0.3.7-9
- Changing ppc64 arch to power64 macro

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 29 2011 Christian Krause <chkr@fedoraproject.org> - 2.0.3.7-4
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Mon Mar 21 2011 Dan Horák <dan[at]danny.cz> - 2.0.3.7-3
- updated the supported arch list

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 24 2010 Christian Krause <chkr@fedoraproject.org> - 2.0.3.7-1
- Update to 2.0.3.7

* Sun Feb 28 2010 Christian Krause <chkr@fedoraproject.org> - 2.0.3.6-2
- Fix compilation on x86_64

* Sat Feb 27 2010 Christian Krause <chkr@fedoraproject.org> - 2.0.3.6-1
- Update to 2.0.3.6

* Thu Feb 18 2010 Karsten Hopp <karsten@redhat.com> 2.0.3.2-5.1
- enable s390, s390x where we have mono now

* Mon Oct 26 2009 Dennis Gilmore <dennis@ausil.us> - 2.0.3.2-5
- switch sparc to sparcv9

* Thu Aug 20 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 2.0.3.2-4
- Build for ppc64

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 31 2009 Xavier Lamien <laxathom@fedoraproject.org> - 2.0.3.2-3
- Build arches ppc.

* Wed Feb 25 2009 David Nielsen <dnielsen@fedoraproject.org> - 2.0.3.2-2
- fix pkgconfig file

* Tue Feb 24 2009 David Nielsen <dnielsen@fedoraproject.org> - 2.0.3.2-1
- Update to 2.0.3.2
- The Banshee project has now taking over upstream responsibilities
- Remove patches
- Enable threaded build in accordance to Fedora guidelines

* Mon Feb 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.3.0-8
- disable doc generation

* Mon Nov 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.3.0-7
- apply mimetypes fix recommended by banshee upstream

* Thu Jun 5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.3.0-6
- fix docs generation

* Thu Jun 5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.3.0-5
- Rebuild against new mono bits

* Sat Apr 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.3.0-4
- don't need to specify pkgconfig as a BR, it gets pulled in

* Sat Apr 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.3.0-3
- BR: monodoc-devel

* Sat Apr 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.3.0-2
- just fix noInjectMenuItem

* Sat Apr 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.3.0-1
- initial package
