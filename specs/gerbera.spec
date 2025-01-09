Name:           gerbera
Version:        2.4.1
Release:        1%{?dist}
Summary:        UPnP Media Server
License:        GPL-2.0-only AND MIT AND OFL-1.1
Url:            https://gerbera.io
Source0:        https://github.com/gerbera/gerbera/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        config.xml
Source2:        gerbera-sysusers.conf

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libupnp-devel
BuildRequires:  libuuid-devel
BuildRequires:  sqlite-devel
BuildRequires:  duktape-devel
BuildRequires:  curl-devel
BuildRequires:  taglib-devel
BuildRequires:  file-devel
BuildRequires:  libexif-devel
BuildRequires:  exiv2-devel
BuildRequires:  cmake
BuildRequires:  zlib-devel
BuildRequires:  libebml-devel
BuildRequires:  libmatroska-devel
BuildRequires:  spdlog-devel
BuildRequires:  pugixml-devel
BuildRequires:  mariadb-connector-c-devel
%{?sysusers_requires_compat}
%{?systemd_ordering}
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  make
Requires:       %{name}-data = %{version}-%{release}

%description
Gerbera is a UPnP media server which allows you to stream your digital
media through your home network and consume it on a variety of UPnP
compatible devices.

%package data
Summary:        Data files for Gerbera
BuildArch:      noarch

%description data
Data files for the Gerbera media server.

%prep
%autosetup -p1

%build
%cmake \
    -DWITH_JS=1 \
    -DWITH_MYSQL=1 \
    -DWITH_CURL=1 \
    -DWITH_TAGLIB=1 \
    -DWITH_MAGIC=1 \
    -DWITH_AVCODEC=0 \
    -DWITH_EXIF=1 \
    -DWITH_EXIV2=1 \
    -DWITH_FFMPEGTHUMBNAILER=0 \
    -DWITH_INOTIFY=1 \
    -DWITH_SYSTEMD=1 \
    -DUPNP_HAS_IPV6=1 \
    -DUPNP_HAS_REUSEADDR=1

%cmake_build

%install
install -p -D -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/gerbera/config.xml
install -p -D -m0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/gerbera.conf

%cmake_install

# make all files under %%_sysconfdir/gerbera owned by
# this package
mkdir -p %{buildroot}%{_sysconfdir}/gerbera
touch %{buildroot}%{_sysconfdir}/gerbera/{gerbera.db,gerbera.html}
mkdir -p %{buildroot}%{_localstatedir}/log/gerbera
touch %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p  %{buildroot}%{_sysconfdir}/logrotate.d
cat > %{buildroot}%{_sysconfdir}/logrotate.d/%{name} << 'EOF'
/var/log/gerbera/gerbera {
create 644 gerbera gerbera
      monthly
      compress
      missingok
}
EOF


%pre
%sysusers_create_compat %{SOURCE2}

%post
%systemd_post gerbera.service

%preun
%systemd_preun gerbera.service

%postun
%systemd_postun_with_restart gerbera.service

