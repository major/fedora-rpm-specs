%global luacompatver 5.1
%global luacompatlibdir %{_libdir}/lua/%{luacompatver}
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}
%global luacompatincludedir %{_includedir}/lua-%{luacompatver}
%global lua51dir %{_builddir}/lua51-%{name}-%{version}-%{release}

Name:		lua-lgi
Version:	0.9.2
Release:	25%{?dist}
Summary:	Lua bindings to GObject libraries
# Automatically converted from old format: MIT - review is highly recommended.
License:	MIT
URL:		https://github.com/pavouk/lgi
Source0:	https://github.com/pavouk/lgi/archive/%{version}/lgi-%{version}.tar.gz
# see gh#212 (commit a127f82)
Patch0:		lgi-0.9.2-fix-s390x.patch
# see gh#215
Patch1:		lgi-0.9.2-fix-gobject-warnings.patch
# see gh#249
Patch2:		lgi-0.9.2-lua54.patch
# fix for glib 2.87
Patch3:		https://github.com/lgi-devs/lgi/pull/352.patch
# fix for lua 5.5
Patch4:		lua-lgi-0.9.2-lua-5.5.patch
# no Gdk.Atom
Patch5:		lua-lgi-0.9.2-no-gdk-atom.patch
# remove unused var "record"
Patch6:		lua-lgi-0.9.2-unused.patch
# Use g_memdup2 when available
Patch7:		lua-lgi-0.9.2-g_memdup2.patch
# no-synclock
Patch8:		lua-lgi-0.9.2-gdk4-no-synclock.patch
# gtk4
Patch9:		lua-lgi-0.9.2-gtk4.patch
# modern glib2 typeclass fix
Patch10:	lua-lgi-0.9.2-modern-glib-typeclass.patch

BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.10.8
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(libffi)
BuildRequires:	lua >= %{lua_version}
BuildRequires:	lua-devel >= %{lua_version}
BuildRequires:	lua-markdown
# for the testsuite:
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(cairo-gobject)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	which
BuildRequires:	Xvfb xauth
BuildRequires:	dbus-x11 at-spi2-core

%global __requires_exclude_from %{_docdir}
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
LGI is gobject-introspection based dynamic Lua binding to GObject
based libraries. It allows using GObject-based libraries directly from
Lua.


%package samples
Summary:    Examples of lua-lgi usage
# gtk-demo is LGPLv2+
# Automatically converted from old format: LGPLv2+ and MIT - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description samples
%{summary}


%package compat
Summary:	Lua bindings to GObject libraries for Lua 5.1
BuildRequires:	compat-lua >= %{luacompatver}
BuildRequires:	compat-lua-devel >= %{luacompatver}

%description compat
LGI is gobject-introspection based dynamic Lua binding to GObject
based libraries. It allows using GObject-based libraries directly from
Lua.


%prep
%autosetup -n lgi-%{version} -p1
rm -rf %{lua51dir}
cp -a . %{lua51dir}


%build
export CFLAGS="%{optflags} -DLUA_COMPAT_APIINTCASTS"
# %%configure || :
make %{?_smp_mflags}

pushd %{lua51dir}
# %%configure || :
make LUA_CFLAGS=-I%{luacompatincludedir} %{?_smp_mflags}
popd

