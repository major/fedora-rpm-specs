Summary:          Image and video capture application using unicap toolkit
Name:             ucview
Version:          0.33
Release:          23%{?dist}
License:          GPLv2+
URL:              https://www.unicap-imaging.org/
Source0:          https://www.unicap-imaging.org/downloads/%{name}-%{version}.tar.gz
Source1:          %{name}.desktop
Patch0:           ucview-0.33-gmodule.patch
BuildRequires:    gcc, make
BuildRequires:    intltool, %{_bindir}/perl, perl(XML::Parser), gettext, GConf2-devel
BuildRequires:    libunicapgtk-devel >= 0.2.23, gtk2-devel >= 2.8.0, libglade2-devel
BuildRequires:    desktop-file-utils, dbus-glib-devel >= 0.73
BuildRequires:    libXv-devel, libtheora-devel, libvorbis-devel
Requires:         hicolor-icon-theme
Requires(pre):    GConf2
Requires(post):   GConf2, scrollkeeper
Requires(preun):  GConf2
Requires(postun): scrollkeeper

%description
UCView is a video image capture application using the unicap toolkit.
It provides a simple way to parametrise the video device, can capture
still images from the video stream or record the stream as mpeg file.
By using unicap, it can access many different video capture devices
like webcams, video grabber boards, IEEE-1394 (FireWire) cameras and
others.

%package devel
Summary:          Development files for UCView
Requires:         %{name}%{?_isa} = %{version}-%{release}, pkgconfig

%description devel
The ucview-devel package includes header files necessary for building
and developing programs and plugins which use UCView.

%prep
%setup -q
%patch0 -p1 -b .gmodule

%build
%configure --disable-schemas-install
%make_build

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%make_install
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

# Install a working ucview.desktop file
desktop-file-install --vendor "" --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

# Create plugin directory for ucview plugins
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/

%find_lang %{name}

%pre
%gconf_schema_prepare %{name}

%post
scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :
%gconf_schema_upgrade %{name}

%if 0%{?rhel} && 0%{?rhel} <= 7
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi
%endif

%preun
%gconf_schema_remove %{name}

%postun
scrollkeeper-update -q || :

%if 0%{?rhel} && 0%{?rhel} <= 7
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi
%endif

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*

%files devel
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 18 2010 Robert Scheck <robert@fedoraproject.org> 0.33-1
- Upgrade to 0.33 (#643107)

* Sat Feb 27 2010 Robert Scheck <robert@fedoraproject.org> 0.31-1
- Upgrade to 0.31 (#530708)

* Sat Oct 24 2009 Robert Scheck <robert@fedoraproject.org> 0.30-1
- Upgrade to 0.30 (#530708)

* Sun Sep 27 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.23-4
- Update desktop file according to F-12 FedoraStudio feature

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 24 2009 Robert Scheck <robert@fedoraproject.org> 0.23-2
- Readded wrongly removed build requirement to dbus-glib-devel

* Mon May 04 2009 Robert Scheck <robert@fedoraproject.org> 0.23-1
- Upgrade to 0.23

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 0.22-3
- Rebuild against gcc 4.4 and rpm 4.6

* Sun Oct 19 2008 Robert Scheck <robert@fedoraproject.org> 0.22-2
- Rebuild against unicap 0.93

* Mon Oct 13 2008 Robert Scheck <robert@fedoraproject.org> 0.22-1
- Upgrade to 0.22

* Sun Jul 27 2008 Robert Scheck <robert@fedoraproject.org> 0.21-1
- Upgrade to 0.21

* Mon May 19 2008 Robert Scheck <robert@fedoraproject.org> 0.20.1-1
- Upgrade to 0.20.1

* Sun May 18 2008 Robert Scheck <robert@fedoraproject.org> 0.17-1
- Upgrade to 0.17
- Initial spec file for Fedora and Red Hat Enterprise Linux
