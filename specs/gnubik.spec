Name:           gnubik
Version:        2.4.3
Release:        22%{?dist}
Summary:        3D interactive graphics puzzle

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.gnu.org/software/gnubik/
Source0:        ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
# There aren't 24x24 logo icons provided
Patch1:         iconfix.patch
# The install-desktop target is broken
Patch2:         installfix.patch
# Allow guile 3.0 to be found
Patch3:		guile-3.0.patch

BuildRequires:	autoconf automake
BuildRequires:  gcc
BuildRequires:  libX11-devel pkgconfig(guile-3.0) libGL-devel libGLU-devel gtk2-devel gtkglext-devel
BuildRequires:  gettext gettext-devel desktop-file-utils texinfo
BuildRequires:  make
Requires:       hicolor-icon-theme

%description
GNUbik is a GNU package.  It is a 3D interactive graphics puzzle. It renders
an image of a magic cube (similar to a rubik cube) and you attempt to solve it.


%prep
%autosetup -p 0
chmod -x src/{quarternion,txfm}.{c,h}
# Remove pregenerated binaries and let them be gerenerated
rm po/*.pot
rm doc/%{name}.info


%build
autoreconf --install
%configure
%make_build

%install
%make_install
%find_lang %{name}

rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 644 doc/%{name}.6 $RPM_BUILD_ROOT%{_mandir}/man6

rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 icons/logo16.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -p -m 644 icons/logo22.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
install -p -m 644 icons/logo32.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -m 644 icons/logo48.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

# Unless some asks for the scheme file I am going to leave it out. 
# It isn't named for the package and I doubt it would be used.
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/gen-dot-desktop.scm

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}
%{_infodir}/%{name}.info.*
%{_mandir}/man*/%{name}*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 30 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 2.4.3-21
- Build with guile 3.0

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.3-20
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 17 2021 Bruno Wolff III <bruno@wolff.to> - 2.4.3-11
- Use guile 2.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 2.4.3-4
- Remove hardcoded gzip suffix from GNU info pages

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 15 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.4.3-1
- update to latest upstream 2.4.3, fixes rhbz #1438618
- spec cleanup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4.2-7
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Bruno Wolff III <bruno@wolff.to> 2.4.2-1
- Error message patch is no longer needed
- Some translation improvements
- Needed to not try to install missing 24x24 logo
- install-desktop target in makefile is broken
- Don't install the icon related scheme file that is new for 2.4.2

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Bruno Wolff III <bruno@wolff.to> 2.4.1-4
- Don't use error messages as formats

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 01 2013 Bruno Wolff III <bruno@wolff.to> 2.4.1-1
- Upstream update to 2.4.1
- 2.4.1 release announcement at: http://lists.gnu.org/archive/html/info-gnu/2013-05/msg00016.html
- Mostly some translation updates

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 22 2012 Bruno Wolff III <bruno@wolff.to> 2.4-6
- Rebuild for pangox soname bump

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 05 2011 Bruno Wolff III <bruno@wolff.to> 2.4-3
- Rebuild for libpng 1.5

* Sun May 15 2011 Bruno Wolff III <bruno@wolff.to> 2.4-2
- Translation filename changed gnubik.pot

* Sun May 15 2011 Bruno Wolff III <bruno@wolff.to> 2.4-1
- Upstream update to 2.4
- Release notes are available at http://savannah.gnu.org/forum/forum.php?forum_id=6774

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 21 2009 Alexey Torkhov <atorkhov@gmail.com> - 2.3-6
- Put icon in right location

* Fri Mar 13 2009 Alexey Torkhov <atorkhov@gmail.com> - 2.3-5
- Fixed rebuilding .info

* Wed Mar 11 2009 Alexey Torkhov <atorkhov@gmail.com> - 2.3-4
- Replaced mesa- requires with generic ones
- Removing pregenerated *.gmo in prep
- Rebuilding .info

* Wed Mar 11 2009 Alexey Torkhov <atorkhov@gmail.com> - 2.3-3
- Put icon into hicolor theme
- Add correct scriptlets and requires
- Add GenericName to desktop file

* Wed Mar 11 2009 Alexey Torkhov <atorkhov@gmail.com> - 2.3-2
- Don't using install -D that doesn't want to work in mock
- Fix incorrect usage of GenericName in desktop file

* Mon Mar 02 2009 Alexey Torkhov <atorkhov@gmail.com> - 2.3-1
- Initial package
