%global newname gfeeds
%global uuid org.gabmus.%{newname}

Name: gnome-feeds
Version: 0.16.2
Release: 7%{?dist}
Summary: RSS/Atom feed reader for GNOME
BuildArch: noarch

License: GPLv3+
URL: https://gabmus.gitlab.io/gnome-feeds
Source0: https://gitlab.com/gabmus/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: libappstream-glib
BuildRequires: meson >= 0.50.0
BuildRequires: python3-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk+-3.0)

Requires: dbus-common
Requires: glib2
Requires: hicolor-icon-theme
Requires: libhandy1
Requires: python3-beautifulsoup4
Requires: python3-brotli
Requires: python3-feedparser
Requires: python3-html5lib
Requires: python3-listparser
Requires: python3-lxml
Requires: python3-pillow
Requires: python3-pygments
Requires: python3-pytz
Requires: python3-readability-lxml
Requires: python3-requests

%description
GNOME Feeds is a minimal RSS/Atom feed reader built with speed and simplicity
in mind.

It offers a simple user interface that only shows the latest news from your
subscriptions.

Articles are shown in a web view by default, with javascript disabled for a
faster and less intrusive user experience. There's also a reader mode
included, built from the one GNOME Web/Epiphany uses.

Feeds can be imported and exported via OPML.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{newname} --with-gnome


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{newname}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{newname}
%{_datadir}/%{newname}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml
%{python3_sitelib}/%{newname}/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.16.2-6
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.16.2-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.16.2-1
- build(update): 0.16.2

* Fri Nov 13 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.16.1-1
- build(update): 0.16.1

* Thu Nov 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.16-1
- build(update): 0.16

* Wed Sep 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.15-1
- Update to 0.15

* Sat Aug 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.14.1-3
- Add libhandy1 compatibility patch

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.14.1-1
- Updato to 0.14.1
- Migrate to 'libhandy1'

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.4-5
- Rebuilt for Python 3.9

* Tue May 05 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.4-4
- Rebuilt for F32 | https://pagure.io/releng/issue/9436

* Sun Mar 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.4-3
- Add dep: python3-pygments

* Sat Mar 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.4-2
- Add dep: python3-beautifulsoup4 | RHBZ#1818526

* Fri Mar 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.4-1
- Update to 0.13.4

* Thu Mar 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.3-1
- Update to 0.13.3
- Add new dep: python3-readability-lxml

* Thu Mar 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.2-1
- Update to 0.13.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.12-1
- Update to 0.12

* Sun Oct 06 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.11-1
- Update to 0.11

* Thu Sep 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.10-3
- Add missed dependency 'python3-pytz'

* Mon Sep 16 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.10-2
- Add missed Requires

* Sun Sep 15 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.10-1
- Update to 0.10

* Sat Sep 07 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9-2
- Add missed new dependency 'python3-brotli'

* Sat Sep 07 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9-1
- Update to 0.9

* Wed Sep 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8-1
- Update to 0.8

* Fri Aug 23 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7-1
- Update to 0.7

* Wed Aug 14 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6-1
- Update to 0.6

* Sat Aug 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.2-3
- Initial package
