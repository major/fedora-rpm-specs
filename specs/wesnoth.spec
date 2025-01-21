Name:           wesnoth
Version:        1.19.7
Release:        2%{?dist}
Summary:        Turn-based strategy game with a fantasy theme

License:        GPL-2.0-or-later
URL:            http://www.wesnoth.org
Source0:        http://www.%{name}.org/files/%{name}-%{version}.tar.bz2
Source1:        wesnothd.service
Source2:        %{name}.sysconfig
Patch0:         scons-env.patch

Requires:       wesnoth-data = %{version}
BuildRequires:  gcc-c++
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_net-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  dbus-devel
BuildRequires:  freetype-devel
BuildRequires:  libpng-devel
BuildRequires:  fribidi-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  boost-devel
BuildRequires:  pango-devel
BuildRequires:  lua-devel
BuildRequires:  readline-devel
BuildRequires:  python3-scons
BuildRequires:  openssl-devel
%if 0%{?fedora} >= 41
BuildRequires:  openssl-devel-engine
%endif
BuildRequires:  libvorbis-devel
BuildRequires:  libcurl-devel
BuildRequires:  systemd

%description
The Battle for Wesnoth is a turn-based strategy game with a fantasy theme.

Build up a great army, gradually turning raw recruits into hardened
veterans. In later games, recall your toughest warriors and form a deadly
host against whom none can stand. Choose units from a large pool of
specialists, and hand-pick a force with the right strengths to fight well
on different terrains against all manner of opposition.

Fight to regain the throne of Wesnoth, of which you are the legitimate
heir, or use your dread power over the Undead to dominate the land of
mortals, or lead your glorious Orcish tribe to victory against the humans
who dared despoil your lands. Wesnoth has many different sagas waiting to
be played out. You can create your own custom units, and write your own
scenarios--or even full-blown campaigns. You can also challenge your
friends--or strangers--and fight multi-player epic fantasy battles.

##%ifnarch noarch
%package server
Summary:        %{summary}
Requires:       %{name} = %{version}-%{release}
Requires(pre):  /usr/sbin/useradd

%description server
This package contains the binaries for running a Wesnoth server
for multi-player games.


%package tools
Summary:        %{summary}
Requires:       %{name} = %{version}-%{release}


%description tools
This package contains the game editor and development tools.

##%else
%package data
Summary:        %{summary}
Requires:       %{name} = %{version}
Requires:	dejavu-sans-fonts
BuildArch:      noarch

%description data
This package contains the data files for Wesnoth.
##%endif

%prep
%autosetup -p0

%build
scons wesnoth wesnothd campaignd prefix=%{_prefix} \
          bindir=%{_bindir} \
          libdir=%{_libdir} \
          boostdir=%{_includedir} \
          boostlibdir=%{_libdir} \
          localedirname=locale \
          python_site_packages_dir=%{python3_sitelib}/wesnoth \
          extra_flags_release="$RPM_OPT_FLAGS $RPM_LD_FLAGS" \
          luadir=%{_includedir} \
          fifodir=/run/wesnothd \
          systemd=True \
          %{?_smp_mflags}

%install
scons install install-pytools destdir=$RPM_BUILD_ROOT

#Workaround for BZ 1981728
sed -i "s|@FIFO_DIR@|\/run\/wesnothd|g" $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/wesnothd.tmpfiles.conf

#Correct user/group
sed -i "s/_wesnoth/wesnothd/g" $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/wesnothd.tmpfiles.conf

%if 0%{?flatpak}
# Fix install paths for flatpak builds where systemd prefix differs from wesnoth prefix
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mv $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system/wesnothd.service $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{_tmpfilesdir}
mv $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/wesnothd.tmpfiles.conf $RPM_BUILD_ROOT%{_tmpfilesdir}
%endif

# extra files we provide
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/wesnothd.service
install -Dpm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/wesnoth

# create this so we can %ghost it
mkdir -p ${RPM_BUILD_ROOT}/run/wesnothd/
touch ${RPM_BUILD_ROOT}/run/wesnothd/socket

%if "%{_sbindir}" != "%{_bindir}"
# move server stuff into sbindir
mkdir -p $RPM_BUILD_ROOT/%{_sbindir}
mv $RPM_BUILD_ROOT/%{_bindir}/wesnothd $RPM_BUILD_ROOT/%{_sbindir}
mv $RPM_BUILD_ROOT/%{_bindir}/campaignd $RPM_BUILD_ROOT/%{_sbindir}
%endif

