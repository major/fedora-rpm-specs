# This needs to be changed accordingly to the application for what tracker-miners is bundled,
# e.g. for gnome-books, it would be org.gnome.Books. For F39+ flatpaks, this is done
# in container.yaml cleanup-commands.
%if 0%{?flatpak}
%global domain_ontology org.gnome.FlatpakApp
%else
%global domain_ontology org.freedesktop
%endif

%global with_enca 1
%global with_libcue 1
%global with_rss 1
%global with_totem_pl_parser 1

%if 0%{?rhel} || 0%{?flatpak}
%global with_enca 0
%global with_libcue 0
%global with_rss 0
%if 0%{?rhel} >= 10
%global with_totem_pl_parser 0
%endif
%endif

%global tracker_version 3.7

%if 0%{?with_rss}
%global systemd_units tracker-extract-3.service tracker-miner-fs-3.service tracker-miner-fs-control-3.service tracker-miner-rss-3.service tracker-writeback-3.service
%else
%global systemd_units tracker-extract-3.service tracker-miner-fs-3.service tracker-miner-fs-control-3.service tracker-writeback-3.service
%endif

# Exclude private libraries from autogenerated provides and requires
%global __provides_exclude_from ^%{_libdir}/tracker-miners-3.0/
%global __requires_exclude ^(libtracker-extract\.so|libtracker-miner-3\.0\.so|libextract-.*\.so|libwriteback-.*\.so)

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           tracker-miners
Version:        3.7.3
Release:        3%{?dist}
Summary:        Tracker miners and metadata extractors

# libtracker-extract and libtracker-miner libraries are LGPLv2+; the miners are a mix of GPLv2+ and LGPLv2+ code
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://gnome.pages.gitlab.gnome.org/tracker/
Source0:        https://download.gnome.org/sources/%{name}/3.7/%{name}-%{tarball_version}.tar.xz
Source1:        flatpak-fixup.sh

BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  giflib-devel
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(dbus-1)
%if 0%{?with_enca}
BuildRequires:  pkgconfig(enca)
%endif
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
%if 0%{?with_libcue}
BuildRequires:  pkgconfig(libcue)
%endif
BuildRequires:  pkgconfig(libexif)
%if 0%{?with_rss}
BuildRequires:  pkgconfig(libgrss)
%endif
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(libgxps)
BuildRequires:  pkgconfig(libiptcdata)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(poppler-glib)
%if 0%{?with_totem_pl_parser}
BuildRequires:  pkgconfig(totem-plparser)
%endif
BuildRequires:  pkgconfig(tracker-sparql-3.0) >= %{tracker_version}
BuildRequires:  pkgconfig(vorbisfile)
%if !0%{?flatpak}
BuildRequires:  pkgconfig(libosinfo-1.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(upower-glib)
%endif

# renamed in F34
Obsoletes:      tracker3-miners < 3.1.0~rc-2
Conflicts:      tracker3-miners < 3.1.0~rc-2
Provides:       tracker3-miners = %{version}-%{release}
Provides:       tracker3-miners%{?_isa} = %{version}-%{release}

%if !0%{?flatpak}
Requires:       tracker%{?_isa} >= %{tracker_version}
%endif

%description
Tracker is a powerful desktop-neutral first class object database,
tag/metadata database and search tool.

This package contains various miners and metadata extractors for tracker.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson \
  -Dtracker_core=system \
%if 0%{?flatpak}
  -Dwriteback=false \
  -Dsystemd_user_services=false \
  -Diso=disabled \
  -Dnetwork_manager=disabled \
  -Dbattery_detection=none \
  -Ddomain_prefix=%{domain_ontology} \
%endif
%if ! 0%{?with_libcue}
  -Dcue=disabled \
%endif
%if ! 0%{?with_rss}
  -Dminer_rss=false \
%endif
%if ! 0%{?flatpak}
  -Dsystemd_user_services_dir=%{_userunitdir} \
%endif
%if ! 0%{?with_totem_pl_parser}
  -Dplaylist=disabled \
%endif
  %{nil}

%meson_build


%install
%meson_install

%if 0%{?flatpak}
install -D -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}-flatpak-fixup.sh
%endif

%find_lang tracker3-miners


%post
%systemd_user_post %{systemd_units}

%preun
%systemd_user_preun %{systemd_units}

%postun
%systemd_user_postun_with_restart %{systemd_units}


