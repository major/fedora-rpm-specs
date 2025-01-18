Summary: Interactive educational geometry software
Name: drgeo
Version: 1.1.0
Release: 54%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.ofset.org/drgeo

Source: http://downloads.sf.net/ofset/%{name}-%{version}.tar.gz
Patch0: drgeo-1.1.0-htmlview.patch
Patch1: drgeo.patch
Patch2: drgeo-1.1.0-anonymous-type.patch
Patch4: drgeo-1.1.0-format-security.patch
Patch5: drgeo-configure-c99.patch

#The following are necessary if using Guile 1.9 or later
#Patch3: drgeo-1.1.0-guile-fixups.patch
#Patch5: drgeo-1.1.0-guile2-runtime.patch

BuildRequires:  gcc-c++
BuildRequires: flex, bison, gmp-devel >= 2.0.2, desktop-file-utils
BuildRequires: libglade2-devel, intltool, gettext

# Despite the two patches above, drgeo still doesn't work with
# Guile 1.9 or later, giving a runtime error.  See
#   https://bugzilla.redhat.com/show_bug.cgi?id=1037042#c4
#BuildRequires: guile-devel
BuildRequires: compat-guile18-devel
BuildRequires: make

%description
Dr. Geo is an interactive geometry GUI application. It allows one to create
geometric figures plus the interactive manipulation of such figure in
respect with their geometric constraints. It is usable in teaching
situation with students from primary or secondary level.

%prep
%setup -q
%patch -P0 -p1 -b .htmlview
%patch -P1 -p1 -b .general
%patch -P2 -p1 -b .anonymous-type
%patch -P4 -p1 -b .format-security
%patch -P5 -p1 -b .configure-c99

# patches for Guile 2 compatibility:
# compile time:
#%patch3 -p1 -b .guile-fixups
# run time:
#   http://bhattigurjot.wordpress.com/2014/05/23/23-may-2014/
#   http://git.savannah.gnu.org/cgit/dr-geo.git/commit/?h=upgrade&id=4c4a75a77bf91c6840cfa9101f3eaabd8fee7dbd
#%patch5 -p1 -b .guile2

%build
export GUILE=/usr/bin/guile1.8
export GUILE_CONFIG=/usr/bin/guile1.8-config
export GUILE_TOOLS=/usr/bin/guile1.8-tools
%configure
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}
perl -pi -e 's/^Icon=gnome-drgenius.png/Icon=drgeo/g' %{buildroot}%{_datadir}/applications/drgeo.desktop
desktop-file-install \
   --dir %{buildroot}%{_datadir}/applications \
   %{buildroot}%{_datadir}/applications/drgeo.desktop

install -D -m0644 glade/drgeo.png %{buildroot}%{_datadir}/pixmaps/drgeo.png
mkdir %{buildroot}%{_datadir}/TeXmacs/
mv %{buildroot}%{_datadir}/texmacs/TeXmacs/plugins/ %{buildroot}%{_datadir}/TeXmacs/.
rmdir %{buildroot}%{_datadir}/texmacs/TeXmacs/
rmdir %{buildroot}%{_datadir}/texmacs/

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/drgeo
%{_bindir}/tm_drgeo
%{_datadir}/drgeo/
%{_datadir}/pixmaps/*.png
%{_datadir}/TeXmacs/plugins/drgeo
%{_datadir}/applications/drgeo.desktop

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.0-53
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Florian Weimer <fweimer@redhat.com> - 1.1.0-47
- Port configure script to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.1.0-38
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.1.0-35
- Rebuilt for switch to libxcrypt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.0-29
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Eric Smith <brouhaha@fedoraproject.org> - 1.1.0-27
- Updated Source tag
- Added format security patch from Yaakov Selkowitz <yselkowi@redhat.com>
  (#1037024, #1106158)
- Added patch for runtime compatibility with Guile 2.x, which still isn't
  adequate.
- Rather than using guile 2.0, build to use compat-guile18.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.1.0-24
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Jonathan Dieter <jdieter@lesbg.com> - 1.1.0-21
- Apply patch from Jan Synacek which allows us to build against guile-2.0.x

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.1.0-19
- Rebuild for new libpng

* Tue Feb 08 2011 Jonathan Dieter <jdieter@lesbg.com> - 1.1.0-18
- Fix FTBFS (bug #631320) for GCC 4.5 using patch from openSUSE

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 16 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.1.0-14
- fix license tag

* Tue Jul 08 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.1.0-13
- BZ 454045

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.0-12
- Autorebuild for GCC 4.3

* Mon Aug 28 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.1.0-11
- Rebuild for Fedora Extras 6

* Tue Jul 04 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.1.0-10
- Modify changelog

* Tue Jul 04 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.1.0-9
- Modify BR to build in mock with the minimal build group

* Tue May 18 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.1.0-8
- Rebuild for devel

* Tue Feb 14 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.1.0-7
- Rebuild for FC5

* Fri Feb 10 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.1.0-6
- Rebuild for FC5

* Fri Feb 10 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.1.0-5
- Rebuild for FC5

* Sun Oct 23 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.1.0-4
- Modify the default doc reader to htmlview

* Sun Oct 23 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.1.0-3
- Modify the default doc reader to firefox

* Sun Oct 23 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.1.0-2
- Modify spec file

* Sun Oct 23 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.1.0-1
- Updated to release 1.1.0.
- Modify spec file

* Sun Mar 06 2005 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 0.9.14-1
- Updated to release 0.9.14.

* Tue Jun 08 2004 Dag Wieers <dag@wieers.com> - 0.9.13-1
- Updated to release 0.9.13.

* Sun Jun 06 2004 Dag Wieers <dag@wieers.com> - 0.9.12-1
- Add improved desktop file.

* Sun Jan 31 2004 Dag Wieers <dag@wieers.com> - 0.9.12-0
- Updated to release 0.9.12.

* Fri Oct 24 2003 Dag Wieers <dag@wieers.com> - 0.9.10-0
- Updated to release 0.9.10.

* Tue Sep 23 2003 Dag Wieers <dag@wieers.com> - 0.9.9-0
- Updated to release 0.9.9.

* Sun Sep 07 2003 Dag Wieers <dag@wieers.com> - 0.9.8-0
- Updated to release 0.9.8.

* Wed Aug 13 2003 Dag Wieers <dag@wieers.com> - 0.9.7-0
- Package renamed to drgeo.
- Updated to release 0.9.7.

* Sun Mar 16 2003 Dag Wieers <dag@wieers.com> - 0.8.4-0
- Updated to release 0.8.4.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 0.8.3-0
- Updated to release 0.8.3.

* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 0.7.2-0
- Initial package. (using DAR)
