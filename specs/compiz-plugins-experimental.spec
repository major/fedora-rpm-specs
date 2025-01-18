%global  basever 0.8.18

Name:    compiz-plugins-experimental
Epoch:   1
Version: %{basever}
Release: 13%{?dist}
Summary: Additional plugins for Compiz
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://gitlab.com/compiz/%{name}
Source0: %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
# libdrm is not available on these arches
ExcludeArch: s390 s390x

BuildRequires: gcc-c++
BuildRequires: compiz-plugins-main-devel >= %{basever}
BuildRequires: compiz-plugins-extra-devel >= %{basever}
BuildRequires: compiz-bcop >= %{basever}
BuildRequires: perl(XML::Parser)
BuildRequires: intltool
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libtool
BuildRequires: libXScrnSaver-devel
BuildRequires: automake
BuildRequires: make

Requires: compiz >= %{basever}
Requires: compiz-plugins-main%{?_isa} >= %{basever}
Requires: compiz-plugins-extra%{?_isa} >= %{basever}
Provides: compiz-plugins-unsupported%{?_isa} = %{epoch}:%{version}-%{release}
Provides: compiz-plugins-unsupported = %{epoch}:%{version}-%{release}
Obsoletes: compiz-plugins-unsupported < %{epoch}:%{version}-%{release}
# https://gitlab.com/compiz/compiz-plugins-experimental/-/merge_requests/48
Patch0: compiz-plugins-experimental-0.8.18-gcc-14-fix.patch

%description
The Compiz Fusion Project brings 3D desktop visual effects that improve
usability of the X Window System and provide increased productivity
though plugins and themes contributed by the community giving a
rich desktop experience.
This package contains additional plugins from the Compiz Fusion Project

%package devel
Summary: Development files for Compiz-Fusion
Requires: compiz-plugins-main-devel%{?_isa} >= %{basever}
Requires: compiz-plugins-extra-devel%{?_isa} >= %{basever}
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Provides: compiz-plugins-unsupported-devel%{?_isa} = %{epoch}:%{version}-%{release}
Provides: compiz-plugins-unsupported-devel = %{epoch}:%{version}-%{release}
Obsoletes: compiz-plugins-unsupported-devel < %{epoch}:%{version}-%{release}

%description devel
This package contain development files required for developing other plugins


%prep
%autosetup -p1 -n %{name}-v%{version}
chmod -x src/cubemodel/fileParser.c src/cubemodel/cubemodel.c src/cubemodel/cubemodel-internal.h

%build
./autogen.sh
%configure

make %{?_smp_mflags} V=1

%install
%{make_install}

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'

%find_lang %{name}


%files -f %{name}.lang
%doc COPYING AUTHORS NEWS
%{_libdir}/compiz/*.so
%dir %{_datadir}/compiz/elements/
%dir %{_datadir}/compiz/fireflies/
%dir %{_datadir}/compiz/snow/
%dir %{_datadir}/compiz/stars/
%dir %{_datadir}/compiz/earth/
%{_datadir}/compiz/*.xml
%{_datadir}/compiz/*/*.frag
%{_datadir}/compiz/*/*.png
%{_datadir}/compiz/*/*.svg
%{_datadir}/compiz/*/*.vert
%{_datadir}/compiz/icons/hicolor/scalable/apps/*.svg

%files devel
%{_includedir}/compiz/compiz-elements.h


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 1:0.8.18-12
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb  6 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 1:0.8.18-10
- Fixed FTBFS with gcc-14
  Resolves: rhbz#2261042

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov  9 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1:0.8.18-1
- New version
  Related: rhbz#1891137

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1:0.8.16-4
- Fixed FTBFS with gcc-10
  Resolves: rhbz#1799249

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr  2 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1:0.8.16-1
- New version
  Related: rhbz#1656467
- New URL

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 20 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1:0.8.14-1
- update to 0.8.14 release
- Add models for the cubemodel plugin.
- Many improvements to the elements plugin.
- Increase bonanza animation speed.
- Add a default enabled option for stars, fireflies, wizard and snow.
- Improvements to the static plugin.
- Exit on user input after starting screensaver manually.
- Improve the default snow texture.
- Increase maximum text size in workspacenames.
- Add earth plugin.
- Update translations.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 28 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12-3
- add correct epoch versions
- own directories
- fix permissions

* Sun Mar 27 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12-2
- initial package
- rename compiz-plugins-unsupported to compiz-plugins-experimental

