%global _hardened_build 1
%global xfceversion 4.12
%global versnum 0.4

Name:		xfce4-pulseaudio-plugin
Version:	0.4.5
Release:	1%{?dist}
Summary:	Pulseaudio plugin for Xfce4

License:	GPLv2+
URL:		https://github.com/andrzej-r/xfce4-pulseaudio-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/%{name}/%{versnum}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:	gcc-c++
BuildRequires:	intltool
BuildRequires:	libxfce4ui-devel >= %{xfceversion}
BuildRequires:	libxfce4util-devel >= %{xfceversion}
BuildRequires:	xfce4-panel-devel >= %{xfceversion}
BuildRequires:	exo-devel
BuildRequires:	pulseaudio-libs-devel >= 0.9.19
BuildRequires:	glib2-devel >= 2.24.0
BuildRequires:	gtk3-devel >= 3.6.0
BuildRequires:	xfconf-devel >= 4.6.0
BuildRequires:	keybinder3-devel
BuildRequires:	libnotify-devel

Obsoletes:	xfce4-mixer <= 4.11
# Obsoletes--->xfce4-volumed <= 0.1.13

Requires:	pulseaudio-daemon
Requires:	pavucontrol

%description
Pulseaudio panel plugin for Xfce Desktop Environment

%prep
%autosetup

# remove empty files
rm -f AUTHORS README

%build
%configure
%make_build

%install
%make_install

# remove libtool archives
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang %{name}

# remove zero-length files
rm -f %{buildroot}/%{defaultdocdir}/AUTHORS
rm -f %{buildroot}/%{defaultdocdir}/README


%files -f %{name}.lang
%{license} COPYING
%doc ChangeLog
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_libdir}/xfce4/panel/plugins/libpulseaudio-plugin.so
%{_datadir}/icons/hicolor/48x48/apps/%{name}*
%{_datadir}/icons/hicolor/scalable/apps/%{name}*
%{_datadir}/icons/hicolor/scalable/status/*

%changelog
* Thu Sep 15 2022 Kevin Fenzi <kevin@scrye.com> - 0.4.5-1
- Update to 0.4.5. Fixes rhbz#2127276

* Sat Sep 03 2022 Kevin Fenzi <kevin@scrye.com> - 0.4.4-1
- Update to 0.4.4. Fixes rhbz#2123909

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.3-4
- Require pulseaudio-daemon instead of pulseaudio

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 29 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.3-1
- Update to 0.4.3

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 13 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.1-21
- Obsolete xfce4-mixer

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.1-20
- rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 12 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Tue Mar 20 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Thu Mar 01 2018 Kevin Fenzi <kevin@scrye.com> - 0.3.5-1
- Update to 0.3.5

* Thu Feb 15 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.2.5-6
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 20 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.5-2
- Add pavucontrol and pulseaudio as requires

* Sat Apr 22 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.2.5-1
- Rebuilt for new upstream 0.2.5 release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 10 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.4-5
- Removed obsoletes for xfce4-volumed and xfce4-mixer
- Fixes bug#1355763

* Sat Apr 16 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.4-4
- Added obsoletes for xfce4-volumed

* Fri Apr 15 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.4-3
- Added xfce4-mixer obsoletes

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 26 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.4-1
- Update 0.2.4

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 11 2015 Kevin Fenzi <kevin@scrye.com> 0.2.3-1
- Update to 0.2.3

* Wed Apr 22 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.2-2
- Add keybinder-devel as BR
- enable keyboard shortcuts support

* Thu Mar 26 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2
- Added symoblic icons for different statuses

* Sun Mar 08 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1
- Bug fix update

* Fri Mar 06 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Sun Mar 01 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.0-1
- New package 
