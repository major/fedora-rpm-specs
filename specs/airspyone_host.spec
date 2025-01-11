#%%global git_commit bfb667080936ca5c2d23b3282f5893931ec38d3f
#%%global git_date 20180615

#%%global git_short_commit %%(echo %%{git_commit} | cut -c -8)
#%%global git_suffix %%{git_date}git%%{git_short_commit}

Name:           airspyone_host
Version:        1.0.10
Release:        10%{?git_suffix}%{?dist}
Summary:        AirSpy host tools and library

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://airspy.com/
#Source:        https://github.com/airspy/%%{name}/archive/%%{git_commit}/%%{name}-%%{git_suffix}.tar.gz
Source:         https://github.com/airspy/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/airspy/airspyone_host/pull/98
Patch:          airspyone_host-1.0.10-c23-fix.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libusbx-devel
BuildRequires:  systemd
Requires:       systemd-udev

%description
Software for AirSpy, a project to produce a low cost, open
source software radio platform.

%package devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
License:        MIT and BSD
Summary:        Development files for %{name}

%description devel
Files needed to develop software against libairspy.

%prep
%autosetup -p1

# Remove win stuff
rm -rf libairspy/vc

# Fix udev rule
sed -i -e 's/GROUP="plugdev"/ENV{ID_SOFTWARE_RADIO}="1"/g' airspy-tools/52-airspy.rules

%build
%cmake -DINSTALL_UDEV_RULES=on

%cmake_build

%install
%cmake_install

# Remove static object
rm -f %{buildroot}%{_libdir}/libairspy.a

# Move udev rule to correct location
mkdir -p %{buildroot}%{_udevrulesdir}
mv %{buildroot}%{_sysconfdir}/udev/rules.d/52-airspy.rules %{buildroot}%{_udevrulesdir}

%post
%?ldconfig
%udev_rules_update

%postun
%?ldconfig
%udev_rules_update

%files
%license airspy-tools/LICENSE.md
%doc README.md
%{_bindir}/airspy_*
%{_libdir}/libairspy.so.*
%{_udevrulesdir}/52-airspy.rules

%files devel
%{_includedir}/libairspy
%{_libdir}/pkgconfig/libairspy.pc
%{_libdir}/libairspy.so

%changelog
* Thu Jan  9 2025 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.10-10
- Used upstream fix to enforce gnu17 standard
  Related: rhbz#2336033

* Tue Jan  7 2025 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.10-9
- Fixed bool conflict in C23
  Resolves: rhbz#2336033

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.10-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 11 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.10-1
- New version
  Resolves: rhbz#2105800

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-13.20180615gitbfb66708
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-12.20180615gitbfb66708
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-11.20180615gitbfb66708
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-10.20180615gitbfb66708
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-9.20180615gitbfb66708
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-8.20180615gitbfb66708
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-7.20180615gitbfb66708
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-6.20180615gitbfb66708
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.9-5.20180615gitbfb66708
- Fixed FTBFS by adding gcc-c++ requirement
  Resolves: rhbz#1603360

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4.20180615gitbfb66708
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.9-3.20180615gitbfb66708
- Various fixes according to review

* Fri Jun 15 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.9-2.20180615gitbfb66708
- Update for Fedora

* Mon Dec 19 2016 Dave Burgess <dvd.burgess@gmail.com> - 1.0.9-1
- Initial package
