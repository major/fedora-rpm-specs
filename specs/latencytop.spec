Name:           latencytop
Version:        0.5
Release:        38%{?dist}
Summary:        System latency monitor (with GUI)

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.latencytop.org/
Source0:        http://www.latencytop.org/download/%{name}-%{version}.tar.gz
Patch0:         latencytop-Makefile-fixes.patch
Patch1:         latencytop-Makefile-default-to-no-gtk.patch
Patch2:         latencytop-remove-the-fsync-view.patch
Patch3:         latencytop-better-error-message.patch
Patch4:         latencytop-add-return-type-c99.patch

BuildRequires:  gcc
BuildRequires:  ncurses-devel glib2-devel gtk2-devel pkgconfig
BuildRequires: make
Requires:       %{name}-common = %{version}-%{release}

%description
LatencyTOP is a tool for software developers (both kernel and userspace), aimed
at identifying where in the system latency is happening, and what kind of
operation/action is causing the latency to happen so that the code can be
changed to avoid the worst latency hiccups.
This package contains a build of LatencyTOP with GUI interface. For a build
without GUI install %{name}-tui instead.

%package tui
Summary:        System latency monitor (text interface only)
Requires:       %{name}-common = %{version}-%{release}

%description tui
LatencyTOP is a tool for software developers (both kernel and userspace), aimed
at identifying where in the system latency is happening, and what kind of
operation/action is causing the latency to happen so that the code can be
changed to avoid the worst latency hiccups.
This package contains a build of LatencyTOP without GUI support (and with few
dependencies).

%package common
Summary:        System latency monitor (shared files for both GUI and TUI builds)

%description common
LatencyTOP is a tool for software developers (both kernel and userspace), aimed
at identifying where in the system latency is happening, and what kind of
operation/action is causing the latency to happen so that the code can be
changed to avoid the worst latency hiccups.
This package contains files needed by both the GUI and TUI builds of LatencyTOP.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p2
%patch -P3 -p2
%patch -P4 -p1

%build
export CFLAGS="${CFLAGS:-%{optflags}}"
# make two builds, first without GUI, then with
make %{?_smp_mflags}
mv latencytop latencytop-tui
make clean
make %{?_smp_mflags} HAS_GTK_GUI=1

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -m 0755 latencytop-tui %{buildroot}%{_sbindir}/
ln -s latencytop.8 %{buildroot}%{_mandir}/man8/latencytop-tui.8

%files
%{_sbindir}/latencytop

%files tui
%{_sbindir}/latencytop-tui

%files common
%{_datadir}/%{name}
%{_mandir}/man8/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5-37
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Peter Fordham <peter.fordham@gmail.com> - 0.5-31
- Add a missing return type for C99 compliance.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 13 2018 Michal Schmidt <mschmidt@redhat.com> - 0.5-21
- BR: gcc
- Drop Group tags

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 21 2012 Michal Schmidt <mschmidt@redhat.com> - 0.5-9
- Make the manpage accessible under the latencytop-tui name as well.

* Sun Feb 19 2012 Michal Schmidt <mschmidt@redhat.com> - 0.5-8
- Print the error message only after cleaning up curses.

* Thu Feb 16 2012 Michal Schmidt <mschmidt@redhat.com> - 0.5-7
- Remove the broken fsync view, stop using the obsolete 'tracing_enabled'.
- Better error message when run as non-root.

* Thu Jan 26 2012 Michal Schmidt <mschmidt@redhat.com> - 0.5-6
- Build both with and without GUI to allow the use on systems where Gtk
  dependency is undesirable. The latencytop package is still the full-blown build.
  latencytop-tui is the miminal build. latencytop-common has the shared files.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 16 2010 Michal Schmidt <mschmidt@redhat.com> 0.5-3
- BuildRequire pkgconfig because the Makefile uses pkg-config.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 14 2009 Michal Schmidt <mschmidt@redhat.com> 0.5-1
- Upstream release 0.5, adds GTK based GUI.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 07 2008 Michal Schmidt <mschmidt@redhat.com> - 0.4-2
- Add an upstream patch to update the translation table.

* Thu Apr 24 2008 Michal Schmidt <mschmidt@redhat.com> - 0.4-1
- Upstream release 0.4.

* Wed Feb 20 2008 Michal Schmidt <mschmidt@redhat.com> - 0.3-5
- Own the data directory.

* Tue Feb  5 2008 Michal Schmidt <mschmidt@redhat.com> - 0.3-4
- Package the translation table too and modify latencytop.c to look for it in
  the correct directory.
 
* Mon Feb  4 2008 Michal Schmidt <mschmidt@redhat.com> - 0.3-3
- Dropped the whitespace-changing hunk from latencytop-standard-cflags.patch.

* Fri Feb  1 2008 Michal Schmidt <mschmidt@redhat.com> - 0.3-2
- From review comments - removed whitespace in latencytop-standard-cflags.patch

* Thu Jan 31 2008 Michal Schmidt <mschmidt@redhat.com> - 0.3-1
- Initial package for Fedora.
