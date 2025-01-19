Name:		lua-penlight
Version:	1.14.0
Release:	2%{?dist}
Summary:	Penlight Lua Libraries
License:	MIT
URL:		https://github.com/lunarmodules/Penlight
Source0:	https://github.com/lunarmodules/Penlight/archive/%{version}/Penlight-%{version}.tar.gz

%global luaver 5.4
%global luapkgdir %{_datadir}/lua/%{luaver}

# there's a circular (build) dependency with lua-ldoc
%bcond_without docs

BuildArch:	noarch
BuildRequires:	lua >= %{luaver}
BuildRequires:	lua-filesystem
BuildRequires:	lua-markdown
%if %{with docs}
BuildRequires:	lua-ldoc
%endif # with docs
Requires:	lua >= %{luaver}
Requires:	lua-filesystem

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global __requires_exclude_from %{_docdir}

%description
A set of pure Lua libraries focusing on input data handling (such as
reading configuration files), functional programming (such as map,
reduce, placeholder expressions, etc.), and OS path management. Much
of the functionality is inspired by the Python standard libraries.


%if %{with docs}
%package doc
Summary:	API docs for lua-penlight
Requires:	%{name} = %{version}-%{release}

%description doc
%{summary}
%endif # with docs


%package examples
Summary:	Examples of lua-penlight usage
Requires:	%{name} = %{version}-%{release}

%description examples
%{summary}


%prep
%setup -q -n Penlight-%{version}


%build
# nothing to do here


%install
mkdir -p %{buildroot}%{luapkgdir}
cp -av lua/pl %{buildroot}%{luapkgdir}

# fix scripts
chmod -x %{buildroot}%{luapkgdir}/pl/dir.lua

# build and install README etc.
mkdir -p %{buildroot}%{_pkgdocdir}
markdown.lua {README,CHANGELOG,CONTRIBUTING,LICENSE}.md
cp -av {README,CHANGELOG,CONTRIBUTING}.html %{buildroot}%{_pkgdocdir}

%if %{with docs}
# build and install docs
ldoc .
cp -av docs %{buildroot}%{_pkgdocdir}
%endif # with docs

# install examples
cp -av examples %{buildroot}%{_pkgdocdir}


%check
# currently disabled: missing luacov
# LUA_PATH="%%{buildroot}%%{luapkgdir}/?/init.lua;%%{buildroot}%%{luapkgdir}/?.lua;;" \
# lua run.lua tests


%files
%dir %{_pkgdocdir}
%license LICENSE.html
%{_pkgdocdir}/README.html
%{_pkgdocdir}/CHANGELOG.html
%{_pkgdocdir}/CONTRIBUTING.html
%{luapkgdir}/pl


%if %{with docs}
%files doc
%{_pkgdocdir}/docs
%endif # with docs


%files examples
%{_pkgdocdir}/examples


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 22 2024 Thomas Moschny <thomas.moschny@gmx.de> - 1.14.0-1
- Update to 1.14.0.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug  3 2022 Thomas Moschny <thomas.moschny@gmx.de> - 1.13.1-1
- Update to 1.13.1.

* Wed Aug  3 2022 Thomas Moschny <thomas.moschny@gmx.de> - 1.13.0-1
- Update to 1.13.0.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 30 2022 Thomas Moschny <thomas.moschny@gmx.de> - 1.12.0-1
- Update to 1.12.0.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep  4 2021 Thomas Moschny <thomas.moschny@gmx.de> - 1.11.0-1
- Update to 1.11.0.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May  1 2021 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.0-1
- Update to 1.10.0.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct  2 2020 Thomas Moschny <thomas.moschny@gmx.de> - 1.9.2-1
- Update to 1.9.2.

* Wed Aug  5 2020 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.0-2
- Re-enable docs.

* Wed Aug  5 2020 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.0-1
- Update to 1.8.0.

* Wed Aug  5 2020 Thomas Moschny <thomas.moschny@gmx.de> - 1.7.0-1
- Update to 1.7.0.
- New upstream URLs.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.4-1
- Update to 1.5.4.

* Wed May 17 2017 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.2-2
- Re-enable docs.

* Tue May 16 2017 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.2-1
- Update to 1.5.2.
- Minor spec file cleanups.

* Wed Apr  5 2017 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.0-1
- Update to 1.5.0.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.1-1
- Update to 1.4.1.
- Re-enable tests.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 21 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.2-1
- Update to 1.3.2.
- Mark license with %%license.
- Re-enable tests.

* Sun Jan 18 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.1-5
- Own the package doc dir.
- Remove extra .md suffix from generated HTML files.

* Fri Jan 16 2015 Tom Callaway <spot@fedoraproject.org> - 1.3.1-4
- build with docs

* Fri Jan 16 2015 Tom Callaway <spot@fedoraproject.org> - 1.3.1-3
- rebuild for lua 5.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov  3 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.1-1
- Update to 1.3.1.
- Use a single package doc dir.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Tom Callaway <spot@fedoraproject.org> - 1.1.0-2
- rebuild with docs

* Sun May 12 2013 Tom Callaway <spot@fedoraproject.org> - 1.1.0-1.1
- rebuild for lua 5.2, no docs

* Thu Mar 21 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.1.0-1
- Update to 1.1.0.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4.a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.3-3.a
- Add BR on lua-filesystem (needed when running the tests).
- Fix line-endings for the examples.

* Wed Jan  9 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.3-2.a
- Fix typos.
- Package examples as a separate subpackage.
- Run tests.

* Fri Jan  4 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.3-1.a
- New package.
