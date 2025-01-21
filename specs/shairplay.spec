%global commit 096b61ad14c90169f438e690d096e3fcf87e504e
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20180824

Name:           shairplay
Version:        0.9.0
Release:        27.%{commit_date}git%{short_commit}%{?dist}
Summary:        Apple AirPlay and RAOP protocol server

# Automatically converted from old format: MIT and BSD and LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/juhovh/%{name}/
Source0:        %{url}/archive/%{short_commit}/%{name}-%{short_commit}.tar.gz
# Shairplay service file, taken from Arch Linux (see
# https://github.com/archlinux/svntogit-community/blob/packages/shairplay/trunk/shairplay.service)
Source1:        %{name}.service
Source2:        airtv.desktop
Source3:        airtv.metainfo.xml
# Fix dns_sd library load
Patch0:         %{name}-0.9.0-dns_sd.patch
# Load airport.key from /etc/ instead of the current directory
Patch1:         %{name}-0.9.0-key_path.patch
# Fix AirTV build
Patch2:         %{name}-0.9.0-AirTV_build.patch

BuildRequires:  avahi-compat-libdns_sd-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  phonon-devel
BuildRequires:  pkgconfig(ao)
BuildRequires:  qt-devel
BuildRequires:  systemd-rpm-macros
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       avahi%{?_isa}
Requires:       avahi-compat-libdns_sd%{?_isa}
Requires(pre):  shadow-utils
%{?systemd_requires}

%description
Free portable AirPlay server implementation similar to ShairPort. Currently only
AirPort Express emulation is supported.


%package libs
Summary:        Libraries for %{name}

%description libs
The %{name}-libs package contains the runtime shared libraries for %{name}.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       libao-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%package -n airtv
Summary:        Qt GUI to start a RAOP server
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       avahi-compat-libdns_sd%{?_isa}

%description -n airtv
AirTV Qt is a GUI to start a RAOP server. Once started, AirTV will add an icon
to the system tray using which you can stop the server.


%prep
%autosetup -n %{name}-%{commit} -p0


%build
[ -f configure ] || ./autogen.sh
%configure \
    --disable-static \
    --with-playfair
# Remove Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

# Build AirTV
pushd AirTV-Qt/
%{qmake_qt4}
%make_build
popd


%install
%make_install
find $RPM_BUILD_ROOT -name "*.la" -delete

install -Dpm 0644 airport.key $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/airport.key

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service

# Install AirTV
pushd AirTV-Qt/
install -Dpm 0755 AirTV $RPM_BUILD_ROOT%{_bindir}/AirTV
desktop-file-install \
    --dir=$RPM_BUILD_ROOT%{_datadir}/applications/ \
    %{SOURCE2}
install -Dpm 0644 images/airtv.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/airtv.svg
install -Dpm 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_metainfodir}/airtv.metainfo.xml


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/airtv.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/airtv.metainfo.xml


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/airport.key


%files libs
%license LICENSE
%{_libdir}/*.so.*


%files devel
%{_includedir}/*
%{_libdir}/*.so


%files -n airtv
%{_bindir}/AirTV
%{_datadir}/applications/airtv.desktop
%{_datadir}/icons/hicolor/*/apps/airtv.*
%{_metainfodir}/airtv.metainfo.xml


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-27.20180824git096b61a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.0-26.20180824git096b61a
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-25.20180824git096b61a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-24.20180824git096b61a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-23.20180824git096b61a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-22.20180824git096b61a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 07 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9.0-21.20180824git096b61a
- Update to latest snapshot

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-20.20160101gitce80e00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-19.20160101gitce80e00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-18.20160101gitce80e00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.0-17.20160101gitce80e00
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-16.20160101gitce80e00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-15.20160101gitce80e00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-14.20160101gitce80e00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-13.20160101gitce80e00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-12.20160101gitce80e00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-11.20160101gitce80e00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-10.20160101gitce80e00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-9.20160101gitce80e00
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8.20160101gitce80e00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7.20160101gitce80e00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6.20160101gitce80e00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 12 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9.0-5.20160101gitce80e00
- Update to latest snapshot

* Wed Feb 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.9.0-4.20150921git498bc5b
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Sep 30 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9.0-3.20150921git498bc5b
- Update to latest snapshot
- Add missing runtime dependency on Avahi
- Add AppData file for AirTV

* Mon Aug 17 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9.0-2.20150508git0f41ade
- Enable shairplay server build
- Enable AirTV GUI build

* Wed Jul 15 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9.0-1.20150508git0f41ade
- Initial RPM release
