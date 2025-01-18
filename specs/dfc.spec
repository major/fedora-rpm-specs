Name:           dfc
Version:        3.1.1
Release:        7%{?dist}
Summary:        Report file system space usage information with style

License:        BSD-3-Clause AND BSD-2-Clause
# main package cites BSD-3-Clause.
# cmake/modules/GettextTranslate.cmake specifically cites BSD-2-Clause
URL:            https://github.com/rolinh/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gettext


%description
dfc is a tool to report file system space usage information. When the
output is a terminal, it uses color and graphs by default. It has a lot of
features such as HTML, JSON and CSV export, multiple filtering options,
the ability to show mount options and so on.


%prep
%autosetup


%build
%cmake \
  -D SYSCONFDIR=%{_sysconfdir}
%cmake_build


%install
%cmake_install

rm -f %{buildroot}%{_docdir}/%{name}/{HACKING.md,LICENSE}

%find_lang %{name}
%find_lang %{name} --with-man


%files -f %{name}.lang
%license LICENSE
%doc AUTHORS.md CHANGELOG.md README.md TRANSLATORS.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/xdg/%{name}/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 06 2022 Jonathan Wright <jonathan@almalinux.org> - 3.1.1-1
- Initial package build
