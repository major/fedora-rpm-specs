Name:           libipuz
Version:        0.3.0
Release:        %autorelease
Summary:        Library for parsing .ipuz puzzle files

License:        LGPL-2.1-or-later AND LGPL-3.0-or-later AND GPL-3.0-or-later
URL:            https://gitlab.gnome.org/jrb/libipuz
Source:         %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  python3

BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel

%description
This is a library for parsing .ipuz puzzle files, for crossword puzzles,
sudokus, etc. The library only handles crosswords for now.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tests
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tests
The %{name}-tests package contains tests for %{name}.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md TODO.md
%{_libdir}/lib%{name}-0.1.so

%files devel
%doc docs/*.md
%{_includedir}/*
%{_libdir}/pkgconfig/%{name}-0.1.pc

%files tests
%dir %{_datadir}/installed-tests
%{_datadir}/installed-tests/%{name}-1.0
%dir %{_libexecdir}/installed-tests
%{_libexecdir}/installed-tests/%{name}-1.0

%changelog
%autochangelog
