%global desc \
The KIWI boxed plugin provides support for self contained building \
of images based on fast booting VM images.

%global srcname kiwi_boxed_plugin

Name:           kiwi-boxed-plugin
Version:        0.2.48
Release:        1%{?dist}
URL:            https://github.com/OSInside/kiwi-boxed-plugin
Summary:        KIWI - Boxed Build Plugin
License:        GPL-3.0-or-later
# We must use the version uploaded to pypi, as it contains all the required files.
Source0:        https://files.pythonhosted.org/packages/source/k/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# doc build requirements
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

Requires:       python3-%{name} = %{version}-%{release}
Supplements:    (kiwi-cli and qemu-kvm)
Provides:       %{srcname} = %{version}-%{release}

BuildArch:      noarch

%description %{desc}

%package -n python3-%{name}
Summary:        KIWI - Boxed Build Plugin - Python 3 implementation
Supplements:    (python%{python3_version}dist(kiwi) and qemu-kvm)
Requires:       qemu-kvm
Provides:       python3-%{srcname} = %{version}-%{release}

%description -n python3-%{name} %{desc}

This package provides the Python 3 library plugin.

%prep
%autosetup -n %{srcname}-%{version} -p1

# Temporarily switch things back to docopt for everything but Fedora 41+
# FIXME: Drop this hack as soon as we can...
%if ! (0%{?fedora} >= 41 || 0%{?rhel} >= 10)
sed -e 's/docopt-ng.*/docopt = ">=0.6.2"/' -i pyproject.toml
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# Build man pages
make -C doc man

%install
%pyproject_install

# Install documentation
make buildroot=%{buildroot}/ docdir=%{_defaultdocdir}/ install

# Delete this now, we'll docify later
rm -f %{buildroot}%{_defaultdocdir}/python-%{srcname}/LICENSE
rm -f %{buildroot}%{_defaultdocdir}/python-%{srcname}/README

%files
%doc README.rst
%{_mandir}/man8/*.8*

%files -n python3-%{name}
%license LICENSE
%{python3_sitelib}/%{srcname}*

%changelog
* Fri Feb 07 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.2.48-1
- Update to 0.2.48

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Sep 26 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.2.38-1
- Update to 0.2.38
- Adapt for docopt->docopt-ng switch on F41+

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 24 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.2.32-1
- Update to 0.2.32 (RH#2154862)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.2.23-3
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 02 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.2.23-1
- Update to 0.2.23 (RH#2065051)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Neal Gompa <ngompa@fedoraproject.org> - 0.2.17-1
- Update to 0.2.17 (RH#1975364)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Neal Gompa <ngompa13@gmail.com> - 0.2.13-2
- Revert upstream change to depend on dead wget python module

* Mon Jun 21 2021 Neal Gompa <ngompa13@gmail.com> - 0.2.13-1
- Update to 0.2.13 (RH#1941662)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.6-2
- Rebuilt for Python 3.10

* Mon Mar 08 2021 Neal Gompa <ngompa13@gmail.com> - 0.2.6-1
- Update to 0.2.6 (RH#1907355)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 2020 Neal Gompa <ngompa13@gmail.com> - 0.1.12-1
- Update to 0.1.12 (RH#1872631)

* Sat Aug 15 2020 Neal Gompa <ngompa13@gmail.com> - 0.1.4-1
- Update to 0.1.4 (RH#1837026)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-2
- Rebuilt for Python 3.9

* Wed May 13 2020 Neal Gompa <ngompa13@gmail.com> - 0.1.0-1
- Initial packaging
