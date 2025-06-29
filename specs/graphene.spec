Name:           graphene
Version:        1.10.8
Release:        1%{?dist}
Summary:        Thin layer of types for graphic libraries

License:        MIT
URL:            https://github.com/ebassi/graphene
Source:         %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
# https://github.com/ebassi/graphene/issues/246
Patch:          graphene-1.10.8-no-fast-math.patch

BuildRequires:  gcc
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.50.1
BuildRequires:  pkgconfig(gobject-2.0) >= 2.30.0

%description
Graphene provides a small set of mathematical types needed to implement graphic
libraries that deal with 2D and 3D transformations and projections.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tests
Summary:        Tests for the %{name} package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
%autosetup -p1

%build
# Disable neon
# https://github.com/ebassi/graphene/issues/215
%meson -Dgtk_doc=true \
%ifarch %{arm}
  -Darm_neon=false \
%endif

%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/girepository-1.0/
%{_libdir}/libgraphene-1.0.so.0*

%files devel
%{_includedir}/graphene-1.0/
%dir %{_libdir}/graphene-1.0
%{_libdir}/graphene-1.0/include/
%{_libdir}/libgraphene-1.0.so
%{_libdir}/pkgconfig/graphene-1.0.pc
%{_libdir}/pkgconfig/graphene-gobject-1.0.pc
%{_datadir}/gir-1.0/
%{_datadir}/gtk-doc/

%files tests
%{_libexecdir}/installed-tests/
%{_datadir}/installed-tests/

%changelog
%autochangelog
