%global git 5a6c336982e5956c6dce5d3d51d057ac034ce7ca
Summary: A desktop recorder
Name: byzanz
Version: 0.3
Release: 0.32%{?dist}
License: GPLv3+
URL: https://gitlab.gnome.org/Archive/byzanz
#Source0: http://download.gnome.org/sources/%{name}/0.2/%{name}-%{version}.tar.bz2
# git archive --format=tar --prefix=byzanz-%{git}/ %{git} | xz > byzanz-%{git}
Source0: byzanz-%{git}.tar.xz
Patch0:  %{name}-gcc11.patch

BuildRequires: gnome-common
BuildRequires: cairo-devel >= 1.8.10
BuildRequires: gtk3-devel
BuildRequires: libXdamage-devel >= 1.0
BuildRequires: glib2-devel >= 2.6.0
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: gettext-devel
BuildRequires: intltool
BuildRequires: perl(XML::Parser)
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make

Requires(pre): GConf2
Requires(post): GConf2
Requires(preun): GConf2

%description
Byzanz is a desktop recorder striving for ease of use. It can record to 
GIF images, Ogg Theora video - optionally with sound - and other formats.
A command-line recording tool is included.

%prep
%setup -q -n byzanz-%{git}
%patch0 -p1

%build
./autogen.sh
CFLAGS="%optflags -Wno-deprecated-declarations"
%ifarch armv7l armv7hl armv7hnl
# http://rwmj.wordpress.com/2014/01/06/alignment-errors-on-fedora-arm/
CFLAGS="$CFLAGS -Wno-cast-align"
%endif
%configure
make

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make DESTDIR=%{buildroot} install
%find_lang byzanz

%files -f byzanz.lang
%doc AUTHORS ChangeLog COPYING NEWS
%{_bindir}/byzanz-playback
%{_bindir}/byzanz-record
%{_datadir}/icons/hicolor/*/apps/byzanz-record-area.*
%{_datadir}/icons/hicolor/*/apps/byzanz-record-desktop.*
%{_datadir}/icons/hicolor/*/apps/byzanz-record-window.*
%{_mandir}/man1/byzanz.1*
%{_mandir}/man1/byzanz-playback.1*
%{_mandir}/man1/byzanz-record.1*

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 30 2021 Jonathan Wakely <jwakely@redhat.com> - 0.3-0.30
- Fix URL (#1861309)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 31 2020 Jeff Law <law@redhat.com> - 0.3-0.27
- Fix bogus volatile caught by gcc-11

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3-0.20
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.3-0.13
- Fix FTBFS on armv7 (#1106024)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Adam Williamson <awilliam@redhat.com> - 0.3.0.10
- use the currently-preferred way of doing gtk-update-icon-cache

* Wed May  8 2013 Tom Callaway <spot@fedoraproject.org> - 0.3-0.9
- sync to latest git, disable panel applet

* Fri Apr 26 2013 Matthias Clasen <mclasen@redhat.com> - 0.3-0.8
- Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec  6 2011 Matthias Clasen <mclasen@redhat.com> - 0.3-0.4
- Deal with deprecations

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.3-0.3
- Rebuild for new libpng

* Fri Jun 24 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.3-0.2
- Update git snapshot (translation updates only)

* Wed Mar 23 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.3-0.1
- Update to prerelease of 0.3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Apr 13 2010 Benjamin Otte <otte@redhat.com> - 0.2.2-1
- Update to 0.2.2

* Mon Feb 22 2010 Benjamin Otte <otte@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 11 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.1-6
- Rebuild for GCC 4.3

* Fri Aug 24 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.1-5
- Update license tag.

* Mon Aug 28 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.1-4
- BR perl(XML::Parser)

* Mon Aug 28 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.1-3
- Bump release and rebuild.

* Wed Jun 14 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.1-2
- Add gettext-devel BR

* Mon May 29 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.1-1
- Update to 1.1.1.

* Mon Feb 20 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.0-6
- Bump for another rebuild.

* Mon Feb 13 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.0-5
- Previous build failed, try without %%{_smp_mflags}.

* Mon Feb 13 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.0-4
- Bump release again.

* Mon Feb 13 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.0-3
- Bump release and rebuild for new gcc4.1 and glibc.

* Thu Jan 26 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.0-2
- Add post and postun scripts to update the GTK+ icon cache.

* Thu Jan 26 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.0-1
- Update to 0.1.0
- Add scriptlet for installing GConf schema.

* Thu Jan 19 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.0.3-3
- Bump release.

* Fri Jan 13 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.0.3-1
- Initial build.