%files
%license LICENSE.md
%doc AUTHORS CONTRIBUTING.md ChangeLog.md
%attr(-,gerbera,gerbera)%dir %{_sysconfdir}/%{name}/
%attr(-,gerbera,gerbera)%config(noreplace) %{_sysconfdir}/%{name}/*
%attr(-,gerbera,gerbera) %{_localstatedir}/log/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_sysconfdir}/logrotate.d
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_unitdir}/gerbera.service
%{_sysusersdir}/gerbera.conf

%files data
%{_datadir}/%{name}/
%config(noreplace) %{_datadir}/%{name}/js/import.js
%config(noreplace) %{_datadir}/%{name}/js/playlists.js
%config(noreplace) %{_datadir}/%{name}/js/common.js

%changelog
* Tue Jan 07 2025 Gwyn Ciesla <gwync@protonmail.com> - 2.4.1-1
- 2.4.1

* Tue Jan 07 2025 Gwyn Ciesla <gwync@protonmail.com> - 2.4.0-1
- 2.4.0

* Tue Nov 26 2024 František Zatloukal <fzatlouk@redhat.com> - 2.3.0-2
- Rebuilt for spdlog 1.15.0

* Thu Sep 19 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.3.0-1
- 2.3.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.2.0-2
- fmt rebuild

* Mon Jul 08 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.2.0-1
- 2.2.0

* Fri Jun 14 2024 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.0-3
- Rebuilt for exiv2 0.28.2

* Tue May 21 2024 František Zatloukal <fzatlouk@redhat.com> - 2.1.0-2
- Rebuilt for spdlog 1.14.1

* Tue Apr 09 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.1.0-1
- 2.1.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 08 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.0.0-1
- 2.0.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 1.12.1-6
- Rebuilt due to spdlog 1.12 update.

* Thu Jun 29 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.12.1-5
- Patch for fmtlib 10

* Wed Jun 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 1.12.1-4
- Rebuilt due to fmt 10 update.

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.12.1-3
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.12.1-1
- 1.12.1

* Fri Dec 16 2022 František Zatloukal <fzatlouk@redhat.com> - 1.12.0-2
- Rebuilt for duktape 2.7.0

* Mon Nov 07 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.12.0-1
- 1.12.0

* Thu Nov 03 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 1.11.0-4
- Rebuilt due to spdlog update.
- Fixed FTBFS on Rawhide. Closes rhbz#2139904.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.11.0-2
- Patch for fmt-9

* Thu May 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.11.0-1
- 1.11.0

* Fri Feb 25 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.10.0-1
- 1.10.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.2-2
- Rebuild for dukpy-2.6.0

* Fri Oct 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.9.2-1
- 1.9.2

* Sat Aug 28 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.9.1-1
- 1.9.1

* Sun Aug 01 2021 Neal Gompa <ngompa@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0
- Update user creation for systemd-sysusers support
- Fix file list for logrotate configuration
- Other minor spec cleanups

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Richard Shaw <hobbes1069@gmail.com> - 1.8.2-2
- Rebuild for new fmt version.

* Tue Jun 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.8.2-1
- 1.8.2

* Mon May 10 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.8.1-1
- 1.8.1

* Wed Apr 07 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.8.0-1
- 1.8.0

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.7.0-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Mar 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.7.0-1
- 1.7.0

* Fri Feb 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.6.4-5
- Add MySQL support.

* Tue Feb 09 2021 Nicolas Chauvet <kwizart@gmail.com> - 1.6.4-4
- Rebuilt for upnp

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Jeff Law <law@redhat.com> - 1.6.4-2
- Fix missing #include for gcc-11

* Thu Oct 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.6.4-1
- 1.6.4

* Fri Sep 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.6.1-1
- 1.6.1

* Tue Aug 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.6.0-3
- fmt rebuild.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.6.0-1
- 1.6.0

* Fri Jul 17 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.5.0-2
- rebuild for libebml and libmatroska soname bump

* Thu Jul 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.5.0-1
- 1.5.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.0-2
- Bump EVR for koji error.

* Mon Dec 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.0-1
- 1.4.0

* Fri Nov 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.3.5-1
- 1.3.5

* Mon Nov 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.3.4-1
- 1.3.4

* Wed Oct 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.3.3-1
- 1.3.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.3.2-1
- 1.3.2

* Thu Apr 04 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.3.1-1
- 1.3.1

* Thu Feb 21 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.3.0-4
- Drop lastlibfm, liblastfm not working yet.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.3.0-2
- rebuild (exiv2)

* Tue Jan 29 2019 Gwyn Ciesla <limburgher@gmail.com> - 1.3.0-1
- 1.3.0

* Mon Dec 03 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2.0-4
- Fix logrotate config, BZ 1655279.

* Mon Nov 12 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2.0-3
- noconfig js, BZ 1648650.

* Tue Oct 23 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2.0-2
- Correct log directory.
- Fix default config.

* Fri Oct 05 2018 Dennis Gilmore <dennis@ausil.us> - 1.2.0-1
- update to the 1.2.0 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6.20180413git2f6dcb5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-5.20180413git2f6dcb5
- Fix Requires

* Mon May 28 2018 Dennis Gilmore <dennis@ausil.us> - 1.1.0-4.20180413git2f6dcb5
- Add back the correct requiresso that the data sub package gets pulled in

* Mon May 28 2018 Dennis Gilmore <dennis@ausil.us> - 1.1.0-3.20180413git2f6dcb5
- remove requires that prevents installation

* Thu Apr 19 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.1.0-2.20180413git2f6dcb5
- Spec corrections.
- Split out data subpackage.

* Fri Apr 13 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.1.0-1
- Adapt to modern packaging guidelines.

* Mon Mar 19 2018 jk@lutty.net
- Initial package derived from mediatomb (fedora) annd gerbera (Suse)
