Name:           sugar-typing-turtle
Version:        32
Release:        8%{?dist}
Summary:        A multilingual animated touch typing trainer

License:        GPLv2+
URL:            http://wiki.sugarlabs.org/go/Activities/Typing_Turtle
Source0:        http://download.sugarlabs.org/sources/honey/TypingTurtle/TypingTurtle-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3
BuildRequires:  gettext
BuildRequires:  setxkbmap
Requires:       sugar

%description
This Sugar activity features a sequence of lessons designed to gradually
introduce students to touch typing, teaching them a few keys at a time
until they have mastered the entire keyboard.

Fun graphics, sounds and characters aim for an entertaining experience.
An on-screen keyboard with overlaid hand positions shows the correct way
to press each key, encouraging good typing habits.


%prep
%setup -q -n TypingTurtle-%{version}

# remove unnecessary libs and files
rm -rf .pydevproject .project strace.sh

sed -i 's/python/python3/' editlesson*.py keybuilder.py lessonbuilder.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/TypingTurtle.activity/

%find_lang org.laptop.community.TypingTurtle


%files -f org.laptop.community.TypingTurtle.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/TypingTurtle.activity


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 32-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 31 2021 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 32-5
- Add Buildrequires setxkbmap

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 32-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 11 2020 Peter Robinson <pbrobinson@fedoraproject.org> 32-1
- Release 32

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 31-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 31-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 31-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 31-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 31-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 31-5
- Fix FTBFS issue 

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 24 2014 Peter Robinson <pbrobinson@fedoraproject.org> 31-1
- Release 31

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 30-2
- Update tar file and other updates for gtk3

* Wed Sep 26 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 30-1
- Release 30

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 2 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 29-1
- Release 29

* Sun Oct  2 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 28-1
- Release 28

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 26-4
- recompiling .py files against Python 2.7 (rhbz#623389)

* Thu Mar 18 2010 Sebastian Dziallas <sebastian@when.com> - 26-3
- don't remove port

* Wed Jan 27 2010 Sebastian Dziallas <sebastian@when.com> - 26-2
- remove hidden files

* Wed Jan 27 2010 Sebastian Dziallas <sebastian@when.com> - 26-1
- initial packaging
