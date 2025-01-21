Name:           taxipilot
Version:        0.9.2
Release:        46%{?dist}
Summary:        Game where you pilot a taxi in space
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://taxipilot.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
Patch1:         taxipilot-0.9.1-desktop.patch
Patch2:         taxipilot-0.9.1-weaksym.patch
Patch3:         taxipilot-0.9.2-arts-startup.patch
Patch4:         taxipilot-0.9.2-gcc45.patch
BuildRequires: make
BuildRequires:  gcc gcc-c++ kdelibs3-devel arts-devel
BuildRequires:  desktop-file-utils libappstream-glib
Requires:       hicolor-icon-theme

%description
Game where you pilot a taxi in space, the objective is to pick up passengers
waiting on a number of platforms and to drop them where they want to go.
That's basically it.


%prep
%autosetup -p1


%build
. /etc/profile.d/qt.sh
%configure --disable-rpath
# Remove useless /usr/lib64 rpath on 64bit archs
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build taxipilot_LDADD="./EXT_wavpo/libEXT_wavpo.la -lartskde -lkdeui -lkdecore -lartsflow_idl -lmcop -lkio $(pkg-config --libs qt-mt)"


%install
. /etc/profile.d/qt.sh
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm $RPM_BUILD_ROOT%{_libdir}/libEXT_wavpo.so
%find_lang %{name}

# install .desktop file and appdata.
desktop-file-install --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applnk/Games/%{name}.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files -f %{name}.lang
%doc AUTHORS ChangeLog TODO
%license COPYING
%{_bindir}/%{name}*
%{_libdir}/libEXT_wavpo.*
%{_libdir}/mcop/EXT_WavPlayObject.mcopclass
%{_datadir}/apps/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/??color/*/apps/%{name}.png
%{_datadir}/doc/HTML/en/%{name}


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.2-45
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 30 2021 Hans de Goede <hdegoede@redhat.com> - 0.9.2-38
- Fix FTBFS (disable rpath harder) (rhbz#1988017)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Hans de Goede <hdegoede@redhat.com> - 0.9.2-35
- Drop taxipilot-0.9.2-kdemm.patch, it was trying to fix taxipilot_LDADD in the
  Makefile, but we override taxipilot_LDADD on the cmdline later
- Dropping this fixes a race where sometimes the build fails because it cannot
  find automake to regenerate Makefile.in because the patch touched Makefile.am
- Fix FTBFS (rhbz#1865568)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-34
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 13 2018 Hans de Goede <hdegoede@redhat.com> - 0.9.2-29
- Fix FTBFS (rhbz#1606489)
- Add appdata

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.2-26
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Hans de Goede <hdegoede@redhat.com> - 0.9.2-23
- Fix FTBFS (rhbz#1424071)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.2-19
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 14 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.2-14
- Remove vendor tag from desktop file
- spec clean up

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 10 2010 Hans de Goede <hdegoede@redhat.com> 0.9.2-10
- Fix building with gcc 4.5 (#631436)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar  9 2009 Hans de Goede <hdegoede@redhat.com> 0.9.2-8
- Try rebuild again now that all the deps are fixed

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.2-6
- Autorebuild for GCC 4.3

* Wed Dec 19 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.2-5
- Add patch by Rex Dieter to no longer BuildRequire kdemultimedia3-devel, as
  that is going away, we now require arts-devel instead (bz 410851)
- Revert "Put our own private lib in a subdir of /usr/lib so that we no longer
  become multilib (bz 343261)" change, as that breaks sound
- Add a patch which ensures artsd gets started if needed

* Sun Dec  2 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.2-4
- BuildRequire kdelibs3-devel (and kdemultimedia3-devel) instead of
  kdelibs-devel as that now is kde4 based, and we need kde 3

* Mon Oct 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.2-3
- Put our own private lib in a subdir of /usr/lib so that we no longer become
  multilib (bz 343261)

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.2-2
- Update License tag for new Licensing Guidelines compliance

* Sun Jun  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.2-1
- New upstream release 0.9.2

* Thu Apr 26 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.1-2
- Ship all relevant docs including COPYING
- Link libEXT_wavpo.so with additional libs to fix unresolved non weak syms

* Tue Apr 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.1-1
- Initial Fedora Extras package
