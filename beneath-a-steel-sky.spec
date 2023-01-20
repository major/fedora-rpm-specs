Name:           beneath-a-steel-sky
Version:        1.3
Release:        22%{?dist}
Summary:        Beneath a Steel Sky - Adventure Game
# For further discussion on distribution rights see:
# http://www.redhat.com/archives/fedora-extras-list/2006-November/msg00030.html
License:        Freely redistributable without restriction
URL:            http://www.revolution.co.uk/_display.php?id=16
Source0:        http://downloads.sourceforge.net/scummvm/BASS-Floppy-%{version}.zip
Source1:        %{name}.desktop
BuildRequires:  desktop-file-utils
BuildArch:      noarch
Requires:       scummvm >= 0.12.0
Obsoletes:      bass <= 0-8
Provides:       bass = 0-8

%description
After the Dungeons and Dragons fantasy setting of Revolution's first game, Lure
of the Temptress, Revolution decided to go down a completely different avenue
with its second adventure game, Beneath a Steel Sky, that of Science Fiction.
A bleak vision of the future was imagined, where mind control and medical
science combined forces to repress the populace. Leading comic artist, Dave
Gibbons, joined the design team to visualise this desperate landscape. The
result is the cult classic Beneath a Steel Sky.

Notice that this package contains the floppy version, the CD version is also
available in the %{name}-cd package. The CD version contains
additional / longer cutscenes and voice acting, but also is much larger: the CD
version ways in at 70 MB where as this version is only 8 MB.

%prep
%setup -q -c

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
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.3-5
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 11 2010 Lucian Langa <cooly@gnome.eu.org> - 1.3-1
- upstream source name/version change

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0348-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr  5 2009 Hans de Goede <hdegoede@hhs.nl> 0.0348-8
- Bump minimal scummvm version to 0.12.0, as the new upstream zip no
  longer includes sky.cpt, that is part of scummvm itself since 0.12.0

* Fri Apr  3 2009 Hans de Goede <hdegoede@hhs.nl> 0.0348-7
- Switch to latest upstream zip, which has some typo's in the readme
  corrected

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0348-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 15 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.0348-5
- "Fix" Source0 URL again (don't make it an URL any more)

* Fri Aug 31 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.0348-4
- Fix Source0 URL

* Sun Aug  5 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.0348-3
- Update License tag for new Licensing Guidelines compliance

* Thu Nov  9 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.0348-2
- Fix Source0 URL
- Various small specfile cleanups (bug 214057)

* Sun Nov  5 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.0348-1
- Initial FE package
