# review at https://bugzilla.redhat.com/show_bug.cgi?id=229930
%global xfceversion 4.16
%global _hardened_build 1
%global debug_package %{nil}

Name:           thunar-volman
Version:        4.16.0
Release:        5%{?dist}
Summary:        Automatic management of removable drives and media for Thunar
License:        GPLv2+
URL:            http://goodies.xfce.org/projects/thunar-plugins/%{name}
#VCS: git:git://git.xfce.org/xfce/thunar-volman
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  exo-devel >= 0.6.0
BuildRequires:  xfconf >= %{xfceversion}
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libgudev1-devel >= 145
BuildRequires:  libnotify-devel >= 0.4.0
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
Requires:       Thunar >= %{xfceversion}

%description
The Thunar Volume Manager is an extension for the Thunar file manager, which 
enables automatic management of removable drives and media. For example, if 
thunar-volman is installed and configured properly, and you plug in your 
digital camera, it will automatically launch your preferred photo application 
and import the new pictures from the camera into your photo collection.


%prep
%setup

sed -i 's/XFCE;//' thunar-volman-settings/thunar-volman-settings.desktop.in.in


%build
%configure
%make_build


%install
%make_install

%find_lang %{name}

desktop-file-install \
%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
    --vendor fedora                        \
%endif
    --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
    --add-only-show-in=XFCE                                 \
    --delete-original                                       \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}-settings.desktop


%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS THANKS
%license COPYING
%{_bindir}/thunar-volman
%{_bindir}/thunar-volman-settings
%{_datadir}/icons/*/*/*/*
%{_datadir}/applications/*thunar-volman-settings.desktop


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.16.0-1
- Update to 4.16.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9.5-1
- Update to 0.9.5

* Mon Jul 29 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9.4-1
- Update to 0.9.4

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9.3-1
- Update to 0.9.3

* Sat May 18 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9.2-1
- Update to 0.9.2

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 02 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9.0-20
- Update to 0.9.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 10 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.8.1-8
- Spec modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 17 2015 Kevin Fenzi <kevin@scrye.com> 0.8.1-1
- Update to 0.8.1

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 0.8.0-9
- Rebuild for Xfce 4.12

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.8.0-8
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.8.0-4
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 29 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0 (Xfce 4.10 final)
- Add VCS key and review #

* Sat Apr 14 2012 Kevin Fenzi <kevin@scrye.com> - 0.7.1-1
- Update to 0.7.1 (Xfce 4.10pre2)

* Tue Apr 03 2012 Kevin Fenzi <kevin@scrye.com> - 0.7.0-1
- Update to 0.7.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 16 2011 Kevin Fenzi <kevin@tummy.com> - 0.6.0-1
- Update to 0.6.0 (for Thunar 1.2.0 on Xfce 4.8 final)

* Sun Dec 05 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.3-1
- Update to 0.5.3 (for Thunar 1.1.5 on Xfce 4.8 pre2)

* Sat Nov 06 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2 (for Thunar 1.1.4 on Xfce 4.8 pre1)
- BR libgudev1-devel
- Fix for libnotify 0.7.0 (bugzilla.xfce.org #6916)

* Sat Nov 06 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.80-5
- Fix missing icons (#650504)

* Sun Oct 03 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.80-4
- Fix the parole patch (#639484)
- Update gtk-icon-cache scriptlets

* Sat Oct 02 2010 Kevin Fenzi <kevin@tummy.om> - 0.3.80-3
- Add patch to default to parole for video/audio (#639484)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Feb 28 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.80-1
- Update to 0.3.80
- Add Category X-XfceSettingsDialog

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.0-2
- Autorebuild for GCC 4.3

* Mon Dec 03 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0 and Thunar 0.9.0

* Tue Aug 21 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-2
- Rebuild for BuildID feature

* Sun Jan 21 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2.

* Wed Jan 17 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-1
- Initial packaging.
