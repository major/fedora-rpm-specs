%global engine_name unico
%global revision 152
%global revision_date 20140109

Name:           gtk-unico-engine
Version:        1.0.3
Release:        0.27.%{revision_date}bzr%{revision}%{?dist}
Summary:        Unico Gtk+ theming engine

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://launchpad.net/unico/
# The source for this package was pulled from upstream's VCS. Use the following
# commands to generate the tarball:
# $ bzr export -r %%{revision} %%{engine_name}-%%{version}-bzr%%{revision}.tar.xz lp:unico
Source0:        %{engine_name}-%{version}-bzr%{revision}.tar.xz

BuildRequires:  gnome-common
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires: make

%description
Unico is a Gtk+ engine that aims to be the more complete yet powerful theming
engine for Gtk+ 3.0 and newer. It’s the first Gtk+ engine written with Gtk+
style context APIs in mind, using CSS as first class citizen.


%prep
%setup -q -n %{engine_name}-%{version}-bzr%{revision}


%build
[ -f autogen.sh ] && NOCONFIGURE=1 ./autogen.sh
%configure \
  --disable-silent-rules \
  --disable-static
make %{?_smp_mflags}


%install
%make_install

rm $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/3.0.0/theming-engines/*.la


%files
# TODO: add ChangeLog and README if non-empty
%doc AUTHORS COPYING NEWS
%{_libdir}/gtk-3.0/3.0.0/theming-engines/lib%{engine_name}.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.27.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.3-0.26.20140109bzr152
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.25.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.24.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.23.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.22.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.21.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.20.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.19.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.18.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.17.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.16.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.15.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.14.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.13.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.12.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.11.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.10.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.9.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.8.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.7.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-0.6.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-0.5.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-0.4.20140109bzr152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.3-0.3.20140109bzr152
- Update to a newer bzr snapshot (sync with Ubuntu 14.04)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-0.2.20121212bzr146
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 07 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.3-0.1.20121212bzr146
- Update to a newer bzr snapshot

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3.20120808bzr139
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 21 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.2-1.20120808bzr139
- Update to a newer bzr snapshot

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 30 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Thu Mar 22 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.1-5.20120229bzr132
- Update to a newer bzr snapshot

* Fri Feb 24 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.1-4.20120224bzr130
- Update to a newer bzr snapshot

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 03 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.1-2
- Remove useless IM scriptlets

* Thu Sep 29 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.1-1
- Initial RPM release
