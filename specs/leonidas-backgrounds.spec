Name:           leonidas-backgrounds
Version:        11.0.0
Release:        30%{?dist}
Summary:        Leonidas desktop backgrounds

License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F11_Artwork

# This is a Fedora maintained package which is specific to our distribution. 
# The source is only available from within this srpm.
# Images in the source archive are basically crops/resizes of 
# https://fedoraproject.org/w/uploads/e/e9/Artwork_F11_Betamockup1_n.jpg
# and
# https://fedoraproject.org/wiki/File:King_4096x1536.xcf.bz2
Source0:        %{name}-%{version}.tar.lzma

BuildArch:      noarch
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-lion-dual = %{version}-%{release}

%description
This package contains desktop backgrounds for the leonidas theme.

%prep
%setup -q

%package        common
Summary:        Leonidas desktop backgrounds shared between GNOME and KDE

%description    common
This package includes the common files used by both GNOME and KDE.

%package        kdm
Summary:        Leonidas desktop background for KDM

%description    kdm
Leonidas desktop background used in KDM.

%package        landscape
Summary:        Leonidas desktop backgrounds with the landscape theme

%description    landscape
This package includes additional Leonidas backgrounds based on the landscape
theme that was used in F11 Leonidas Beta.

%package        lion
Summary:        Extra leonidas desktop background featuring lion 
Requires:       %{name}-lion-dual = %{version}-%{release}

%description    lion
This package includes extra leonidas background featuring the lion that is 
present in F11 Leonidas only on dual screens both on single screens as well.

%package        lion-dual
Summary:        Shared dual screen lion themed Leonidas desktop backgrounds

%description    lion-dual
This package includes dual screen images shared between the 
leonidas-backgrounds and leonidas-backgrounds-lion packages.


%build


%install
rm -rf $RPM_BUILD_ROOT
# prepare the dir structure
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape/normal
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape/wide
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape/normal.dual
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape/wide.dual
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion/normal
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion/normalish
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion/wide
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion/normal.dual
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion/normalish.dual
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion/wide.dual
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties

# copy the landscape images
cp -a $RPM_BUILD_DIR/%{name}-%{version}/landscape/normal \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape
cp -a $RPM_BUILD_DIR/%{name}-%{version}/landscape/wide \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape
cp -a $RPM_BUILD_DIR/%{name}-%{version}/landscape/normal.dual \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape
cp -a $RPM_BUILD_DIR/%{name}-%{version}/landscape/wide.dual \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape

# copy the lion images
cp -a $RPM_BUILD_DIR/%{name}-%{version}/lion/normal \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion
cp -a $RPM_BUILD_DIR/%{name}-%{version}/lion/normalish \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion
cp -a $RPM_BUILD_DIR/%{name}-%{version}/lion/wide \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion
cp -a $RPM_BUILD_DIR/%{name}-%{version}/lion/normal.dual \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion
cp -a $RPM_BUILD_DIR/%{name}-%{version}/lion/normalish.dual \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion
cp -a $RPM_BUILD_DIR/%{name}-%{version}/lion/wide.dual \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion

# copy slideshow xml files
cp -a $RPM_BUILD_DIR/%{name}-%{version}/leonidas.xml \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas
cp -a $RPM_BUILD_DIR/%{name}-%{version}/leonidas-lion.xml \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas
cp -a $RPM_BUILD_DIR/%{name}-%{version}/leonidas_left.xml \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas
cp -a $RPM_BUILD_DIR/%{name}-%{version}/leonidas_right.xml \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas

# copy metadata xmls file
cp -a $RPM_BUILD_DIR/%{name}-%{version}/desktop-backgrounds-leonidas.xml \
        $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties
cp -a $RPM_BUILD_DIR/%{name}-%{version}/desktop-backgrounds-leonidas-lion.xml \
        $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties
cp -a $RPM_BUILD_DIR/%{name}-%{version}/desktop-backgrounds-leonidas-landscape.xml \
        $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties


%files
%doc COPYING
%{_datadir}/gnome-background-properties/desktop-backgrounds-leonidas.xml
%{_datadir}/backgrounds/leonidas/leonidas.xml

