Name:           pw3270
Version:        5.4
Release:        8%{?dist}
Summary:        IBM 3270 Terminal emulator for GTK

License:        LGPLv3
URL:            https://github.com/PerryWerneck/pw3270
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Fixing fedora builds
Patch0:         %{url}/commit/5fbb011dac42b03539ca24b68a8d51b04f733773.patch
# Adaptation of PR#20 to convert from appdata to metainfo
Patch1:         metainfo.patch
# Fixing appstream-validate error
Patch2:         %{url}/commit/a46f3f89834e9f58243d45cc0a15735677a98df3.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  libv3270-devel

Suggests:       font(ibm3270)

%description
GTK-based IBM 3270 terminal emulator with many advanced features. It can be
used to communicate with any IBM host that supports 3270-style connections
over TELNET.

Based on the original x3270 code, pw3270 was originally created for Banco do
Brasil, and is now used worldwide.

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure
# override SHELL to make the build more verbose
%make_build all SHELL='sh -x'

%install
%make_install
%find_lang %{name}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{name}
%{_libdir}/%{name}-plugins
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.metainfo.xml
%{_datadir}/glib-2.0/schemas/%{name}*.gschema.xml
%{_datadir}/mime/packages/%{name}.xml

%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 23 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 5.4-1
- New upstream release
- Update URL
- Backport upstream metainfo fix
- Add suggests for ibm3270 font

* Thu Mar 18 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 5.3-3
- Update build requires
- Convert from appdata to metainfo

* Sat Mar 13 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 5.3-2
- Do not remove buildroot on install
- Make build output more verbose
- Ensure build flags are applied

* Wed Mar  3 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 5.3-1
- Initial package
