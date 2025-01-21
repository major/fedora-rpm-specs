Name:		wfview
URL:		https://gitlab.com/eliggett/wfview/
Version:	1.64
Release:	4%{?dist}
License:	GPL-3.0-only
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	pkgconf-pkg-config
BuildRequires:	desktop-file-utils
# for "appstream-util validate-relax"
BuildRequires:	libappstream-glib
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qtserialport-devel
BuildRequires:	qt5-qtmultimedia-devel
BuildRequires:	qt5-qtgamepad-devel
BuildRequires:	qcustomplot-qt5-devel
BuildRequires:	systemd-devel
BuildRequires:	opus-devel
BuildRequires:	eigen3-devel
BuildRequires:	hidapi-devel
BuildRequires:	portaudio-devel
BuildRequires:	rtaudio-devel
BuildRequires:	speexdsp-devel
BuildRequires:	systemd-rpm-macros
%{?sysusers_requires_compat}
BuildRequires:	hicolor-icon-theme
Requires:	hicolor-icon-theme
Summary:	Software for the control of Icom radios
Source0:	%{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Source1:	wfserver.sysusers
Source2:	wfserver.service
# drop when upstreamed
# https://gitlab.com/eliggett/wfview/-/commit/b68874d32878278e6e84668aaa44534255e7e1f5
Source3:	wfview.png
Source4:	wfserver.conf
Source5:	README.fedora
# https://gitlab.com/eliggett/wfview/-/issues/147
Patch0:		wfview-1.64-sane-build-defines.patch
# https://gitlab.com/eliggett/wfview/-/issues/147
Patch1:		wfview-1.64-qcustomplot-pkgconfig.patch
# https://gitlab.com/eliggett/wfview/-/issues/147
Patch2:		wfview-1.64-no-strip.patch
# https://gitlab.com/eliggett/wfview/-/commit/b68874d32878278e6e84668aaa44534255e7e1f5
Patch3:		wfview-1.64-appstream-metainfo.patch
# https://gitlab.com/eliggett/wfview/-/commit/1805861274019beb996391828ed800abd794bef0
Patch4:		wfview-1.64-pmr-fix.patch
# https://gitlab.com/eliggett/wfview/-/issues/147
Patch5:		wfview-1.64-system-speexdsp.patch
# https://gitlab.com/eliggett/wfview/-/merge_requests/23
Patch6:		wfview-1.64-dtr-support.patch
# https://gitlab.com/eliggett/wfview/-/merge_requests/24
Patch7:		wfview-1.64-increase-poll.patch
# https://gitlab.com/eliggett/wfview/-/merge_requests/25
Patch8:		wfview-1.64-ic706mk2g-preamp-fix.patch
# https://gitlab.com/eliggett/wfview/-/merge_requests/26
Patch9:		wfview-1.64-s390x-build-fix.patch

%description
The wfview is open-source software for the control of modern Icom radios,
including the IC-7300, IC-7610, IC-705, IC-R8600 and IC-9700. USB and
LAN are supported.

%prep
%autosetup -n %{name}-v%{version} -p1

cp %{SOURCE5} .

# unbundle speexdsp
rm -f resampler/*
rmdir resampler

# drop when upstreamed
# https://gitlab.com/eliggett/wfview/-/commit/b68874d32878278e6e84668aaa44534255e7e1f5
mkdir -p resources/unix_icons
cp %{SOURCE3} resources/unix_icons/%{name}.png

%build
mkdir %{name} wfserver
pushd %{name}
%{qmake_qt5} PREFIX=%{_prefix} ../%{name}.pro
%make_build
popd
pushd wfserver
%{qmake_qt5} PREFIX=%{_prefix} ../wfserver.pro
%make_build
popd

%install
pushd %{name}
%make_install INSTALL_ROOT=%{buildroot}
popd
pushd wfserver
%make_install INSTALL_ROOT=%{buildroot}
popd

# systemd-sysusers
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/wfserver.conf

# systemd service
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_unitdir}/wfserver.service

# install default service configuration file
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/wfserver.conf

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.%{name}.%{name}.metainfo.xml

%pre
# Add user and groups if necessary
%sysusers_create_compat %{SOURCE1}

%post
%systemd_post wfserver.service

%preun
%systemd_preun wfserver.service

%postun
%systemd_postun_with_restart wfserver.service

%files
%license LICENSE
%doc WHATSNEW README.md RIG_ISSUES_AND_LIMITS.md CONTRIBUTING.md CI-V.md
%doc CHANGELOG README.fedora
%config(noreplace) %{_sysconfdir}/wfserver.conf
%{_unitdir}/wfserver.service
%{_bindir}/wfview
%{_bindir}/wfserver
%{_datadir}/wfview
# systemd-sysusers
%{_sysusersdir}/wfserver.conf
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/org.wfview.wfview.metainfo.xml

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 28 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 1.64-3
- Added some more not yet upstreamed patches

* Thu Oct 24 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 1.64-2
- Updated according to the review

* Sun Oct 20 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 1.64-1
- Initial version
