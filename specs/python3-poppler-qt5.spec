Name:           python3-poppler-qt5
Version:        21.3.0
Release:        12%{?dist}
Summary:        Python bindings for the Poppler PDF rendering library

License:        LGPL-2.1-or-later
URL:            https://github.com/frescobaldi/python-poppler-qt5
Source0:        %{url}/archive/v%{version}.tar.gz#/python-poppler-qt5-%{version}.tar.gz
Patch0:         binpaths.patch
Patch1:         40e71ad88173d02648bceb2438bc0567e60dacd5.patch
Requires: python3-qt5
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-qt5-devel
BuildRequires:  %{py3_dist sip} >= 5
BuildRequires:  %{py3_dist PyQt-builder}
BuildRequires:  pkgconfig(poppler-qt5)

# we don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_setup
}

%description
Python 3 bindings for the Poppler PDF rendering library. It is needed to
run programs written in Python 3 and using Poppler set.


%prep
%setup -qn python-poppler-qt5-%{version}

%patch -P0 -p0
#%patch1 -p1

%build
sip-build --qmake=%{_qt5_qmake} --verbose --no-make \
  --qmake-setting 'QMAKE_CFLAGS_RELEASE="%{optflags}"' \
  --qmake-setting 'QMAKE_CXXFLAGS_RELEASE="%{optflags}"' \
  --qmake-setting 'QMAKE_LFLAGS_RELEASE="%{?__global_ldflags}"'
%make_build -C build

%install
%make_install INSTALL_ROOT=%{buildroot} -C build
chmod +x %{buildroot}/%{python3_sitearch}/*.so

%files
%license LICENSE
%doc README.rst
%{python3_sitearch}/popplerqt5.cpython-*.so
%{python3_sitearch}/python_poppler*
%{python3_sitearch}/PyQt5/bindings/popplerqt5

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 21.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 21.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 21.3.0-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 21.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 21.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 21.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 21.3.0-6
- Rebuilt for Python 3.12

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 21.3.0-5
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 21.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 21.3.0-2
- Rebuilt for Python 3.11

* Tue May 10 2022 Gwyn Ciesla <gwync@protonmail.com> - 21.3.0-1
- 21.3.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 03 2021 Scott Talbert <swt@techie.net> - 21.1.0-3
- Update to build with sip5+

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 21.1.0-2
- Rebuilt for Python 3.10

* Tue Feb 23 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.1.0-1
- 21.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.75.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.75.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.75.0-5
- BR python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.75.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.75.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 0.75.0-2
- Rebuild for poppler-0.84.0

* Fri Nov 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.75.0-1
- 0.75.0

* Wed Sep 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.74.0-1
- 0.74.0

* Wed Sep 18 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.24.2-15
- fix sip dep harder

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.24.2-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 26 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.24.2-12
- Fix sip deps again.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Miro Hrončok <mhroncok@redhat.com> - 0.24.2-10
- Don't drag in Python 2 via sip-devel

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.24.2-8
- Rebuilt for Python 3.7

* Fri Mar 23 2018 Marek Kasik <mkasik@redhat.com> - 0.24.2-7
- Rebuild for poppler-0.63.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.24.2-3
- Rebuild due to bug in RPM (RHBZ #1468476)

* Fri Jun 09 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.24.2-2
- Review fixes.

* Thu Jun 08 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.24.2-1
- Initial package for Fedora
