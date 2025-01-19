Name:           ignuit
Version:        2.24.3
Release:        19%{?dist}
Summary:        Memorization aid based on the Leitner flashcard system

# Automatically converted from old format: GPLv3+ and GPLv2 - review is highly recommended.
License:        GPL-3.0-or-later AND GPL-2.0-only
URL:            http://crash.ihug.co.nz/~trmusson/programs.html
Source0:        http://crash.ihug.co.nz/~trmusson/stuff/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gstreamer1-devel
BuildRequires:  gnome-doc-utils
BuildRequires:  intltool
BuildRequires:  libglade2-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  libxslt-devel
BuildRequires:  rarian-compat
BuildRequires:  desktop-file-utils
BuildRequires:  GConf2
BuildRequires: make

Requires:       gstreamer1-plugins-base

Requires(pre):   GConf2
Requires(post):  GConf2
Requires(preun): GConf2
Requires(post):  info
Requires(preun): info

%description
Ignuit is a memorization aid based on the Leitner flashcard system. It has a 
GNOME look and feel, a good selection of quiz options, and supports UTF-8. Cards
can include embedded audio, images, and mathematical formulae (via LaTeX). It 
can import and export several file formats, including CSV. Ignuit can be used 
for both long-term learning and cramming.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=%{buildroot} INSTALL='install -p'
%find_lang %{name}
desktop-file-install                                    \
    --remove-key="Encoding"                             \
    --remove-key="MimeType"                             \
    --delete-original                                   \
    --dir=%{buildroot}%{_datadir}/applications          \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
rm -f %{buildroot}%{_infodir}/dir

%pre
%gconf_schema_prepare %{name}

%post
%gconf_schema_upgrade %{name}

%preun
%gconf_schema_remove %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING COPYING.extras NEWS README TODO examples
%{_mandir}/man1/%{name}.1.*
%{_infodir}/%{name}.info.*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome/help/%{name}/
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_datadir}/omf/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 2.24.3-18
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.24.3-2
- Remove obsolete scriptlets

* Fri Nov 17 2017 Fabian Affolter <mail@fabian-affolter.ch> - 2.24.3-1
- Update to new upstream version 2.24.3 (rhbz#1514436)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Apr 16 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.24.2-1
- Update to new upstream version 2.24.2 (rhbz#1321385)

* Tue May 19 2015 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.24.0-1
- Update to 2.24.0 (#1222726)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 05 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.20.0-1
- Add man page and info
- Update spec file
- Update to new upstream version 2.20.0 (rhbz#1084962 and rhbz#1037128)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.0.16-3
- Rebuild for new libpng

* Sat Feb 19 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.16-2
- Fix license tag
- Drop texinfo.tex from %%doc
- Remove "Encoding" and "MimeType" from ignuit.desktop

* Mon Jan 03 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.16-1
- Initial packaging
