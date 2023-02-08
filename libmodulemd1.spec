Name:           libmodulemd1
Version:        1.8.16
Release:        9%{?dist}
Summary:        Module metadata manipulation library

License:        MIT
URL:            https://github.com/fedora-modularity/libmodulemd
Source0:        %{url}/releases/download/libmodulemd-%{version}/modulemd-%{version}.tar.xz

BuildRequires:  meson >= 0.47
BuildRequires:  pkgconfig
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glib2-doc
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-gobject-base

Obsoletes: libmodulemd < 1.8.15
Provides: libmodulemd = %{version}-%{release}
Provides: libmodulemd%{?_isa} = %{version}-%{release}

# Patches


%description
C Library for manipulating module metadata files.
See https://github.com/fedora-modularity/libmodulemd/blob/master/README.md for
more details.


%package -n python%{python3_pkgversion}-%{name}
Summary: Python 3.6 bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python%{python3_pkgversion}-gobject-base
Obsoletes: python3-modulemd < 1.3.4
Obsoletes: python2-%{name} < 1.8.15-3

%description -n python%{python3_pkgversion}-%{name}
Python 3 bindings for %{name}


%package devel
Summary:        Development files for libmodulemd
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      libmodulemd-devel

%description devel
Development files for libmodulemd.


%prep
%autosetup -p1 -n modulemd-%{version}


%build
%meson -Ddeveloper_build=false
%meson_build


%check
export LC_CTYPE=C.utf8
# causes test failures on multiple arches, but this is just a compat version
export MMD_SKIP_VALGRIND=1
%meson_test


%install
%meson_install


%files
%license COPYING
%doc README.md
%{_bindir}/modulemd-validator-v1
%{_libdir}/libmodulemd.so.1*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Modulemd-1.0.typelib


%files devel
%{_libdir}/libmodulemd.so
%{_libdir}/pkgconfig/modulemd.pc
%{_includedir}/modulemd/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Modulemd-1.0.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/modulemd-1.0/


%files -n python%{python3_pkgversion}-%{name}


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Stephen Gallagher <sgallagh@redhat.com> - 1.8.16-1
- Improve the merge logic to handle third-party repos more sanely

* Tue Jul 30 2019 Stephen Gallagher <sgallagh@redhat.com> - 1.8.15-3
- Drop python2 subpackage

* Thu Jul 25 2019 Stephen Gallagher <sgallagh@redhat.com> - 1.8.15-2
- Fix Obsoletes

* Wed Jul 24 2019 Stephen Gallagher <sgallagh@redhat.com> - 1.8.15-1
- First separate release of libmodulemd1

