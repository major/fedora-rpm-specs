Name:		jack-keyboard
Version:	2.7.2
Release:	12%{?dist}
Summary:	Virtual keyboard for JACK MIDI
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://sourceforge.net/projects/jack-keyboard/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Icon is derived from the image on the website:
Source1:	%{name}.png
# Upstreamable patch. Fix DSO linking
Patch0:		%{name}-dso-linking.patch
# cmake should look for gcc only
Patch1:		jack-keyboard-cproject.patch
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	gcc
BuildRequires:	gtk2-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lash-devel

%description
jack-keyboard is a virtual MIDI keyboard - a program that allows you to send
JACK MIDI events using your PC keyboard. It is somewhat similar to vkeybd,
except it uses JACK MIDI instead of ALSA, and the default keyboard mapping is
much better - it uses the same layout as trackers (like Impulse Tracker) did,
so you have two and half octaves under your fingers.

%prep
%setup -q
%patch -P0 -p1 -b .dso.linking
%patch -P1 -p1 -b .cproject

# Add GenericName to the desktop file
echo "GenericName=Virtual MIDI Keyboard" >> src/%{name}.desktop

# Fix man dir
sed -i 's|man/man1|%{_mandir}/man1|' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

rm -fr $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/72x72/apps/
install -pm 644	%{SOURCE1} \
	$RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/72x72/apps/

desktop-file-install						\
	--dir=$RPM_BUILD_ROOT%{_datadir}/applications		\
	--add-category=X-Jack					\
	$RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS NEWS README.md TODO
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_datadir}/icons/hicolor/72x72/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.7.2-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Guido Aulisi <guido.aulisi@gmail.com> - 2.7.2-1
- Update to 2.7.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-20
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.7.1-13
- Backported hardware keycodes patch from trunk

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 12 2013 Brendan Jones <brendan.jones.it@gmail.com> 2.7.1-5
- format-security patch

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.7.1-1
- Update to 2.7.1
- Specfile cleanup
- Drop upstreamed Dvorak patch

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.5-7
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 19 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.5-5
- Add dvorak keyboard support

* Wed Aug 05 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.5-4
- Update the .desktop file

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 20 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.5-2
- Update GenericName

* Fri Mar 20 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.5-1
- Initial build
