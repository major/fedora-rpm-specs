Name:    kf6
# This version MUST remain in sync with released KF6 versions!
# XXX: Right now, there is no released kf6, so version 0.0
Version: 0.0
Release: 1%{?dist}
Summary: Filesystem and RPM macros for KDE Frameworks 6
License: BSD-3-Clause
URL:     http://www.kde.org
Source0: macros.kf6
Source1: LICENSE

%description
Filesystem and RPM macros for KDE Frameworks 6

%package filesystem
Summary: Filesystem for KDE Frameworks 6
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
Requires: kde-filesystem >= 5
%endif
%{?_qt6_version:Requires: qt6-qtbase >= %{_qt6_version}}
%description filesystem
Filesystem for KDE Frameworks 6.

%package rpm-macros
Summary: RPM macros for KDE Frameworks 6
Requires: cmake >= 3
Requires: qt6-rpm-macros >= 6
# misc build environment dependencies
Requires: gcc-c++
BuildArch: noarch
%description rpm-macros
RPM macros for building KDE Frameworks 6 packages.

%install
# See macros.kf6 where the directories are specified
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt6/plugins/kf6/
mkdir -p %{buildroot}%{_includedir}/kf6
mkdir -p %{buildroot}%{_includedir}/KF6
mkdir -p %{buildroot}%{_datadir}/{kf6,kservicetypes6}
mkdir -p %{buildroot}%{_datadir}/kservices6/ServiceMenus
mkdir -p %{buildroot}%{_datadir}/qlogging-categories6/
mkdir -p %{buildroot}%{_docdir}/qt6
mkdir -p %{buildroot}%{_libexecdir}/kf6
mkdir -p %{buildroot}%{_datadir}/kf6/
%if ! (0%{?fedora} >= 40 || 0%{?rhel} >= 10)
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/kconf_update_bin
mkdir -p %{buildroot}%{_datadir}/{config.kcfg,kconf_update}
mkdir -p %{buildroot}%{_datadir}/kpackage/{genericqml,kcms}
mkdir -p %{buildroot}%{_datadir}/knsrcfiles/
mkdir -p %{buildroot}%{_datadir}/solid/{actions,devices}
mkdir -p %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/{env,shutdown}
%endif

install -Dpm644 %{_sourcedir}/macros.kf6 %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf6
install -Dpm644 %{_sourcedir}/LICENSE %{buildroot}%{_datadir}/kf6/LICENSE
sed -i \
  -e "s|@@kf6_VERSION@@|%{version}|g" \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf6

%files filesystem
%{_datadir}/kf6/
%{_datadir}/kservices6/
%{_datadir}/kservicetypes6/
%{_datadir}/qlogging-categories6/
%{_docdir}/qt6/
%{_includedir}/kf6/
%{_includedir}/KF6/
%{_libexecdir}/kf6/
%{_prefix}/%{_lib}/qt6/plugins/kf6/
%{_prefix}/lib/qt6/plugins/kf6/
%if ! (0%{?fedora} >= 40 || 0%{?rhel} >= 10)
%{_datadir}/config.kcfg/
%{_datadir}/kconf_update/
%{_datadir}/knsrcfiles/
%{_datadir}/kpackage/
%{_datadir}/solid/
%{_prefix}/%{_lib}/kconf_update_bin/
%{_prefix}/lib/kconf_update_bin/
%{_sysconfdir}/xdg/plasma-workspace/
%endif

%files rpm-macros
%{_rpmconfigdir}/macros.d/macros.kf6

%changelog
* Fri Sep 15 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.0-1
- Version reset in preparation for kf6 initial release

* Thu Sep 14 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 7-2
- Use kde-filesystem for unversioned directories in F40+

* Fri Sep 8 2023 Justin Zobel <justin@1707.io> 7-1
- Create and own /usr/include/KF6

* Thu Mar 2 2023 Justin Zobel <justin@1707.io> 6-1
- Initial Version

