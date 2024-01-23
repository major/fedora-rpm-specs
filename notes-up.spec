%global uuid    com.github.philip_scott.%{name}

Name:           notes-up
Version:        2.0.6
Release:        6%{?dist}
Summary:        Markdown notes editor & manager

# The entire source code is GPLv2+ except:
# BSD:          highlight.LICENSE
License:        GPLv2+ and BSD
URL:            https://github.com/Philip-Scott/Notes-up
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9.10
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(libmarkdown)
BuildRequires:  pkgconfig(sqlite3) >= 3.5.9
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       hicolor-icon-theme

%description
The intuitive writing app for everyone, from students to developers.

With powerful features like:

- Easy-to-use markdown editor.
- Notebooks and tags, quickly find and organize your notes.
- Your work is saved automatically as you write, you will never loose
  your work.
- Plugins: such as embedding YouTube videos and setting text color.
- Export as PDF and Markdown files.
- Cross-Note Links to quickly reference other notes.
- 3 Beautiful app themes to help you create the best writing environment.
- And much more!


%prep
%autosetup -n Notes-up-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{uuid}

# Remove HiDPI dupes
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/@2/


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{uuid}.lang
%doc README.md
%license LICENSE data/assets/highlightjs/highlight.LICENSE
%{_bindir}/%{uuid}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 03 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.6-1
- chore(update): 2.0.6

* Thu Nov 25 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.5-1
- chore(update): 2.0.5

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-8
- Rebuilt for granite 6 soname bump.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep  2 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.2-6
- Backport patches for new Vala compatibility | Fix FTBFS f33 | RH#1865072

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.2-4
- Rebuild with out-of-source builds new CMake macros

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.2-1
- Update to 2.0.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.0-3
- Initial package
