Name:    lite-xl
Version: 2.1.7

Release: %autorelease

%forgemeta

Summary: A lightweight text editor written in Lua, adapted from lite
License: MIT and OFL
URL:     https://lite-xl.com/
Source:  https://github.com/lite-xl/lite-xl/archive/refs/tags/v%{version}.tar.gz
# https://github.com/lite-xl/lite-xl/issues/2014
Patch:   000-stdlib.patch

BuildRequires: gcc
BuildRequires: meson
BuildRequires: (pkgconfig(lua) >= 5.4 with pkgconfig(lua) < 5.5)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(sdl2)
BuildRequires: desktop-file-utils

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
A lightweight, simple, fast, feature-filled, and extremely
extensible text editor written in C, and Lua, adapted from lite.
Lite XL is derived from lite. It is a lightweight text editor
written mostly in Lua — it aims to provide something practical,
pretty, small and fast easy to modify and extend, or to use
without doing either.
The aim of Lite XL compared to lite is to be more user friendly, 
improve the quality of font rendering, and reduce CPU usage.

%prep
# %forgesetup 
%autosetup -n lite-xl-%{version} -p1

%build
%meson -Darch_tuple=%{_arch}-linux -Duse_system_lua=true
%meson_build

%install
%meson_install

%check
%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/org.lite_xl.lite_xl.desktop

%files
%license LICENSE
%license %{_docdir}/%{name}/licenses.md
%doc README.md changelog.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor
%{_datadir}/applications/org.lite_xl.lite_xl.desktop
%{_datadir}/metainfo/org.lite_xl.lite_xl.appdata.xml

%changelog
%autochangelog
