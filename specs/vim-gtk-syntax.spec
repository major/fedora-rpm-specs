Name:           vim-gtk-syntax
Version:        20130716
Release:        23%{?dist}
Summary:        Vim syntax highlighting for GLib, Gtk+, Gstreamer, and more

# Automatically converted from old format: Public Domain - needs further work
License:        LicenseRef-Callaway-Public-Domain
URL:            http://www.vim.org/scripts/script.php?script_id=1000
#Source0:       http://www.vim.org/scripts/download_script.php?src_id=20534
# The source for this package was downloaded from the URL above, and renamed to
# include the version number:
# mv gtk-vim-syntax.tar.gz gtk-vim-syntax-20130716.tar.gz
Source0:        gtk-vim-syntax-20130716.tar.gz
Source1:        vim-gtk-syntax.metainfo.xml

BuildRequires:  /usr/bin/appstream-util
Requires:       vim-filesystem
BuildArch:      noarch

%description
A collection of C extension syntax files for xlib, glib (gobject, gio),
gdk-pixbuf, gtk2 (gdk2), gtk3 (gdk3), atk, at-spi, pango, cairo, clutter, gimp,
gstreamer, dbus-glib, json-glib, libglade, gtksourceview, gnome-desktop,
libgsf, libnotify, librsvg, libunique, libwnck, gtkglext, vte, poppler, evince. 

The xlib one was originally created by Hwanjin Choe (vimscript #570), the
others were generated from gtk-doc declaration lists and support
enabling/disabling of highlighting of deprecated declarations.

%prep
%setup -q -n gtk-vim-syntax


%build
# Nothing to build.


%install
install -d %{buildroot}%{_datadir}/vim/vimfiles/syntax
install -pm 0644 *.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml


%check
appstream-util validate %{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml --nonet


%files
%doc c.vim.example README
%{_datadir}/appdata/%{name}.metainfo.xml
%{_datadir}/vim/vimfiles/syntax


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20130716-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20130716-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20130716-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20130716-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20130716-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20130716-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20130716-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20130716-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20130716-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20130716-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20130716-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20130716-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20130716-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20130716-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20130716-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130716-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130716-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20130716-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130716-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 01 2014 David King <amigadave@amigadave.com> - 20130716-4
- Do not own the appdata directory

* Mon Aug 11 2014 David King <amigadave@amigadave.com> - 20130716-3
- Add AppStream metainfo file (#1128829)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130716-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 21 2014 David King <amigadave@amigadave.com> - 20130716-1
- Initial import (#985446)
