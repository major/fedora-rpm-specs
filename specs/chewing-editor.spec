%global snapdate 20240716
%global commit  0c25a466458dcf6ad94fa4ca3501babb85a3cce2
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           chewing-editor
Version:        0.1.1^%{snapdate}g%{shortcommit}
Release:        2%{?dist}
Summary:        Cross platform chewing user phrase editor
Summary(zh_TW): 跨平台酷音詞庫編輯器

# chewing-editor GPL-2.0-or-later
# gmock BSD-3-Clause
License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            https://github.com/chewing/chewing-editor
%if 0
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
%endif
Source0:        %{url}/archive/%{commit}.tar.gz#/chewing-editor-%{shortcommit}.tar.gz

BuildRequires:  cmake gcc-c++
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(chewing) >= 0.4.0
BuildRequires:  help2man
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
chewing-editor is a cross platform chewing user phrase editor. It provides a
easy way to manage user phrase. With it, user can customize their user phrase
to increase input performance.

%description -l zh_TW
chewing-editor 是一個跨平台的詞庫編輯器。它提供了簡單管理使用者詞庫的界面，
有了它，使用者可以自訂自己的詞庫來提高輸入效率。

%prep
%autosetup -p1 -n %{name}-%{commit}


%build
%cmake
%cmake_build


%install
%cmake_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/chewing-editor.desktop


%files
%license COPYING
%doc README.md
%{_bindir}/chewing-editor
%{_datadir}/applications/chewing-editor.desktop
%{_datadir}/icons/hicolor/scalable/apps/chewing-editor.svg
%{_datadir}/icons/hicolor/256x256/apps/chewing-editor.png
%{_mandir}/man1/chewing-editor.1.gz


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1^20240716g0c25a46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 27 2024 Kan-Ru Chen <kanru@kanru.info> - 0.1.1^20240716g0c25a46-1
- Initial import (fedora#2298050)

