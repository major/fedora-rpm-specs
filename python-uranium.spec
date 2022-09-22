Name:           python-uranium
Version:        4.13.1
Release:        4%{?dist}
Summary:        A Python framework for building desktop applications
License:        LGPLv3+
URL:            https://github.com/Ultimaker/Uranium
Source0:        %{url}/archive/%{version}.tar.gz#/Uranium-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  /usr/bin/doxygen
BuildRequires:  /usr/bin/msgmerge
BuildRequires:  cmake
BuildRequires:  git-core

# Tests
BuildRequires:  python3-arcus == %{version}
BuildRequires:  python3-cryptography
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy
BuildRequires:  python3-shapely
BuildRequires:  python3-qt5
BuildRequires:  python3-pytest
BuildRequires:  python3-twisted

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
ExcludeArch:    %{ix86}
%endif

%description
Uranium is a Python framework for building 3D printing related applications.

%package -n python3-uranium
Summary:        %{summary}
Provides:       uranium = %{version}-%{release}
%{?python_provide:%python_provide python3-uranium}

Requires:       python3-arcus == %{version}
Requires:       python3-cryptography
Requires:       python3-numpy
Requires:       python3-scipy
Requires:       python3-shapely
Requires:       python3-qt5
Recommends:     python3-numpy-stl

%description -n python3-uranium
Uranium is a Python framework for building 3D printing related applications.

%package doc
Summary: Documentation for %{name} package

%description doc
Documentation for Uranium, a Python framework for building 3D printing
related applications.

%prep
%autosetup -n Uranium-%{version} -p1 -S git

%build
# there is no arch specific content, so we set LIB_SUFFIX to nothing
# see https://github.com/Ultimaker/Uranium/commit/862a246bdfd7e25541b04a35406957612c6f4bb7
%cmake -DLIB_SUFFIX:STR=
%cmake_build
%cmake_build -- doc

%check
%{__python3} -m pip freeze

# skipping failing tests, see:
# * https://github.com/Ultimaker/Uranium/issues/594
# * https://github.com/Ultimaker/Uranium/issues/603
%{__python3} -m pytest -v -k "not (TestSettingFunction and test_init_bad) and not TestHttpRequestManager"


%install
%cmake_install

# Move the cmake files
mv %{buildroot}%{_datadir}/cmake* %{buildroot}%{_datadir}/cmake

# Sanitize the location of locale files
pushd %{buildroot}%{_datadir}
mv uranium/resources/i18n locale
ln -s ../../locale uranium/resources/i18n
rm locale/uranium.pot
rm locale/*/uranium.po
popd

# Bytecompile the plugins
%py_byte_compile %{__python3} %{buildroot}%{_prefix}/lib/uranium

%find_lang uranium


%files -n python3-uranium -f uranium.lang
%license LICENSE
%doc README.md
%{python3_sitelib}/UM
%{_datadir}/uranium
# Own the dir not to depend on cmake:
%{_datadir}/cmake
%{_prefix}/lib/uranium


%files doc
%license LICENSE
%doc html


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 4.13.1-3
- Rebuilt for Python 3.11

* Wed Mar 02 2022 Miro Hrončok <mhroncok@redhat.com> - 4.13.1-2
- Fix build with cmake 3.23.0rc2
- Related: rhbz#2059201, rhbz#2059188, rhbz#2057738

* Tue Feb 01 2022 Gabriel Féron <feron.gabriel@gmail.com> - 4.13.1-1
- Update to 4.13.1

* Fri Jan 21 2022 Gabriel Féron <feron.gabriel@gmail.com> - 4.13.0-1
- Update to 4.13.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Gabriel Féron <feron.gabriel@gmail.com> - 4.12.1-1
- Update to 4.12.1

* Mon Nov 08 2021 Miro Hrončok <mhroncok@redhat.com> - 4.11.0-2
- Round coordinates on getFaceIdAtPosition, to fix crash with Python 3.10+
- Fixes a crash when using "Select face to align to the build plate" tool
- Fixes rhbz#2021157

* Wed Sep 15 2021 Gabriel Féron <feron.gabriel@gmail.com> - 4.11.0-1
- Update to 4.11.0

* Mon Aug 16 2021 Gabriel Féron <feron.gabriel@gmail.com> - 4.10.0-1
- Update to 4.10.0

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Gabriel Féron <feron.gabriel@gmail.com> - 4.9.1-1
- Update to 4.9.1

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.9.0-2
- Rebuilt for Python 3.10

* Mon Apr 26 2021 Gabriel Féron <feron.gabriel@gmail.com> - 4.9.0-1
- Update to 4.9.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Jan Pazdziora <jpazdziora@redhat.com> - 4.8.0-1
- Update to 4.8.0

* Fri Nov 27 2020 Miro Hrončok <mhroncok@redhat.com> - 4.7.1-2
- Round coordinates before creating QPoint
- Fixes a test failure with Python 3.10

* Thu Sep 03 2020 Miro Hrončok <mhroncok@redhat.com> - 4.7.1-1
- Update to 4.7.1

* Mon Aug 31 2020 Gabriel Féron <feron.gabriel@gmail.com> - 4.7.0-1
- Update to 4.7.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.6.1-2
- Rebuilt for Python 3.9

* Tue May 5 2020 Gabriel Féron <feron.gabriel@gmail.com> - 4.6.0-1
- Update to 4.6.1

* Tue Apr 21 2020 Gabriel Féron <feron.gabriel@gmail.com> - 4.6.0-1
- Update to 4.6.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Gabriel Féron <feron.gabriel@gmail.com> - 4.4.0-1
- Update to 4.4.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Gabriel Féron <feron.gabriel@gmail.com> - 4.1.0-1
- Update to 4.1.0

* Wed Apr 03 2019 Gabriel Féron <feron.gabriel@gmail.com> - 4.0.0-1
- Update to 4.0.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Gabriel Féron <feron.gabriel@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 3.5.1-1
- Update to 3.5.1 (#1644323)

* Tue Aug 28 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.1-1
- Update to 3.4.1 (#1599724)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-4
- Rebuilt for Python 3.7

* Thu Jun 07 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-3
- Bytecompile the plugins explicitly

* Mon May 28 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-2
- Fix PluginRegistry test

* Wed May 02 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-1
- Update to 3.3.0 (#1571792)
- Skip test_emptyPlugin

* Mon Mar 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-1
- Update to 3.2.1 (#1523904)
- Force install to /usr/lib and keep this noarch

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-1
- Update to 3.1.0 (#1523904)
- No need to sed dist-packages out anymore
- getMimeTypeForFile fails no more
- but some others tests are, add a fix

* Fri Oct 20 2017 Charalampos Stratakis <cstratak@redhat.com> - 3.0.3-1
- Update to 3.0.3 (#1504439)

* Wed Aug 30 2017 Miro Hrončok <mhroncok@redhat.com> - 2.7.0-2
- Relocate Japanese locale to ja

* Wed Aug 30 2017 Miro Hrončok <mhroncok@redhat.com> - 2.7.0-1
- Update to 2.7.0 (#1486741)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-2
- Fix the test_uniqueName test failure

* Wed Jun 28 2017 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-1
- Update to 2.6.1
- Skip test_uniqueName test (reported)

* Tue Jun 27 2017 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-1
- Update to 2.6.0

* Wed May 03 2017 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-2
- Actually include the cmake files (needed for cura)

* Wed Apr 26 2017 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-1
- Initial package

