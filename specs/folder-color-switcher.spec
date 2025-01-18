Name:           folder-color-switcher
Version:        1.6.7
Release:        2%{?dist}
Summary:        Change a folder colour

License:        GPL-3.0-only
URL:            https://github.com/linuxmint/folder-color-switcher
Source0:        http://packages.linuxmint.com/pool/main/f/%{name}/%{name}_%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  gettext
Requires:       python3

%description
Change a folder colour

%package nemo
Summary:        Nemo folder colour
Requires:       %{name} = %{version}-%{release}
Requires:       nemo-python

%description nemo
Support for Nemo folder colour

%package caja
Summary:        Caja folder colour
Requires:       %{name} = %{version}-%{release}
Requires:       python-caja

%description caja
Support for Caja folder colour


%prep
%autosetup -n %{name}
chmod 644 COPYING.GPL3

%build
%make_build


%install
cp -Rp usr/ %{buildroot}/

for lib in %{buildroot}%{_datadir}/*-python/extensions/*.py; do
 sed '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%find_lang %{name}

%files -f %{name}.lang
%license COPYING.GPL3
%{_datadir}/%{name}/

%files nemo
%{_datadir}/nemo-python/extensions/*

%files caja
%{_datadir}/caja-python/extensions/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan 06 2025 Leigh Scott <leigh123linux@gmail.com> - 1.6.7-1
- Update to 1.6.7

* Fri Dec 06 2024 Leigh Scott <leigh123linux@gmail.com> - 1.6.6-1
- Update to 1.6.6

* Mon Nov 25 2024 Leigh Scott <leigh123linux@gmail.com> - 1.6.5-1
- Update to 1.6.5

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Leigh Scott <leigh123linux@gmail.com> - 1.6.3-1
- Update to 1.6.3

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 04 2024 Leigh Scott <leigh123linux@gmail.com> - 1.6.2-1
- Update to 1.6.2

* Thu Dec 21 2023 Leigh Scott <leigh123linux@gmail.com> - 1.6.1-1
- Update to 1.6.1

* Sun Dec 03 2023 Leigh Scott <leigh123linux@gmail.com> - 1.6.0-1
- Update to 1.6.0

* Wed Jun 07 2023 Leigh Scott <leigh123linux@gmail.com> - 1.5.9-1
- Initial build

