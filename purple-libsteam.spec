%global repo_name pidgin-opensteamworks
%global plugin_name libsteam
%global dir_name steam-mobile

Name: purple-%{plugin_name}
Version: 1.7.1
Release: 3%{?dist}

License: GPL-3.0-or-later
URL: https://github.com/EionRobb/%{repo_name}
Summary: Steam plugin for Pidgin/Adium/libpurple
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(zlib)

BuildRequires: gcc
BuildRequires: make

%package -n pidgin-%{plugin_name}
Summary: Adds pixmaps, icons and smileys for Steam protocol
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: pidgin

%description
Adds support for Steam to Pidgin, Adium, Finch and other libpurple 
based messengers.

%description -n pidgin-%{plugin_name}
Adds pixmaps, icons and smileys for Steam protocol implemented by steam-mobile.

%prep
%autosetup -n %{repo_name}-%{version}

# fix W: wrong-file-end-of-line-encoding
sed -i -e "s,\r,," README.md

%build
%set_build_flags
%make_build -C %{dir_name}

%install
%make_install -C %{dir_name}
chmod 755 %{buildroot}%{_libdir}/purple-2/%{plugin_name}.so

%files
%{_libdir}/purple-2/%{plugin_name}.so
%doc README.md
%license %{dir_name}/LICENSE

%files -n pidgin-%{plugin_name}
%{_datadir}/pixmaps/pidgin/protocols/*/steam.png

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 27 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.7.1-1
- Updated to version 1.7.1.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 04 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.7-1
- Updated to version 1.7 (regular release).

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-26.20190117gitfeece3c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 22 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-25.20190117gitfeece3c
- Updated to latest snapshot.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-24.20180801gitb16a636
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 03 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-23.20180801gitb16a636
- Updated to latest snapshot.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-22.20180514git4a09c08
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-21.20180514git4a09c08
- Updated to latest snapshot.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-20.20171225git7f761df
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-19.20171225git7f761df
- Updated to latest snapshot.

* Tue Jan 23 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-18.20170929gitab6d446
- Fixed build under Fedora Rawhide.

* Sun Oct 08 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-17.20170929gitab6d446
- Minor SPEC changes. Fixed build under Rawhide.

* Sun Oct 08 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-16.20170929gitab6d446
- Updated to latest snapshot.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-15.20160618git0f51fd6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-14.20160618git0f51fd6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-13.20160618git0f51fd6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 21 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-12.20160618git0f51fd6
- Updated to latest Git snapshot. Added missing LDFLAGS to build.

* Sun Jun 19 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-11.20160618gitcd5a294
- Updated to latest Git snapshot.

* Sat Jun 18 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-10.20160416gitbf7dd28
- Updated package description.

* Sun Jun 12 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-9.20160416gitbf7dd28
- Removed empty configure script.

* Mon May 02 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-8.20160416gitbf7dd28
- Updated to latest version from Git.

* Fri Mar 04 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-7.20160218git5a5beba
- Updated to latest version from Git.

* Tue Feb 16 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-6.20160216git9d51f30
- Updated to latest version from Git.

* Tue Jan 12 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-5.20160108git8646d36
- Updated to latest version from Git.

* Thu Dec 24 2015 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-4.20151224gitef6215f
- Updated to latest version.

* Fri Dec 04 2015 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-3.20151204git72fdb9d
- Added license file.

* Sun Nov 29 2015 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-2.20151115git5aef56a
- Applyed Maxim Orlov's fixes.

* Wed Oct 14 2015 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-1
- Created first RPM spec for Fedora/openSUSE.
