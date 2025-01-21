Name:          vrms-rpm
Summary:       Report non-free software
License:       GPL-3.0-only

Version:       2.3
Release:       4%{?dist}

BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: libcmocka-devel
BuildRequires: make
BuildRequires: rpm-devel

%global git_tag release-%{version}
URL:           https://github.com/suve/%{name}
Source0:       %{url}/archive/%{git_tag}/%{name}-%{git_tag}.tar.gz

%description
vrms-rpm ("virtual Richard M. Stallman") reports non-free packages
installed on the system.

%prep
%autosetup -n %{name}-%{git_tag}

%build
make all PREFIX=%{_prefix} %{?_smp_mflags} \
	DEFAULT_GRAMMAR=spdx-lenient \
	DEFAULT_LICENCE_LIST=tweaked

%check
make test %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}
%find_lang %{name} --with-man

%files -f %{name}.lang
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_datadir}/suve/
%{_datadir}/bash-completion/completions/%{name}
%license LICENCE.txt IMAGE-CREDITS.txt

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Aug 20 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.3-1
- Update to latest release
- Migrate license tag to SPDX

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Artur Iwicki <fedora@svgames.pl> - 2.2-2
- Re-fetch the source tarball (upstream over-wrote the git tag without bumping version)

* Fri Jul 24 2020 Artur Iwicki <fedora@svgames.pl> - 2.2-1
- Update to upstream release v2.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Artur Iwicki <fedora@svgames.pl> - 2.1-1
- Update to latest upstream version
- Drop Patch0 (issue fixed upstream)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Artur Iwicki <fedora@svgames.pl> - 2.0-1
- Update to newest upstream release
- No longer a noarch package

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Artur Iwicki <fedora@svgames.pl> 1.3-1
- Update to new upstream version
- Use tag/name-tag.tar.gz as Source0 instead of tag.tar.gz#/name-tag.tar.gz

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 suve <veg@svgames.pl> 1.2-2
- Use "_prefix" macro instead of bare string "/usr" during build & install
- Remove curly braces from "find_lang" macro call
- Adjust URL (remove trailing slash) and Source0

* Thu Jun 01 2017 suve <veg@svgames.pl> 1.2-1
- New upstream version
- gettext added as depencency
- Install section now relies on upstream's Makefile

* Sat May 20 2017 suve <veg@svgames.pl> 1.1-3
- Use "{?dist}" instead of "{dist}" in release number

* Sat Apr 15 2017 suve <veg@svgames.pl> 1.1-2
- Use the -p option (preserve timestamps) with install

* Fri Apr 07 2017 suve <veg@svgames.pl> 1.1-1
- Change version number to match upstream

* Fri Apr 07 2017 suve <veg@svgames.pl> 1.0-5
- Use URL variable when defining Source0
- Use #/ in Source0 to request a better archive name from GitHub

* Thu Mar 23 2017 suve <veg@svgames.pl> 1.0-4
- Add grep as a dependency

* Wed Mar 22 2017 suve <veg@svgames.pl> 1.0-3
- Use the GitHub archive link for Source0
- Do not use the _builddir variable during install section
- Use wildcard for the manpage in files section
- Include licence in files section
- Add bash as a dependency

* Sun Mar 19 2017 suve <veg@svgames.pl> 1.0-2
- Initial packaging

