%global abi_ver 4

Name:           fcft
Version:        3.1.10
Release:        1%{?dist}
Summary:        Simple library for font loading and glyph rasterization

# main source:  MIT
# unicode/*:    Unicode-3.0
# nanosvg:      Zlib
License:        MIT AND Unicode-3.0 AND Zlib
URL:            https://codeberg.org/dnkl/%{name}
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.sig
# Daniel Eklöf (Git signing) <daniel@ekloef.se>
Source2:        gpgkey-5BBD4992C116573F.asc

Patch:          %{url}/commit/9922e00843.patch#/fcft-3.1.10-unicode-update-license.patch

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.58.0

BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(tllist)
# require *-static for header-only library
BuildRequires:  tllist-static
# test dependencies: 'Serif' and 'emoji' fonts
BuildRequires:  font(dejavuserif)
BuildRequires:  font(notocoloremoji)

Provides:       bundled(nanosvg) = 0^20231229g93ce879

%description
fcft is a small font loading and glyph rasterization library built
on top of FontConfig, FreeType2 and pixman.
It can load and cache fonts from a fontconfig-formatted name string,
e.g. Monospace:size=12, optionally with user configured fallback fonts.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
cp 3rd-party/nanosvg/LICENSE.txt LICENSE.nanosvg
cp unicode/license.txt LICENSE.Unicode


%build
%meson \
    -Dtest-text-shaping=true
%meson_build


%install
%meson_install
# license will be installed to the correct location with rpm macros
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE


%check
%meson_test


%files
%license LICENSE
%license LICENSE.nanosvg
%license LICENSE.Unicode
%{_libdir}/lib%{name}.so.%{abi_ver}{,.*}
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/CHANGELOG.md
%{_docdir}/%{name}/README.md

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/%{name}*.3*


%changelog
* Thu Jan 02 2025 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.1.10-1
- Update to 3.1.10 (#2335230)

* Thu Oct 24 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.1.9-1
- Update to 3.1.9 (#2321265)
- Verify source signature

* Tue Oct 08 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.1.8-3
- Rebuilt for utf8proc 2.9.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 26 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.1.8-1
- Update to 3.1.8

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 16 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.1.7-1
- Update to 3.1.7 (#2254699)
- Convert License tag to SPDX

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.1.6-1
- Update to 3.1.6 (#2222888)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.1.5-1
- Update to 3.1.5 (#2128499)

* Tue Sep 06 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.1.4-1
- Update to 3.1.4 (#2124656)

* Wed Aug 24 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.1.3-1
- Update to 3.1.3 (#2120308)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 20 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.1.2-1
- Update to 3.1.2 (#2088509)

* Sun May 01 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1 (#2080746)

* Sat Feb 05 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1 (#2050997)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 08 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1 (#2030410)

* Sat Nov 13 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0 (#2022959)
- Enable text shaping tests

* Sun Oct 24 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.4.6-1
- Update to 2.4.6 (#2016766)

* Sun Aug 15 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.4.5-1
- Update to 2.4.5

* Wed Jul 28 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.4.4-1
- Update to 2.4.4

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 18 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.4.3-1
- Update to 2.4.3

* Thu Jul 08 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.4.2-1
- Update to 2.4.2

* Fri Jun 25 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1

* Wed Apr 14 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.3.3-1
- Update to 2.3.3

* Mon Mar 08 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.3.2-3
- Rebuild for tllist 1.0.5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 23 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.3.2-1
- Initial import (#1912855)
