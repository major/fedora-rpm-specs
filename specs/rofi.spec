Name:    rofi
Version: 1.7.7
Release: 1%{?dist}
Summary: A window switcher, application launcher and dmenu replacement

# lexer/theme-parser.[ch]:
# These files are generated from lexer/theme-parser.y and licensed with GPLv3+
# with Bison exception.
# As the source file is licensed with MIT, according to the Bison exception,
# the shipped files are considered to be MIT-licensed.
# See also
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/message/C4VVT54Z4WFGJPPD5X54ILKRF6X2IFLZ/
License: MIT
URL:     https://github.com/davatorium/%{name}
Source:  %{URL}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig
BuildRequires: gcc
BuildRequires: bison
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: flex
BuildRequires: graphviz
BuildRequires: meson
BuildRequires: pandoc
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-xcb)
BuildRequires: pkgconfig(check) >= 0.11.0
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-aux)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-imdkit)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-randr)
BuildRequires: pkgconfig(xcb-xinerama)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)

# https://github.com/sardemff7/libgwater
Provides: bundled(libgwater)
# https://github.com/sardemff7/libnkutils
Provides: bundled(libnkutils)

Requires:      %{name}-themes = %{version}-%{release}
Requires:      hicolor-icon-theme


%description
Rofi is a dmenu replacement. Rofi, like dmenu, will provide the user with a
textual list of options where one or more can be selected. This can either be,
running an application, selecting a window or options provided by an external
script.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        devel-doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    devel-doc
The %{name}-devel-doc package contains documentation files for developing
applications that use %{name}.

%package        themes
Summary:        Themes for %{name}
BuildArch:      noarch

%description    themes
The %{name}-themes package contains themes for %{name}.

%prep
%autosetup -p1


%build
%meson
%meson_build

%meson_build doxy
find %{_vpath_builddir}/doc/html/html -name "*.map" -delete
find %{_vpath_builddir}/doc/html/html -name "*.md5" -delete


%install
%meson_install


%check
%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/rofi*.desktop


%files
%doc README.md
%license COPYING
%{_bindir}/rofi
%{_bindir}/rofi-sensible-terminal
%{_bindir}/rofi-theme-selector
%{_datadir}/applications/rofi.desktop
%{_datadir}/applications/rofi-theme-selector.desktop
%{_datadir}/icons/hicolor/scalable/apps/rofi.svg
%{_mandir}/man1/rofi*
%{_mandir}/man5/rofi*

%files themes
%license COPYING
%{_datarootdir}/rofi

%files devel
%{_includedir}/rofi
%{_libdir}/pkgconfig/rofi.pc

%files devel-doc
%license COPYING
%doc %{_vpath_builddir}/doc/html/html/*



%changelog
* Sun Jan 05 2025 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7.7-1
- Update to 1.7.7 (#2334339)
- Build with meson

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 21 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 1.7.5-1
- Update to 1.7.5 (#2119919)
  update owner in URL

* Mon Aug 15 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7.4-1
- Update to 1.7.4 (#2118201)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7.3-1
- Update to 1.7.3 (#2048137)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 30 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7.2-1
- Update to 1.7.2 (#2027032)

* Mon Sep 06 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec  3 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.6.1-1
- New upstream release 1.6.1 (rhbz#1900420)

* Sun Sep 13 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.6.0-1
- New upstream release (rhbz#1876283)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.5.4-1
- Update to 1.5.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.2-1
- Update to 1.5.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.5.1-7
- Add patch to fix undefined behavior of char* initialization

* Sun Nov 11 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.5.1-6
- Do not package .md5 or .map files
- Remove scriptlet to modify shebang, rely on mangler instead

* Sat Nov 10 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.5.1-5
- Replace BR pkconfig(xcb-util) -> pkgconfig(xcb-aux)
- Clarify license of bison-generated files

* Thu Nov 08 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.5.1-4
- Rename doc sub-package to devel-doc

* Tue Nov 06 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.5.1-3
- Install license file to all independently installable packages

* Tue Nov 06 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.5.1-2
- Move themes into a separate noarch sub-package
- Make doc sub-package noarch

* Mon Nov 05 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1
- Run tests
- Remove upstreamed patch
- Add missing BR: doxygen
- Add missing BR: graphviz

* Tue Oct 24 2017 Till Hofmann <thofmann@fedoraproject.org> - 1.4.2-1
- Initial package
