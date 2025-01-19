Summary:	GLib Ncurses Toolkit
Name:		libgnt
Version:	2.14.1
Release:	12%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://keep.imfreedom.org/libgnt/libgnt/
BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	gobject-introspection
BuildRequires:	gtk-doc
BuildRequires:	glib2-devel
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRequires:	python3-devel
BuildRequires:	gnupg2
Source0:	https://sourceforge.net/projects/pidgin/files/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:	https://sourceforge.net/projects/pidgin/files/%{name}-%{version}.tar.xz.asc
# https://issues.imfreedom.org/issue/LIBGNT-10
Source2:	libgnt-maintainers-keyring.asc
# https://keep.imfreedom.org/libgnt/libgnt/rev/2da723f790d6
Patch0:		libgnt-2.14.1-gcc-14-fix.patch

%description
GNT is an ncurses toolkit for creating text-mode graphical user interfaces
in a fast and easy way. It is based on GLib and ncurses.

%package devel
Summary:	Developmentfiles for libgnt
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libgnt.

%package doc
Summary:	Documentation for libgnt

%description doc
Documentation files for libgnt.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_libdir}/libgnt.so.*
%{_libdir}/gnt

%files devel
%{_libdir}/libgnt.so
%{_libdir}/pkgconfig/gnt.pc
%{_includedir}/gnt

%files doc
%{_datadir}/gtk-doc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.14.1-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 2.14.1-9
- FTBFS fix (gcc-14)
  Resolves: rhbz#2261323

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb  8 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 2.14.1-1
- New version
  Resolves: rhbz#1925383

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.14.0-2
- Fixed according to the review

* Thu Jul 16 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.14.0-1
- Initial package