# Wesnoth ships its own fonts, replace with Fedora packaged versions
for f in dejavu-sans-fonts/DejaVuSans-Bold.ttf dejavu-sans-mono-fonts/DejaVuSansMono-Bold.ttf dejavu-sans-mono-fonts/DejaVuSansMono.ttf dejavu-sans-fonts/DejaVuSans-Oblique.ttf dejavu-sans-fonts/DejaVuSans.ttf ; do
    rm $RPM_BUILD_ROOT%{_datadir}/wesnoth/fonts/$(basename $f)
    ln -s /usr/share/fonts/$f $RPM_BUILD_ROOT%{_datadir}/wesnoth/fonts/$(basename $f)
done

# language stuff
%find_lang %{name} LANGFILES --with-man

%pre server
/usr/sbin/useradd -c "Wesnoth server" -s /sbin/nologin \
          -r -d /run/wesnothd wesnothd 2> /dev/null || :


%post server
%systemd_post wesnothd.service

%preun server
%systemd_preun wesnothd.service

%postun server
%systemd_postun_with_restart wesnothd.service


%files
%license COPYING
%doc changelog.md README.md copyright
%docdir %{_docdir}/wesnoth
%{_docdir}/wesnoth
%{_bindir}/%{name}

%files tools
%{_bindir}/wesnoth_addon_manager
%{_bindir}/wml*
%{python3_sitelib}/wesnoth
%{_datadir}/wesnoth/data/tools

%files server
%config(noreplace) %{_sysconfdir}/sysconfig/wesnoth
%{_sbindir}/wesnothd
%{_sbindir}/campaignd
%attr(0700,wesnothd,wesnothd) %dir /run/wesnothd/
%ghost /run/wesnothd/socket
%{_unitdir}/wesnothd.service
%{_tmpfilesdir}/wesnothd.tmpfiles.conf
%exclude %{_prefix}/lib/sysusers.d/wesnothd.sysusers.conf

%files data -f LANGFILES
%{_datadir}/applications/org.wesnoth.Wesnoth.desktop
%{_datadir}/icons/*
%{_datadir}/metainfo/org.wesnoth.Wesnoth.appdata.xml
%{_datadir}/wesnoth/
%exclude %{_datadir}/wesnoth/data/tools
%{_mandir}/man6/wesnoth*.6*
%{_mandir}/*/man6/wesnoth*.6*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 19 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.19.7-1
- 1.19.7

* Tue Nov 26 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.19.6-1
- 1.19.6

* Wed Oct 23 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.19.5-1
- 1.19.5

* Mon Sep 23 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.19.4-1
- 1.19.4

* Fri Aug 23 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.19.3-1
- 1.19.3

* Wed Jul 31 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.18.2-1
- 1.18.2

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 09 2024 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.18.0-3
- Rebuilt for the bin-sbin merge

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.18.0-2
- Rebuilt for Python 3.13

* Mon Mar 18 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.18.0-1
- 1.18.0

* Wed Feb 21 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.17.26-1
- 1.17.26

* Mon Jan 22 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.17.25-1
- 1.17.25

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 1.17.24-2
- Rebuilt for Boost 1.83

* Mon Dec 18 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.17.24-1
- 1.17.24

* Tue Nov 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.17.23-1
- 1.17.23

* Wed Oct 18 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.17.22-1
- 1.17.22

* Tue Sep 19 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.17.21-1
- 1.17.21

* Wed Aug 23 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.17.20-1
- 1.17.20

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.17.19-1
- 1.17.19

* Mon Jun 26 2023 Python Maint <python-maint@redhat.com> - 1.17.18-2
- Rebuilt for Python 3.12

* Tue Jun 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.17.18-1
- 1.17.18

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.17.17-3
- Rebuilt for Python 3.12

* Thu May 25 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.17.17-2
- Workaround for BZ 1981728.

* Mon May 22 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.17.17-1
- 1.17.17

* Mon Apr 24 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.17.16-1
- 1.17.16

* Mon Apr 17 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.17.15-1
- 1.17.15

* Mon Mar 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.17.14-1
- 1.17.14

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.17.13-3
- migrated to SPDX license

* Thu Feb 23 2023 Kalev Lember <klember@redhat.com> - 1.17.13-2
- Rebuilt for Boost 1.81

