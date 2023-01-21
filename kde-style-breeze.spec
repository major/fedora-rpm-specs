
%undefine __cmake_in_source_build

Name:    kde-style-breeze 
Epoch:   1
Version: 5.18.5
Release: 7%{?dist}
Summary: KDE 4 version of Plasma 5 artwork, style and assets 

License: GPLv2+
URL:     https://invent.kde.org/plasma/breeze
Source0: http://download.kde.org/stable/plasma/%{version}/breeze-%{version}.tar.xz

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
%autosetup -n breeze-%{version}


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