%files common
%doc COPYING
%dir %{_datadir}/backgrounds/leonidas
%dir %{_datadir}/backgrounds/leonidas/lion
%dir %{_datadir}/backgrounds/leonidas/lion/normal
%dir %{_datadir}/backgrounds/leonidas/lion/normal/2048x1536
%dir %{_datadir}/backgrounds/leonidas/lion/normalish
%dir %{_datadir}/backgrounds/leonidas/lion/normalish/1280x1024
%dir %{_datadir}/backgrounds/leonidas/lion/wide
%dir %{_datadir}/backgrounds/leonidas/lion/wide/1920x1200
%{_datadir}/backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg
%{_datadir}/backgrounds/leonidas/lion/normalish/1280x1024/leonidas-1-noon.jpg
%{_datadir}/backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg

%files lion-dual
%doc COPYING
%dir %{_datadir}/backgrounds/leonidas
%dir %{_datadir}/backgrounds/leonidas/lion
%{_datadir}/backgrounds/leonidas/lion/normal.dual
%{_datadir}/backgrounds/leonidas/lion/normalish.dual
%{_datadir}/backgrounds/leonidas/lion/wide.dual

%files lion
%doc COPYING
%dir %{_datadir}/backgrounds/leonidas/lion/normal
%dir %{_datadir}/backgrounds/leonidas/lion/normal/2048x1536
%dir %{_datadir}/backgrounds/leonidas/lion/normalish
%dir %{_datadir}/backgrounds/leonidas/lion/normalish/1280x1024
%dir %{_datadir}/backgrounds/leonidas/lion/wide
%dir %{_datadir}/backgrounds/leonidas/lion/wide/1920x1200
%{_datadir}/gnome-background-properties/desktop-backgrounds-leonidas-lion.xml
%{_datadir}/backgrounds/leonidas/leonidas-lion.xml
%{_datadir}/backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg
%{_datadir}/backgrounds/leonidas/lion/normalish/1280x1024/leonidas-1-noon_right.jpg
%{_datadir}/backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg

%files kdm
%doc COPYING
%dir %{_datadir}/backgrounds/leonidas
%dir %{_datadir}/backgrounds/leonidas/lion/normal
%dir %{_datadir}/backgrounds/leonidas/lion/normal/2048x1536
%{_datadir}/backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.png

%files landscape
%doc COPYING
%dir %{_datadir}/backgrounds/leonidas
%{_datadir}/backgrounds/leonidas/landscape
%{_datadir}/gnome-background-properties/desktop-backgrounds-leonidas-landscape.xml
%{_datadir}/backgrounds/leonidas/leonidas_left.xml
%{_datadir}/backgrounds/leonidas/leonidas_right.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 11.0.0-29
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 04 2012 Bruno Wolff III <bruno@wolff.to> - 11.0.0-5
- Removed extra newline from sources file

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 09 2009 Martin Sourada <mso@fedoraproject.org> - 11.0.0-1
- Include the lion design optionally on single screens as well via -lion 
  subpackage
- Split the dual screen images with lion design into -lion-dual subpackage
  to allow having only one of the single screens installed
- Don't forget to own some all used directories not provided by other pkgs

* Mon Apr 13 2009 Martin Sourada <mso@fedoraproejct.org> - 10.93.1-1
- Updated lion backgrounds
- Don't display the lion for single screens
- Use just leonidas-1-noon.png for the kdm version, no need to add the '-simple'
  suffix

* Fri Apr 10 2009 Martin Sourada <mso@fedoraproject.org> - 10.93.0-1
- Add lion backgrounds
- Split -common (shared between GNOME and KDE), -kdm (simplified version for 
  KDM) and -landscape (F11 Leonidas Beta wallpapers) subpackages

* Mon Mar 09 2009 Martin Sourada <mso@fedoraproject.org> - 10.92.1-2
- Add note about source (we are upstream and don't host the source elsewhere)
- Don't pass -r to cp, it's already implied by -a

* Mon Mar 09 2009 Martin Sourada <mso@fedoraproject.org> - 10.92.1-1
- Update to newer version
 - add dual screen versions
 - add left part of dual screen as a wallpaper on its own

* Thu Mar 05 2009 Martin Sourada <mso@fedoraproject.org> - 10.92.0-1
- Initial packaging

