Summary:        A fast and lightweight vim like web browser
Name:           vimb
License:        GPL-3.0-only

Version:        3.7.0
Release:        4%{?dist}

URL:            https://fanglingsu.github.io/vimb/
Source0:        https://github.com/fanglingsu/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
Vimb is a fast and lightweight vim like web browser based on the webkit
web browser engine and the GTK toolkit. Vimb is modal like the great vim
editor and also easily configurable during runtime. Vimb is mostly
keyboard driven and does not distract you from your daily work.


%prep
%autosetup

%build
sed -i 's/EXTLDFLAGS  =/EXTLDFLAGS  = ${LDFLAGS} /g' config.mk
%make_build DOTDESKTOPPREFIX=%{_datadir}/applications \
            EXTENSIONDIR=%{_libdir}/vimb

%install
%make_install PREFIX=%{_prefix} \
              LIBDIR=%{buildroot}/%{_libdir}/%{name} \
              EXTENSIONDIR=%{buildroot}/%{_libdir}/%{name}

strip --strip-unneeded %{buildroot}/%{_libdir}/%{name}/webext_main.so

%check
make test
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files 
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/webext_main.so
%{_mandir}/man1/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.metainfo.xml

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 3.7.0-1
- Update to 3.7.0

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 05 2023 Benson Muite <benson_muite@emailplus.org> - 3.6.0-2
- Use macros for installation
- Update source location
- Use pkgconfig instead of devel
- Indicate gtk3 is a direct dependency

* Tue Mar 07 2023 Benson Muite <benson_muite@emailplus.org> - 3.6.0-1
- Initial packaging