# generate html documentation
markdown.lua README.md docs/*.md


%install
mkdir -p \
  %{buildroot}%{lua_libdir} \
  %{buildroot}%{lua_pkgdir}
make install \
  "PREFIX=%{_prefix}" \
  "LUA_LIBDIR=%{lua_libdir}" \
  "LUA_SHAREDIR=%{lua_pkgdir}" \
  "DESTDIR=%{buildroot}"

pushd %{lua51dir}
mkdir -p \
  %{buildroot}%{luacompatlibdir} \
  %{buildroot}%{luacompatpkgdir}
make install \
  "PREFIX=%{_prefix}" \
  "LUA_LIBDIR=%{luacompatlibdir}" \
  "LUA_SHAREDIR=%{luacompatpkgdir}" \
  "DESTDIR=%{buildroot}"
popd

# install docs
mkdir -p %{buildroot}%{_pkgdocdir}
cp -av README.html docs/*.html \
  %{buildroot}%{_pkgdocdir}
cp -av samples %{buildroot}%{_pkgdocdir}
find %{buildroot}%{_pkgdocdir} -type f \
  -exec chmod -x {} \;


%check
export CFLAGS="%{optflags} -DLUA_COMPAT_APIINTCASTS"
# %%configure || :
# report failing tests, don't fail the build
timeout 60s xvfb-run -a -w 1 make check || :

pushd %{lua51dir}
# report failing tests, don't fail the build
xvfb-run -a -w 1 make check \
  LUA=%{_bindir}/lua-5.1 \
  LUA_CFLAGS=-I%{luacompatincludedir} || :
popd


%files
%dir %{_pkgdocdir}
%license LICENSE
%{_pkgdocdir}/*.html
%{lua_pkgdir}/lgi.lua
%{lua_pkgdir}/lgi
%{lua_libdir}/lgi


%files compat
%license LICENSE
%{luacompatpkgdir}/lgi.lua
%{luacompatpkgdir}/lgi
%{luacompatlibdir}/lgi


%files samples
%{_pkgdocdir}/samples


%changelog
* Fri Feb 27 2026 Tom Callaway <spot@fedoraproject.org> - 0.9.2-25
- lua 5.5 and other modernizations

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep  2 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.2-21
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar  4 2023 Thomas Moschny <thomas.moschny@gmx.de> - 0.9.2-16
- Apply patch by yselkowi@redhat.com: Drop unneeded Requires: lua.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 15 2020 Thomas Moschny <thomas.moschny@gmx.de> - 0.9.2-9
- Update for Lua 5.4.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb  8 2019 Thomas Moschny <thomas.moschny@gmx.de> - 0.9.2-4
- Update BRs.
- Add one patch to fix a problem on s390x, and one to fix a warning in
  the testsuite.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun  4 2018 Thomas Moschny <thomas.moschny@gmx.de> - 0.9.2-1
- Update to 0.9.2.
- Update BRs.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 Thomas Moschny <thomas.moschny@gmx.de> - 0.9.1-3
- Add -compat subpackage (rhbz#1323428).
- Minor spec file cleanups.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun  3 2016 Thomas Moschny <thomas.moschny@gmx.de> - 0.9.1-1
- Update to 0.9.1.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Thomas Moschny <thomas.moschny@gmx.de> - 0.9.0-1
- Update to 0.9.0.

* Sat Mar 14 2015 Thomas Moschny <thomas.moschny@gmx.de> - 0.8.0-4
- Mark license with %%license.

* Fri Jan 16 2015 Tom Callaway <spot@fedoraproject.org> - 0.8.0-3
- rebuild for lua 5.3

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul  4 2014 Thomas Moschny <thomas.moschny@gmx.de> - 0.8.0-1
- Update to 0.8.0.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Thomas Moschny <thomas.moschny@gmx.de> - 0.7.2-1
- Update to 0.7.2.
- Use a single package doc dir.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 12 2013 Tom Callaway <spot@fedoraproject.org> - 0.7.1-2
- rebuild for lua 5.2

* Thu Mar 21 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.7.1-1
- Update to 0.7.1.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan  8 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.6.2-5
- Update license tag.

* Mon Jan  7 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.6.2-4
- Remove unnecessary patch.
- Update license tag: gtk-demo is licensed under LGPLv2+.
- Put fully versioned dependency in subpackage.

* Wed Jan  2 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.6.2-3
- Move samples to separate package.
- Generate HTML documentation from markdown docs.

* Sun Dec 23 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.6.2-2
- Add gtk3 as BR, required by the testsuite.

* Sun Dec 23 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.6.2-1
- New package.
