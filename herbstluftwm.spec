#%%define __cmake_in_source_build 1

#%%global commit 35a0b465cebb577389644ca5149c4569b3c2990d
#%%global shortcommit %%(c=%%{commit}; echo ${c:0:7})

Name:           herbstluftwm
Version:        0.9.4
Release:        2%{?dist}
Summary:        A manual tiling window manager
License:        BSD
URL:            http://herbstluftwm.org
#Source0:        https://github.com/%%{name}/%%{name}/archive/%%{commit}/%%{name}-%%{shortcommit}.tar.gz
Source0:        http://herbstluftwm.org/tarballs/%{name}-%{version}.tar.gz
Patch0:         %{name}-gcc11.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  asciidoc

Requires:	xsetroot

%description
herbstluftwm is a manual tiling window manager for X11 using Xlib and Glib.
Its main features can be described with:

- The layout is based on splitting frames into subframes which can be split
again or can be filled with windows;
- Tags (or workspaces or virtual desktops or …) can be added/removed at
runtime. Each tag contains an own layout exactly one tag is viewed on each
monitor. The tags are monitor independent;
- It is configured at runtime via ipc calls from herbstclient. So the
configuration file is just a script which is run on startup.

%package        zsh
Summary:        Herbstluftwm zsh completion support
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       zsh

%description    zsh
This package provides zsh completion script of %{name}.

%package        fish
Summary:        Herbstluftwm fish completion support
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       fish

%description    fish
This package provides fish completion script of %{name}.

%prep
#%%autosetup -p1 -n %%{name}-%%{commit}
%autosetup -p1

%build
# Set the proper build flags
%cmake
%cmake_build

%install
%cmake_install

# Change the shebangs of the upstream files to be proper
for f in "%{buildroot}%{_pkgdocdir}/examples/*.sh"
do
    sed -i -e "s|#!/usr/bin/env bash|#!/usr/bin/bash|" $f
done

for f in "%{buildroot}%{_sysconfdir}/xdg/%{name}/*"
do
    sed -i -e "s|#!/usr/bin/env bash|#!/usr/bin/bash|" $f
done

# Remove unnecessary and/or redundant files
rm %{buildroot}%{_pkgdocdir}/LICENSE
rm -r %{buildroot}%{_pkgdocdir}/html

%files
%license LICENSE
%doc AUTHORS MIGRATION NEWS
%doc doc/*.{html,txt}
%{_sysconfdir}/xdg/%{name}
%{_bindir}/*
%{_datadir}/bash-completion/completions/herbstclient
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_pkgdocdir}/examples/
%{_pkgdocdir}/hlwm-doc.json

%files zsh
%{_datadir}/zsh/site-functions/_herbstclient

%files fish
%{_datadir}/fish/vendor_completions.d/herbstclient.fish

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 17 2022 Jani Juhani Sinervo <jani@sinervo.fi> - 0.9.4-1
- Update to latest version

* Tue Jan 25 2022 Jani Juhani Sinervo <jani@sinervo.fi> - 0.9.3-1
- Update to latest version
- Add xsetroot as runtime dependency

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7.git20201206git35a0b46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6.git20201206git35a0b46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5.git20201206git35a0b46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 07 2020 Jani Juhani Sinervo <jani@sinervo.fi> - 0.9.0-4.git20201206git35a0b46
- Pull latest version from upstream that fixes upstream bug #1056

* Fri Dec 04 2020 Jeff Law <law@redhat.com> - 0.9.0-3
- Fix another missing #include for gcc-11

* Wed Dec 02 2020 Jeff Law <law@redhat.com> - 0.9.0-2
- Fix missing #include for gcc-11

* Tue Dec 01 2020 Jani Juhani Sinervo <jani@sinervo.fi> - 0.9.0-1
- Set build system to cmake like upstream
- Update to 0.9.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Jani Juhani Sinervo <jani@sinervo.fi> - 0.7.2-1
- Revive under new maintainer

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 11 2014 Christopher Meng <rpm@cicku.me> - 0.6.2-1
- Update to 0.6.2

* Tue Mar 25 2014 Christopher Meng <rpm@cicku.me> - 0.6.1-1
- Update to 0.6.1

* Fri Mar 21 2014 Christopher Meng <rpm@cicku.me> - 0.6.0-1
- Update to 0.6.0

* Fri Dec 27 2013 Christopher Meng <rpm@cicku.me> - 0.5.3-1
- Update to 0.5.3

* Mon Aug 05 2013 Christopher Meng <rpm@cicku.me> - 0.5.2-2
- Move bash completion to better place.

* Mon Aug 05 2013 Christopher Meng <rpm@cicku.me> - 0.5.2-1
- Initial Package.
