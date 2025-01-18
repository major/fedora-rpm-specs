Name:           catimg
Version:        2.7.0
Release:        13%{?dist}
Summary:        Print images in a terminal with 256 colors support

License:        MIT
URL:            https://github.com/posva/catimg
Source0:        %{URL}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: catimg-c99.patch

BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++

%description
%{name} prints images in a terminal with 256 colors support. It supports
JPEG, PNG, ICO and GIF formats.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
install -D --preserve-timestamps --mode 644 completion/_catimg %{buildroot}%{_datadir}/zsh/site-functions/_catimg

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_catimg
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 22 2022 Florian Weimer <fweimer@redhat.com> - 2.7.0-7
- Improve C99 compatibility

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 07 2022 K. de Jong <keesdejong@fedoraproject.org> - 2.7.0-5
- Updated cmake arguments to latest macro requirements

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 13 2020 K. de Jong <keesdejong@fedoraproject.org> - 2.7.0-1
- New upstream release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 31 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Filip Szymański <fszymanski at, fedoraproject.org> - 2.2.2-1
- Update to 2.2.2

* Fri Jan 13 2017 Filip Szymański <fszymanski at, fedoraproject.org> - 2.2.1-1
- Initial release
