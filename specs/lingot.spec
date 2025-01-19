Name:       lingot
Version:    1.1.1
Release:    14%{?dist}
Summary:    A musical instruments tuner

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
URL:        https://www.nongnu.org/%{name}/
Source0:    https://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fftw-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  json-c-devel
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  libappstream-glib
BuildRequires:  libglade2-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires: make

%description
LINGOT is a musical instrument tuner. It's accurate, easy to use, and highly
configurable. Originally conceived to tune electric guitars, its
configurability gives it a more general character.

%package devel
Summary:  %{summary}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the headers and shared libraries for %{name}.
NOTE: The library is currently experimental and its interface is subject to
change.


%prep
%autosetup


%build
%configure
%make_build

%install
%make_install
# we install these ourselves to have total control over what files are being
# placed there. COPYING, for example needs to be placed using the license macro
rm -rf %{buildroot}/%{_defaultdocdir}/%{name}

# Delete static libraries
find %{buildroot}/%{_libdir}/ -name "liblingot.*a" -delete

%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/*%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README THANKS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/metainfo/*%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/scalable/apps/*.%{name}.svg
%{_libdir}/liblingot.so.0
%{_libdir}/liblingot.so.0.0.0

%files devel
%{_includedir}/%{name}
%{_libdir}/liblingot.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.1-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 1.1.1-4
- Rebuild for versioned symbols in json-c

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.1.1-1
- Update to new release
- https://bugzilla.redhat.com/show_bug.cgi?id=1833596
- Modernise spec
- Incorrect FSF address reported: https://github.com/ibancg/lingot/issues/56

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.0.1-1
- Update to 1.0.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.0.0-2
- do not use metainfodir
- metainfodir on f27 seems to point to /usr/share/appdata instead of metainfo

* Fri Jul 06 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.0.0-1
- Update to 1.0.0
- Use upstream's appdata file
- Remove unneeded patch

* Sat Mar 10 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.1-17
- Add gcc to BR
- Use license macro
- Move appdata to metainfo dir
- Use buildroot macro instead of RPM_BUILD_ROOT

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.9.1-10
- Add an AppData file for the software center

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.9.1-8
- Fix FTBFS with -Werror=format-security (#1037177, #1106098)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.1-2
- Rebuild for new libpng

* Tue Aug 23 2011 Karel Volný <kvolny at redhat dot com> 0.9.1-1
- New version 0.9.1
-  Fixed bug #33046: Lingot fails to compile with libjack-dev version < 2
-   (removed lingot-0.9.0-jackportisactive.patch)
-  Fixed bug #34007: JACK support broken in lingot 0.9.0
-  Added 48K sample rate to OSS and ALSA.

* Fri Jun 24 2011 Karel Volný <kvolny at redhat dot com> 0.9.0-1
- New version 0.9.0
- Support for different scales
- Backported patch for newer JACK (hg rev 243:749df5080742)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Mar 18 2010 Karel Volný <kvolny at redhat dot com> 0.8.1-1
- New version 0.8.1
- Fixes missing linker flags, a crash and a hang

* Sat Mar 06 2010 Karel Volný <kvolny at redhat dot com> 0.8.0-1
- New version 0.8.0
- Native ALSA support, alsa-oss no longer needed
- JACK support
- Removed Requires gtk2 WRT bug #517970

* Tue Aug 18 2009 Karel Volný <kvolny at redhat dot com> 0.7.6-1
- Initial Fedora release.
