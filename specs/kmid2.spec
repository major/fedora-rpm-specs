Name:           kmid2
Version:        2.4.0
Release:        32%{?dist}
Summary:        A MIDI/karaoke player for KDE

# GPLv2+ for the code and the MMA examples, CC-BY-SA for the MIDI examples
License:        GPLv2+ and CC-BY-SA
URL:            http://userbase.kde.org/KMid2

Source0:        http://downloads.sourceforge.net/project/%{name}/%{version}/kmid-%{version}.tar.bz2


BuildRequires:  kdelibs4-devel
BuildRequires:  kde-filesystem
BuildRequires:  cmake
BuildRequires:  alsa-lib-devel
BuildRequires:  drumstick0-devel >= 0.4
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires: make

%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api}}
%{?_kde4_version:Requires: kdelibs4%{?_isa} >= %{_kde4_version}}
Requires:       oxygen-icon-theme
Requires:       drumstick0 >= 0.4
Requires:       %{name}-libs = %{version}-%{release}

Obsoletes:      kmid < 2.0-1
Provides:       kmid = %{version}-%{release}

%description
KMid2 is a MIDI/karaoke file player, with configurable midi mapper, real
Session Management, drag & drop, customizable fonts, etc. It has a very
nice interface which let you easily follow the tune while changing the
color of the lyrics.
It supports output through external synthesizers, AWE, FM and GUS cards.
It also has a keyboard view to see the notes played by each instrument.

%package libs
Summary:        Runtime libraries for %{name}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later

%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api}}
%{?_kde4_version:Requires: kdelibs4%{?_isa} >= %{_kde4_version}}

%description libs
%{summary}.

%package devel
Summary:        Development files for %{name}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later

Requires:       %{name}-libs = %{version}-%{release}

Obsoletes:      kmid-devel < 2.0-1
Provides:       kmid-devel = %{version}-%{release}

%description devel
%{summary}.

%prep
%setup -q -n kmid-%{version}
# zap bundled copy of drumstick to guarantee it's never used
rm -rf drumstick


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} -C %{_target_platform}
desktop-file-validate %{buildroot}%{_kde4_datadir}/applications/kde4/kmid.desktop
%find_lang kmid --with-kde



%ldconfig_scriptlets libs

%files -f kmid.lang
%doc ChangeLog COPYING README TODO
%{_kde4_bindir}/kmid
%{_kde4_appsdir}/kmid/
%{_kde4_appsdir}/kmid_part/
%{_kde4_datadir}/applications/kde4/kmid.desktop
%{_kde4_datadir}/config.kcfg/*
%{_kde4_datadir}/kde4/services/*
%{_kde4_datadir}/kde4/servicetypes/*
%{_kde4_iconsdir}/hicolor/*/apps/*
%{_kde4_libdir}/kde4/*
%{_datadir}/dbus-1/interfaces/org.kde.KMid.xml
%{_datadir}/dbus-1/interfaces/org.kde.KMidPart.xml

%files libs
%{_kde4_libdir}/libkmidbackend.so.*

%files devel
%{_kde4_libdir}/libkmidbackend.so
%{_kde4_includedir}/kmid/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.0-31
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4.0-15
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.4.0-9
- Rebuilt for GCC 5 C++11 ABI change

* Mon Nov 17 2014 Robin Lee <cheeselee@fedoraproject.org> - 2.4.0-8
- Use drumstick0 instead of drumstick

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 12 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.4.0-1
- Update to 2.4.0 (#712330)
- Drop obsolete backported kde#240394 patch, already included in 2.4.0
- Bump minimum drumstick version to 0.4

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jun 03 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.3.0-2
- Fix crash in ALSA backend due to reloadDeviceList (kde#240394, upstream patch)

* Fri May 28 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.3.0-1
- Update to 2.3.0 (new versioning scheme)
- BR drumstick-devel >= 0.3
- Requires: drumstick >= 0.3
- Drop obsolete drumstick-version patch
- Examples now partly CC-BY-SA, partly GPLv2+ (instead of CC-BY)
- Use _kde4_version macro
- Add -devel and -libs subpackages
- Package COPYING

* Tue Feb 09 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.2.1-2
- Requires: drumstick >= 0.2.99-0.3

* Tue Feb 09 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.2.1-1
- Update to 0.2.1
- Drop upstreamed timidity-pulseaudio patch
- Drop dont-translate-output-names patch, should not be needed anymore
- BR drumstick-devel >= 0.2.99-0.3 (0.2.1 needs the 20100208 snapshot)
- relax drumstick version check in CMakeLists.txt as 0.3 is not out yet

* Fri Feb 05 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.2.0-3
- Don't translate output names, breaks autospawning sequencers

* Sun Jan 31 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.2.0-2
- Support PulseAudio when autospawning TiMidity++ (-OO -opulse switches)

* Sun Jan 31 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.2.0-1
- Update to 0.2.0
- The examples with copyright issues have been dropped by upstream
- BR drumstick-devel instead of aseqmm-devel

* Wed Jan 27 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.1.1-4
- Fix the kde4-config output parsing for 4.4 ("KDE Development Platform:")

* Wed Jan 27 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.1.1-3
- Correctly require at least the kdelibs version used for building

* Wed Jan 27 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.1.1-2
- Remove nonsense Requires: kdelibs4 >= %%{version}, as %%{version} is 0.1.1

* Fri Jan 22 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.1.1-1
- First Fedora package, replaces kmid
