%global pname   skinflatplus

# The plugin ABI is expressed through vdr(abi); don't export private .so provides.
%global __provides_exclude_from ^%{vdr_libdir}/.*\\.so.*$

Name:           vdr-skinflatplus
Version:        1.3.1
Release:        1%{?dist}
Summary:        A fast, modern and up-to-date skin for the Video Disc Recorder
License:        GPL-2.0-or-later
URL:            https://github.com/MegaV0lt/vdr-plugin-%{pname}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Plugin parameters passed by runvdr. Fedora specific, not in upstream.
Source1:        %{name}.conf
# For upstream: replace the FSF's stale postal address in COPYING with the
# license URLs; rpmlint rejects the old address.
Patch0:         %{name}-fsf-address.patch
# For upstream: default the channel logo path to VDR's shared <resdir>/logos
# instead of a plugin private directory the plugin never installs.
Patch1:         %{name}-logopath.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  pkgconfig(GraphicsMagick++)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  vdr-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
Requires:       %{name}-data = %{version}-%{release}

%description
This plugin for Klaus Schmidinger's Video Disc Recorder VDR adds the "flatPlus"
skin. Skin flatPlus is a fast, modern and up-to-date skin for VDR. The design
is flat and straightforward (no glossy or 3D effects).

%package data
Summary:        Data files for VDR skin flatPlus
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description data
Data files for the VDR skin flatPlus.

%prep
%autosetup -n vdr-plugin-%{pname}-%{version} -p1

%build
%make_build IMAGELIB=graphicsmagick

%install
# Upstream's install target derives every path from vdr.pc, so it already
# lands where this package wants it: themes in <configdir>/themes -- the only
# place stock VDR looks (vdr.c: SetThemesDirectory) and a directory the vdr
# package owns -- decors/icons under <resdir>/plugins, configs under
# <configdir>/plugins, widgets under <libdir>.
%make_install

install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf

%find_lang %{name}

%check
# vdr resolves VDRPluginCreator after dlopen; a plugin without that export
# is broken even if it links cleanly
nm -D --defined-only %{buildroot}%{vdr_libdir}/libvdr-%{pname}.so.%{vdr_apiversion} | grep -q ' VDRPluginCreator$'

%files -f %{name}.lang
%license COPYING icons/COPYRIGHT
%doc HISTORY* README*
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%config(noreplace) %{vdr_configdir}/plugins/%{pname}/
%{vdr_libdir}/libvdr-%{pname}.so.%{vdr_apiversion}
%{vdr_libdir}/%{pname}/
%config(noreplace) %{vdr_configdir}/themes/flatPlus-*.theme

%files data
%dir %{vdr_resdir}/plugins/%{pname}
%{vdr_resdir}/plugins/%{pname}/*

%changelog
* Thu Aug 13 2026 Dirk Nehring <dnehring@gmx.net> - 1.3.1-1
- Install the themes into /etc/vdr/themes, where stock VDR looks for them
- Split the channel logos out into the separate vdr-channellogos source
  package
- Default the compiled-in logo path to the shared, skin-independent
  /usr/share/vdr/logos instead of a plugin private directory that is
  never installed; --logopath is no longer needed in the sysconfig snippet
- Modernize spec
- create subpackage data
- Add file COPYRIGHT to %%license
- Add RR of data subpackage to main package

* Fri Apr 03 2026 Martin Gansser <martinkg@fedoraproject.org> - 1.2.10-1
- Update to 1.2.10

* Wed Mar 25 2026 Martin Gansser <martinkg@fedoraproject.org> - 1.2.9-1
- Update to 1.2.9
- Rebuilt for new VDR 2.8.1 API version 12

* Sun Mar 08 2026 Dirk Nehring  <dnehring@gmx.net> - 1.2.8-2
- Add logos and needed decors

* Fri Mar 06 2026 Martin Gansser <martinkg@fedoraproject.org> - 1.2.8-1
- Update to 1.2.8

* Tue Mar 03 2026 Martin Gansser <martinkg@fedoraproject.org> - 1.2.6-1
- Update to 1.2.6

* Mon Feb 23 2026 Martin Gansser <martinkg@fedoraproject.org> - 1.2.5-1
- Update to 1.2.5

* Sat Dec 20 2025 Martin Gansser <martinkg@fedoraproject.org> - 1.2.4-1
- Update to 1.2.4

* Wed Dec 17 2025 Martin Gansser <martinkg@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3

* Tue Dec 16 2025 Martin Gansser <martinkg@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Thu Oct 09 2025 Martin Gansser <martinkg@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Fri Aug 01 2025 Martin Gansser <martinkg@fedoraproject.org> - 1.2.0-1
- Rebuilt for new VDR API version 2.7.7
- Update to 1.2.0

* Sat Jun 21 2025 Martin Gansser <martinkg@fedoraproject.org> - 1.1.11-2
- Rebuilt for new VDR API version 2.7.6

* Tue May 27 2025 Martin Gansser <martinkg@fedoraproject.org> - 1.1.10-1
- Rebuilt for new VDR API version 2.7.5
- Update to 1.1.11

* Tue Feb 25 2025 Martin Gansser <martinkg@fedoraproject.org> - 1.1.8-1
- Update to 1.1.8

* Tue Jan 14 2025 Martin Gansser <martinkg@fedoraproject.org> - 1.1.6-1
- Update to 1.1.6

* Thu Jan 09 2025 Martin Gansser <martinkg@fedoraproject.org> - 1.1.5-1
- Update to 1.1.5

* Fri Dec 13 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.1.4-1
- Update to 1.1.4

* Tue Nov 19 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3

* Sun Nov 10 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2

* Wed Nov 06 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Wed Oct 30 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Tue Oct 01 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8

* Mon Jul 15 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Wed Jan 31 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Tue Oct 24 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.7.5-1
- Initial Build
