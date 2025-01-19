
%undefine __cmake_in_source_build

Name:    kde-style-breeze 
Epoch:   1
Version: 5.18.5
Release: 14%{?dist}
Summary: KDE 4 version of Plasma 5 artwork, style and assets 

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://invent.kde.org/plasma/breeze
Source0: http://download.kde.org/stable/plasma/%{version}/breeze-%{version}.tar.xz
Patch0:  breeze-5.18.5-cstdint.patch

# filter plugin provides
%global __provides_exclude_from ^(%{_kde4_libdir}/kde4/.*\\.so)$

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kdelibs4-devel
BuildRequires:  libxcb-devel

Obsoletes:      plasma-breeze-kde4 < 5.1.95
Provides:       plasma-breeze-kde4%{?_isa} = %{version}-%{release}
# to consider ? -- rex
%if 0
Supplements: (kde-runtime and plasma-workspace)
%endif

%description
%{summary}.


%prep
%autosetup -p1 -n breeze-%{version}


%build

%global _vpath_builddir %{_target_platform}

%cmake_kde4 \
  -B %{_vpath_builddir} \
  -DUSE_KDE4:BOOL=TRUE

%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%{_libdir}/libbreezecommon4.so.5*
%{_kde4_libdir}/kde4/plugins/styles/breeze.so
%{_kde4_libdir}/kde4/kstyle_breeze_config.so
%{_kde4_appsdir}/kstyle/themes/breeze.themerc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.18.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1:5.18.5-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.18.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.18.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.18.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.18.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun May 28 2023 Robert Scheck <robert@fedoraproject.org> - 1:5.18.5-8
- Add missing cstdint include in libbreezecommon (#2171584, #2188911)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.18.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.18.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.18.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.18.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.18.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 03 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:5.18.5-2
- use cmake-macros
- update URL
- drop use of %%base_name

* Sat Oct 03 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:5.18.5-1
- 5.18.5, first try
- Epoch:1, for upgrade path from subpkg from plasma-5.19+
