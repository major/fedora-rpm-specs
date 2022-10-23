%global _build_id_links none
%global __requires_exclude ^libjabber\\.so.*$
%global libgd_commit c7c7ff4e05d3fe82854219091cf116cce6b19de0
%global libcmatrix_commit 13bdda3e2b6ef4747feeccbb0a9ddcfafb63f898

Name: chatty
Version: 0.7.0~rc1
Release: 0%{?dist}
Summary: A libpurple messaging client

License: GPLv3+
URL: https://source.puri.sm/Librem5/chatty
Source0: https://source.puri.sm/Librem5/%{name}/-/archive/v0.7.0_rc1/%{name}-v0.7.0_rc1.tar.gz
Source1: https://gitlab.gnome.org/GNOME/libgd/-/archive/%{libgd_commit}/libgd-%{libgd_commit}.tar.gz
Source2: https://source.puri.sm/Librem5/libcmatrix/-/archive/%{libcmatrix_commit}/libcmatrix-%{libcmatrix_commit}.tar.gz

# Chatty links against a libpurple private library (libjabber).
# Obviously, Fedora build tooling doesn't support that, so we have to use
# some kind of workaround. This seemed simplest.
# We do not want to provide a private library, which is from another
# project, to be used in other packages.
Patch0:  0001-hacky-hack.patch

# Temporary. Test failure on ppc64le
ExcludeArch:	ppc64le

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:	itstool
BuildRequires:  pkgconfig(libebook-contacts-1.2)
BuildRequires:  pkgconfig(libebook-1.2) >= 3.42.0
BuildRequires:  pkgconfig(libfeedback-0.0)
BuildRequires:  pkgconfig(libhandy-1) >= 1.1.90
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(purple)
BuildRequires:  pkgconfig(sqlite3) >= 3.26.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(mm-glib) >= 1.12.0
BuildRequires:	gspell-devel
BuildRequires:  libolm-devel
BuildRequires:	openssl1.1-devel
BuildRequires:  libphonenumber-devel
BuildRequires:  protobuf-devel
BuildRequires:  libsecret-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  /usr/bin/xauth

Requires: hicolor-icon-theme

# Those packages may be dynamically loaded, but they depend on libsoup-2.4
# libsoup-2.4 and libsoup-3.0 can't exist in the same process
# Better to create a conflict, so user doesn't get a hard to debug error
Conflicts: purple-chime <= 1.4.1
Conflicts: purple-sipe <= 1.25.0

%description
Chatty is a libpurple based messaging client for mobile phones,
works best with the phosh mobile DE.

%prep

# Copy private libjabber library in so we can build against it
cp `pkg-config --variable=plugindir purple`/libjabber.so.0 /tmp/libjabber.so

%setup -a1 -a2 -n %{name}-v0.7.0_rc1
%patch0 -p1

rm -rf subprojects/libcmatrix
mv libcmatrix-%{libcmatrix_commit} subprojects/libcmatrix

rmdir subprojects/libgd
mv libgd-%{libgd_commit} subprojects/libgd

%build
%meson
%meson_build

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/sm.puri.Chatty.metainfo.xml

desktop-file-validate %{buildroot}/%{_datadir}/applications/sm.puri.Chatty.desktop

# the upstream meson tests already validate the desktop file
# and the appstream file

LC_ALL=C.UTF-8 xvfb-run sh <<'SH'
%meson_test -t 2
SH

%install
%meson_install

# Adding libjabber to link against
mkdir -p %{buildroot}%{_libdir}
cp `pkg-config --variable=plugindir purple`/libjabber.so.0 %{buildroot}%{_libdir}

# Adding ld.so.conf.d in order to use the libjabber at runtime
mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/chatty" > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/chatty.conf

%find_lang purism-chatty

# The mesa vulkan bug breaks tests
# https://bugzilla.redhat.com/show_bug.cgi?id=1911130

