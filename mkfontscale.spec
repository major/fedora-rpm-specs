Name:       mkfontscale
Version:    1.2.2
Release:    2%{?dist}
Summary:    Tool to generate legacy X11 font system index files

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

Patch0:     mkfontscale-examine-all-encodings.patch

BuildRequires:  gcc make libtool
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  zlib-devel

Conflicts:  xorg-x11-font-utils < 7.5-51

# Used to be a separate upstream repo in xorg-x11-font-utils, now it's part
# of mkfontscale. Keep the Provides alive though.
Provides:   mkfontdir = %{version}

%description
mkfontscale creates the fonts.scale and fonts.dir index files used by the
legacy X11 font system.  It now includes the mkfontdir script previously
distributed separately for compatibility with older X11 versions.

%prep
%autosetup

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/mkfontdir
%{_bindir}/mkfontscale
%{_mandir}/man1/mkfontdir.1*
%{_mandir}/man1/mkfontscale.1*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 04 2022 Peter Hutterer <peter.hutterer@redhat.com> - 1.2.2-1
- mkfontscale 1.2.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.2.1-2
- Fix the Conflicts line to properly conflict with the -50 font-utils,
  without a {?dist} <= doesn't work as expected.

* Thu Feb 25 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.2.1-1
- Split mkfontscale/mkfontdir out from xorg-x11-font-utils into its own
  package (#1932734)
