Name:           tilda
Version:        2.0.0
Release:        4%{?dist}
Summary:        A Gtk based drop down terminal for Linux and Unix

# Automatically converted from old format: GPLv2 and MIT - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-MIT
URL:            http://github.com/lanoxx/tilda 
Source0:        https://github.com/lanoxx/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libconfuse-devel
BuildRequires:  libX11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXt-devel
BuildRequires:  vte291-devel

# License GPLv2
Provides:  bundled(eggaccelerators)
Provides:  bundled(xerror)
# License MIT
Provides:  bundled(tomboykeybinder)

%description
Tilda is a Linux terminal taking after the likeness of many classic terminals
from first person shooter games, Quake, Doom and Half-Life (to name a few),
where the terminal has no border and is hidden from the desktop until a key is
pressed.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
autoreconf -fi
%configure
%make_build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}

%make_install
desktop-file-install --vendor=""                               \
        --dir=%{buildroot}%{_datadir}/applications             \
        --mode 0644                                            \
        --remove-category="Application"                        \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

install -D -p -m 644 %{name}.png \
        %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README.md ChangeLog TODO.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/tilda-dbus.desktop
%{_datadir}/man/man1/tilda.1.gz
%{_metainfodir}/tilda.appdata.xml

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.0-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 05 2024 Johannes Lips <hannes@fedoraproject.org> - 2.0.0-1
- update to upstream version 2.0.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 08 2022 Leigh Scott <leigh123linux@gmail.com> - 1.5.4-5
- Fix wrong glib-devel build requires

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Johannes Lips <hannes@fedoraproject.org> - 1.5.4-1
- update to upstream version 1.5.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Johannes Lips <hannes@fedoraproject.org> - 1.5.1-1
- update to upstream version 1.5.1
- added the provides for bundled libraries
- additional license MIT for bundled library

* Fri May 01 2020 Johannes Lips <hannes@fedoraproject.org> - 1.5.0-1
- update to upstream version 1.5.0
- added fix to also run on Wayland

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Johannes Lips <hannes@fedoraproject.org> - 1.4.1-1
- update to upstream version 1.4.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.3-8
- Remove obsolete scriptlets

* Tue Aug 22 2017 Johannes Lips <hannes@fedoraproject.org> - 1.3.3-7
- libconfuse rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.3.3-4
- libconfuse rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Jon Ciesla <limburgher@gmail.com> - 1.3.3-2
- libconfuse rebuild.

* Sat Apr 30 2016 Johannes Lips <hannes@fedoraproject.org> - 1.3.3-1
- update to upstream version 1.3.3

* Mon Mar 14 2016 Johannes Lips <hannes@fedoraproject.org> - 1.3.2-1
- update to upstream version 1.3.2

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 22 2015 Johannes Lips <hannes@fedoraproject.org> - 1.2.4-1
- update to upstream version 1.2.4

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 17 2014 Johannes Lips <hannes@fedoraproject.org> - 1.2.2-1
- update to upstream version 1.2.2
- fixed bug #1164476

* Thu Oct 16 2014 Johannes Lips <hannes@fedoraproject.org> - 1.2.1-1
- update to upstream version 1.2.1

* Thu Oct 16 2014 Johannes Lips <hannes@fedoraproject.org> - 1.2-1
- update to upstream version 1.2

* Sun Sep 14 2014 Johannes Lips <hannes@fedoraproject.org> - 1.1.13-1
- Initial Release
