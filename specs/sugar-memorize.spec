Name:          sugar-memorize
Version:       58
Release:       11%{?dist}
Summary:       Memorize for Sugar
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://wiki.sugarlabs.org/go/Activities/Memorize
Source0:       https://download.sugarlabs.org/sources/honey/Memorize/Memorize-%{version}.tar.bz2
# Upstream has applied this.
Patch0:        Fix-use-of-getchildren-with-Element-object.patch 
BuildArch:     noarch

BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3
BuildRequires: gettext
Requires: gstreamer-plugins-espeak
Requires: sugar

%description
The game memorize is about finding matching pairs. A pair can consist of any
multimedia object. At the moment these are images, sounds and text but this
could be extended to animations or movie snippets as well. Which pairs do 
match is up to the creator of the game. Memorize is actually more than just
a predefined game you can play, it allows you to create new games yourself
as well.

%prep
%autosetup -n Memorize-%{version}

sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build


%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Memorize.activity/

%find_lang org.laptop.Memorize


%files -f org.laptop.Memorize.lang
%license COPYING
%doc AUTHORS NEWS
%{sugaractivitydir}/Memorize.activity/
%{_datadir}/metainfo/org.laptop.Memorize.appdata.xml


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 58-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 58-10
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 58-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 58-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 58-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 58-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 58-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 58-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 58-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 09 2021 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 58-2
- Apply Fix-use-of-getchildren-with-Element-object patch

* Mon Feb 22 2021 Kalpa Welivitigoda <callkalpa@gmail.com> - 58-1
- v58

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 57-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 57-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Chihurumnaya Ibiam <ibiamchihurumnaya@gmail.com> - 57-1
- Update to 57
- Add file for package data

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 55-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 55-1
- Update to 55

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 16 2018 Peter Robinson <pbrobinson@fedoraproject.org> 54-1
- Update to 54

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 52-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 28 2017 Peter Robinson <pbrobinson@fedoraproject.org> 52-1
- Update to 52

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 51-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 51-4
- Fix FTBFS issue

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 51-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Peter Robinson <pbrobinson@fedoraproject.org> 51-1
- Update to 51

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 26 2014 Peter Robinson <pbrobinson@fedoraproject.org> 49-1
- Update to 49

* Sun Jul 27 2014 Peter Robinson <pbrobinson@fedoraproject.org> 48-1
- Update to 48

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 15 2014 Peter Robinson <pbrobinson@fedoraproject.org> 47-1
- Update to 47

* Sun Jan 12 2014 Peter Robinson <pbrobinson@fedoraproject.org> 46-1
- Update to v46, build using sugar gtk3 support

* Thu Oct 17 2013 Peter Robinson <pbrobinson@fedoraproject.org> 45-3
- Add gstreamer-python runtime dependency

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul  2 2013 Peter Robinson <pbrobinson@fedoraproject.org> 45-1
- Update to 45

* Sat Jun 29 2013 Peter Robinson <pbrobinson@fedoraproject.org> 44-1
- Update to 44

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 43-1
- Update to 43

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 41-1
- Update to 41

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct  2 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 39-1
- Update to 39

* Tue Sep 20 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 37-1
- Update to 37

* Wed Sep  7 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 36-4
- add missing libxml2-python dependency

* Sun May 15 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 36-3
- Fix Requires

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 16 2010 Fabian Affolter <fabian@bernewireless.net> - 35-1
- Updated to new upstream version 35

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 33-4
- recompiling .py files against Python 2.7 (rhbz#623380)

* Mon Dec 14 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 33-3
- Add buildreq gettext to fix build issues on F-12/rawhide - fixes # 539053

* Sat Aug 08 2009 Fabian Affolter <fabian@bernewireless.net> - 33-2
- Bump release

* Tue Aug 04 2009 Fabian Affolter <fabian@bernewireless.net> - 33-1
- Changed source url, now hosted on Sugarlabs
- Updated to new upstream version 33

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 29-2
- Rebuild for Python 2.6

* Wed Nov 19 2008 Fabian Affolter <fabian@bernewireless.net> - 29-1
- updated to version 29
- changed source0 to release tarball
- removed permission hacks, end-lind-encoding, hidden files

* Thu Oct 16 2008 Fabian Affolter <fabian@bernewireless.net> - 28-1
- Initial package for Fedora
