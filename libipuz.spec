%bcond_without docs

Name:           libipuz
Version:        0.4.1
Release:        %autorelease
Summary:        Library for parsing .ipuz puzzle files

License:        LGPL-2.1-or-later AND LGPL-3.0-or-later AND GPL-3.0-or-later
URL:            https://gitlab.gnome.org/jrb/libipuz
Source:         %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  python3
%if %{with docs}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(myst-parser)
%endif

BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel

%description
This is a library for parsing .ipuz puzzle files, for crossword puzzles,
sudokus, etc. The library only handles crosswords for now.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if %{with docs}
Suggests:       %{name}-doc = %{version}-%{release}
%endif

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with docs}
%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains additional documentation for %{name}.
%endif

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

%if %{with docs}
sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md NEWS.md TODO.md
%{_libdir}/lib%{name}-0.4.so

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/%{name}-0.4.pc

%if %{with docs}
%files doc
%license COPYING
%doc html
%endif

%files tests
%dir %{_datadir}/installed-tests
%{_datadir}/installed-tests/%{name}-1.0
%dir %{_libexecdir}/installed-tests
%{_libexecdir}/installed-tests/%{name}-1.0

%changelog
%autochangelog
