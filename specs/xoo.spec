Summary: Xoo is a graphical wrapper around xnest
Name: xoo
Version: 0.8
Release: 26%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
# upstream was in the process of moving source to freedesktop.org
# but now seems to be at yoctoproject.org. Still all confusing
Url: http://www.freedesktop.org/wiki/Software/%{name}/
Source0: http://downloads.yoctoproject.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1: neo1973.png
Patch1: xoo-0.8-neo1973.patch
Patch2: xoo-0.7-glib.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires: libXtst-devel, gtk2-devel, libglade2-devel, expat-devel
BuildRequires: libX11-devel, GConf2-devel,libXt-devel
Requires: xorg-x11-server-Xephyr

%description
Xoo is a graphical wrapper around Xnest/Xephyr, the nested X server. You can
make Xnest look like a particular device's display and set up buttons on that
device. This is useful for embedded developers who want to simulate a target
device on their desktop machine.

%prep
%setup -q 
%patch -P1 -p1 -b .neo1973
%patch -P2 -p1 -b .glib
cp %{SOURCE1}  data/
# ImplicitDSOlinking fix
sed -i 's/-lXtst/-lXtst -lX11/' configure.ac

%build
%configure --with-x
make LDFLAGS=-lX11 %{?_smp_mflags}

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
%{__make} install

%files 
%{_bindir}/xoo
%dir %attr(0755,root,root) %{_prefix}/share/%{name}
%{_prefix}/share/%{name}/*
%{_prefix}/share/applications/%{name}.desktop
%{_prefix}/share/pixmaps/%{name}.png
%doc README COPYING TODO AUTHORS NEWS

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8-25
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 Paul Wouters <pwouters@redhat.com> - 0.8-1
- Upgraded to 0.8
- New url and upstream location
- Support Zephyr
- Fix implicit linking of -lX11
- Cleanup specfile

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 11 2012 Adam Jackson <ajax@redhat.com> 0.7-15
- xoo-0.7-glib.patch: Fix for new glib

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.7-14
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 23 2010 Paul Wouters <paul@xelerance.com> - 0.7-12
- bz#599871 FTBFS xoo-0.7-11.fc12: ImplicitDSOLinking fix

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7-9
- Fix license tag.
- Move %%configure call inside %%build.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.7-8
- Autorebuild for GCC 4.3

* Tue Aug 28 2007 Paul Wouters <paul@xelerance.com> 0.7-7
- Rebuild for new expat

* Sat Jul 28 2007 Paul Wouters <paul@xelerance.com> 0.7-6
- Bump for EVR

* Sat Jul 28 2007 Paul Wouters <paul@xelerance.com> 0.7-4
- Fixed patch file

* Sat Jul 28 2007 Paul Wouters <paul@xelerance.com> 0.7-3
- Added neo1973 skins with permission of copyright holder
  Sean Moss-Pultz <sean@openmoko.com>

* Thu Jul  5 2007 Paul Wouters <paul@xelerance.com> 0.7-2
- Dependancy fixes, removed post/postun sections.

* Thu Apr 12 2007 Paul Wouters <paul@xelerance.com> 0.7-1
- Initial release