%files -f tracker3-miners.lang
%license COPYING*
%doc AUTHORS NEWS README.md
%config(noreplace) %{_sysconfdir}/xdg/autostart/tracker-miner-fs-3.desktop
%if 0%{?with_rss}
%config(noreplace) %{_sysconfdir}/xdg/autostart/tracker-miner-rss-3.desktop
%endif
%{_bindir}/tracker3-*
%{_libdir}/tracker-miners-3.0/
%{_libexecdir}/tracker*
%{_datadir}/dbus-1/interfaces/org.freedesktop.Tracker3.Miner.Files.Index.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Tracker3.Miner.xml
%{_datadir}/dbus-1/services/%{domain_ontology}.Tracker*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/tracker3-miners/
%dir %{_datadir}/tracker3
%dir %{_datadir}/tracker3/commands
%{_datadir}/tracker3/commands/tracker-*.desktop
%{_mandir}/man1/tracker*.1*
%if !0%{?flatpak}
%{_userunitdir}/tracker*.service
%endif
%if 0%{?flatpak}
%{_datadir}/tracker3/domain-ontologies/%{domain_ontology}.domain.rule
%{_bindir}/%{name}-flatpak-fixup.sh
%endif


%changelog
* Tue Aug 06 2024 Tomas Popela <tpopela@redhat.com> - 3.7.3-3
- totem-pl-parser won't be part of RHEL 10

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 03 2024 David King <amigadave@amigadave.com> - 3.7.3-1
- Update to 3.7.3

* Wed Apr 24 2024 David King <amigadave@amigadave.com> - 3.7.2-1
- Update to 3.7.2

* Thu Mar 28 2024 David King <amigadave@amigadave.com> - 3.7.1-1
- Update to 3.7.1

* Tue Mar 26 2024 David King <amigadave@amigadave.com> - 3.7.0-2
- Backport 2 upstream MRs for crash and db corruption

* Mon Mar 18 2024 David King <amigadave@amigadave.com> - 3.7.0-1
- Update to 3.7.0

* Fri Mar 08 2024 David King <amigadave@amigadave.com> - 3.7~rc-1
- Update to 3.7.rc

* Wed Feb 14 2024 David King <amigadave@amigadave.com> - 3.7~beta-1
- Update to 3.7.beta

* Mon Feb 12 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 3.7~alpha-4
- Bypass kernel landlock check during build

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 3.7~alpha-3
- Rebuild for ICU 74

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 David King <amigadave@amigadave.com> - 3.7~alpha-1
- Update to 3.7.alpha

* Tue Oct 31 2023 Kalev Lember <klember@redhat.com> - 3.6.2-1
- Update to 3.6.2

* Fri Sep 29 2023 Sandro Bonazzola <sbonazzo@redhat.com> - 3.6.1-2
- Do not include RSS miner service on RHEL/ELN
  Original patch by Carlos Garnacho <cgarnach@redhat.com>
  https://gitlab.com/redhat/centos-stream/rpms/tracker-miners/-/commit/4507ad77005aad38cb17b7a72a779446dce0981c

* Thu Sep 28 2023 Kalev Lember <klember@redhat.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 19 2023 Kalev Lember <klember@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 06 2023 Kalev Lember <klember@redhat.com> - 3.6~rc-1
- Update to 3.6.rc

* Fri Aug 11 2023 Kalev Lember <klember@redhat.com> - 3.6~beta-2
- Fix required tracker version

* Fri Aug 11 2023 Kalev Lember <klember@redhat.com> - 3.6~beta-1
- Update to 3.6.beta

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6~alpha-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 3.6~alpha-2
- Rebuilt for ICU 73.2

* Tue Jul 04 2023 Kalev Lember <klember@redhat.com> - 3.6~alpha-1
- Update to 3.6.alpha

* Sun May 14 2023 David King <amigadave@amigadave.com> - 3.5.2-1
- Update to 3.5.2

* Wed Apr 26 2023 David King <amigadave@amigadave.com> - 3.5.1-1
- Update to 3.5.1

