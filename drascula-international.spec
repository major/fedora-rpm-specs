Name:           drascula-international
Version:        1.0
Release:        25%{?dist}
Summary:        Subtitles for Drascula: The Vampire Strikes Back
# For further discussion on distribution rights see:
# http://www.redhat.com/archives/fedora-extras-list/2006-November/msg00030.html
License:        Freely redistributable without restriction
URL:            http://wiki.scummvm.org/index.php/Drascula:_The_Vampire_Strikes_Back
Source0:        http://downloads.sourceforge.net/scummvm/drascula-int-%{version}.zip
Source1:        drascula-fr.desktop
Source2:        drascula-de.desktop
Source3:        drascula-es.desktop
Source4:        drascula-it.desktop
Buildarch:      noarch
BuildRequires:  desktop-file-utils

%description
Spanish, German, French and Italian subtitles for Drascula: The Vampire
Strikes Back.


%package -n drascula-fr
Summary:        French subtitles for Drascula: The Vampire Strikes Back
Requires:       drascula
Supplements:    (drascula and langpacks-fr)

%description -n drascula-fr
French subtitles for Drascula: The Vampire Strikes Back.

%package -n drascula-de
Summary:        German subtitles for Drascula: The Vampire Strikes Back
Requires:       drascula
Supplements:    (drascula and langpacks-de)

%description -n drascula-de
German subtitles for Drascula: The Vampire Strikes Back.

%package -n drascula-es
Summary:        Spanish subtitles for Drascula: The Vampire Strikes Back
Requires:       drascula
Supplements:    (drascula and langpacks-es)

%description -n drascula-es
Spanish subtitles for Drascula: The Vampire Strikes Back.

%package -n drascula-it
Summary:        Italian subtitles for Drascula: The Vampire Strikes Back
Requires:       drascula
Supplements:    (drascula and langpacks-it)

%description -n drascula-it
Italian subtitles for Drascula: The Vampire Strikes Back.


%prep
%setup -q -c


%build
# nothing todo content only


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/drascula
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install -p -m 644 PACKET.00? $RPM_BUILD_ROOT%{_datadir}/drascula
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE3}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE4}

%files -n drascula-fr
%doc readme.txt
%{_datadir}/drascula/PACKET.002
%{_datadir}/applications/drascula-fr.desktop

%files -n drascula-de
%doc readme.txt
%{_datadir}/drascula/PACKET.003
%{_datadir}/applications/drascula-de.desktop

%files -n drascula-es
%doc readme.txt
%{_datadir}/drascula/PACKET.004
%{_datadir}/applications/drascula-es.desktop

%files -n drascula-it
%doc readme.txt
%{_datadir}/drascula/PACKET.005
%{_datadir}/applications/drascula-it.desktop


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 02 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.0-12
- Add Supplements: for https://fedoraproject.org/wiki/Packaging:Langpacks guidelines
- Drop Group, BuildRoot tags
- Drop %%clean and %%defattr()

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 15 2009 Hans de Goede <hdegoede@redhat.com> 1.0-2
- Fixup license tag, this was never even close to being licensed
  under GPLv2+, but it is freely redistributable (#494199)

* Sun Apr  5 2009 Hans de Goede <hdegoede@redhat.com> 1.0-1
- Initial Fedora package
