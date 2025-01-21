%global tomoe_ver 0.6.0

Name:           tomoe-gtk
Version:        %{tomoe_ver}
Release:        46%{?dist}
Summary:        Gtk library for tomoe for Japanese and Chinese handwritten input

License:        LGPL-2.0-or-later
URL:            https://sourceforge.net/projects/tomoe/
Source0:        http://downloads.sourceforge.net/project/tomoe/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-0.6.0-rpath.patch
Patch1:         %{name}-0.6.0-cflags.patch

Requires:       tomoe >= %{tomoe_ver}
Obsoletes:      libtomoe-gtk < 0.6.0-4
Provides:       libtomoe-gtk = %{version}-%{release}
BuildRequires: make
BuildRequires:  libtool
BuildRequires:  autoconf, automake
BuildRequires:  tomoe-devel >= %{tomoe_ver}, gtk2-devel
# does not currently build with gucharmap-2
#BuildRequires:  gucharmap-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  gettext

%description
Gtk library for tomoe Japanese handwritten input.
This package is used by scim-tomoe or uim-tomoe.


%package devel
Summary:    Gtk library for tomoe Japanese handwritten input
Requires:   %{name} = %{version}-%{release}
Requires:   gtk2-devel, libgnomeui-devel, gucharmap-devel, tomoe-devel
Obsoletes:  libtomoe-gtk-devel < 0.6.0-4
# added for F10
Provides:   libtomoe-gtk-devel = %{version}-%{release}


%description devel
The libtomoe-devel package includes the header files for libtomoe-gtk.
Install this if you want to develop programs which will use libtomoe-gtk.


%prep
%setup -q
%patch -P0 -p0 -b .rpath
%patch -P1 -p0 -b .cflags

%build
autoreconf -ivf
%configure --disable-static --without-gucharmap --disable-dependency-tracking \
  --disable-rpath --with-python=no
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" 
cd po
mkdir -p locale
for p in *.po;do
    loc=$(basename $p .po)
    mkdir -p locale/$loc/LC_MESSAGES
    msgfmt $p -o locale/$loc/LC_MESSAGES/%{name}.mo
done
cd ..

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}
cp -R po/locale $RPM_BUILD_ROOT/%{_datadir}

rm $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%ldconfig_scriptlets

%ldconfig_scriptlets devel

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README TODO
%{_libdir}/lib%{name}.so.*
%{_datadir}/%{name}/

%files devel
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so
%{_includedir}/tomoe/*
%{_datadir}/gtk-doc/html/lib%{name}/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Takao Fujiwara <tfujiwar@redhat.com> - 0.6.0-41
- Migrate license tag to SPDX

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Takao Fujiwara <tfujiwar@redhat.com> - 0.6.0-34
- Disable python2

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 08 2019 Takao Fujiwara <tfujiwar@redhat.com> - 0.6.0-32
- Replaced python_sitearch with python2_sitearch

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 22 2016 Ding-Yi Chen <dchen@redhat.com> - 0.6.0-25
- Fixed Bug 1240071 - tomoe-gtk: FTBFS in rawhide
- Correct path for translation

* Tue May 10 2016 Ding-Yi Chen <dchen@redhat.com> - 0.6.0-24
- Fixed Bug 1240071 - tomoe-gtk: FTBFS in rawhide

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 25 2013 Ding-Yi Chen - 0.6.0-18
- Fixed Bug 926646 - tomoe-gtk: Does not support aarch64 in f19 and rawhide

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.6.0-14
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 29 2009 Ding-Yi Chen <dchen at redhat.com> - 0.6.0-11
- Add patch src/Makefile.am to fix RH Bug 499880: tomoe-gtk not built with $RPM_OPT_FLAGS

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Ding-Yi Chen <dchen at redhat.com> - 0.6.0-9
- Add back autoconf, automake to fix RH Bug 499880: tomoe-gtk not built with $RPM_OPT_FLAGS

* Fri Jul 10 2009 Ding-Yi Chen <dchen at redhat.com> - 0.6.0-8
- Actually Fixed RH Bug 499880: tomoe-gtk not built with $RPM_OPT_FLAGS

* Wed May 13 2009 Ding-Yi Chen <dchen at redhat.com> - 0.6.0-7
- Fixed RH Bug 499880: tomoe-gtk not built with $RPM_OPT_FLAGS
- Add libtool BuildRequires.
- Fixed rpath issues.
- Add tomoegtk.so

* Fri May  8 2009 Ville Skyttä <ville.skytta at iki.fi> - 0.6.0-6
- Build with $RPM_OPT_FLAGS (patch to avoid discarding user set $CFLAGS).
- Disable autotools dependency tracking during build for cleaner build logs
  and possible slight build speedup.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Jens Petersen <petersen@redhat.com> - 0.6.0-4.fc10
- package renamed from libtomoe-gtk to tomoe-gtk in line with upstream
- no longer need pkgname macro
- obsolete libtomoe-gtk
- make license field LGPLv2+
- disable gucharmap for now since doesn't build yet with gucharmap-2

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6.0-3.fc9
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.6.0-2
- Rebuild for selinux ppc32 issue.

* Fri Jun 29 2007 Jens Petersen <petersen@redhat.com> - 0.6.0-1
- update to 0.6.0
- add %%pkgname for new upstream package name tomoe-gtk

* Thu Apr 12 2007 Jens Petersen <petersen@redhat.com> - 0.5.1-2
- rebuild for libgucharmap.so.6

* Thu Feb 15 2007 Jens Petersen <petersen@redhat.com> - 0.5.1-1
- update to 0.5.1
- add some more doc files

* Sun Jan 21 2007 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 0.5.0-2
- fix the building dependencies.

* Thu Jan 18 2007 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 0.5.0-1
- update to 0.5.0.

* Thu Dec 21 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 0.4.0-1
- update to 0.4.0.

* Sat Sep 16 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 0.1.0-7
- mass rebuilding.

* Wed Jul 26 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 0.1.0-6
- add a buildreq of gettext.

* Tue Feb 28 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 0.1.0-5
- add "ldconfig" for the devel subpackage (Thanks, John Mahowald)

* Fri Jan 27 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 0.1.0-4
- modify "ldconfig" in the "post" section (Thanks, John Mahowald)

* Fri Dec 30 2005 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 0.1.0-3
- a bit more cleanup

* Fri Dec 23 2005 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 0.1.0-2
- add gtk2-devel in the build requirements (Thanks, John Mahowald)

* Wed Dec 7 2005 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 0.1.0-1
- initial packaging for fedora extras
