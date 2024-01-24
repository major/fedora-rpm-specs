%global __provides_exclude_from ^%{_qt5_plugindir}/.*\\.so$

Name: qt-jdenticon
Version: 0.3.0
Release: 6%{?dist}

License: MIT
Summary: Jdenticon Qt5 plugin
URL: https://github.com/Nheko-Reborn/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: qt5-qtbase-devel

%description
Special Qt5/C++14 port of Jdenticon distributed as a Qt plugin.

The eventual plan for this is that it will be made into a Qt5 library that can
be used in other applications with a command-line application for use as a
standalone generator.

%prep
%autosetup -p1

%build
%qmake_qt5 QtIdenticon.pro
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%if 0%{?flatpak}
# qtbase is part of runtime in /usr, this is built in /app
mv %{buildroot}/usr %{buildroot}/app
%endif

%files
%doc README.md
%license LICENSE
%{_qt5_plugindir}/libqtjdenticon.so

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.0-1
- Updated to version 0.3.0.

* Fri Nov 19 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.1-1
- Initial SPEC release.
