Name:           ibus-array
Version:        0.3.0
Release:        %autorelease
Summary:        The Array 30 input method for IBus input platform
Summary(zh_TW): IBus行列30輸入法
License:        GPL-2.0-or-later
URL:            https://github.com/lexical/ibus-array
Source0:        %{url}/archive/refs/tags/release-%{version}.tar.gz#/ibus-array-release-%{version}.tar.gz

Patch0:         0001-remove-unused-python3-shebang.patch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconf
BuildRequires:  python3-devel
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(opencc)
Requires:   ibus

%description
Array 30 input method for IBus that uses the latest keymap table
and follows the Array input method spec implementation.

%description -l zh_TW
IBus行列30輸入法，遵循行列輸入法規格書的定義，
含最新鍵碼表版本，符合一般行列輸入法用戶的慣用方式。

%prep
%autosetup -p1 -n %{name}-release-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README ChangeLog
%license COPYING
%{_datadir}/ibus-array
%{_libexecdir}/ibus-engine-array
%{_libexecdir}/ibus-setup-array
%{_datadir}/ibus/component/array.xml

%changelog
%autochangelog
