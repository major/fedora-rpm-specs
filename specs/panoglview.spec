Summary:       Immersive viewer for spherical panoramas
Name:          panoglview
Version:       0.2.2
Release:       44%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://hugin.sourceforge.net/
Source0:       http://downloads.sourceforge.net/hugin/%{name}-%{version}.tar.gz
Source1:       %{name}.desktop
Source2:       %{name}.png
Patch0:        wxwidgets3.0.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires: libtiff-devel libjpeg-devel libpng-devel
BuildRequires: wxGTK-devel zlib-devel desktop-file-utils

%description
Use panoglview to explore equirectangular panoramic images.  Equirectangular
panoramas are typically JPEG/TIFF/PNG images with a 2:1 aspect ratio.

%prep
%setup -q
%patch -P0 -p1
chmod -x src/*.h src/*.cpp

%build
%configure
make %{?_smp_mflags} LDFLAGS="-lGL -lGLU"

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
desktop-file-install --vendor="" \
  --dir=%{buildroot}/%{_datadir}/applications %{SOURCE1}
install -D -m 0755 %{SOURCE2} %{buildroot}/%{_datadir}/pixmaps/%{name}.png

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.2-43
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-37
- Rebuild due to wxGLCanvas ABI change

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 0.2.2-36
- Rebuild with wxWidgets 3.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Scott Talbert <swt@techie.net> - 0.2.2-29
- Rebuild with wxWidgets GTK3 build

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Bruno Postle <bruno@postle.net> - 0.2.2-26
- update wxWidgets 3.0 patch from upstream

* Tue Nov 06 2018 Scott Talbert <swt@techie.net> - 0.2.2-25
- Rebuild with wxWidgets 3.0 (GTK+ 2 build)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.2-16
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 0.2.2-8
- rebuilt against wxGTK-2.8.11-2

* Tue Feb 23 2010 Bruno Postle <bruno@postle.net> 0.2.2-7
- Fix for implicit DSO linking bug #564711

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 01 2009 Bruno Postle <bruno@postle.net> 0.2.2-5
- spec improvements, add icon

* Tue Jun 16 2009 Bruno Postle <bruno@postle.net> 0.2.2-4
- spec improvements

* Mon Jul 28 2008 Bruno Postle <bruno@postle.net> 0.2.2-3
- 0.2.2 release

* Fri Jul 20 2007 Bruno Postle <bruno@postle.net> 0.2.2-1cvs20070720
- CVS snapshot add .desktop

* Mon Jul 02 2007 Bruno Postle <bruno@postle.net> 0.2-6
- rebuild for fc7 with spec cleanup

* Tue May 16 2006 Bruno Postle <bruno@postle.net> 0.2-5.fc5.bp

* Fri Mar 24 2006 Bruno Postle <bruno@postle.net> 0.2-4.fc5.bp
- rebuild for fc5

* Tue Dec 06 2005 Bruno Postle <bruno@postle.net>
- build on another host due to mystery c++ 3.6.4 errors

* Wed Nov 30 2005 Bruno Postle <bruno@postle.net>
- switch to current CVS, remove old build patches. requires freshrpms wxGTK >= 2.6.0

* Fri Jul 22 2005 Bruno Postle <bruno@postle.net>
- new build for fc4.  now uses GTK2

* Wed Oct 20 2004 Bruno Postle <bruno@postle.net>
- new build for fc2

* Tue Jun 22 2004 Bruno Postle <bruno@postle.net>
  - initial RPM