* Mon Mar 20 2023 David King <amigadave@amigadave.com> - 3.5.0-1
- Update to 3.5.0 (#2179709)

* Sun Mar 05 2023 David King <amigadave@amigadave.com> - 3.5.0~rc-1
- Update to 3.5.0.rc (#2160269)

* Wed Feb 15 2023 David King <amigadave@amigadave.com> - 3.5.0~beta-1
- Update to 3.5.0.beta

* Fri Feb 10 2023 David King <amigadave@amigadave.com> - 3.5.0~alpha-2
- Fix depedency on tracker

* Mon Feb 06 2023 David King <amigadave@amigadave.com> - 3.5.0~alpha-1
- Update to 3.5.0.alpha

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 3.4.2-2
- Rebuild for ICU 72

* Tue Dec 06 2022 David King <amigadave@amigadave.com> - 3.4.2-1
- Update to 3.4.2 (#2116593)

* Wed Oct 26 2022 David King <amigadave@amigadave.com> - 3.4.1-1
- Update to 3.4.1

* Tue Sep 20 2022 Kalev Lember <klember@redhat.com> - 3.4.0-1
- Update to 3.4.0

* Tue Sep 06 2022 Kalev Lember <klember@redhat.com> - 3.4.0~rc-1
- Update to 3.4.0.rc

* Tue Aug 09 2022 Kalev Lember <klember@redhat.com> - 3.4.0~beta-1
- Update to 3.4.0.beta

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 3.4.0~alpha-3
- Rebuilt for ICU 71.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Kalev Lember <klember@redhat.com> - 3.4.0~alpha-1
- Update to 3.4.0.alpha

* Wed Jun 01 2022 David King <amigadave@amigadave.com> - 3.3.1-1
- Update to 3.3.1

* Mon May 02 2022 Ray Strode <rstrode@redhat.com> - 3.3.0-2
- file monitor fix
  Resolves: #2079308

* Sun Mar 20 2022 David King <amigadave@amigadave.com> - 3.3.0-1
- Update to 3.3.0

* Tue Mar 08 2022 David King <amigadave@amigadave.com> - 3.3.0~rc-1
- Update to 3.3.0.rc

* Mon Feb 14 2022 David King <amigadave@amigadave.com> - 3.3.0~beta-1
- Update to 3.3.0.beta

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 David King <amigadave@amigadave.com> - 3.3.0~alpha-1
- Update to 3.3.0.alpha

* Mon Nov 01 2021 Kalev Lember <klember@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Wed Sep 22 2021 Jan Beran <jaberan@redhat.com> - 3.2.0-2
- If building for flatpak, adapt the behavior to work as a private
  instance inside the flatpak

* Sat Sep 18 2021 Kalev Lember <klember@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Wed Sep 08 2021 Kalev Lember <klember@redhat.com> - 3.2.0~rc-1
- Update to 3.2.0.rc

* Thu Aug 19 2021 Kalev Lember <klember@redhat.com> - 3.2.0~alpha.1-1
- Update to 3.2.0.alpha.1

* Wed Aug 04 2021 Kalev Lember <klember@redhat.com> - 3.1.2-3
- BuildRequire systemd-rpm-macros instead of systemd
- Avoid systemd_requires as per updated packaging guidelines

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Kalev Lember <klember@redhat.com> - 3.1.2-1
- Update to 3.1.2

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 3.1.1-2
- Rebuild for ICU 69

* Sat Apr 03 2021 Kalev Lember <klember@redhat.com> - 3.1.1-1
- Update to 3.1.1

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 3.1.0-1
- Update to 3.1.0

* Fri Mar 19 2021 Kalev Lember <klember@redhat.com> - 3.1.0~rc-3
- Add conflicts with tracker3-miners to help with the upgrade path

* Fri Mar 19 2021 Kalev Lember <klember@redhat.com> - 3.1.0~rc-2
- Update to 3.1.0.rc, based on earlier tracker3-miners packaging
- Obsolete separate tracker3-miners package

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 03 2020 Adam Williamson <awilliam@redhat.com> - 2.3.5-2
- Backport patch to allow newfstatat and fstatat64 syscalls (#1892452)

* Mon Sep 07 2020 Kalev Lember <klember@redhat.com> - 2.3.5-1
- Update to 2.3.5

* Mon Sep 07 2020 Kalev Lember <klember@redhat.com> - 2.3.4-2
- Backport an upstream patch to allow statx syscall (#1875398)

* Tue Aug 25 2020 Kalev Lember <klember@redhat.com> - 2.3.4-1
- Update to 2.3.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 2.3.3-2
- Rebuild for ICU 67

* Tue Mar 10 2020 Kalev Lember <klember@redhat.com> - 2.3.3-1
- Update to 2.3.3

* Wed Feb 19 2020 Kalev Lember <klember@redhat.com> - 2.3.2-2
- Backport a fix for tracker erroring out with "Failed to set scheduler settings"

* Wed Feb 19 2020 Kalev Lember <klember@redhat.com> - 2.3.2-1
- Update to 2.3.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 2.3.1-3
- Rebuild for poppler-0.84.0

* Sat Nov 30 2019 Adam Williamson <awilliam@redhat.com> - 2.3.1-2
- Rebuild with libosinfo 1.7.0

* Fri Nov 29 2019 Kalev Lember <klember@redhat.com> - 2.3.1-1
- Update to 2.3.1

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 2.3.0-2
- Rebuild for ICU 65

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 2.3.0-1
- Update to 2.3.0

* Fri Sep 06 2019 Nikola Forró <nforro@redhat.com> - 2.2.99.1-2
- Rebuilt for exempi 2.5.1

* Fri Sep 06 2019 Kalev Lember <klember@redhat.com> - 2.2.99.1-1
- Update to 2.2.99.1

* Mon Aug 12 2019 Kalev Lember <klember@redhat.com> - 2.2.99.0-1
- Update to 2.2.99.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 03 2019 David King <amigadave@amigadave.com> - 2.2.2-1
- Update to 2.2.2

* Fri Mar 08 2019 Kalev Lember <klember@redhat.com> - 2.2.1-1
- Update to 2.2.1

* Thu Feb 21 2019 Kalev Lember <klember@redhat.com> - 2.2.0-3
- Exclude private libraries from autogenerated provides and requires

* Thu Feb 21 2019 Kalev Lember <klember@redhat.com> - 2.2.0-2
- Fix the package to be installable again

* Wed Feb 20 2019 Kalev Lember <klember@redhat.com> - 2.2.0-1
- Update to 2.2.0
- Switch to the meson build system

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 2.1.5-3
- Rebuild for ICU 63

* Mon Jan 21 2019 Kevin Fenzi <kevin@scrye.com> - 2.1.5-2
- Rebuild to drop libiptcdata deps

* Fri Sep 28 2018 Kalev Lember <klember@redhat.com> - 2.1.5-1
- Update to 2.1.5

* Wed Sep 05 2018 Kalev Lember <klember@redhat.com> - 2.1.4-2
- Rebuilt with fixed vala

* Tue Sep 04 2018 Kalev Lember <klember@redhat.com> - 2.1.4-1
- Update to 2.1.4

* Mon Sep 03 2018 Kalev Lember <klember@redhat.com> - 2.1.3-1
- Update to 2.1.3

* Sun Aug 19 2018 Kalev Lember <klember@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Wed Jul 25 2018 Kalev Lember <klember@redhat.com> - 2.1.0-1
- Update to 2.1.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 2.0.5-2
- Rebuild for ICU 62

* Tue Jun 26 2018 Kalev Lember <klember@redhat.com> - 2.0.5-1
- Update to 2.0.5

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 2.0.4-4
- Rebuild for ICU 61.1

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 2.0.4-3
- Rebuild (giflib)

* Thu Feb 08 2018 Kalev Lember <klember@redhat.com> - 2.0.4-2
- Rebuild to really enable the RAW extractor

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 2.0.4-1
- Update to 2.0.4
- Enable new gexiv2 based RAW extractor

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 2.0.3-2
- Rebuild for ICU 60.1

* Tue Nov 21 2017 Kalev Lember <klember@redhat.com> - 2.0.3-1
- Update to 2.0.3

* Fri Oct 06 2017 Kalev Lember <klember@redhat.com> - 2.0.2-1
- Update to 2.0.2

* Tue Sep 19 2017 Kalev Lember <klember@redhat.com> - 2.0.0-3
- Backport a fix for a crash when processing virtual elements (#1488707)

* Fri Sep 15 2017 Kalev Lember <klember@redhat.com> - 2.0.0-2
- Package review fixes (#1491725):
- Pass --disable-mp3 to use the generic gstreamer extractor
- Disable libstemmer support to match the previous behaviour
- Fix removing .so symlinks for private libraries
- Remove ldconfig rpm scripts as we don't install any shared libraries
- Correct license tag and add comment explaining mixed source licensing

* Thu Sep 14 2017 Kalev Lember <klember@redhat.com> - 2.0.0-1
- Initial Fedora packaging