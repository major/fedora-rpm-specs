Name:           pulsecaster
Version:        0.9
Release:        19%{?dist}
Summary:        A PulseAudio-based podcast recorder

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://fedorahosted.org/pulsecaster
Source0:        http://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel, python3-setuptools
BuildRequires:  desktop-file-utils, gettext

Requires:       python3-pulsectl
Requires:       python3-gobject
Requires:       gstreamer1 >= 1.0
Requires:       python3-dbus >= 0.83


%description
PulseCaster is a simple PulseAudio-based tool for making podcast
interviews. It is designed for ease of use and simplicity. The user
makes a call with a preferred PulseAudio-compatible Voice-over-IP
(VoIP) softphone application such as Ekiga or Twinkle, and then starts
PulseCaster to record the conversation to a multimedia file. The
resulting file can be published as a podcast or distributed in other
ways.

%prep
%setup -q


%build
%{__python3} setup.py build
for F in po/*.po ; do
    L=`echo $F | %{__sed} 's@po/\([^\.]*\).po@\1@'`
    msgfmt -o po/$L.mo $F
done


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
desktop-file-install \
    --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
    %{name}.desktop
for D in ${RPM_BUILD_ROOT}%{_datadir}/locale/* ; do
    mv ${D}/LC_MESSAGES/*.mo ${D}/LC_MESSAGES/%{name}.mo
done
%find_lang %{name}

 
%files -f %{name}.lang
%doc AUTHORS README.md COPYING TODO
%{python3_sitelib}/*
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/GConf/gsettings/*
%{_datadir}/appdata/*
%{_datadir}/glib-2.0/schemas/*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9-18
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9-16
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.9-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 14 2019 Paul W. Frields <stickster@gmail.com> - 0.9-1
- Update to upstream 0.9, now Python 3 only

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Paul W. Frields <stickster@gmail.com> - 0.1.10-12
- Fix scriptlets for Python 2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.10-9
- Remove obsolete scriptlets

* Fri Jan 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.10-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb  8 2014 Paul W. Frields <stickster@gmail.com> - 0.1.10-1
- Update to upstream 0.1.10

* Fri Sep 20 2013 Paul W. Frields <stickster@gmail.com> - 0.1.9-5
- Updated translations from upstream

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 14 2012 Paul W. Frields <stickster@gmail.com> - 0.1.9-2
- Fix missing BR: gettext

* Thu Dec 13 2012 Paul W. Frields <stickster@gmail.com> - 0.1.9-1
- Update to upstream 0.1.9

* Mon Aug  6 2012 Paul W. Frields <stickster@gmail.com> - 0.1.8.1-6
- Fix missing README doc

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Mar 26 2011 Paul W. Frields <stickster@gmail.com> - 0.1.8.1-3
- Fix missing Requires (#689295)

* Sat Mar 26 2011 Paul W. Frields <stickster@gmail.com> - 0.1.8.1-2
- Fix icon setting in .desktop file (#689419)

* Wed Mar 16 2011 Paul W. Frields <stickster@gmail.com> - 0.1.8.1-1
- Update to upstream 0.1.8.1

* Wed Mar 16 2011 Paul W. Frields <stickster@gmail.com> - 0.1.8-1
- Update to upstream 0.1.8

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 16 2011 Paul W. Frields <stickster@gmail.com> - 0.1.7-2
- Fix missing package requirement (#669913)

* Sun Dec 19 2010 Paul W. Frields <stickster@gmail.com> - 0.1.7-1
- Update to upstream 0.1.7
- Fix scriptlets to update icon cache

* Fri Jul 30 2010 Paul W. Frields <stickster@gmail.com> - 0.1.6-3
- Bump release for Python 2.7 rebuild

* Thu Jun 10 2010 Paul W. Frields <stickster@gmail.com> - 0.1.6-2
- Fix missing dependency (#602593)

* Thu May  6 2010 Paul W. Frields <stickster@gmail.com> - 0.1.6-1
- New upstream 0.1.6

* Wed Mar 31 2010 Paul W. Frields <stickster@gmail.com> - 0.1.5-1
- New upstream 0.1.5, fixes desktop entry file

* Sat Feb 20 2010 Paul W. Frields <stickster@gmail.com> - 0.1.4-1
- Initial RPM release

