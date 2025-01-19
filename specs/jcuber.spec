# Copyright (c) 2015  Dave Love, University of Liverpool
# MIT licence, per Fedora policy

Name:           jcuber
Version:        4.8
Release:        8%{?dist}
Summary:        CUBE reader for Java
# tarviewer is ASL
License:        BSD-3-Clause AND Apache-2.0
URL:            http://www.scalasca.org/software/cube-4.x/download.html
Source0:        http://apps.fz-juelich.de/scalasca/releases/cube/%(echo %version|awk -F. '{print $1 "." $2}')/dist/jcuber-%version.tar.gz
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  xerces-j2
BuildRequires: make
Requires:       java jpackage-utils
Obsoletes:      cube-java <= 4.3.2-1
Provides:       cube-java = %version-%release
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch


%description
A CUBE reader written in Java.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Conflicts:      cube-java <= 4.3.2-1

%description    doc
The %{name}-doc package contains documentation for %{name}.

%prep
%setup -q


%build
%configure
# As an alternative to patching configure.ac and then worrying about
# autoconf268 in EPEL6:
sed -i -e s/jCubeR/jcuber/ -e 's|/cube|/jcuber|' bin/jcuber-config
# nothing to parallelize
make


%check
make check


%install
make install install-html DESTDIR=%buildroot
cp -rp examples AUTHORS %buildroot%_defaultdocdir/%name


%files
%dir %_defaultdocdir/%name
%license COPYING
%_defaultdocdir/%name/AUTHORS
%_datadir/java/CubeReader.jar
# rpmlint complains, but I don't think they should be in a devel package --
# at least the file extension should be relevant at runtime.
%_bindir/jcuber-config*
%_datadir/jcuber
%exclude %_docdir/jcuber

%files doc
%_defaultdocdir/%name
%license COPYING


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 4.8-6
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 18 2022 Dave Love <loveshack@fedoraproject.org> - 4.8-1
- New version (#2074552)

* Thu Sep  8 2022 Dave Love <loveshack@fedoraproject.org> - 4.6-6
- Use SPDX licence tag

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 4.6-4
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 4.6-3
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 28 2021 Dave Love <loveshack@fedoraproject.org> - 4.6-1
- New version

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 4.5-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Jun  8 2020 Dave Love <loveshack@fedoraproject.org> - 4.5-1
- New version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug  1 2019 Dave love <loveshack@fedoraproject.org> - 4.4.2-1
- New version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 21 2019 Dave Love <loveshack@fedoraproject.org> - 4.4.1-1
- New version
- Drop patch

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec  5 2018 Dave Love <loveshack@fedoraproject.org> - 4.4-3
- Fix shebangs in config scripts

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 11 2018 Dave Love <loveshack@fedoraproject.org> - 4.4-1
- New version (#1575600)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May  4 2016 Dave Love <loveshack@fedoraproject.org> - 4.3.4-1
- New version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Dave Love <loveshack@fedoraproject.org> - 4.3.3-2
- Fix "==" in provides
- Add some comments to spec

* Tue Jan 12 2016 Dave Love <loveshack@fedoraproject.org> - 4.3.3-1
- New version

* Tue Dec  8 2015 Dave Love <loveshack@fedoraproject.org> - 4.3.2-2
- Add check
- Require java, not java-headless
- Install examples
- Fix jcuber-config

* Mon Jun 29 2015 Dave Love <loveshack@fedoraproject.org> - 4.3.2-1
- Initial packaging
