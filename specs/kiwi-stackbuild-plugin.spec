# Enable Python dependency generation
%{?python_enable_dependency_generator}

%global desc \
The KIWI plugin to build images using a container layer as the rootfs \
origin. This allows to build an image on top of a non empty \
image root directory.

%global srcname kiwi_stackbuild_plugin

Name:           kiwi-stackbuild-plugin
Version:        1.0.10
Release:        1%{?dist}
URL:            https://github.com/OSInside/kiwi-stackbuild-plugin
Summary:        KIWI - Stack Build Plugin
License:        GPL-3.0-or-later
# We must use the version uploaded to pypi, as it contains all the required files.
Source0:        https://files.pythonhosted.org/packages/source/k/%{srcname}/%{srcname}-%{version}.tar.gz

# Backports from upstream
## From: https://github.com/OSInside/kiwi-stackbuild-plugin/pull/7
Patch0001:      0001-setup.py-Drop-unused-dependency-on-mock.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# doc build requirements
BuildRequires:  make
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
BuildRequires:  python3dist(docopt-ng)
%else
BuildRequires:  python3dist(docopt)
%endif
BuildRequires:  python3dist(kiwi)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(requests)

Requires:       python3-%{name} = %{version}-%{release}
Supplements:    (kiwi-cli and kiwi-systemdeps-containers)
Provides:       %{srcname} = %{version}-%{release}

BuildArch:      noarch

%description %{desc}

%package -n python3-%{name}
Summary:        KIWI - Stack Build Plugin - Python 3 implementation
Supplements:    python%{python3_version}dist(kiwi)
Requires:       kiwi-systemdeps-containers
Provides:       python3-%{srcname} = %{version}-%{release}

%description -n python3-%{name} %{desc}

This package provides the Python 3 library plugin.

%prep
%autosetup -n %{srcname}-%{version} -p1

# Switch things to docopt-ng for Fedora 41+
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
sed -e 's/docopt/docopt-ng>=0.9.0/' -i setup.py
%endif

%build
%py3_build

%install
%py3_install

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
* Fri Nov 15 2024 Neal Gompa <ngompa@fedoraproject.org> - 1.0.10-1
- Initial package

