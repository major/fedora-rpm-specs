%global optflags %{optflags} -flto=auto
%global build_ldflags %{build_ldflags} -flto

Name:           sakura
Version:        3.8.9
Release:        %autorelease
Summary:        Terminal emulator based on GTK and VTE

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://launchpad.net/sakura
Source0:        https://launchpad.net/sakura/trunk/%{version}/+download/sakura-%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(glib-2.0) >= 2.20
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  vte291-devel
BuildRequires:  cmake desktop-file-utils gettext /usr/bin/pod2man
BuildRequires:  pcre2-devel

%description
Sakura is a terminal emulator based on GTK and VTE. It's a terminal emulator 
with few dependencies, so you don't need a full GNOME desktop installed to 
have a decent terminal emulator.


%prep
%autosetup

%build
find . -type f -name CMakeCache.txt -exec rm -rf {} \;
%cmake -DCMAKE_AR=/usr/bin/gcc-ar -DCMAKE_RANLIB=/usr/bin/gcc-ranlib \
       -DCMAKE_NM=/usr/bin/gcc-nm CMAKE_C_FLAGS="%{optflags}" -Wno-dev
%cmake_build


%install
%cmake_install
desktop-file-install \
  --delete-original \
  --remove-category=Utility \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
# location of the docs is hardcoded, so we remove them
rm -rf %{buildroot}%{_datadir}/doc/


%check
ctest .


%files -f %{name}.lang
%doc AUTHORS README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/terminal-tango.svg
%{_mandir}/man1/%{name}.1.*


%changelog
%autochangelog
