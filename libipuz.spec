%bcond docs 1

Name:           libipuz
Version:        0.4.5
Release:        %autorelease
Summary:        Library for parsing .ipuz puzzle files

License:        LGPL-2.1-or-later OR MIT
URL:            https://gitlab.gnome.org/jrb/libipuz
Source:         %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

# Ensure we only enable rust support from 0.4.6 onwards
%bcond rust %([ $(echo %{version} | tr -d .) -ge 046 ] && echo 1 || echo 0)

%if %{with rust}
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  sed
%endif
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
%autosetup -p1

%if %{with rust}
%cargo_prep

# Drop version locks
rm libipuz/rust/Cargo.lock
sed -i '/Cargo.lock/d' libipuz/rust/meson.build

%generate_buildrequires
cd libipuz/rust
%cargo_generate_buildrequires
%endif

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
%{_libdir}/lib%{name}-0.4.so

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/%{name}-0.4.pc

%if %{with docs}
%files doc
%license LICENSE COPYING.LGPL COPYING.MIT
%doc html
%endif

%files tests
%dir %{_datadir}/installed-tests
%{_datadir}/installed-tests/%{name}-1.0
%dir %{_libexecdir}/installed-tests
%{_libexecdir}/installed-tests/%{name}-1.0

%changelog
%autochangelog
