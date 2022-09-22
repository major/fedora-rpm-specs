%global _hardened_build 1
# checkout by commit for a valid persistent source link
# the corresponding git tag is v3.2-latest
%global commit      54145b03f4240222e336a9a2f402e93facefde65
%global date        20220425
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           libsearpc
Version:        3.2.0
Release:        8%{?dist}
Summary:        A simple and easy-to-use C language RPC framework

License:        LGPLv3
URL:            https://github.com/haiwen/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{version}%{?date:-%{date}git%{shortcommit}}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  python3-devel


%description
Searpc is a simple C language RPC framework based on GObject system. Searpc
handles the serialization/deserialization part of RPC, the transport part is
left to users.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%prep
%setup -qn %{name}-%{commit}
sed -i -e /\(DESTDIR\)/d %{name}.pc.in
sed -i 's@/usr/bin/env python@/usr/bin/env python3@' ./lib/searpc-codegen.py ./pysearpc/test_pysearpc.py ./tests/generate.py
sed -i 's@/usr/bin/python@/usr/bin/python3@' ./pysearpc/pygencode.py


%build
./autogen.sh
%configure --disable-static --disable-compile-demo --with-python3
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%check
# tests are failing on big endian arches
# https://bugzilla.redhat.com/show_bug.cgi?id=1388453
%ifnarch ppc ppc64 s390 s390x
%make_build check
%endif


%ldconfig_scriptlets


%files
%doc AUTHORS README.markdown
%license LICENSE.txt
%{_libdir}/%{name}.so.1*
%{_bindir}/searpc-codegen.py
%{python3_sitearch}/pysearpc/

%files devel
%license LICENSE.txt
%{_includedir}/searpc*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.2.0-7
- Sync with v3.2-latest to pick C++ compatibility fix

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.2.0-6
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.2.0-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 25 2020 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.2.0-1
- Change version to 3.2.0 (no source changes)

* Wed Nov 04 2020 Aleksei Bavshin <alebastr@fedoraproject.org> - 3.2-1
- Update to 3.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1-17
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Julien Enselme <jujens@jujens.eu> - 3.1-15
- Remove dependency on /usr/bin/python2

* Sun Nov 03 2019 Julien Enselme <jujens@jujens.eu> - 3.1-14
- Make this package compatible with Python3

* Wed Sep 11 2019 Julien Enselme <jujens@jujens.eu> - 3.1-13
- Update latest tag to latest version.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.1-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Aug 14 2017 Iryna Shcherbina <ishcherb@redhat.com> - 3.1-7
- Add a build-time dependency on python2-devel

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 08 2016 Dan Horák <dan[at]danny.cz> - 3.1-3
- Skip the tests in a better way

* Tue Nov 08 2016 Julien Enselme <jujens@jujens.eu> - 3.1-2
- Skip failing tests on ppc64 and s390

* Sun Oct 23 2016 Julien Enselme <jujens@jujens.eu> - 3.1-1
- Update to 3.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.7-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Feb 02 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 3.0.7-1
- Update to 3.0.7

* Fri Dec 04 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 3.0-6
- Add optflags

* Fri Sep 11 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 3.0-5
- Fix license

* Fri Sep 11 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 3.0-4
- Fix license
- Fix build requiremets
- Add check

* Sat Apr 11 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 3.0-3
- Use release tag instead of commit

* Wed Nov 05 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.0-2
- Update to latest tag
- Remove merged patch

* Tue Aug 12 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.0-1
- Initial version of the package
