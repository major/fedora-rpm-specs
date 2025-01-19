Name:           jwm
Version:        2.4.2
Release:        7%{?dist}
Summary:        Joe's Window Manager

License:        MIT
URL:            http://joewing.net/projects/jwm/
Source0:        https://github.com/joewing/jvm/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	gettext-devel
BuildRequires:	make
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xrender)
Recommends:	/usr/bin/xterm
Recommends:	/usr/bin/xlock

%description
JWM is a window manager for the X11 Window System. It's written in C and uses
only Xlib at a minimum. The following libraries can also be used if available:

* cairo and librsvg2 for SVG icons and backgrounds.
* fribidi for bi-directional text support.
* libjpeg for JPEG icons and backgrounds.
* libpng for PNG icons and backgrounds.
* libXext for the shape extension.
* libXrender for the render extension.
* libXmu for rounded corners.
* libXft for anti-aliased and true type fonts.
* libXinerama for multiple head support.
* libXpm for XPM icons and backgrounds.

JWM supports MWM and Extended Window Manager Hints (EWMH).

Note that the Fedora package is built with all supported features enabled.

%prep
%autosetup

# Preserve timestamps in installation
sed -i -e 's|install -m|install -pm|g' Makefile.in

%build
./autogen.sh
%configure
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/xsessions
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/xsessions/

%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/system.jwmrc
%{_bindir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 05 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 2.4.2-1
- Update to 2.4.2 (RHBZ #2021057)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.3.7-1
- Update to 2.3.7

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 13 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.3.6-1
- Update to 2.3.6 (RHBZ #1366603)

* Wed Jun 22 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.3.5-1
- Update to 2.3.5
- Update BRs

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 14 2015 Christopher Meng <rpm@cicku.me> - 2.3.2-1
- Update to 2.3.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep 17 2014 Christopher Meng <rpm@cicku.me> - 2.2.2-1
- Update to 2.2.2

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 12 2014 Germán A. Racca <skytux@fedoraproject.org> - 2.2.0-1
- Updated to new upstream version 2.2.0
- Cleaned spec file
- Changed tarball format (from bz2 to xz)
- Recreated patches jwm-nostrip and jwm-timestamps
- Dropped patch jwm-destdir
- Added translations
- Added gettext as BR

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 2.1.0-4
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 2.1.0-3
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 09 2012 Germán A. Racca <skytux@fedoraproject.org> - 2.1.0-1
- Updated from snapshot to new release
- Rearranged spec file

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-8.svn500
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.0.1-7.svn500
- Rebuild for new libpng

* Tue Aug 30 2011 Germán A. Racca <skytux@fedoraproject.org> 2.0.1-6.svn500
- Added patch to remove strip from makefile
- Recreated the other patches and changed order of application
- Removed optflags from make line

* Mon Aug 22 2011 Germán A. Racca <skytux@fedoraproject.org> 2.0.1-5.svn500
- Added optflags to the make line
- Replaced libjpeg-devel by libjpeg-turbo-devel in BR
- Added freetype-devel as BR

* Fri Aug 19 2011 Germán A. Racca <skytux@fedoraproject.org> 2.0.1-4.svn500
- Added xterm as requires
- Modified release tag format

* Sun Jan 09 2011 Germán A. Racca <skytux@fedoraproject.org> 2.0.1-3.20110108svn
- Updated to snapshot 20110108
- Removed some patches because they were fixed by upstream

* Thu Jun 17 2010 German A. Racca <gracca@gmail.com> 2.0.1-2.20100616svn
- Rebuild for Fedora 13
- Updated to snapshot 20100616

* Wed May 19 2010 German A. Racca <gracca@gmail.com> 2.0.1-1.20100503svn
- Initial release of RPM package
