Name:           stacer
Version:        1.1.0
Release:        21%{?dist}
Summary:        Linux system optimizer and monitoring

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/oguzhaninan/Stacer
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Charts)
BuildRequires:  pkgconfig(Qt5Svg)

Requires:       hicolor-icon-theme
Requires:       qt5-qtcharts%{?_isa}

%description
Stacer is an open source system optimizer and application monitor that helps
users to manage entire system with different aspects, its an all in one system
utility.


%package        devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries files for developing applications
that use %{name}.


%prep
%autosetup -n Stacer-%{version}


%build
%qmake_qt5
%make_build

# Build translations
lrelease-qt5 stacer/stacer.pro

%install
install -Dp -m 0755 stacer/stacer \
    %{buildroot}%{_libdir}/stacer/stacer

mkdir -p            %{buildroot}%{_bindir}
ln -s               %{_libdir}/stacer/stacer \
    %{buildroot}%{_bindir}/stacer

install -D -m 0755  stacer-core/libstacer-core.so.1.0.0 \
    %{buildroot}%{_libdir}

ln -s   'libstacer-core.so.1.0.0' %{buildroot}%{_libdir}/libstacer-core.so.1.0
ln -s   'libstacer-core.so.1.0.0' %{buildroot}%{_libdir}/libstacer-core.so.1
ln -s   'libstacer-core.so.1.0.0' %{buildroot}%{_libdir}/libstacer-core.so
mkdir -p            %{buildroot}%{_datadir}
cp -ar              icons %{buildroot}%{_datadir}
install -D -m 0644  applications/stacer.desktop \
    %{buildroot}%{_datadir}/applications/stacer.desktop

# Install translations
mkdir   -p          %{buildroot}%{_libdir}/stacer/translations
install -D -m 0644  translations/*qm \
    %{buildroot}%{_libdir}/stacer/translations/

%find_lang %{name} --with-qt


%check
# https://github.com/oguzhaninan/Stacer/pull/283
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license LICENSE
%doc README.md
%dir %{_libdir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_libdir}/%{name}/%{name}
%{_libdir}/libstacer-core.so.1*

# Translations files which rpm macros cant handle
%dir %{_libdir}/%{name}/translations/
%{_libdir}/%{name}/translations/stacer_ca-es.qm
%{_libdir}/%{name}/translations/stacer_zh-cn.qm
%{_libdir}/%{name}/translations/stacer_zh-tw.qm

%files devel
%{_libdir}/libstacer-core.so


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.0-20
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb 27 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-12
- build: Add qt5-qtcharts dep | RH#1933328

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-8
- Cosmetic spec file fixes
- Enable LTO

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-6
- Initial package
