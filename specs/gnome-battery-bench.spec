Name:           gnome-battery-bench
Version:        3.15.4
Release:        25%{?dist}
Summary:        Measure power usage in defined scenarios

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://git.gnome.org/browse/%{name}
Source0:        https://download.gnome.org/sources/%{name}/3.15/%{name}-%{version}.tar.xz

Patch0:         wayland-no-shortcut.patch

BuildRequires:  gcc
BuildRequires: asciidoc
BuildRequires: desktop-file-utils
BuildRequires: xmlto
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xtst)
BuildRequires: make

%description
This application is designed for measuring power usage. It does it by
recording the reported battery statistics as it replays recorded event
logs, and then using that to estimate power consumption and total
battery lifetime.

%prep
%setup -q
%patch -P0  -p1

%build
%configure
make %{?_smp_mflags}


%install
%make_install

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.BatteryBench.desktop

%files
%doc README
%license COPYING
%{_bindir}/%{name}
%{_bindir}/gbb
%{_datadir}/%{name}
%{_datadir}/applications/org.gnome.BatteryBench.desktop
%{_datadir}/dbus-1/services/org.gnome.BatteryBench.service
%{_datadir}/dbus-1/system-services/org.gnome.BatteryBench.Helper.service
%{_datadir}/polkit-1/actions/org.gnome.BatteryBench.Helper.policy
%{_libexecdir}/gnome-battery-bench-helper
%{_mandir}/man1/gbb.1*
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.gnome.BatteryBench.Helper.conf

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.15.4-24
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar  9 2017 Christian Kellner <ckellner@redhat.com> - 3.15.4-5
- Add fix to not crash on wayland when a test is started (rhbz#1276566)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 12 2015 Owen Taylor <otaylor@localhost.localdomain> - 3.15.4-1
- Fix RPM style issues (From review by Florian Lehner)

* Mon Feb 9 2015 Owen Taylor <otaylor@redhat.com> - 3.15.4-0.1
- Fix mixed use of $RPM_BUILD_ROOT and %%{buildroot} (From review by
  Florian Lehner)

* Thu Jan 29 2015 Owen Taylor <otaylor@redhat.com> - 3.15.4-0
- Initial spec version
