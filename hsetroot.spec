Name:		hsetroot
Version:	1.0.5
Release:	4%{?dist}
Summary:	Yet another wallpaper application

License:	GPLv2
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
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Leigh Scott <leigh123linux@gmail.com> - 1.0.5-3
- Rebuild fo new imlib2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Jani Juhani Sinervo <jani@sinervo.fi> - 1.0.5-1
- Do initial packaging work
