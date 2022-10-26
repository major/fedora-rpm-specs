Name:           trelby
Version:        2.4.7
Release:        1%{?dist}
Summary:        The free, multiplatform, feature-rich screenwriting program

License:        GPLv2 and GPLv3+
URL:            https://github.com/limburgher/trelby
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wxpython4
BuildRequires:  python3-lxml
BuildRequires:  docbook-style-xsl
BuildRequires:  make
BuildRequires:  python3-pytest > 7
Requires:       python3-wxpython4
Requires:       python3-lxml
Requires:       hicolor-icon-theme

%description
Trelby is simple, fast and elegantly laid out to make
screenwriting simple. It is infinitely configurable.

%prep
%setup -q

sed -i "s|src|%{python3_sitelib}/trelby/src|g" bin/trelby

%build
make dist
%{__python3} setup.py build
rm -rf doc/.gitignore

%install
%{__python3} setup.py install --prefix=%{_prefix} \
    --install-lib=%{python3_sitelib}/trelby \
    --install-data=%{_datadir} \
    --skip-build \
    --root $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/trelby/resources
ln -s %{python3_sitelib}/trelby/resources/icon256.png $RPM_BUILD_ROOT%{_datadir}/trelby/resources/icon256.png

desktop-file-validate %{buildroot}/%{_datadir}/applications/trelby.desktop

%check
make test

%files
%license LICENSE
%doc fileformat.txt README.md manual.html
%{_bindir}/*
%{_datadir}/trelby/resources
%{_datadir}/applications/trelby.desktop
%{python3_sitelib}/trelby*
%{_mandir}/man1/trelby.1.gz

%changelog
* Mon Oct 24 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.4.7-1
- 2.4.7

* Wed Aug 31 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.4.6-1
- 2.4.6

* Mon Aug 15 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.4.5-1
- 2.4.5

* Fri Jul 22 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.4.4-1
- 2.4.4

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 2.4.3-4
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4.3-1
- 2.4.3

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.2-2
- Rebuilt for Python 3.10

* Thu Mar 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4.2-1
- Fix license tag, validate desktop file, move to unittest.mock.

* Thu Mar 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4.1-2
- Use macro for prefix.

* Tue Mar 02 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4.1-1
- 2.4.1

* Mon Feb 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4-3
- Fix man page, manual, tests, 2.4 final.

* Wed Dec 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.4-2
- Fix for title page editing.

* Thu Aug 15 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.4-1
- Python3

* Fri Mar 16 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.3-0.dev
- First build.
