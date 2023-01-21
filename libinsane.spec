Name:           libinsane
Version:        1.0.9
Release:        7%{?dist}
Summary:        Cross-platform access to image scanners

License:        LGPLv3+
URL:            https://doc.openpaper.work/libinsane/latest/
Source0:        https://gitlab.gnome.org/World/OpenPaperwork/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(sane-backends)
BuildRequires:  doxygen
BuildRequires:  pkgconfig(cunit)
BuildRequires:  valgrind

%description
Libinsane is the library to access scanners on both Linux and Windows. It's
cross-platform, cross-programming languages, cross-scanners :-). It takes care
of all the quirks of all the platforms and scanners.


%package devel
Summary:        Development files for libinsane

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and header files for libinsane.


%package gobject
Summary:        GObject access to image scanners

BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gobject
Libinsane is the library to access scanners on both Linux and Windows. It's
cross-platform, cross-programming languages, cross-scanners :-). It takes care
of all the quirks of all the platforms and scanners.

This package provides GObject wrappers around the main library.


%package gobject-devel
Summary:        Development files for libinsane-gobject

Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-gobject%{?_isa} = %{version}-%{release}

%description gobject-devel
Development libraries and header files for libinsane-gobject.


%package vala
Summary:        Vala bindings for libinsane

BuildArch:      noarch

BuildRequires:  vala

Requires:       %{name}-gobject-devel = %{version}-%{release}

%description vala
Vala bindings for libinsane.


%prep
%autosetup -p1


%build
%meson
%meson_build
%meson_build doc


%install
%meson_install


%check
%meson_test -v -t 10


%files
%doc README.markdown ChangeLog
%license LICENSE
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.1.*

%files devel
%doc doc
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files gobject
%{_libdir}/%{name}_gobject.so.1
%{_libdir}/%{name}_gobject.so.1.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Libinsane-1.0.typelib

%files gobject-devel
%{_includedir}/%{name}-gobject
%{_libdir}/%{name}_gobject.so
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Libinsane-1.0.gir
%{_datadir}/gtk-doc

%files vala
%{_datadir}/vala/vapi/%{name}.deps
%{_datadir}/vala/vapi/%{name}.vapi


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.9-6
- Drop support for i686

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.9-1
- Update to latest version (#1911915)

* Sat Oct 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.8-1
- Update to latest version (#1886948)

* Tue Sep 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.7-1
- Update to latest version (#1873874)

* Mon Aug 31 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.6-1
- Update to latest version (#1873874)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 17 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.4-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-1
- Update to latest version

* Wed Oct 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.2-1
- Update to latest version

* Sat Aug 24 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-1
- Update to latest version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0-1
- Initial release
