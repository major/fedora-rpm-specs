Name:		squeekboard
Version:	1.22.0
Release:	3%{?dist}
Summary:	a Wayland virtual keyboard

License:	GPLv3+
URL:		https://gitlab.gnome.org/World/Phosh/squeekboard
Source0:	https://gitlab.gnome.org/World/Phosh/squeekboard/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:	squeekboard.desktop
Source2:	Cargo.toml

# temporary until upstreamed
Patch0: 0001-use-latest-compatible-crates.patch

ExclusiveArch:	%{rust_arches}

# Temporary. Breaks on ppc64le
ExcludeArch:	ppc64le

# s390x is having build problems
# https://koji.fedoraproject.org/koji/taskinfo?taskID=55048351
# https://bugzilla.redhat.com/show_bug.cgi?id=1897522
ExcludeArch:	s390x

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:	rust-packaging
BuildRequires:	pkgconfig(gio-2.0) >= 2.26
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0) >= 3.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:	pkgconfig(wayland-client) >= 1.14
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(wayland-protocols) >= 1.12
BuildRequires:	pkgconfig(libfeedback-0.0)
BuildRequires:	pkgconfig(libbsd)
BuildRequires:	desktop-file-utils

%description
Squeekboard is a virtual keyboard supporting Wayland, built primarily
for the Librem 5 phone. It squeaks because some Rust got inside.

%prep
%autosetup -p1 -n %{name}-v%{version}
%cargo_prep

# We need the old Cargo.toml for the rust build to work
cp %{SOURCE2} .
rm -f Cargo.lock
%generate_buildrequires
%cargo_generate_buildrequires -a

%build
# ensure standard Rust compiler flags are set
export RUSTFLAGS="%build_rustflags"
%meson -Dnewer=true
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart/
cp %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/autostart/
chmod +x %{buildroot}%{_bindir}/squeekboard-entry

cp tools/squeekboard-restyled %{buildroot}%{_bindir}
chmod +x %{buildroot}%{_bindir}/squeekboard-restyled

%find_lang %{name}

%check
# ensure standard Rust compiler flags are set
export RUSTFLAGS="%build_rustflags"
%meson_test
desktop-file-validate %{buildroot}/%{_datadir}/applications/sm.puri.Squeekboard.desktop

%files -f %{name}.lang
%{_bindir}/squeekboard
%{_bindir}/squeekboard-entry
%{_bindir}/squeekboard-test-layout
%{_bindir}/squeekboard-restyled
%{_datadir}/applications/sm.puri.Squeekboard.desktop
%{_sysconfdir}/xdg/autostart/squeekboard.desktop
%doc README.md
%license COPYING

%changelog
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

%autochangelog

* Sun Feb 05 2023 Fabio Valentini <decathorpe@gmail.com> - 1.20.0-3
- Ensure standard Rust compiler flags are set.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 11 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.20.0-1
- Update to 1.20.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Kalev Lember <klember@redhat.com> - 1.19.0-2
- Rebuilt for libgnome-desktop soname bump

* Mon Jul 18 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.19.0-1
- Update to 1.19.0

* Thu Jun 02 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.18.0-1
- Update to 1.18.0

* Fri Jan 28 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.16.0-2
- Patch not starting bug

* Tue Jan 25 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.16.0-1
- Update to 1.16.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.14.0-1
- Update to 1.14.0

* Thu Apr 15 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.13.0-1
- Update to 1.13.0

* Thu Feb 18 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.12.0-3
- Bump version for rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.12.0-1
- Update to 1.12.0

* Mon Nov 23 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.11.1-1
- Update to 1.11.1

* Sat Nov 14 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0

* Fri Oct 23 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.10.0-1
- Update to 1.10.0

* Sun Aug 09 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.9.3-1
- Update to 1.9.3 including new dependencies and new patch file and Cargo.toml

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Josh Stone <jistone@redhat.com> - 1.9.2-2
- Bump to cairo 0.9 and gtk 0.9

* Fri Jun 19 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.9.2-1
- Update to 1.9.2, including updated patch file.
- Remove unused libcroco
- Temporarily excluding ppc64le architecture 

* Tue Mar 24 2020 Nikhil Jha <hi@nikhiljha.com> - 1.9.1-1
- Update to 1.9.1

* Tue Mar 24 2020 Nikhil Jha <hi@nikhiljha.com> - 1.9.0-2
- Validate desktop file

* Thu Feb 27 2020 Nikhil Jha <hi@nikhiljha.com> - 1.9.0-1
- Initial packaging
