Name:           blackbox
Version:        0.77
Release:        4%{?dist}
Summary:        Very small and fast Window Manager
License:        MIT
URL:            https://github.com/bbidulock/blackboxwm
Source0:        https://github.com/bbidulock/blackboxwm/releases/download/%{version}/%{name}-%{version}.tar.lz
Source1:        blackbox.desktop
Source2:        blackbox.session
Patch0:         d3481ee7b7d104ef53ead4d35b9a9254c64bb87a.patch
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXt-devel
BuildRequires:  lzip
BuildRequires:  make

%description
Blackbox is a window manager for the X Window environment, which is
almost completely compliant with ICCCM specified operation policies.
It features nice and fast interface with multiple workspaces and
simple menus. Fast built-in graphics code that can render solids,
gradients and bevels is used to draw window decorations. Remaining
small in size, blackbox preserves memory and CPU.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libXft-devel%{?_isa}

%description    devel
This package contains the Blackbox Toolbox files, headers and static library
of the utility class library for writing small applications.

%prep
%autosetup -p1
# %%{__global_ldflags} wrongly passed to pkgconfig file
sed -i 's|@LDFLAGS@||g' lib/libbt.pc.in

%build
# Required to cleanly get rid of the useless rpath
sh autogen.sh
autoreconf -fiv
%configure \
    --enable-shared \
    --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete -print

# Install the desktop entry
install -pDm0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/xsessions/blackbox.desktop

# Install GDM session file
install -pDm0755 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/X11/gdm/Sessions/Blackbox

%find_lang %{name}
%ldconfig_scriptlets

%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS ChangeLog COMPLIANCE NEWS README* RELEASE* THANKS TODO
%license COPYING
%{_sysconfdir}/X11/gdm/Sessions/Blackbox
%{_bindir}/blackbox
%{_bindir}/bsetbg
%{_bindir}/bsetroot
%{_bindir}/bstyleconvert
%{_libdir}/libbt.so.*
%{_datadir}/blackbox/
%{_datadir}/xsessions/blackbox.desktop
%{_mandir}/man1/blackbox.1*
%{_mandir}/man1/bsetbg.1*
%{_mandir}/man1/bsetroot.1*
%{_mandir}/*/man1/blackbox.1*
%{_mandir}/*/man1/bsetroot.1*

%files devel
%{_includedir}/bt/
%{_libdir}/libbt.so
%{_libdir}/pkgconfig/libbt.pc

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.77-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 27 2022 Filipe Rosset <rosset.filipe@gmail.com> - 0.77-3
- Fix FTBFS rhbz#2113121

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 23 2022 Filipe Rosset <rosset.filipe@gmail.com> - 0.77-1
- Update to 0.77 fixes rhbz#1959905

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 16 2020 Filipe Rosset <rosset.filipe@gmail.com> - 0.76-2
- make spec compatible with EPEL8

* Sun Feb 16 2020 Filipe Rosset <rosset.filipe@gmail.com> - 0.76-1
- Update to 0.76

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 21 2019 Filipe Rosset <rosset.filipe@gmail.com> - 0.75-1
- Update to 0.75 fixes rhbz#1749810
- src file changed to lzip format added lzip as BR

* Sun Aug 04 2019 Filipe Rosset <rosset.filipe@gmail.com> - 0.74-1
- Update to 0.74 and remove upstreamed patches fixes rhbz#1595818 and rhbz#1603495
- Fix FTBFS + spec cleanup and modernization fixes rhbz#1674698 and rhbz#1734979

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.70.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.70.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.70.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.70.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.70.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.70.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.70.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.70.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.70.1-25
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Christopher Meng <rpm@cicku.me> - 0.70.1-23
- Fix messy pkg-config file.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70.1-18
- Rebuilt for c++ ABI breakage

* Thu Jan 19 2012 Niels de Vos <devos@fedoraproject.org> - 0.70.1-17
- Fix Fails To Build From Source (#660798)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 01 2009 Caolán McNamara <caolanm@redhat.com> - 0.70.1-13
- make build

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 24 2008 Matthias Saou <http://freshrpms.net/> 0.70.1-11
- Include patch to fix build with gcc 4.3.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org>
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 0.70.1-9
- Rebuild for new BuildID feature.

* Fri Aug  3 2007 Matthias Saou <http://freshrpms.net/> 0.70.1-8
- Fix License field, it was "GPL" but should have been "MIT" all along.
- Remove dist tag, since the package will seldom change.

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 0.70.1-7
- Switch to using the DESTDIR install method.
- Remove old X build requirements conditionals.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 0.70.1-6
- Switch to shared libbt library, so have devel require main and call ldconfig.
- Make the GDM session file be a separate source.
- Autoreconf to cleanly get rid of the useless rpath.
- Add missing libXft-devel build requirement.
- Switch to using downloads.sf.net source URL.
- Minor spec file tweaks.
- Add new libXft-devel devel sub-package requirement.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 0.70.1-5
- FC6 rebuild.
- Remove gcc-c++ build requirement and devel sub-package requirement.
- Remove pkgconfig buildd requirement, as it's pulled in by Xorg devel now.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 0.70.1-4
- FC5 rebuild.

* Wed Feb  8 2006 Matthias Saou <http://freshrpms.net/> 0.70.1-3
- Rebuild for new gcc/glibc.

* Mon Jan 23 2006 Matthias Saou <http://freshrpms.net/> 0.70.1-2
- Add conditional to build with/without modular X depending on FC version.

* Thu Nov  3 2005 Matthias Saou <http://freshrpms.net/> 0.70.1-1
- Update to 0.70.1.

* Sat Mar 12 2005 Matthias Saou <http://freshrpms.net/> 0.70.0-1
- Update to 0.70.0.
- Use bz2 source instead of gz.
- Add devel sub-package for the libbt stuff.

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 0.65.0-10
- Bump release to provide Extras upgrade path.

* Mon Nov 15 2004 Matthias Saou <http://freshrpms.net/> 0.65.0-9
- Added gcc 3.4 patch from Arch Linux.

* Thu May  6 2004 Matthias Saou <http://freshrpms.net/> 0.65.0-8
- Removed switchdesk file, it doesn't work because of hardcoded stuff.

* Wed Mar 24 2004 Matthias Saou <http://freshrpms.net/> 0.65.0-8
- Removed explicit XFree86 dependency.

* Mon Feb 23 2004 Matthias Saou <http://freshrpms.net/> 0.65.0-7
- Added blackbox.desktop file for xsessions based on the GNOME one.

* Tue Feb 10 2004 Scott R. Godin <nospam@webdragon.net> 0.65.0-6
- Patch for #include <cassert> in Window.cc
- Fixed nls problem, left in --disable just in case. Smile, Matthias. :-)

* Fri Nov 14 2003 Matthias Saou <http://freshrpms.net/> 0.65.0-5
- Rebuild for Fedora Core 1.

* Wed May 14 2003 Matthias Saou <http://freshrpms.net/>
- Added --without nls to enable rebuilding on Red Hat Linux 9 :-(

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sun Oct  6 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Fri Sep 20 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.65.0 final.

* Mon Aug 12 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

