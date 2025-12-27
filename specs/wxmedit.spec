%global forgeurl https://github.com/wxMEdit/wxMEdit
Version:        3.2
%global date 20251010
%global commit 18d14b12bf5f2a17d9e46f8450789d3ef56bfa70
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%forgemeta

Name:           wxmedit
Release:        %autorelease
Summary:        a Cross-platform Text/Hex Editor, an improved version of MadEdit
License:        GPL-3.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  libicu-devel
BuildRequires:  wxGTK-devel
BuildRequires:  libcurl-devel

BuildRequires:  desktop-file-utils

%description
wxMEdit is a cross-platform Text/Hex Editor written in C++ & wxWidgets.
wxMEdit is an improved version of MadEdit which has been discontinued.
wxMEdit supports many useful functions, e.g. Bookmark, Syntax Highlightings,
Word Wraps, Encodings, Column/Hex Modes, Updates checking.
In HexMode, wxMEdit can open large files which size is up to 32GB (INT_MAX*16).

%prep
%forgeautosetup -p1

%build
%configure
%make_build

%install
%make_install

rm -r %{buildroot}%{_datadir}/doc/wxmedit

%find_lang %{name}

%check
make check || (cat ./test-suite.log && exit 1)

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%license LICENSE
%doc README.txt
%{_bindir}/wxmedit
%{_datadir}/applications/wxmedit.desktop
%{_datadir}/icons/hicolor/*/apps/wxmedit.png
%{_datadir}/icons/hicolor/scalable/apps/wxmedit.svg
%{_datadir}/pixmaps/wxmedit_*.xpm
%dir %{_datadir}/wxmedit
%{_datadir}/wxmedit/syntax/

%changelog
%autochangelog
