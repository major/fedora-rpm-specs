%global desc \
The KIWI plugin to build images using a container layer as the rootfs \
origin. This allows to build an image on top of a non empty \
image root directory.

%global srcname kiwi_stackbuild_plugin

Name:           kiwi-stackbuild-plugin
Version:        1.0.11
Release:        2%{?dist}
URL:            https://github.com/OSInside/kiwi-stackbuild-plugin
Summary:        KIWI - Stack Build Plugin
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
Supplements:    (kiwi-cli and kiwi-systemdeps-containers)
Provides:       %{srcname} = %{version}-%{release}

BuildArch:      noarch

%description %{desc}

%package -n python3-%{name}
Summary:        KIWI - Stack Build Plugin - Python 3 implementation
Supplements:    (python%{python3_version}dist(kiwi) and kiwi-systemdeps-containers)
Requires:       kiwi-systemdeps-containers
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
* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 1.0.11-2
- Rebuilt for Python 3.14

* Tue Mar 25 2025 Neal Gompa <ngompa@fedoraproject.org> - 1.0.11-1
- Update to 1.0.11

* Fri Jan 24 2025 Neal Gompa <ngompa@fedoraproject.org> - 1.0.10-3
- Backport fix to stop using mock module

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 15 2024 Neal Gompa <ngompa@fedoraproject.org> - 1.0.10-1
- Initial package

