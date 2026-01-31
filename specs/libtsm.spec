Name:           libtsm
Version:        4.4.2
Release:        1%{?dist}
Summary:        DEC-VT terminal emulator state machine
License:        MIT AND LGPL-2.1-or-later
URL:            https://github.com/kmscon/libtsm
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(check)

%description
TSM is a state machine for DEC VT100-VT520 compatible terminal
emulators. It can be used to implement terminal emulators, or other
applications that need to interpret terminal escape sequences. The
library does no rendering or window management of its own, and does
not depend on a graphics stack, unlike the similar GNOME libvte.

%package devel
Summary:        Development files for the DEC-VT terminal state machine library
License:        LGPL-2.1-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
TSM is a state machine for DEC VT100-VT520 compatible terminal
emulators. It can be used to implement terminal emulators, or other
applications that need to interpret terminal escape sequences. The
library does no rendering or window management of its own, and does
not depend on a graphics stack, unlike the similar GNOME libvte.

This package contains the development headers for the library found
in %{name}.

%prep
%autosetup -p1

%conf
%meson

%build
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING LICENSE_htable
%{_libdir}/libtsm.so.4{,.*}

%files devel
%doc README.md
%{_includedir}/libtsm.h
%{_libdir}/libtsm.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Jan 29 2026  Jocelyn Falempe <jfalempe@redhat.com> - 4.4.2-1
- Update to 4.4.2

* Thu Jan 22 2026  Jocelyn Falempe <jfalempe@redhat.com> - 4.4.1-1
- Update to 4.4.1

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Nov 14 2025 Jocelyn Falempe <jfalempe@redhat.com> - 4.3.0-1
- Update to 4.3.0, and switch to meson

* Wed Jul 2 2025 Jocelyn Falempe <jfalempe@redhat.com> - 4.1.0
- Update to 4.1.0, and clean the spec file

* Fri Dec 13 2024 Jocelyn Falempe <jfalempe@redhat.com> - 4.0.2^1.git69922bde-0
- Update to the upstream develop branch, which hasn't seen a release yet.

* Sun Jun 09 2024 Michael Bryant <shadow53@shadow53.com> - 4.0.2-0
- Update to 4.0.2

* Sun Nov 22 2020 Michael Bryant <shadow53@shadow53.com> - 4.0.1-2
- Add personal patch to add nord color scheme support

* Sun Jan 19 2020 Michael Bryant <shadow53@shadow53.com> - 4.0.1-1
- Switch to Aetf's fork, latest release

* Wed Jul 18 2018 Fabian Vogt <fvogt@suse.com>
- Switch to version 4.0.0 from https://github.com/Aetf/libtsm:
  * Add soft-black and base16-light and -dark color palettes
  * Support underline/italic rendering (with a patched version of kmscon)
  * Support 24-bit true color
  * Support Ctrl + Arrow keys
  * Support custom title using OSC
  * Bug fixes:
    + Repsonse to 'CSI c' contains random bytes
    + Fix invalid cpr values
- Run make check in %%check
- Add patch to fix make check:
  * 0001-Fix-filename-in-test_common.h.patch
- Add patch to add palette with default linux console colors:
  * 0001-Add-new-palette-with-standard-VGA-colors.patch

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Aug  3 2014 Jan Engelhardt <jengelh@inai.de>
- Initial package (version 3) for build.opensuse.org

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 01 2013 Christopher Meng <rpm@cicku.me> - 3-1
- Initial Package.
