%bcond docs 1
%bcond introspection 1

# The shared library version
%global soversion 0.5

Name:           libipuz
Version:        0.5.1
Release:        %autorelease
Summary:        Library for parsing .ipuz puzzle files

License:        LGPL-2.1-or-later OR MIT
URL:            https://gitlab.gnome.org/jrb/libipuz
Source:         %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  python3
BuildRequires:  sed
%if %{with docs}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(myst-parser)
%endif

BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel
%if %{with introspection}
BuildRequires:  gi-docgen
BuildRequires:  gobject-introspection-devel
%endif

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
%autosetup -p1
%cargo_prep

# Drop version locks
rm libipuz/rust/Cargo.lock
sed -i '/Cargo.lock/d' libipuz/rust/meson.build

%generate_buildrequires
cd libipuz/rust
%cargo_generate_buildrequires

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
%license LICENSE COPYING.LGPL COPYING.MIT
%doc README.md NEWS.md
%{_libdir}/lib%{name}-%{soversion}.so

%files devel
%{_includedir}/*
%if %{with introspection}
%{_datadir}/gir-1.0/Ipuz-1.0.gir
%{_libdir}/girepository-1.0/Ipuz-1.0.typelib
%endif
%{_libdir}/pkgconfig/%{name}-%{soversion}.pc

%if %{with docs}
%files doc
%license LICENSE COPYING.LGPL COPYING.MIT
%doc html
%if %{with introspection}
%doc %{_docdir}/%{name}-1.0/
%endif
%endif

%files tests
%dir %{_datadir}/installed-tests
%{_datadir}/installed-tests/%{name}-1.0
%dir %{_libexecdir}/installed-tests
%{_libexecdir}/installed-tests/%{name}-1.0

%changelog
%autochangelog
