# Review at https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=238349

%global minor_version 0.3
%global thunar_version 1.8.0
%global xfceversion 4.13

Name:           thunar-media-tags-plugin
Version:        0.3.0
Release:        28%{?dist}
Summary:        Media Tags plugin for the Thunar file manager

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:        http://archive.xfce.org/src/thunar-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2
#VCS:           git:git://git.xfce.org/thunar-plugins/thunar-media-tags-plugin

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  exo >= 0.12.0
BuildRequires:  libxfce4util-devel >= %{xfceversion}
BuildRequires:  Thunar-devel >= %{thunar_version}
BuildRequires:  libxml2-devel
BuildRequires:  intltool
BuildRequires:  gettext
BuildRequires:  taglib-devel >= 1.4

Requires:       Thunar >= %{thunar_version}

%description
This plugin adds special features for media files to the Thunar file manager.
It includes a special media file page for the file properties dialog, a tag 
editor for ID3 or OGG/Vorbis tags and a so-called bulk renamer, which allows 
users to rename multiple audio files at once, based on their tags.


%prep
%setup -q


%build
%configure

%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_libdir}/thunarx-*/%{name}.so


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.0-20
- Update to 0.3.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 0.2.1-5
- Rebuild for Xfce 4.12

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 11 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1 (fixes #926630)
- Define Thunar version conditionally
- Spec file clean-up

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul  8 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.2-13
- add intltool build dep

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 0.1.2-12
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.1.2-10
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Adam Williamson <awilliam@redhat.com> - 0.1.2-8
- port to exo-1 and thunarx-2, fix an implicit linking issue, and
  a crash: all from Debian maintainer Lionel Le Folgoc

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 20 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-5
- Rebuild for Thunar 0.9.93 (Xfce 4.6. Beta 3)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.1.2-4
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-3
- Rebuild for BuildID feature

* Mon Jan 22 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-2
- Rebuild for Thunar 0.8.0.

* Sat Jan 20 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2.

* Sat Nov 11 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.1-1
- Initial Fedora Extras Version.
