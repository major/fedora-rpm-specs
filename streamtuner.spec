%global __python %{__python3}
%global _name   streamtuner2

Name:           streamtuner
Version:        2.2.2
Release:        1%{?dist}
Summary:        An internet radio browser
License:        Public Domain
URL:            http://sourceforge.net/projects/streamtuner2/
Source0:        http://downloads.sf.net/streamtuner2/streamtuner2-%{version}.src.txz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  fdupes

Requires:       gtk3
Requires:       python3
Requires:       python3-gobject-base
Requires:       python3-lxml
Requires:       python3-pillow
Requires:       python3-pyquery
Requires:       python3-simplejson
Requires:       python3-requests
Requires:       xterm
Requires:       audacious
Requires:       perl-interpreter
# Needed for properties icons (channels & features)
Requires:       gdouros-symbola-fonts

# required for youtube record
Requires:       youtube-dl

# Patches
Patch0:         streamtuner2-default-config-desktop-file.patch

%description
Streamtuner lists radio directory services like Shoutcast, Xiph, Live365, 
MyOggRadio, Jamendo. It allows listening via any audio player and recording of
streams via streamripper.
This is streamtuner2 which mimics the older streamtuner 0.99.99 application
in look and feel. But it's an independent rewrite and runs on Python;
is therefore easier to extend.

%prep
%setup -qn %{_name}
%patch0 -p1 -b .default-config-desktop-file
# rpmlint
find . -type f -exec sed -i -e 's|\/usr\/bin\/env python|\/usr\/bin\/python3|g' {} \;

%build

%install
rm help/guiseq
# rpmlint
rm .zip.py

install -D -m 755 bin %{buildroot}/%{_bindir}/%{_name}
install -D -m 644 %{_name}.desktop %{buildroot}/%{_datadir}/applications/%{_name}.desktop
install -D -m 644 %{_name}.png %{buildroot}/%{_datadir}/pixmaps/%{_name}.png

mkdir %{buildroot}/%{_datadir}/%{_name}
install -m 644 gtk3.xml.gz %{buildroot}/%{_datadir}/%{_name}/
files=`find . -maxdepth 1 -type f -name "*.py" -or -name "*.png" -or -name "*.glade"`
for f in $files
    do %__install -m 644 $f %{buildroot}/%{_datadir}/%{_name}/
done

mkdir %{buildroot}/%{_datadir}/%{_name}/channels
pushd channels
files=`find . -maxdepth 1 -type f -name "*.py" -or -name "*.png"`
for f in $files
    do install -m 644 $f %{buildroot}/%{_datadir}/%{_name}/channels/
done
popd

mkdir -p %{buildroot}/%{_mandir}/man1
install -m 644 help/streamtuner2.1 %{buildroot}/%{_mandir}/man1/
rm help/streamtuner2.1

desktop-file-install                         \
  --dir %{buildroot}%{_datadir}/applications \
  --add-category Audio                       \
  --add-category Tuner                       \
  --add-category GTK                         \
  --delete-original                          \
  %{buildroot}%{_datadir}/applications/%{_name}.desktop

fdupes -s %{buildroot}


%files
%doc README CREDITS NEWS help/
%{_bindir}/%{_name}
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/pixmaps/%{_name}.png
%{_datadir}/%{_name}/
%{_mandir}/man1/streamtuner2.1.*

%changelog
* Thu Sep 15 2022 Leigh Scott <leigh123linux@gmail.com> - 2.2.2-1
- Update to 2.2.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Leigh Scott <leigh123linux@gmail.com> - 2.2.1-1
- Update to 2.2.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.2.0-1
- Update to 2.2.0
- Switch to python3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.9-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 2.1.9-7
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 12 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.1.9-4
- Use gtk3 for default (fixes hidpi scaling issues)

* Fri Jul 10 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.1.9-3
- readd kronos

* Sun Jul 05 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.1.9-2
- patch make file so it can do the install
- clean up Requires
- remove scriptlet as there is no mimetype in desktop file

* Sat Jun 20 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.1.9-1
- update to 2.1.9
- add requires gtk3
- spec file clean up

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 09 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.1.8-1
- update to 2.1.8

* Sun Aug 17 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.1.3-1
- update to 2.1.3
- drop upstream patch
- readd live365 plugin
- drop requires gtk-doc

* Thu Jul 03 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.1.1-8
- add requires youtube-dl (required for youtube record)

* Thu Jul 03 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.1.1-7
- fix issue with totem playing youtube video

* Thu Jul 03 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.1.1-6
- fix myoggradio plugin

* Mon Jun 23 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.1.1-5
- fix logo and menu icon

* Sun Jun 22 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.1.1-4
- remove un-needed python3 lib (python-urllib3)
- add requires python-simplejson
- remove live365 plugin till it's fixed
- preserve file timestamps

* Sat Jun 21 2014 Matthias Haase <matthias_haase@bennewitz.com> - 2.1.1-3
- bump up release
- merge of changes done by Leigh Scott

* Tue Jun 17 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.1.1-2
- add missing python requires
- add bundled kronos python lib
- add man file

* Thu Jun 12 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.1.1-1
- update to 2.1.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 12 2010 Matthias Haase <matthias_haase@bennewitz.com> - 2.0.8-7
- bump up release on rawhide

* Fri Nov 12 2010 Matthias Haase <matthias_haase@bennewitz.com> - 2.0.8-6
- bump up release on rawhide

* Thu Nov 11 2010 endur <matthias_haase@bennewitz.com> - 2.0.8-3
- enhanced default-config-desktop-file.patch

* Thu Nov 11 2010 Matthias Haase <matthias_haase@bennewitz.com> - 2.0.8-2
- Many specfile enhancements and corrections
- default-config-desktop-file.patch
- Initial build for Fedora

* Sat Nov 06 2010 Brendan Jones <brendan.jones.it@gmail.com> 2.0.8-1
- initial build 