%files -f purism-chatty.lang
%{_bindir}/chatty
%{_sysconfdir}/xdg/autostart/sm.puri.Chatty-daemon.desktop
%{_datadir}/glib-2.0/schemas/sm.puri.Chatty.gschema.xml
%{_datadir}/applications/sm.puri.Chatty.desktop
%{_datadir}/icons/hicolor/*/apps/sm.puri.Chatty*.svg
%{_metainfodir}/sm.puri.Chatty.metainfo.xml
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/chatty
%{_datadir}/help/C/chatty/index.page
%{_libdir}/libjabber.so.0
%{_sysconfdir}/ld.so.conf.d/chatty.conf
%doc README.md
%license COPYING

%changelog
* Fri Oct 21 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.7.0~rc1-1
- Bugfix release 0.7.0~rc1

* Tue Oct 18 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.7.0~rc0-1
- Update to 0.7.0~rc0

* Sat Aug 13 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.6.7-3
- Thanks to Marcin <marcin@ipv8.pl> for providing patches and fixes
- Adding patches for libsoup3 support to fix breaking builds
- Fixing icons for GNOME 43 changes
- Conflicts for purple plugins sipe and chime

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 26 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.6.7-1
- Update to 0.6.7

* Sun Apr 24 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.6.3-1
- Update to 0.6.3

* Fri Feb 25 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2

* Tue Feb 08 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Tue Jan 25 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0~beta-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.6.0~beta-1
- Update to 0.6.0_beta

* Wed Dec 15 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.5.0~beta4-1
- Update to 0.5.0_beta4

* Fri Dec 10 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.5.0~beta3-1
- Update to 0.5.0_beta3

* Tue Nov 16 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.5.0~beta-1
- Update to 0.5.0_beta

* Sat Oct 30 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.0-2
- Rebuild for deps

* Sat Sep 11 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Tue Sep 07 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.0~beta3-1
- Update to 0.4.0_beta3

* Mon Aug 30 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.0~beta2-1
- Update to 0.4.0_beta2

* Mon Aug 23 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.0~beta-1
- Update 0.4.0_beta

* Thu Jul 29 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.4-1
- Update to chatty 0.3.4

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.3-1
- Update to chatty 0.3.3

* Tue Jun 29 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.2-1
- Update to chatty 0.3.2

* Fri May 28 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.1-1
- Update to chatty 0.3.1

* Thu May 06 2021 Torrey Sorensen <torbuntu@fedpraproject.org> - 0.3.0-1
- Update to chatty 0.3.0

* Wed Apr 14 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.0_beta2-1
- Update to chatty 0.3.0 beta 2

* Sun Mar 28 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.0_beta-2
* Add patch for matrix crash in encrypted rooms

* Fri Mar 26 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.0_beta-1
- Update to 0.3.0_beta

* Sat Mar 13 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.2.0-5
- Update for package review

* Mon Feb 15 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.2.0-4
- Build for new evolution dep

* Sat Feb 06 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.2.0-3
- Re-add tests

* Mon Jan 11 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.2.0-2
- Updating for f34

* Mon Nov 16 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.2.0-1
- Update version to 0.2.0

* Tue Nov 03 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.17-1
- Update versoin to 0.1.17

* Thu Oct 15 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.16-2
- Updating meson tests for timeout

* Sun Sep 27 2020 Nikhil Jha <hi@nikhiljha.com> - 0.1.16-1
- Update version to 0.1.16

* Thu Aug 20 2020 Nikhil Jha <hi@nikhiljha.com> - 0.1.15-1
- Update version to 0.1.15

* Mon Jul 20 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.14-1
- Update version to 0.1.14 

* Thu Jun 25 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.12-1
- Update version to 0.1.12

* Fri May 29 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.11-1
- Update version to 0.1.11
- Remove 2 patches 

* Wed Mar 04 2020 Nikhil Jha <hi@nikhiljha.com> - 0.1.8-3
- Remove the buildid

* Wed Mar 04 2020 Nikhil Jha <hi@nikhiljha.com> - 0.1.8-2
- Bundle libjabber with it

* Mon Mar 02 2020 Nikhil Jha <hi@nikhiljha.com> - 0.1.8-1
- Initial packaging
