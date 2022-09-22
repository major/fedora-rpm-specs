Name:		fbpanel
Version:	7.0
Release:	14%{?dist}
Summary:	A lightweight X11 desktop panel

# %%{_bindir}/fbpanel and almost all plugins are under LGPLv2+
# Some plugins (cpu.so, pager.so, tray.so) are under GPLv2+
License:	LGPLv2+ and GPLv2+
URL:		https://github.com/aanatoly/fbpanel
Source:	https://github.com/aanatoly/fbpanel/archive/%{version}/fbpanel-%{version}.tar.gz
# Fix for gcc10 -fno-common
Patch0:     fbpanel-7.0-gcc10-fno-common.patch
# Port script to python3
Patch1:     fbpanel-7.0-script-py3.patch
# Port script to python3.10
Patch2:     fbpanel-7.0-script-py310.patch

# distro specific patches
Patch10:        fbpanel-7.0-default-config.patch
Patch11:        fbpanel-6.1-default-applications.patch

BuildRequires:  gcc
BuildRequires:  python3
BuildRequires:  gtk2-devel
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  desktop-file-utils
BuildRequires:  make
Requires:       xdg-utils

%description
fbpanel is a lightweight X11 desktop panel. It works with any ICCCM / NETWM 
compliant window manager such as sawfish, metacity, openbox, xfwm4, or KDE.
It features tasklist, pager, launchbar, clock, menu and systray.

%package     doc
Summary:   Documentation for %{name}
BuildArch: noarch

%description    doc
This subpackage contains documentation files for %{name}

%prep
%setup -q
%patch0 -p1 -b .gcc10
%patch1 -p1 -b .py3
%patch2 -p1 -b .py310
%patch10 -p1 -b .default-config
%patch11 -p1 -b .default-applications
# honor optflags
sed -i.optflags -e \
	'\@CFLAGS =@s|-Wall -Werror|%{optflags}|' \
	.config/rules.mk
# Fix path...
sed -i.path panel/panel.c \
	-e 's|LIBEXECDIR "/fbpanel/|LIBEXECDIR "/|'

LANG=C grep -rl %{_bindir}/python | \
	xargs sed -i -e 's@%{_bindir}/python$@%{_bindir}/python3@'

# preserve timestamps during install
sed -i.timstamps -e 's|install -m|install -p -m|' scripts/install.sh
# Keep timestamps more forcely!!
grep -rl -- "-m 644" | xargs sed -i -e 's|-m 644 |-p -m 644 |'
sed -i data/images/Makefile -e '\@IMAGES@s|install |install -cp -m 0644 |'

%build
# %%configure macro doesn't work
./configure \
    V=1 \
    --prefix=%{_prefix} \
    --libdir=%{_libdir}/%{name} \
    --libexecdir=%{_libexecdir}/%{name} \
    --datadir=%{_datadir}/%{name} \
    --mandir=%{_mandir}/man1
make %{?_smp_mflags} V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT

# change some icon names that were also changed in the default panel config
#mv $RPM_BUILD_ROOT%{_datadir}/%{name}/images/logo.png \
#    $RPM_BUILD_ROOT%{_datadir}/%{name}/images/start-here.png
ln -sf logo.png \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/images/start-here.png

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/images/gnome-session-halt.png \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/images/system-shutdown.png

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/images/gnome-session-reboot.png \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/images/system-reboot.png

# volume plugin is not working and prevents starting of fbpanel, lets remove it.
# https://sourceforge.net/tracker/?func=detail&aid=3121295&group_id=66031&atid=513125
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/libvolume.so


%files
%license COPYING
%doc CHANGELOG
%doc CREDITS
%doc NOTES
%doc README.md

%{_bindir}/%{name}
%dir	%{_libdir}/%{name}/
%{_libdir}/%{name}/lib*.so

%dir	%{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/make_profile
%{_libexecdir}/%{name}/xlogout

%dir	%{_datadir}/%{name}/
%{_datadir}/%{name}/default
%{_datadir}/%{name}/images/
%{_datadir}/%{name}/pager

%{_mandir}/man1/%{name}.1.*

%files doc
%doc www

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 7.0-12
- Port build script to python3.10

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 23 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 7.0-10
- Port build script to python3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 23 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 7.0-6
- Fix compilation with gcc10 -fno-common

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 7.0-2
- Include documentation

* Tue Feb 20 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 7.0-1
- 7.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.1-16
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 6.1-11
- Fix build for gdk-pixbuf2 package split

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 6.1-3
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 28 2010 Christoph Wickert <cwickert@fedoraproject.org> - 6.1-1
- Update to 6.1
- Require xdg-utils for screenlocking
- Add patch to make sure default applications are installed

* Thu Feb 25 2010 Christoph Wickert <cwickert@fedoraproject.org> - 5.6-2
- Add patch to fix DSO linking (#565202)

* Sun Feb 07 2010 Christoph Wickert <cwickert@fedoraproject.org> - 5.6-1
- Update to 5.6
- Update icon-cache scriptlets
- Remove useless desktop file

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 04 2008 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 4.12-6
- Add icon.patch to bring the Fedora icon to the panel
- Modified the existing apps in the Panel (like emacs -> gedit)

* Wed Jun 18 2008 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 4.12-5
- Add comment about the license
- Remove redundant Source2:

* Tue Jun 17 2008 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 4.12-4
- Add correct url for Source:
- Add gtk-update-icon-cache
- Add timestamps
- Add missing debuginfo rpm
- Changed licence, MIT to LGPLv2+ and GPLv2+
- Remove unneeded ldconfig
- Remove redundant BuildRequires: atk-devel, pango-devel and cairo-devel

* Sun Jun 15 2008 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 4.12-3
- Solved build failure and broken libs-patch with patch from Robert Scheck

* Sat Jun 07 2008 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 4.12-2
- fixed rpmlint errors
- new .desktop file
- cleanup

* Sun May 25 2008 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 4.12-1
- first version of the SPEC file
