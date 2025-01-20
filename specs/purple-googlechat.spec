%global plugin_name googlechat

%global commit0 ddc118bdb46f02d865ae56b470cf3176520df59b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20240101

Name: purple-%{plugin_name}
Version: 0
Release: 5.%{date}git%{shortcommit0}%{?dist}

License: GPL-3.0-or-later
Summary: Google Chat plugin for libpurple
URL: https://github.com/EionRobb/%{name}
Source0: %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libprotobuf-c)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(zlib)

BuildRequires: gcc
BuildRequires: make

Provides: purple-hangouts = 1:%{version}-%{release}
Obsoletes: purple-hangouts < 1:0-80.20210629git55b9f01

%package -n pidgin-%{plugin_name}
Summary: Adds pixmaps, icons and smileys for Google Chat protocol
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: pidgin
Provides: pidgin-hangouts = 1:%{version}-%{release}
Obsoletes: pidgin-hangouts < 1:0-80.20210629git55b9f01

%description
Adds support for Google Chat to Pidgin, Adium, Finch and other libpurple
based messengers.

%description -n pidgin-%{plugin_name}
Adds pixmaps, icons and smileys for Google Chat protocol implemented by
purple-googlechat.

%prep
%autosetup -n %{name}-%{commit0}

# fix W: wrong-file-end-of-line-encoding
sed -i -e "s,\r,," README.md

%build
%set_build_flags
%make_build

%install
%make_install
chmod 755 %{buildroot}%{_libdir}/purple-2/lib%{plugin_name}.so

%files
%{_libdir}/purple-2/lib%{plugin_name}.so
%license LICENSE
%doc README.md

%files -n pidgin-%{plugin_name}
%{_datadir}/pixmaps/pidgin/protocols/*/%{plugin_name}.png

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20240101gitddc118b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 21 2024 Jan Kratochvil <jan@jankratochvil.net> - 0-4.20240101gitddc118b
- Update to the latest snapshot.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.20221106gitb6b824a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.20221106gitb6b824a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 06 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20221106gitb6b824a
- Initial SPEC release.
