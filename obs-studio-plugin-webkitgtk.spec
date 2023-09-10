%global srcname obs-webkitgtk
%global commit 0e32b92dde4197f2b0503fd2c7197f4230836793
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20201202

Name:           obs-studio-plugin-webkitgtk
Version:        0~git%{commitdate}.%{shortcommit}
Release:        4%{?dist}
Summary:        OBS Browser source plugin based on WebKitGTK

License:        GPL-2.0-or-later
URL:            https://github.com/fzwoch/obs-webkitgtk
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

# Fix load paths for webkitgtk helper
## From: https://github.com/fzwoch/obs-webkitgtk/pull/1
Patch0001:      0001-Support-libexec-and-lib64-paths-for-the-webkitgtk-he.patch

BuildRequires:  meson
BuildRequires:  gcc

BuildRequires:  pkgconfig(libobs)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.1)

Supplements:    obs-studio%{?_isa}

# Replace older packages
Obsoletes:      obs-webkitgtk < %{version}-%{release}
Provides:       obs-webkitgtk = %{version}-%{release}
Provides:       obs-webkitgtk%{?_isa} = %{version}-%{release}

%description
%{name}.

%prep
%autosetup -n %{srcname}-%{commit}

# Use webkit2gtk-4.1
# Cf. https://fedoraproject.org/wiki/Changes/Remove_webkit2gtk-4.0_API_Version
sed -e 's/webkit2gtk-4.0/webkit2gtk-4.1/g' -i meson.build


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE
%{_libexecdir}/obs-plugins/%{srcname}*
%{_libdir}/obs-plugins/%{srcname}*


%changelog
* Fri Sep 08 2023 Neal Gompa <ngompa@fedoraproject.org> - 0~git20201202.0e32b92-4
- Add patch to fix load path for webkitgtk helper (RH#2225973)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0~git20201202.0e32b92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 03 2023 Neal Gompa <ngompa@fedoraproject.org> - 0~git20201202.0e32b92-2
- Adapt for Fedora

* Wed Dec 28 2022 Neal Gompa <ngompa@fedoraproject.org> - 0~git20201202.0e32b92-1
- Initial packaging
