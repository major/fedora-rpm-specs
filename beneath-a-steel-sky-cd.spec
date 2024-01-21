Name:           beneath-a-steel-sky-cd
Version:        0.0372
Release:        27%{?dist}
Summary:        Beneath a Steel Sky - Adventure Game - CD version
# For further discussion on distribution rights see:
# http://www.redhat.com/archives/fedora-extras-list/2006-November/msg00030.html
License:        Freely redistributable without restriction
URL:            https://en.wikipedia.org/wiki/Beneath_a_Steel_Sky
Source0:        http://sourceforge.net/projects/scummvm/files/extras/Beneath%20a%20Steel%20Sky/bass-cd-1.2.zip
Source1:        %{name}.desktop
BuildRequires:  desktop-file-utils
BuildArch:      noarch
Requires:       scummvm >= 0.9.1, hicolor-icon-theme

%description
After the Dungeons and Dragons fantasy setting of Revolution's first game, Lure
of the Temptress, Revolution decided to go down a completely different avenue
with its second adventure game, Beneath a Steel Sky, that of Science Fiction.
A bleak vision of the future was imagined, where mind control and medical
science combined forces to repress the populace. Leading comic artist, Dave
Gibbons, joined the design team to visualise this desperate landscape. The
result is the cult classic Beneath a Steel Sky.

This package contains the CD version, which contains additional / longer
cutscenes and voice acting, but also is much larger: 70 MB where as the also
available floppy version (package name beneath-a-steel-sky) is only 8 MB.

%prep
%setup -q -n bass-cd-1.2

%build
# Nothing to build data only

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 sky.* $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

%files
%doc readme.txt
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0372-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0372-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0372-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0372-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0372-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0372-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0372-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0372-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0372-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0372-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0372-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0372-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0372-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0372-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0372-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0372-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0372-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0372-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0372-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.0372-8
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines
- fixed url and sourceurl

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0372-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0372-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0372-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0372-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0372-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Aug  5 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.0372-2
- Update License tag for new Licensing Guidelines compliance

* Sun Nov  5 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.0372-1
- Initial FE package
