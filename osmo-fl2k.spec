# http://git.osmocom.org/osmo-fl2k
# https://github.com/osmocom/osmo-fl2k/
%global git_commit 197f421c98f929d4266a09bc9d667b7869e09c27
%global git_date 20211018

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:             osmo-fl2k
URL:              https://osmocom.org/projects/osmo-fl2k/wiki
Version:          0.1.1
Release:          0.14.%{git_suffix}%{?dist}
License:          GPLv2+ and GPLv3+
BuildRequires:    cmake, gcc-c++, libusbx-devel
Requires:         systemd-udev
Summary:          Turns FL2000-based USB 3.0 to VGA adapters into low cost DACs
Source0:          https://github.com/osmocom/osmo-fl2k/archive/%{git_commit}/%{name}-%{git_suffix}.tar.gz
Patch0:           osmo-fl2k-0.1.1-lib-version-fix.patch

%description
Turns FL2000-based USB 3.0 to VGA adapters into low cost DACs.

%package libs
Summary:          Libraries for osmo-fl2k

%description libs
Libraries for osmo-fl2k.

%package devel
Summary:          Development files for osmo-fl2k
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development files for osmo-fl2k.

%prep
%autosetup -p1 -n %{name}-%{git_commit}

%build
%cmake
%cmake_build

%install
%cmake_install

# Remove static objects
rm -f %{buildroot}%{_libdir}/libosmo-fl2k.a

# Fix udev rule
sed -i 's/MODE:="0666"/MODE:="0660", ENV{ID_SOFTWARE_RADIO}="1"/' ./osmo-fl2k.rules
install -Dpm 644 ./osmo-fl2k.rules %{buildroot}%{_prefix}/lib/udev/rules.d/10-osmo-fl2k.rules

%ldconfig_scriptlets

%files
%license COPYING
%{_bindir}/fl2k_file
%{_bindir}/fl2k_fm
%{_bindir}/fl2k_tcp
%{_bindir}/fl2k_test
%{_prefix}/lib/udev/rules.d/10-osmo-fl2k.rules

%files libs
%doc AUTHORS README.md
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.14.20211018git197f421c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.13.20211018git197f421c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-0.12.20211018git197f421c
- New version
  Resolves: rhbz#2014756
- Switched to github mirror

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.11.20190501gitdf33203d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.10.20190501gitdf33203d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug  5 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-0.9.20190501gitdf33203d
- Fixed FTBFS
  Resolves: rhbz#1865184

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.8.20190501gitdf33203d
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.7.20190501gitdf33203d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Jeff Law <law@redhat.com> - 0.1.1-0.6.20190501gitdf33203d
- Fix inline vs static inline issue exposed by LTO

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.5.20190501gitdf33203d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.4.20190501gitdf33203d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May  7 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-0.3.20190501gitdf33203d
- Updated according to the review

* Tue May  7 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-0.2.20190501gitdf33203d
- Updated according to the review

* Wed May  1 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-0.1.20190501gitdf33203d
- Initial version
