Name:          awf-gtk3
Version:       3.2.0
Release:       3%{?dist}
Summary:       Theme preview application for GTK 3
Summary(fr):   Application d'aperçu de thème pour GTK 3
License:       GPL-3.0-or-later
URL:           https://github.com/luigifab/awf-extended
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: aspell-fr
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: desktop-file-utils
BuildRequires: libnotify-devel >= 0.7.0
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: gtk3-devel
Requires:      gtk3
Requires:      libnotify >= 0.7.0
Requires:      hicolor-icon-theme

%description %{expand:
A widget factory is a theme preview application for GTK. It displays the
various widget types provided by GTK in a single window allowing to see
the visual effect of the applied theme.

This package provides the GTK 3 version.}

%description -l fr %{expand:
La fabrique à widgets est une application d'aperçu de thème pour GTK. Elle
affiche les différents types de widgets fournis par GTK dans une seule
fenêtre permettant de voir l'effet visuel du thème appliqué.

Ce paquet fournit la version GTK 3.}


%prep
%setup -q -n awf-extended-%{version}

%build
autoreconf -fi
%configure --enable-only-gtk3
%make_build

%install
%make_install
install -dm 755 %{buildroot}%{_datadir}/applications/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ data/%{name}.desktop

install -dm 755 %{buildroot}%{_datadir}/icons/hicolor/
for file in data/icons/*/*/awf.png; do mv $file ${file/\/awf.png/\/%{name}.png}; done
for file in data/icons/*/*/awf.svg; do mv $file ${file/\/awf.svg/\/%{name}.svg}; done
cp -a data/icons/* %{buildroot}%{_datadir}/icons/hicolor/

install -Dpm 644 data/%{name}.bash %{buildroot}%{bash_completions_dir}/%{name}
install -Dpm 644 data/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -Dpm 644 data/%{name}.fr.1 %{buildroot}%{_mandir}/fr/man1/%{name}.1

for file in src/po/*.po; do
  code=$(basename "$file" .po)
  install -dm 755 %{buildroot}%{_datadir}/locale/$code/LC_MESSAGES/
  msgfmt src/po/$code.po -o %{buildroot}%{_datadir}/locale/$code/LC_MESSAGES/%{name}.mo
done
%find_lang %{name} --with-man

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{bash_completions_dir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Oct 10 2025 Fabrice Creuzot <code@luigifab.fr> - 3.2.0-1
- New upstream release

* Fri Aug 08 2025 Fabrice Creuzot <code@luigifab.fr> - 3.1.0-1
- New upstream release
- Add support for CSD dialog

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon May 05 2025 Fabrice Creuzot <code@luigifab.fr> - 3.0.0-1
- New upstream release
- Add support for CSD window
- Add --enable-only-gtkx and --disable-gtkx options

* Fri Apr 04 2025 Fabrice Creuzot <code@luigifab.fr> - 2.9.0-1
- New upstream release

* Mon Mar 03 2025 Fabrice Creuzot <code@luigifab.fr> - 2.8.1-1
- New upstream release

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 msuchy <msuchy@redhat.com> - 2.8.0-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 02 2024 Fabrice Creuzot <code@luigifab.fr> - 2.8.0-1
- New upstream release

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Fabrice Creuzot <code@luigifab.fr> - 2.7.0-2
- Package spec update

* Tue Jun 06 2023 Fabrice Creuzot <code@luigifab.fr> - 2.7.0-1
- New upstream release

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 09 2021 Fabrice Creuzot <code@luigifab.fr> - 2.6.0-1
- New upstream release

* Wed Jul 07 2021 Fabrice Creuzot <code@luigifab.fr> - 2.5.0-1
- New upstream release

* Wed May 05 2021 Fabrice Creuzot <code@luigifab.fr> - 2.4.0-1
- New upstream release

* Sun Apr 04 2021 Fabrice Creuzot <code@luigifab.fr> - 2.3.0-1
- New upstream release

* Wed Nov 11 2020 Fabrice Creuzot <code@luigifab.fr> - 2.2.0-1
- Initial Fedora package release (Closes: rhbz#1893323)
