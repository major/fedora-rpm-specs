Name:           transmission-remote-gtk
Version:        1.5.1
Release:        3%{?dist}
Summary:        GTK remote control for the Transmission BitTorrent client

License:        GPLv2+
URL:            https://github.com/transmission-remote-gtk/transmission-remote-gtk
Source0:        https://github.com/transmission-remote-gtk/transmission-remote-gtk/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  json-glib-devel
BuildRequires:  gtk3-devel
BuildRequires:  libproxy-devel
BuildRequires:  glib2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libappindicator-gtk3-devel
BuildRequires:  GeoIP-devel
BuildRequires:  git

%description
transmission-remote-gtk is a GTK client for remote management of
the Transmission BitTorrent client, using its HTTP RPC protocol.

%prep
%autosetup -p1 -S git

%build
%meson -Dmrss=disabled
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README.md AUTHORS ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/io.github.TransmissionRemoteGtk.desktop
%{_datadir}/metainfo/io.github.TransmissionRemoteGtk.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1*

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Yaakov Selkowitz <yselkowi@redhat.com> - 1.5.1-1
- new version (#2073639)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 1.4.2-1
- new version (#2014968)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 06 2020 Bastien Nocera <bnocera@redhat.com> - 1.4.1-3
+ transmission-remote-gtk-1.4.1-3
- Fix missing icon in gnome-shell

* Thu Apr 02 2020 Bastien Nocera <bnocera@redhat.com> - 1.4.1-2
+ transmission-remote-gtk-1.4.1-2
- Add missing changelog entry

* Thu Apr 02 2020 Bastien Nocera <bnocera@redhat.com> - 1.4.1-1
+ transmission-remote-gtk-1.4.1-1
- Update to 1.4.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.1-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 12 2016 Patrick Griffis <tingping@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Fri Aug 12 2016 Patrick Griffis <tingping@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.1.1-1
- New Release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 17 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.1-1
- New Release

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 2 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.0.2-1
- New Release

* Wed Feb 8 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.0.1-1
- New Release

* Sun Nov 20 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.7-3
- Minor changes according to review

* Thu Oct 27 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.7-2
- Added icon cache

* Tue Oct 18 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.7-1
- Initial version of the package
