Name: ghostwriter
Version: 2.2.0
Release: 1%{?dist}

License: GPLv3+ and CC-BY and CC-BY-SA and MPLv1.1 and BSD and LGPLv3 and MIT and ISC
Summary: Cross-platform, aesthetic, distraction-free Markdown editor
URL: https://github.com/wereturtle/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Help)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5WebEngine)
BuildRequires: cmake(Qt5WebEngineWidgets)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5XmlPatterns)

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: hunspell-devel
BuildRequires: libappstream-glib
BuildRequires: make

Provides: bundled(cmark-gfm) = 0.29.0.gfm.3
Provides: bundled(fontawesome-fonts) = 5.10.2
Provides: bundled(nodejs-mathjax-full) = 3.1.2
Provides: bundled(nodejs-react) = 17.0.1
Provides: bundled(QtAwesome) = 5

Requires: hicolor-icon-theme

Recommends: cmark%{?_isa}
Recommends: multimarkdown%{?_isa}
Recommends: pandoc%{?_isa}

# Required qt5-qtwebengine is not available on some arches.
ExclusiveArch: %{qt5_qtwebengine_arches}

%description
Ghostwriter is a text editor for Markdown, which is a plain text markup
format created by John Gruber. For more information about Markdown, please
visit John Gruber’s website at http://www.daringfireball.net.

Ghostwriter provides a relaxing, distraction-free writing environment,
whether your masterpiece be that next blog post, your school paper,
or your novel.

%prep
%autosetup -n %{name}-%{version} -p1
mkdir -p %{_vpath_builddir}
rm -rf 3rdparty/hunspell

%build
pushd %{_vpath_builddir}
    %qmake_qt5 PREFIX=%{_prefix} ..
popd
%make_build -C %{_vpath_builddir}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_vpath_builddir}
%find_lang %{name} --with-qt

%files -f %{name}.lang
%doc CHANGELOG.md CONTRIBUTING.md CREDITS.md README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%dir %{_datadir}/ghostwriter
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_metainfodir}/%{name}.appdata.xml

%changelog
* Mon Sep 19 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2.0-1
- Updated to version 2.2.0.

* Wed Sep 14 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.6-1
- Updated to version 2.1.6.

* Sun Sep 11 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.5-1
- Updated to version 2.1.5.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.4-1
- Updated to version 2.1.4.

* Sun May 29 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.3-1
- Updated to version 2.1.3.

* Mon Mar 14 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.2-1
- Updated to version 2.1.2 with CVE-2022-24724 vulnerability fix.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 26 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.1-1
- Updated to version 2.1.1.

* Sun Nov 21 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.0-1
- Updated to version 2.1.0.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 27 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.2-1
- Updated to version 2.0.2.

* Tue May 18 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.1-1
- Updated to version 2.0.1.

* Sun May 09 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-2
- Added supported Markdown exporters as weak dependencies.

* Sun May 09 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-1
- Updated to version 2.0.0.

* Sun Jan 31 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-0.1.rc4
- Updated to version 2.0.0 (RC4).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 23 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.8.1-1
- Updated to version 1.8.1.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.8.0-1
- Updated to version 1.8.0.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.7.4-1
- Updated to version 1.7.4.

* Sat Oct 27 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.7.3-1
- Initial SPEC release.
