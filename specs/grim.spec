Name:		grim
Version:	1.5.0
Release:	1%{?dist}
Summary:	Screenshot tool for Sway

License:	MIT
URL:		https://gitlab.freedesktop.org/emersion/grim
Source0:	%{url}/-/releases/v%{version}/downloads/%{name}-%{version}.tar.gz
Source1:	%{url}/-/releases/v%{version}/downloads/%{name}-%{version}.tar.gz.sig
Source2:	dj3498u4hyyarh35rkjfnghbjxug6b19

BuildRequires:	pkgconfig(bash-completion)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols) >= 1.37
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	scdoc
BuildRequires:	meson >= 0.59.0
BuildRequires:	gcc
BuildRequires:	gnupg2

%description
Grim is a command-line tool to grab images from Sway.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%meson \
	-Dbash-completions=true \
	-Dfish-completions=true
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%{_bindir}/grim
%{_mandir}/man1/grim.1*
%{bash_completions_dir}/grim*
%{fish_completions_dir}/grim*

%changelog
* Sat Jul 19 2025 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0 (#2379015)
- Update upstream URL

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1 (#2215017)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb 28 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (#2052418)
- Build bash and fish completions

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Apr 18 2021 Benjamin Lowry <ben@ben.gmbh> - 1.3.2-1
- Grim 1.3.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Benjamin Lowry <ben@ben.gmbh> 1.3.1-1
- Grim 1.3.1

* Sun Mar 8 2020 Benjamin Lowry <ben@ben.gmbh> 1.3.0-3
- Clarify package description (RHBZ#1811403)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Benjamin Lowry <ben@ben.gmbh> 1.3.0-1
- Grim 1.3.0

* Fri Jan 10 2020 Benjamin Lowry <ben@ben.gmbh> 1.2.0-2
- Use PGP key from author's website instead of keyserver

* Sun Dec 29 2019 Benjamin Lowry <ben@ben.gmbh> 1.2.0-1
- Initial Fedora package
