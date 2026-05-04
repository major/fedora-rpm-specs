Name:           mhwaveedit
Version:        1.4.22
Release:        17%{?dist}
Summary:        Sound editing program        

License:        GPLv2+
URL:            http://gna.org/projects/mhwaveedit
Source:         http://download.gna.org/mhwaveedit/%{name}-%{version}.tar.bz2

Requires:       pulseaudio
Requires:       hicolor-icon-theme

BuildRequires:  gcc
BuildRequires:  pulseaudio-libs-devel alsa-lib-devel jack-audio-connection-kit-devel
BuildRequires:  libsndfile-devel libsamplerate-devel ladspa-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel
BuildRequires:  gettext


%description
mhWaveEdit is a graphical program for editing sound files. It is completely
free (GPL).
%prep
%setup -q


%build
%configure

iconv -f iso-8859-1 -t utf-8 AUTHORS > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS
make %{?_smp_mflags} 

%install
#removal of buildroot is no longer necassary, except for EPEL5
make install DESTDIR=%{buildroot}

#install the icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mv share/pixmaps/%{name}.xpm %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.xpm


%find_lang %{name}
desktop-file-install    \
    --dir %{buildroot}%{_datadir}/applications \
     share/applications/%{name}.desktop

%files -f %{name}.lang
#Upstream has been contacted about incorrect fsf address 2012-08-07
%doc AUTHORS COPYING README BUGS NEWS TODO HACKING ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.xpm
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/%{name}.1.*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.22-13
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 07 2012 Jørn Lomax <northlomax@gmail.com> 1.4.22-3
- Convert AUTHORS to utf8m upstream notified about incorrect fsf address
* Tue Aug 07 2012 Jørn Lomax <northlomax@gmail.com> 1.4.22-2
- added BUGS, NEWS, TODO, HACKING and changelog. Shortned desciption
* Mon Jul 30 2012 Jørn Lomax <northlomax@gmail.com> 1.4.22-1
- inital package
