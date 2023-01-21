Name:           howl
Version:        0.6
Release:        18%{?dist}
Summary:        Lightweight editor with a keyboard-centric minimalistic UI

# For a breakdown of the licensing, see LICENSE.md
License:        MIT and Public Domain and BSD
URL:            https://howl.io
Source0:        https://github.com/howl-editor/howl/releases/download/%{version}/%{name}-%{version}.tgz
# Bundled LuaJIT-2.1.0-beta3 failed to compile with this arches
ExcludeArch:    aarch64 ppc64le s390x

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires: make

Requires:       %{name}-data
Requires:       hicolor-icon-theme

Recommends:     fontawesome-fonts

Provides:       bundled(luajit) = 2.1.0~beta3

%global _description \
Howl is a general purpose editor that aims to be both lightweight and fully\
customizable. It's built on top of the very fast LuaJIT runtime, uses Gtk for\
its interface, and can be extended in either Lua or Moonscript. It's known to\
work on Linux, but should work on at least the *BSD's as well.

%description %{_description}

%package        data
BuildArch:      noarch

Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
# Python, Ruby not necessary for for Howl it only requires by example files so
# disable auto requires
AutoReq:        no
Summary:        Data files for %{name}

%description    data %{_description}

Data files for %{name}.

%prep
%autosetup

%build
%make_build -C src

%install
%make_install -C src PREFIX=%{_prefix}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_avoid_bundling_of_fonts_in_other_packages
# We can install it in *Requires*
rm -r       %{buildroot}%{_datadir}/%{name}/fonts
# https://github.com/howl-editor/howl/pull/502
mv          %{buildroot}%{_datadir}/appdata %{buildroot}%{_metainfodir}
# https://github.com/howl-editor/howl/issues/501#issuecomment-484565885
find        %{buildroot}%{_datadir}/%{name}/bundles/python/misc/ -type f -name "*.py" -exec sed -e 's@/usr/bin/env python@/usr/bin/python3@g' -i "{}" \;
find        %{buildroot}%{_datadir}/%{name}/bundles/ruby/misc/ -type f -name "*.rb" -exec sed -e 's@/usr/bin/env ruby@/usr/bin/ruby@g' -i "{}" \;

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md Changelog.md
%license LICENSE.md
%{_bindir}/%{name}
%{_bindir}/%{name}-spec
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/%{name}.appdata.xml

%files data
%{_datadir}/%{name}

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6-10
- Add ExcludeArch: aarch64 ppc64le s390x
- Remove Requires %{?_isa} from noarch package
- Remove fdupes

* Wed Apr 17 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6-9
- Initial package