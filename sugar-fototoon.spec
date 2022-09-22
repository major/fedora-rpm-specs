Name:           sugar-fototoon
Version:        26
Release:        4%{?dist}
Summary:        An activity used to create cartoons
License:        GPLv3+
URL:            http://activities.sugarlabs.org/en-US/sugar/addon/4253
Source0:        http://download.sugarlabs.org/sources/honey/FotoToon/FotoToon-%{version}.tar.bz2

BuildRequires:  python3-devel sugar-toolkit-gtk3 gettext
BuildArch:      noarch
Requires:       sugar >= 0.116

%description
Fototoon is a sugar activity used to create cartoons using photos 
or drawings. After selecting the images, the user can select globes 
and write text to tell a story.

%prep
%setup -q -n FotoToon-%{version}
chmod +x slideview.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Fototoon.activity/

%find_lang org.eq.FotoToon

%files -f org.eq.FotoToon.lang
%{sugaractivitydir}/FotoToon.activity/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 23 2021 Kalpa Welivitigoda <callkalpa@gmail.com> - 26-1
- Update to v26

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 25-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 25-2
- drop python3 sed workaround

* Mon Feb 24 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 25-1
- Update to 25

* Tue Feb 11 2020 Peter Robinson <pbrobinson@fedoraproject.org> 23.1-1
- Release version 23.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 23-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 28 2017 Peter Robinson <pbrobinson@fedoraproject.org> 23-1
- Release version 23

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 22-5
- Remove the generated .desktop file (#1424490)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan 11 2015 Kalpa Welivitigoda <callkalpa@gmail.com> - 22-1
- Release version 22

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 06 2014 Kalpa Welivitigoda <callkalpa@gmail.com> - 21-1
- Release version 21

* Tue Feb 04 2014 Kalpa Welivitigoda <callkalpa@gmail.com> - 20-1
- Release version 20

* Thu Dec 26 2013 Kalpa Welivitigoda <callkalpa@gmail.com> 19-1
- Release version 19

* Tue Oct 29 2013 Peter Robinson <pbrobinson@fedoraproject.org> 18-1
- Release version 18

* Wed Oct 23 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 17-1
- Release version 17

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 16-2
- fixed rpmline issues

* Wed Jun 12 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 16-1
- Release version 16

* Mon May 27 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 15-2
- rectified the error of uploading the source with a different extension

* Mon May 27 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 15-1
- Release version 15

* Sat Apr 13 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 14-2
- fixed a typo

* Sat Apr 13 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 14-1
- Release version 14
- gtk3 port

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 11 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 13-2
- modified all to use macros
- replaced python with python2-devel in BuildRequires

* Sat Jan 07 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 13-1
- initial packaging