* Tue Feb 21 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.17.13-1
- 1.17.13

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.17.7-3
- Rebuilt for Boost 1.81

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 22 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.17.7-1
- 1.17.7

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.17.6-1
- 1.17.6

* Tue Jun 21 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.17.5-1
- 1.17.5

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.17.4-2
- Rebuilt for Python 3.11

* Mon May 16 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.17.4-1
- 1.17.4

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.17.3-2
- Rebuilt for Boost 1.78

* Mon Apr 18 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.17.3-1
- 1.17.3

* Mon Mar 21 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.17.2-1
- 1.17.2

* Tue Feb 22 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.17.1-1
- 1.17.1

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.17.0-1
- 1.17.0

* Tue Nov 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.1-1
- 1.16.1

* Fri Oct 29 2021 Kalev Lember <klember@redhat.com> - 1.16.0-2
- Remove Python 2 workarounds as everything has been ported to Python 3
- Drop post/preun/postun requires on systemd

* Sun Oct 24 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.16.0-1
- 1.16.0

* Mon Sep 27 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.15.18-1
- 1.15.18

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.15.17-2
- Rebuilt with OpenSSL 3.0.0

* Thu Sep 02 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.15.17-1
- 1.15.17

* Mon Aug 23 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.15.16-1
- 1.15.16

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 1.15.15-3
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.15.15-1
- 1.15.15

* Mon Jun 21 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.15.14-1
- 1.15.14

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.15.13-2
- Rebuilt for Python 3.10

* Mon May 17 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.15.13-1
- 1.15.13

