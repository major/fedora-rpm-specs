Name:      glglobe
Version:   0.2
Release:   44%{?dist}
Summary:   OpenGl Globe - Earth simulation for linux

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:   GPL-2.0-only
URL:       http://www.geocities.com/harpin_floh/glglobe_page.html
Source0:   http://www.geocities.com/harpin_floh/mysoft/glglobe-0.2.tar.gz
# glglobe does not have icons of its own. I modifed the upstream website's
# banner logo, selected a limited part to get the sun effect, then scaled that 
# to the standard icon sizes required. On 2007-07-29 I requested upstream to 
# provide suitable icons, or provide feedback on those I created, but no 
# response has been received.
Source1:   glglobe.16x16.png
Source2:   glglobe.24x24.png
Source3:   glglobe.48x48.png
# This desktop file was created by hand.
Source4:   glglobe.desktop

Patch0:    glglobe-0.2-fix-newline-warnings.patch
Patch1:    glglobe-0.2-fix-signedness-differs-warnings.patch
# if the default params are not set, glglobe segfaults when the middle click
# menu is activated
Patch2:    glglobe-0.2-set-default-params.patch
Patch3:    glglobe-0.2-makefile_accept_passed_optflags.patch
Patch4:    glglobe-freeglut.patch

BuildRequires:  gcc
BuildRequires: freeglut-devel libpng-devel libjpeg-devel 
BuildRequires: libXext-devel libXaw-devel libXi-devel desktop-file-utils
BuildRequires: make
##Requires:       todo!

%description
GLGlobe is an OpenGL - globe simulation for Linux. It was inspired by XGlobe or
XEarth and can use the marker-files of these programs. The simulation includes
day light and night time rendering, and the globe can be rotated and scaled 
interactively, or automatically rotated based on the current time of day


%prep
# -n sets tgz extract folder to match version
%setup -q -n glglobe
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p0

%build
#no configure, so:
export CFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
# manual install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 glglobe %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/glglobe
install -p -m 0644 depths_1440.jpg xglobe-markers earth-markers-schaumann %{buildroot}%{_datadir}/glglobe

#mkdir -p %{buildroot}%{_docdir}/glglobe
#install -p -m 0644 ChangeLog COPYING README TODO %{buildroot}%{_docdir}/glglobe

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/
install -p -m 644 %{SOURCE1} \
        %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/24x24/apps/
install -p -m 644 %{SOURCE2} \
        %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
install -p -m 644 %{SOURCE3} \
        %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/

mkdir -p %{buildroot}%{_datadir}/applications
#install -p -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications %{SOURCE4}





%files
%{_bindir}/glglobe
%{_datadir}/glglobe
%{_datadir}/applications/*glglobe.desktop
%{_datadir}/icons/hicolor/*/apps/glglobe.*.png
%doc ChangeLog COPYING README TODO


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2-43
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-33
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.2-30
- Rebuilt for new freeglut

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2-25
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.2-16
- Drop desktop vendor tag.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.2-14
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.2-13
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.2-10
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2-6
- Autorebuild for GCC 4.3

* Sat Aug 11 2007 David Timms <dtimms at iinet.net.au> - 0.2-5
- actually build with updated .desktop file

* Thu Aug  9 2007 David Timms <dtimms at iinet.net.au> - 0.2-4
- add comment re Source1..4 creation
- mod .desktop category to Education
- del .desktop category deprecated items
- del extraneous Requires(post/postun) for desktop-file-utils
- mod desktop-file-install to simpler command, using SOURCEx
- add ownership of app data directory
- mod ownership of icon data to glglobe specific filenames
- mod License to meet new Licensing Guidelines

* Tue Jul 31 2007 David Timms <dtimms at iinet.net.au> - 0.2-3
- add BuildRequires: desktop-file-utils so that it builds in mock

* Sun Jul 29 2007 David Timms <dtimms at iinet.net.au> - 0.2-2
- del commenting about non-existent configure.
- add export CFLAGS="$RPM_OPT_FLAGS" so that rpm flags are used during build.
- add makefile patch to use environment CFLAGS if they are defined.

* Sun Jul 29 2007 David Timms <dtimms at iinet.net.au> - 0.2-1
- Initial fedora package submission for review

