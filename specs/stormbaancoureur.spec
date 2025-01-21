Name:           stormbaancoureur
Version:        2.1.6
Release:        34%{?dist}
Summary:        Simulated obstacle course for automobiles
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.stolk.org/stormbaancoureur/
Source0:        http://www.stolk.org/stormbaancoureur/download/%{name}-%{version}.tar.gz 
Source1:        %{name}.desktop
Source2:        sturmbahnfahrer.png
Patch0:         stormbaancoureur-1.5.3-no-static-ode.patch
Patch1:         stormbaancoureur-2.0.2-snd-debug.patch
Patch2:         stormbaancoureur-2.1.6-ode.patch
Patch3:         stormbaancoureur-freeglut.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  plib-devel ode-devel freeglut-devel desktop-file-utils
BuildRequires:  alsa-lib-devel
Requires:       hicolor-icon-theme opengl-games-utils
Provides:       sturmbahnfahrer = %{version}-%{release}
Obsoletes:      sturmbahnfahrer < %{version}-%{release}

%description
Stormbaancoureur is Dutch for "assault course driver"... for expert drivers
only. If you want to master the obstacle course, try to have the laws of
physics work with you, not against you.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p0
%patch -P3 -p0

sed -i 's|/usr/share/games/%{name}|%{_datadir}/%{name}|' src-%{name}/main.cxx


%build
pushd src-%{name}
make %{?_smp_mflags} \
  CXXFLAGS="$RPM_OPT_FLAGS -I../src-common -DGAMEVERSION=%{version}-Fedora"
popd


%install
pushd src-%{name}
make install DESTDIR=$RPM_BUILD_ROOT GAMEDIR=$RPM_BUILD_ROOT%{_datadir}/%{name}
popd

# upstream's makefile forgets to install a few of these
install -p -m 644 models-%{name}/*.3ds \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/models

# move the binary from /usr/games to /usr/bin
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT%{_prefix}/games/%{name} $RPM_BUILD_ROOT%{_bindir}
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%files
%doc src-%{name}/JOYSTICKS src-%{name}/LICENCE src-%{name}/README
%doc src-%{name}/TODO src-%{name}/%{name}.keys.example
%doc src-%{name}/debian/changelog
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.6-33
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jul 24 2022 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.6-28
- Rebuilt for Ode soname bump

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.1.6-26
- Rebuild for new ode-0.16

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-22
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.1.6-19
- Rebuilt for new freeglut

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.6-14
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1.6-8
- Rebuilt for GCC 5 C++11 ABI change

* Wed Oct 29 2014 Hans de Goede <hdegoede@redhat.com> - 2.1.6-7
- Rebuild for ode-0.13.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.1.6-3
- Remove --vendor from desktop-file-install in F19+. https://fedorahosted.org/fesco/ticket/1077

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 20 2012 Jon Ciesla <limburgher@gmail.com> - 2.1.6-1
- New upstream, patch and rebuild for new ode.
- gcc44 patch upstreamed.
- crash on no network patch upstreamed.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 20 2009 Hans de Goede <hdegoede@redhat.com> 2.1.5-6
- Don't crash on network failures when trying to post scores to the
  internet (#547551)

* Mon Aug  3 2009 Hans de Goede <hdegoede@redhat.com> 2.1.5-5
- Update URL's for upstream domainname change

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 21 2009 Hans de Goede <hdegoede@redhat.com> 2.1.5-2
- Fix build with gcc 4.4

* Tue May 13 2008 Hans de Goede <hdegoede@redhat.com> 2.1.5-1
- new upstream release 2.1.5
- Rebuild for new ode

* Tue May 13 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.1.4-1
- new upstream release 2.1.4
- Rebuild for new plib

* Fri Mar 21 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.1.2-1
- new upstream release 2.1.2

* Sat Feb  9 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.1.0-1
- new upstream release 2.1.0

* Sun Jan  6 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.2-1
- new upstream release 2.0.2
- drop most patches (upstreamed)
- better sound error messages in an attempt to debug bz 427592

* Fri Jan  4 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.0-2
- Fix compilation with gcc-4.3
- Fix running with the nvidea-legacy drivers, patch by Alexis de Ruelle

* Mon Dec 31 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.0-1
- New upstream release 2.0.0
- Fix sound when using pulseaudio

* Thu Oct 18 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.5.3-1
- New upstream bugfix release 1.5.3

* Tue Sep 25 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.5.1-2
- Use opengl-games-utils wrapper to show error dialog when DRI is missing

* Thu Aug 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.5.1-1
- New upstream bugfix release 1.5.1

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.5-1
- New upstream release 1.5 (final)

* Mon Aug  6 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.5-0.1.rc1
- New upstream release 1.5rc1
- Renamed by upstream from sturmbahnfahrer to stormbaancoureur
- Update License tag for new Licensing Guidelines compliance

* Tue Jun  5 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4-1
- New upstream release 1.4
- Drop all patches (all upstream now)

* Wed Feb 14 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2-3
- Fix a bug triggering an assert in ode-0.8

* Tue Aug 29 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2-2
- FE6 Rebuild

* Mon Jul 31 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2-1
- New upstream version 1.2 with customizable keybindings
- Drop many hacks from %%install as upstream has improved "make install"

* Wed Jul 26 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-3
- Added a patch to call the left and right keys COMMA and POINT instead of
  LESSTHEN and GREATERTHEN, so that the text is correct for non qwerty
  keyboards too. And add a binding for normal brake to the Y key for more
  convenient controls with a German (QWERTZ) keyboard.
  Upstream has been notified that the current hardcoded keys are awkward
  with non qwerty keyboards so that upstream can create a proper fix.

* Wed Jul 19 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-2
- Add missing BR: alsa-lib-devel
- Stop linking with the unused libs: -lXmu -lXi -lX11 (-lX11 is used
  indirectly, through other libs but not directly).

* Tue Jul 18 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-1
- Initial Fedora Extras package
