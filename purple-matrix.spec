%global plugin_name matrix

Name: purple-%{plugin_name}
Version: 0.1.0
Release: 5%{?dist}

License: GPL-2.0-or-later
Summary: Matrix plugin for libpurple
URL: https://github.com/matrix-org/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/matrix-org/purple-matrix/pull/49
Patch0: %{name}-makefile-fixes.patch

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(olm)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(sqlite3)

BuildRequires: gcc
BuildRequires: http-parser-devel
BuildRequires: make

%package -n pidgin-%{plugin_name}
Summary: Adds pixmaps, icons and smileys for Matrix protocol
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: pidgin

%description
Adds support for Matrix to Pidgin, Adium, Finch and other libpurple
based messengers.

%description -n pidgin-%{plugin_name}
Adds pixmaps, icons and smileys for Matrix protocol implemented by
purple-matrix.

%prep
%autosetup -p1

%build
%set_build_flags
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md CHANGES.md AUTHORS.rst CONTRIBUTING.rst
%{_libdir}/purple-2/lib%{plugin_name}.so

%files -n pidgin-%{plugin_name}
%{_datadir}/pixmaps/pidgin/protocols/*/%{plugin_name}.png

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 27 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-1
- Updated to version 0.1.0.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-20.20191228git1d23385
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-19.20191228git1d23385
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-18.20191228git1d23385
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0-17.20191228git1d23385
- Rebuild for http-parser 2.9.4

* Tue Apr 07 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0-16.20191228git1d23385
- Updated to latest snapshot.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-15.20180927gitf26edd5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-14.20180927gitf26edd5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-13.20180927gitf26edd5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0-12.20180927gitf26edd5
- Rebuilt due to libolm update.

* Wed Nov 21 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0-11.20180927gitf26edd5
- Updated to latest snapshot.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20180325git49ea988
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 04 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0-9.20180325git49ea988
- Updated to latest snapshot.

* Sun Feb 25 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0-8.20180224gitca2f214
- Updated to latest snapshot.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20170902gitf4ab172
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 09 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-6.20170902gitf4ab172
- Updated to latest snapshot.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20170530gitbe53d53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20170530gitbe53d53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-3.20170530gitbe53d53
- Small fixes.

* Thu Jun 22 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-2.20170530gitbe53d53
- Small fixes.

* Thu Jun 22 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20170530gitbe53d53
- First SPEC release.
