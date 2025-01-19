Name:			lxhotkey
Version:		0.1.1
Release:		11%{?dist}
Summary:		Hotkeys management utility

License:		GPL-2.0-or-later
URL:			https://wiki.lxde.org/en/LXHotkey
Source0:		http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	pkgconfig(libfm)
BuildRequires:	pkgconfig(gtk+-2.0)

%description
LXHotkey is an utility which let you to have an interface 
to manage hotkeys (also known as shortcuts), 
i.e. key combinations which, when pressed, do something 
with your desktop.

%package		devel
Summary:		Development files for %{name}
Requires:		%{name}%{?_isa} = %{version}-%{release}

%description 	devel
The %{name}-devel package contains header files for
developing applications that use %{name}.

%prep
%autosetup

%build
%configure \
	--with-gtk=2 \
	--disable-silent-rules \
	%{nil}

%make_build

%install
%make_install
# Rather than writing multiple "--not-show-in", currently
# write --add-only-show-in with LXDE
# Set Icon to the value below, About dialog uses this
desktop-file-install \
	--delete-original \
	--remove-key=NotShowIn \
	--add-only-show-in=LXDE \
	--set-icon=preferences-desktop-keyboard \
	%{buildroot}%{_datadir}/applications/%{name}-gtk.desktop

%find_lang %{name}

%files	-f %{name}.lang
%license	COPYING

%{_bindir}/%{name}
%{_datadir}/applications/%{name}-gtk.desktop
# No plan to support GNOME, and no plan to
# support appdata

%dir	%{_libdir}/%{name}
# Explicitly write up plugin modules
%{_libdir}/%{name}/gtk.so
%{_libdir}/%{name}/ob.so

%{_mandir}/man1/%{name}.1*

%files devel
# Note: these files are to write "modules" for
# lxhotkey, so no .so file is provided.
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan  2 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.1-7
- SPDX migration

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb  4 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.1-1
- 0.1.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.0-2
- A bit cleanup

* Fri Dec 30 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.0-1
- Initial packaging

