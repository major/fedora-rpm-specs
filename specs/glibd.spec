Name:           glibd
Version:        2.4.3
Release:        5%{?dist}
Summary:        D bindings for the GLib C Utility Library

License:        LGPL-3.0-or-later
URL:            https://github.com/gtkd-developers/GlibD
Source0:        %{url}/archive/v%{version}/GlibD-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  ldc
# Cf. rhbz#1813529
BuildRequires:  meson > 0.53.2-1

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  gir-to-d >= 0.23.2

ExclusiveArch:  %{ldc_arches}

%description
%{summary}.


%package devel
Summary:        Development files for using %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the development files for building
applications that use %{name}.

%prep
%autosetup -n GlibD-%{version} -p1

# Fix version in meson.build
sed -e "s/    version: '.*'/    version: '%{version}'/" -i meson.build

%build
# Drop '-specs=/usr/lib/rpm/redhat/redhat-hardened-ld' as LDC doesn't support it
export LDFLAGS="-Wl,-z,relro"
# Export DFLAGS
export DFLAGS="%{_d_optflags}"
%meson
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc AUTHORS README.md
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_d_includedir}/glibd-2/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Kalev Lember <klember@redhat.com> - 2.4.3-4
- Rebuilt for ldc 1.40

* Tue Aug 06 2024 Kalev Lember <klember@redhat.com> - 2.4.3-3
- Rebuilt for ldc 1.39

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 14 2024 Neal Gompa <ngompa@fedoraproject.org> - 2.4.3-1
- Rebase to 2.4.3

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Kalev Lember <klember@redhat.com> - 2.3.0-10
- Rebuilt for ldc 1.32

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 27 2022 Kalev Lember <klember@redhat.com> - 2.3.0-8
- Rebuilt for ldc 1.30

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 16 2022 Neal Gompa <ngompa@fedoraproject.org> - 2.3.0-6
- Add fixes from upstream to fix FTBFS with glib2 2.72 (#2045439)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 17 2021 Kalev Lember <klember@redhat.com> - 2.3.0-4
- Rebuilt for ldc 1.27

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Apr 03 2021 Neal Gompa <ngompa13@gmail.com> - 2.3.0-2
- Add fixes from upstream to fix FTBFS with glib2 2.68 (#1923462)

* Sun Feb 28 2021 Neal Gompa <ngompa13@gmail.com> - 2.3.0-1
- Update to 2.3.0 to fix FTBFS (#1923462)

* Mon Feb 22 2021 Kalev Lember <klember@redhat.com> - 2.2.0-3
- Rebuilt for ldc 1.25

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 21 2020 Neal Gompa <ngompa13@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 19 2020 Neal Gompa <ngompa13@gmail.com> - 2.1.0-5
- Drop backported fix that has been reverted upstream due to glib2 changes
- Rebuild against Meson 0.53.2 snapshot to fix glibd build

* Mon Mar 02 2020 Neal Gompa <ngompa13@gmail.com> - 2.1.0-4
- Backport fix from upstream to work with glib2 >= 2.64

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Neal Gompa <ngompa13@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Mon Feb 18 2019 Kalev Lember <klember@redhat.com> - 2.0.2-2
- Rebuilt for ldc 1.14

* Fri Feb 01 2019 Neal Gompa <ngompa13@gmail.com> - 2.0.2-1
- Initial packaging for Fedora
