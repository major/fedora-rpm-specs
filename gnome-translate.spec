Name: gnome-translate
Summary: GNOME interface to libtranslate -- Natural language translator
Version: 0.99
Release: 41%{?dist}
License: GPLv2+
URL: http://www.nongnu.org/libtranslate/gnome-translate
Source: http://savannah.nongnu.org/download/libtranslate/gnome-translate-%{version}.tar.gz
Patch0: gnome-translate-0.99-drop_eel2.patch
Patch1: gnome-translate-0.99-selected_tag.patch
Patch2: gnome-translate-0.99-enchant.patch


BuildRequires:  gcc
BuildRequires: libgnomeui-devel, libtranslate-devel, enchant-devel
BuildRequires: intltool, automake, autoconf

BuildRequires: desktop-file-utils >= 0.2.90
BuildRequires: startup-notification-devel >= 0.5
BuildRequires: scrollkeeper gettext

# For intltool:
BuildRequires: perl-XML-Parser >= 2.31-16
BuildRequires: make

Requires(pre): GConf2
Requires(post): GConf2, scrollkeeper
Requires(preun): GConf2
Requires(postun): scrollkeeper


%description
GNOME Translate is a GNOME interface to libtranslate library.
It can translate a text or web page between several natural languages,
and it can automatically detect the source language as you type.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

intltoolize --automake --force
aclocal
automake
autoconf


%build

export LDFLAGS="-Wl,--export-dynamic"

%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

desktop-file-install --delete-original      \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications             \
  $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %{name}



%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :
fi


%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :


%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
fi


%postun
scrollkeeper-update -q || :


%files -f %{name}.lang

%doc AUTHORS COPYING README

%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/gnome/help/%{name}
%{_datadir}/omf/%{name}
%{_datadir}/applications/*
%{_sysconfdir}/gconf/schemas/%{name}.schemas


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-37
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.99-22
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.99-18
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 18 2010 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.99-16
- Drop eel2 dependencies (#555502, #555509)
- Run autoconf stuff to actualy enable enchant isntead of aspell

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.99-14
- Use enchant instead of aspell for language autodetection
  (#477274, patch by Caolan McNamara <caolanm@redhat.com>)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.99-12
- Autorebuild for GCC 4.3

* Thu Aug 16 2007 Dmitry Butskoy <Dmitry@Butskoy.name>
- Change License tag to GPLv2+

* Tue Jun 26 2007 Dmitry Butskoy <Dmitry@Butskoy.name>
- drop X-Fedora category from desktop file

* Tue Nov 21 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.99-11
- Don't set "ShowOnlyIn=Gnome" flag, it is not needed.

* Fri Sep  1 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.99-10
- rebuild for FC6

* Mon Aug 14 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.99-9
- add patch to properly restore selected languages from
  the previous invocation (required for recent gtk2 libraries)
- drop killall -HUP in scripts -- no more needed.

* Sun Jul 16 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.99-8
- rebuild for new libgail

* Tue Apr 11 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.99-7
- use "export-dynamic" for the linker, as it is recommended
  by upstream (Solves #188491)

* Wed Feb 15 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.99-6
- rebuild for FC5

* Thu Feb  2 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.99-5
- add patch for compatibility with eel2 library >= 2.13

* Tue Sep 13 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.99-4
- Hack: add an extra dependency -- gnome-keyring-devel,
  due to missing one in current rawhide's libgnomeui-devel

* Mon Sep 12 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.99-3
- more spec file cleanups
- accepted for Fedora Extra
  (review by Aurelien Bompard <gauret@free.fr>)

* Sat Sep 10 2005 Dmitry Butskoy <Dmitry@Butskoj.name> - 0.99-2
- clenups (#165960)

* Fri Aug 19 2005 Dmitry Butskoy <Dmitry@Butskoj.name> - 0.99-1
- Initial release.
