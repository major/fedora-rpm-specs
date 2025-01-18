%global snapshot 20060225
Name:           duel3
Version:        0.1
Release:        0.43.%{snapshot}%{?dist}
Summary:        One on one spaceship duel in a 2D arena
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
# Upstream has vanished
#URL:            http://ts-games.com/duel3.php
Source0:        http://downloads.sourceforge.net/%{name}/Duel3_%{snapshot}_src.zip
Source1:        http://downloads.sourceforge.net/%{name}/Duel3_%{snapshot}_bin.zip
Source2:        %{name}.desktop
Source3:        %{name}.png
Source4:        music-credits.txt
Patch0:         Duel3_20060225-fixes.patch
Patch1:         Duel3_20060225-windowed-mode.patch
Patch2:         Duel3_20060225-fix-buf-oflow.patch
Patch3:         Duel3_20060225-extra-fix-buf-oflow.patch
BuildRequires:  gcc-c++
BuildRequires:  alleggl-devel dumb-devel libGLU-devel desktop-file-utils
BuildRequires: make
Requires:       hicolor-icon-theme opengl-games-utils

%description
The sudden attack from the Martain Rim miners caught the Earth by surprise,
there was no way the meager Earth Space Fleet could defend themselves. The
miners attacked, and eliminated their enemies, and then returned to the
asteroid belt. However, Earth could not accept such an embarrassing defeat. The
military developed new space fighters, and trained several squadrons of elite
pilots. The task force was then deployed against the miners. These trained
pilots utterly defeated the miners in a matter of weeks, and the first space
war in human history was finished.

The military, however, now had a new problem on their hands. These new elite
pilots were becoming restless, and there was no way for them to test their
skills. The military dare not disband the force, or let their skills dull, so
the Duel Combat League was formed. The newly formed league quickly became the
premier entertainment form on the planet, and the military's largest source of
income.

Take control of a Duel fighter, and test your skills against your opponents and
the arena itself in fast-paced space combat.


%prep
%setup -q -a 1 -n Duel3_%{snapshot}_src
mv Duel3_%{snapshot}_bin/* Source
cp %{SOURCE4} .
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
sed -i 's/\r//' Source/readme.txt license.txt music-credits.txt
iconv -f iso8859-1 -t utf-8 music-credits.txt > temp
mv temp music-credits.txt


%build
pushd Source
make %{?_smp_mflags} PREFIX=%{_prefix} \
  CFLAGS="-std=c++14 $RPM_OPT_FLAGS -fsigned-char -Wno-deprecated-declarations -Wno-non-virtual-dtor"
popd


%install
pushd Source
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}
popd
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps



%files
%doc Source/readme.txt license.txt music-credits.txt
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.43.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1-0.42.20060225
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.41.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.40.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.39.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.38.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.37.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.36.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.35.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.34.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.33.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.32.20060225
- Force C++14 as this code is not C++17 ready

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.31.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.30.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.29.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.28.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.27.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.26.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1-0.25.20060225
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.24.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.23.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.22.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.21.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.20.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1-0.19.20060225
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.18.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.17.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.16.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Rahul Sundaram <sundaram@fedoraproject.org> -  0.1-0.15.20060225
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines
- fix desktop file to follow specification

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.14.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.13.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 03 2012 Bruno Wolff III <bruno@wolff.to> - 0.1-0.12.20060225
- Short term work around for buffer overflow issue

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.11.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 13 2011 Hans de Goede <hdegoede@redhat.com> - 0.1-0.10.20060225
- Rebuilt for new allegro-4.4

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.9.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.8.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.7.20060225
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec  3 2008 Hans de Goede <hdegoede@redhat.com> 0.1-0.6.20060225
- Fix a buffer overflow crash (bz 473374)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.1-0.5.20060225
- Autorebuild for GCC 4.3

* Tue Sep 25 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.1-0.4.20060225
- Use opengl-games-utils wrapper to show error dialog when DRI is missing

* Sat Mar 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.1-0.3.20060225
- Fixup .desktop file categories for games-menus usage

* Sat Feb  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.1-0.2.20060225
- Add missing "Requires: hicolor-icon-theme" (bz 226729)
- Add music-credits.txt, properly giving credits for the used music (bz 226729)

* Thu Jan 25 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.1-0.1.20060225
- Initial Fedora Extras package, many thanks to my students Albert-Jan Visser
  and Bas Meel for doing the Linux port of this!
