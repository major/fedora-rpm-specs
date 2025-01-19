Name:		hsetroot
Version:	1.0.5
Release:	9%{?dist}
Summary:	Yet another wallpaper application

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		https://github.com/himdel/hsetroot
Source0:	https://github.com/himdel/hsetroot/archive/refs/tags/%{version}.tar.gz

# Adds DESTDIR, see upstream pull request #38.
Patch0: 1.0.5-add-destdir.patch

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	pkgconfig(xinerama)

%description
hsetroot is an imlib2-based wallpaper composer, which also works with
compositors like compton or picom. It has a lot of options
like rendering gradients, solids, images but it also allows you
to perform manipulations on those things, or chain them together.

%prep
%autosetup
# Make sure that executables don't get stripped
sed -i -e 's/install -st/install -t/' Makefile

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%{_bindir}/hsetroot
%{_bindir}/hsr-outputs

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.5-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Leigh Scott <leigh123linux@gmail.com> - 1.0.5-3
- Rebuild fo new imlib2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Jani Juhani Sinervo <jani@sinervo.fi> - 1.0.5-1
- Do initial packaging work