* Mon Apr 19 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.15.12-1
- 1.15.12

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 1.15.11-2
- Rebuilt for removed libstdc++ symbol (#1937698)

* Mon Mar 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.5.11-1
- 1.5.11

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.15.10-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Feb 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.15.10-1
- 1.15.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.15.9-2
- Rebuilt for Boost 1.75

* Tue Jan 19 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.15.9-1
- 1.15.9

* Mon Dec 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.8-1
- 1.15.8

* Sun Dec 06 2020 Jeff Law <law@redhat.com> - 1.15.7-2
- Fix missing #include for gcc-11

* Mon Nov 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.7-1
- 1.15.7

* Mon Oct 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.6-1
- 1.15.6

* Mon Sep 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.5-1
- 1.15.5

* Wed Sep 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.4-2
- Upstream crash patch.

* Mon Aug 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.4-1
- 1.15.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 1.15.3-4
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.15.3-3
- Rebuilt for Python 3.9

* Mon May 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15.3-2
- Update dejavu font paths.

* Thu Mar 12 2020 Kalev Lember <klember@redhat.com> - 1.15.3-1
- 1.15.3

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.15.2-1
- 1.15.2

* Tue Sep 03 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.15.1-1
- 1.15.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.14.7-6
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.14.7-5
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.14.7-4
- Exclude Python 2 tools per upstream.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Kalev Lember <klember@redhat.com> - 1.14.7-2
- Move tools python scripts from -data subpackage to -tools

* Tue Apr 16 2019 Kalev Lember <klember@redhat.com> - 1.14.7-1
- Update to 1.14.7

* Tue Feb 26 2019 Kalev Lember <klember@redhat.com> - 1.14.6-1
- Update to 1.14.6
- Enable ppc64le build again

* Thu Feb 14 2019 Kalev Lember <klember@redhat.com> - 1.14.5-3
- Add missing dbus-devel and readline-devel BRs for optional features
- Fix dejavu font unbundling
- Drop obsolete sazanami-gothic and wqy-zenhei font deps

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.14.5-1
- 1.14.5.

* Mon Jul 23 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.14.4-1
- 1.14.4.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 1.14.3-3
- Rebuild for ICU 62

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.14.3-2
- Rebuilt for Python 3.7

* Mon Jun 11 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.14.3-1
- 1.14.3.

* Tue May 29 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.14.2-1
- 1.14.2.

* Tue May 22 2018 Pete Walter <pwalter@fedoraproject.org> - 1.14.1-3
- Don't install duplicate appdata

* Wed May 16 2018 Pete Walter <pwalter@fedoraproject.org> - 1.14.1-2
- Rebuild for ICU 61.1

* Wed May 09 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.14.1-1
- 1.14.1.

* Wed May 02 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.14.0-1
- 1.14.0.

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 1.13.14-2
- Rebuild for ICU 61.1

* Tue Apr 17 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.13.14-1
- 1.13.14.

* Mon Apr 02 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.13.13-1
- 1.13.13.

* Mon Mar 26 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.13.12-1
- 1.13.12.

* Mon Feb 19 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.13.11-1
- 1.13.11.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.13.10-1
- 1.13.10.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 1.13.8-2
- Rebuilt for Boost 1.64

* Mon May 22 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.13.8-1
- 1.13.8.

* Wed Mar 22 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.13.7-1
- 1.13.7.

* Thu Feb 23 2017 Jon Ciesla <limburgher@gmail.com> - 1.13.6-4.20170103git795624ab4e
- ExcludeArch ppc64le

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.6-3.20170103git795624ab4e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.13.6-2.20170103git795624ab4e
- Rebuilt for Boost 1.63

* Tue Jan 03 2017 Jon Ciesla <limburgher@gmail.com> - 1.13.6-1.20170103git795624ab4e
- 1.13.6 snapshot 795624ab4e for FTBFS.

* Thu Dec 29 2016 Jon Ciesla <limburgher@gmail.com> - 1.13.6-1.2016129git181503
- 1.13.6 snapshot 181503 for FTBFS.

* Mon Dec 19 2016 Jon Ciesla <limburgher@gmail.com> - 1.13.6-1.20161219git3621a3
- 1.13.6 snapshot 3621a3 for FTBFS.
- Dropped some tools, dropped upstream.

* Tue Sep 06 2016 Jon Ciesla <limburgher@gmail.com> - 1.13.5-1
- 1.13.5.
- Disabled byte-complilation, project is a mix between Python 2 and 3.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun May 22 2016 Jon Ciesla <limburgher@gmail.com> - 1.12.6-1
- 1.12.6.

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 1.12.5-4
- Rebuilt for linker errors in boost (#1331983)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 1.12.5-2
- Rebuilt for Boost 1.60

* Wed Nov 11 2015 Jon Ciesla <limburgher@gmail.com> - 1.12.5-1
- 1.12.5.

* Tue Sep 22 2015 Jon Ciesla <limburgher@gmail.com> - 1.12.4-5
- Fix boost FTBFS, BZ 1261123.

* Sat Sep 05 2015 Bruno Wolff III <bruno@wolff.to> - 1.12.4-4
- Rebuild for boost 1.59 again as it still was using 1.58

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.12.4-2
- rebuild for Boost 1.58

* Mon Jun 29 2015 Jon Ciesla <limburgher@gmail.com> - 1.12.4-1
- Upstream maintenance release.

* Fri Jun 26 2015 Jon Ciesla <limburgher@gmail.com> - 1.12.2-3
- Patches for CVE-2015-5069 and CVE-2015-5070.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 13 2015 Jon Ciesla <limburgher@gmail.com> - 1.12.2-1
- 1.12.2, security release.

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.12.1-3
- Add an AppData file for the software center

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.12.1-2
- Rebuild for boost 1.57.0

* Mon Jan 26 2015 Jon Ciesla <limburgher@gmail.com> - 1.12.1-1
- 1.12.1, bugfix release.

* Mon Nov 24 2014 Jon Ciesla <limburgher@gmail.com> - 1.12-1
- 1.12 final.

* Mon Nov 10 2014 Jon Ciesla <limburgher@gmail.com> - 1.11.19-1
- 1.12 RC3.

* Mon Oct 27 2014 Jon Ciesla <limburgher@gmail.com> - 1.11.18-1
- 1.12 RC2.

* Thu Oct 16 2014 Jon Ciesla <limburgher@gmail.com> - 1.11.17-1
- 1.12 RC1.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 14 2014 Jon Ciesla <limburgher@gmail.com> - 1.11.16-1
- 1.12 Beta 6.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Jon Ciesla <limburgher@gmail.com> - 1.11.15-1
- 1.12 Beta 5.
- Changelog fix.

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.11.13-3
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 1.11.13-2
- rebuild for boost 1.55.0

* Thu Apr 24 2014 Jon Ciesla <limburgher@gmail.com> - 1.11.13-1
- 1.12 Beta 4.

* Wed Mar 26 2014 Jon Ciesla <limburgher@gmail.com> - 1.11.12-1
- 1.12 Beta 3.

* Fri Mar 07 2014 Jon Ciesla <limburgher@gmail.com> - 1.11.11-1
- 1.12 Beta 2.

* Tue Feb 25 2014 Jon Ciesla <limburgher@gmail.com> - 1.11.10-1
- 1.12 Beta 1.

* Mon Aug 26 2013 Jon Ciesla <limburgher@gmail.com> - 1.10.7-1
- Latest upstream stable release.
- Crash patch upstreamed.

* Mon Aug 12 2013 Jon Ciesla <limburgher@gmail.com> - 1.10.6-8
- Spec cleanup, better scons build, BZ 991376.
- Add systemd macros, BZ 850365.
- Fix font requires.

* Thu Aug 01 2013 Jon Ciesla <limburgher@gmail.com> - 1.10.6-7
- Another man page fix attempt.

* Tue Jul 30 2013 Jon Ciesla <limburgher@gmail.com> - 1.10.6-6
- Fix man page ownership, with comments from BZ 905379.

* Sat Jul 27 2013 pmachata@redhat.com - 1.10.6-5
- Rebuild for boost 1.54.0

* Thu Jul 25 2013 Jon Ciesla <limburgher@gmail.com> - 1.10.6-4
- Fix man page ownership, BZ 958465.

* Thu Apr 25 2013 Jon Ciesla <limburgher@gmail.com> - 1.10.6-3
- Add PIE, BZ 955196.

* Wed Apr 24 2013 Jon Ciesla <limburgher@gmail.com> - 1.10.6-2
- Fix for crash, BZ 953327.

* Thu Mar 28 2013 Jon Ciesla <limburgher@gmail.com> - 1.10.6-1
- New upstream maintainance release.

* Mon Feb 11 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.10.5-5
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.10.5-4
- Rebuild for Boost-1.53.0

* Fri Feb 01 2013 Jon Ciesla <limburgher@gmail.com> - 1.10.5-3
- Fin man page locations, BZ 905379.

* Tue Nov 20 2012 Jon Ciesla <limburgher@gmail.com> - 1.10.5-2
- Switched from cmake to scons to fix build issue.

* Tue Nov 20 2012 Jon Ciesla <limburgher@gmail.com> - 1.10.5-1
- New upstream maintainance release.

* Tue Aug 28 2012 Jon Ciesla <limburgher@gmail.com> - 1.10.4-1
- New upstream maintainance release.

* Fri Jul 27 2012 Jon Ciesla <limburgher@gmail.com> - 1.10.3-5
- Fix for translation issue, BZ 840916.

* Thu Jul 26 2012 Jon Ciesla <limburgher@gmail.com> - 1.10.3-4
- Rebuild for boost 1.50.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Jon Ciesla <limburgher@gmail.com> - 1.10.3-1
- New upstream maintainance release.

* Fri Apr 13 2012 Jon Ciesla <limburgher@gmail.com> - 1.10.2-2
- Added hardened build.

* Mon Apr 09 2012 Jon Ciesla <limburgher@gmail.com> - 1.10.2-1
- New upstream maintainance release.

* Mon Feb 27 2012 Jon Ciesla <limburgher@gmail.com> - 1.10.1-1
- New upstream maintainance release.

* Tue Jan 31 2012 Jon Ciesla <limburgher@gmail.com> - 1.10-2
- Migrate to systemd, BZ 661241.
- Placed python modules.

* Sun Jan 29 2012 Jon Ciesla <limburgher@gmail.com> - 1.10-1
- New upstream, 1.10 final.

* Tue Jan 10 2012 Jon Ciesla <limburgher@gmail.com> - 1.9.14-1
- New upstream, 1.10-rc1.

* Wed Dec 21 2011 Jon Ciesla <limburgher@gmail.com> - 1.9.13-1
- New upstream.

* Thu Dec 08 2011 Jon Ciesla <limb@jcomserv.net> - 1.9.12-1
- Update to latest development release.
- Dropped ogg-test patch.
- Dropped cstddef patch, upstreamed.
- Moved from autotools to cmake build system.
- Could not get cmake install to work, did it my way.

* Sun Nov 20 2011 Bruno Wolff III <bruno@wolff.to> - 1.8.6-5
- Rebuild for boost soname bump

* Sun Nov 06 2011 Bruno Wolff III <bruno@wolff.to> - 1.8.6-4
- Include zlib.h since libpng 1.5 no longer does
- Replace some macros for null values with NULL no longer defined by png.h

* Thu Jul 21 2011 Jon Ciesla <limb@jcomserv.net> - 1.8.6-3
- Rebuild for new boost.
- Patch for foreach change, BZ 724818.

* Fri Jun 17 2011 Jon Ciesla <limb@jcomserv.net> - 1.8.6-2
- Bump and rebuild for BZ 712251.

* Fri May 13 2011 Jon Ciesla <limb@jcomserv.net> - 1.8.6-1
- Upstream maintenance release.

* Fri Apr 08 2011 Bruno Wolff III <bruno@wolff.to> - 1.8.5-5
- Rebuild for boost 1.46.1 soname bump in rawhide

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Thomas Spura <tomspur@fedoraproject.org> - 1.8.5-3
- rebuild for new boost

* Tue Oct 05 2010 Jon Ciesla <limb@jcomserv.net> - 1.8.5-2
- Font symlink correction, BZ 604905.

* Thu Sep 30 2010 Jon Ciesla <limb@jcomserv.net> - 1.8.5-1
- Upstream maintenance release.
- Boost iostreams patch upstreamed.

* Tue Aug 10 2010 Jon Ciesla <limb@jcomserv.net> - 1.8.4-1
- Upstream maintenance release.

* Thu Aug  5 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.8.3-3
- Fix boost.m4 configure check.

* Wed Jul 28 2010 Jon Ciesla <limb@jcomserv.net> - 1.8.3-2
- Rebuild for new Boost.

* Tue Jul 06 2010 Jon Ciesla <limb@jcomserv.net> - 1.8.3-1
- Upstream maintenance release.

* Mon Jun 07 2010 Jon Ciesla <limb@jcomserv.net> - 1.8.2-1
- Upstream maintenance release.

* Thu May 13 2010 Jon Ciesla <limb@jcomserv.net> - 1.8.1-2
- Rebuild for new Boost, BZ 590205.

* Tue May 04 2010 Jon Ciesla <limb@jcomserv.net> - 1.8.1-1
- Upstream maintenance release.

* Mon Apr 05 2010 Jon Ciesla <limb@jcomserv.net> - 1.8-1
- New stable.

* Wed Mar 17 2010 Jon Ciesla <limb@jcomserv.net> - 1.7.15-1
- RC1.

* Thu Mar 11 2010 Jon Ciesla <limb@jcomserv.net> - 1.7.14-1
- Beta 7.

* Thu Feb 11 2010 Jon Ciesla <limb@jcomserv.net> - 1.7.13-1
- Beta 6.

* Fri Jan 22 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.7.12-2
- Rebuild for Boost soname bump
- Fix mixed space and tabs
- Fix def attr

* Tue Jan 19 2010 Jon Ciesla <limb@jcomserv.net> - 1.7.12-1
- Beta 5.

* Mon Jan 04 2010 Jon Ciesla <limb@jcomserv.net> - 1.7.11-1
- Beta 4.

* Tue Dec 15 2009 Jon Ciesla <limb@jcomserv.net> - 1.7.10-1
- Beta 3.

* Tue Dec 01 2009 Jon Ciesla <limb@jcomserv.net> - 1.7.9-1
- Beta.
- Add lua-devel BR, altered autoreconf options.
- Dropped fribidi patch, upstreamed.

* Sun Sep 06 2009 Warren Togami <wtogami@redhat.com> - 1.6.5-1
- 1.6.5

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Jon Ciesla <limb@jcomserv.net> - 1.6.4-2
- Fribidi patch, BZ 504526.

* Sun Jul 05 2009 Warren Togami <wtogami@redhat.com> - 1.6.4-1
- 1.6.4 maintenance release

* Sun Jun 28 2009 Warren Togami <wtogami@redhat.com> - 1.6.3-1
- 1.6.3 maintenance release

* Tue May 12 2009 Jon Ciesla <limb@jcomserv.net> - 1.6.2-1
- 1.6.2 maintenance release.

* Tue Apr 21 2009 Debarshi Ray <rishi@fedoraproject.org> - 1.6.1-2
- Respect $RPM_OPT_FLAGS, BZ 496897.

* Mon Apr 20 2009 Jon Ciesla <limb@jcomserv.net> - 1.6.1-1
- 1.6.1 maintenance release.

* Mon Mar 23 2009 Jon Ciesla <limb@jcomserv.net> - 1.6-1
- Update to 1.6 stable.

* Tue Mar 17 2009 Jon Ciesla <limb@jcomserv.net> - 1.5.14-1
- Update to 1.5.14.

* Wed Mar 11 2009 Jon Ciesla <limb@jcomserv.net> - 1.5.13-1
- Update to 1.5.13.

* Wed Mar 04 2009 Jon Ciesla <limb@jcomserv.net> - 1.5.12-1
- Update to 1.5.12.

* Wed Feb 25 2009 Jon Ciesla <limb@jcomserv.net> - 1.5.11-5
- Drop -Werror.

* Wed Feb 25 2009 Jon Ciesla <limb@jcomserv.net> - 1.5.11-4
- Add pango BR.

* Wed Feb 25 2009 Jon Ciesla <limb@jcomserv.net> - 1.5.11-3
- Add SDL_ttf BR.

* Wed Feb 25 2009 Jon Ciesla <limb@jcomserv.net> - 1.5.11-2
- Rename rediffed ogg test patch.

* Wed Feb 25 2009 Jon Ciesla <limb@jcomserv.net> - 1.5.11-1
- Update to dev version 1.5.11.

* Tue Feb 24 2009 Jon Ciesla <limb@jcomserv.net> - 1.5.10-1
- Update to dev version 1.5.10.
- Move data to noarch.

* Wed Feb 04 2009 Jon Ciesla <limb@jcomserv.net> - 1.5.9-1
- Update to dev version 1.5.9.

* Mon Feb 02 2009 Jon Ciesla <limb@jcomserv.net> - 1.5.8-1
- Update to dev version 1.5.8.
- Rediffed remove-ogg-test patch.

* Sun Dec 28 2008 Warren Togami <wtogami@redhat.com> - 1.4.7-1
- 1.4.7
- Remove font requirement

* Wed Dec 17 2008 Benjamin Kosnik  <bkoz@redhat.com> - 1.4.6-6
- Rebuild for boost-1.37.0.

* Sun Dec 14 2008 Warren Togami <wtogami@redhat.com> - 1.4.6-5
- No longer ship Wesnoth's redundant copy of fonts.
  We now symlink to the Fedora packaged fonts that wesnoth expects.
  dejavu-fonts (Latin)
  sazanami-fonts-gothic (Japanese)
  wqy-zenhei-fonts (Chinese)
  We do not explicitly require these fonts.  Normally these fonts would be 
  already installed by your system to use that language.

* Wed Dec 10 2008 Jon Ciesla <limb@jcomserv.net> - 1.4.6-4
- Rediffed fuzzy gcc43 patch.

* Tue Nov 18 2008 Warren Togami <wtogami@redhat.com> 1.4.6-3
- split into -data noarch subpackage to save mirror space

* Mon Nov 17 2008 Jon Ciesla <limb@jcomserv.net> - 1.4.6-1
- New upstream release.

* Tue Sep 09 2008 Jon Ciesla <limb@jcomserv.net> - 1.4.5-1
- New upstream release.

* Tue Aug 12 2008 Jon Ciesla <limb@jcomserv.net> - 1.4.4-1
- New upstream release.
- Introduced patch fuzz workaround, will fix.

* Thu May 08 2008 Jon Ciesla <limb@jcomserv.net> - 1.4.2-1
- New upstream maintenance release.

* Fri Apr 18 2008 Jon Ciesla <limb@jcomserv.net> - 1.4.1-1
- New upstream bugfix release.

* Wed Apr 09 2008 Jon Ciesla <limb@jcomserv.net> - 1.4-2
- LSB initscript fix, BZ 247094.

* Tue Mar 11 2008 Jon Ciesla <limb@jcomserv.net> - 1.4-1
- Update to 1.4 stable.

* Fri Feb 15 2008 Jon Ciesla <limb@jcomserv.net> - 1.3.16-1
- Update to 1.3.16.
- Updated ogg test patch.
- Corrected license tag.
- Added boost-devel BR.
- Corrected .desktop/icon handling for subpackage.

* Mon Feb 11 2008 Warren Togami <wtogami@redhat.com> - 1.2.8-5
- Patch to fix build with gcc-4.3.

* Fri Feb  8 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.2.8-4
- Rebuild for gcc-4.3.

* Fri Nov 30 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.8-3
- Re-add the server-gid that accidently got removed.

* Fri Nov 30 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.8-2
- Add patch to drop ogg test from configure script, until better workaround.
- Enable python support.

* Thu Nov 29 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.8-1
- Update to 1.2.8.

* Tue Oct  9 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.7-1
- Update to 1.2.7. Fixes #324841 (CVE-2007-3917)

* Tue Aug 21 2007 Warren Togami <wtogami@redhat.com> - 1.2.6-2
- rebuild

* Sat Jul 28 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.6-1
- Update to 1.2.6.

* Sat Jun 16 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.5-2
- Drop wmlxgettext.

* Sat Jun 16 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.5-1
- Update to 1.2.5.

* Sat Apr 21 2007 Warren Togami <wtogami@redhat.com> - 1.2.4-1
- 1.2.4

* Fri Mar 16 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3.

* Sat Feb 24 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.2-2
- Bump.

* Sat Feb 24 2007 Warren Togami <wtogami@redhat.com> - 1.2.2-1
- 1.2.2

* Mon Jan 15 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1.

* Sun Dec 24 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.2-1
- Update to 1.2.

* Sat Dec 23 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.1.14-1
- Update to 1.1.14.
- Add BR on fribidi-devel.
- Drop X-Fedora category from desktop file.
- Drop help speedup patch, fixed upstream.
- Drop ttf patch, fixed upstream.

* Thu Sep  7 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.0.2-4
- Rebuild for FC6.
- Remove unnecessary BR on SDL-devel.

* Tue Jul 18 2006 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.2-3
- fix #199079, so loading some help pages like the "License" doesn't
  take ages
- remove BR SDL_ttf-devel, an included/patched copy is used since 0.8.7
- patch included SDL_ttf to build with freetype 2.x and not access
  an old freetype 1.x internal

* Wed Feb 15 2006 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.2-2
- rebuilt for FC5

* Wed Dec 21 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.2-1
- update to 1.0.2

* Sat Oct 22 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.1-1
- update to 1.0.1

* Tue Oct  4 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0-1
- update to 1.0
- remove README.fedora warning about game development status

* Wed Sep 21 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0-0.1.rc1
- update to 1.0rc1
- remove exe bit from Turkish manual

* Wed Sep 14 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.7-1
- update to 0.9.7

* Wed Aug 31 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.6-2
- update summary and description
- move and specify server package scriptlet requirements

* Sun Aug 28 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.6-1
- update to 0.9.6

* Sat Aug 13 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.5-1
- update to 0.9.5

* Wed Jul 27 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.4-1
- update to 0.9.4

* Fri Jul  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.3-1
- update to 0.9.3

* Mon Jun 13 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.2-1
- update to 0.9.2
- BR libpng-devel is needed
- add initscript and scriptlets for -server package
- don't build campaign server (upstream suggestion)
- split off editor+tools into -tools sub-package
- install translations into system's locale directories
- merge Panu's changes:
  Sat Apr 16 2005 Panu Matilainen <pmatilai@welho.com> 0.9.0-1
- enable campaign server and tools
- split server to separate package
- add wesnothd user in server %%pre
- buildrequire gettext

* Thu May 26 2005 Jeremy Katz <katzj@redhat.com> - 0.8-5
- fix build on x86_64

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.8-4
- rebuild on all arches

* Fri Apr 08 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Fri Jul 09 2004 Panu Matilainen <pmatilai@welho.com> 0:0.8-0.fdr.2
- use upstream desktop file and icon

* Sat Jul 03 2004 Panu Matilainen <pmatilai@welho.com> 0:0.8-0.fdr.1
- update to 0.8

* Tue Mar 30 2004 Panu Matilainen <pmatilai@welho.com> 0:0.7-0.fdr.1
- update to 0.7

* Wed Dec 17 2003 Panu Matilainen <pmatilai@welho.com> 0:0.6.1-0.fdr.1
- update to 0.6.1

* Mon Dec 15 2003 Panu Matilainen <pmatilai@welho.com> 0:0.6-0.fdr.2
- update to bugfixed tarball of 0.6

* Fri Dec 12 2003 Panu Matilainen <pmatilai@welho.com> 0:0.6-0.fdr.1
- update to 0.6
- adapt to the new autoconf make system
- enable editor and server

* Tue Nov 11 2003 Panu Matilainen <pmatilai@welho.com> 0:0.5.1-0.fdr.1
- update to 0.5.1
- Fedora -> fedora in desktop file vendor

* Tue Nov 04 2003 Panu Matilainen <pmatilai@welho.com> 0:0.5-0.fdr.1
- Initial Fedora packaging.
