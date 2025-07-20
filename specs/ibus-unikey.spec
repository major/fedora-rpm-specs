%global source_version %%(echo "%version" | tr '~' '-')
%global commit 46b5b9e4bfb75fbccc5043b07ef5c76a3cc72ce3
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          ibus-unikey
Version:       0.7.0~beta1
Release:       %autorelease
Summary:       Vietnamese engine for IBus input platform

License:       GPL-3.0-only
URL:           https://github.com/vn-input/ibus-unikey/
Source0:       https://github.com/vn-input/ibus-unikey/archive/refs/tags/%{source_version}.tar.gz#/%{name}-%{source_version}.tar.gz
Patch1:        %{name}-2267853-super-space.patch
Patch2:        %{name}-2257688-segv-load-config.patch
Patch3:        %{name}-2380650-cmake-4.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: ibus-devel
BuildRequires: gtk3-devel
BuildRequires: intltool
BuildRequires: pkgconf-pkg-config

Requires: ibus

%description
A Vietnamese engine for IBus input platform that uses Unikey.


%prep
%autosetup -p1 -n %{name}-%{source_version}

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name}


%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_datadir}/%{name}/
%{_datadir}/ibus/component/unikey.xml
%{_libexecdir}/ibus-engine-unikey
%{_libexecdir}/ibus-setup-unikey
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.unikey.gschema.xml

%changelog
%autochangelog

