%global summary A set of libraries and tools for managing boot loader entries
%global sphinx_docs 1

Name:		boom-boot
Version:	1.6.9
Release:	%autorelease
Summary:	%{summary}

License:	Apache-2.0
URL:		https://github.com/snapshotmanager/boom-boot
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	make
BuildRequires:	python3-devel
%if 0%{?rhel} && 0%{?rhel} < 11
BuildRequires:	python3-setuptools
BuildRequires:	python3-pip
BuildRequires:	python3-wheel
%endif
BuildRequires:	python3-pytest
%if 0%{?sphinx_docs}
BuildRequires:	python3-dbus
BuildRequires:	python3-sphinx
%endif
BuildRequires:	make

Requires: python3-boom = %{version}-%{release}
Requires: %{name}-conf = %{version}-%{release}
Requires: python3-dbus
%if 0%{?rhel} == 9
Requires: systemd >= 252-18
%else
Requires: systemd >= 254
%endif

%package -n python3-boom
Summary: %{summary}
%{?python_provide:%python_provide python3-boom}
Requires: %{__python3}
Recommends: (lvm2 or brtfs-progs)
Recommends: %{name}-conf = %{version}-%{release}

# There used to be a boom package in fedora, and there is boom packaged in
# copr. How to tell which one is installed? We need python3-boom and no boom
# only.
Conflicts: boom

%package conf
Summary: %{summary}

%description
Boom is a boot manager for Linux systems using boot loaders that support
the BootLoader Specification for boot entry configuration.

Boom requires a BLS compatible boot loader to function and is tested
with the grub2 builds provided in Fedora, CentOS and Red Hat Enterprise
Linux.

%description -n python3-boom
Boom is a boot manager for Linux systems using boot loaders that support
the BootLoader Specification for boot entry configuration.

Boom requires a BLS compatible boot loader to function and is tested
with the grub2 builds provided in Fedora, CentOS and Red Hat Enterprise
Linux.

%description conf
Boom is a boot manager for Linux systems using boot loaders that support
the BootLoader Specification for boot entry configuration.

Boom requires a BLS compatible boot loader to function and is tested
with the grub2 builds provided in Fedora, CentOS and Red Hat Enterprise
Linux.

This package provides configuration files for boom.

%prep
%autosetup -p1 -n %{name}-%{version}

%if 0%{?fedora} || 0%{?rhel} >= 11
%generate_buildrequires
%pyproject_buildrequires
%endif

%build
%if 0%{?sphinx_docs}
make %{?_smp_mflags} -C doc html
rm doc/_build/html/.buildinfo
mv doc/_build/html doc/html
rm -rf doc/_build
rm -rf doc/_static
rm doc/*.rst
%endif

%if 0%{?rhel} && 0%{?rhel} < 11
%py3_build
%else
%pyproject_wheel
%endif

%install
%pyproject_install

# Make configuration directories
# mode 0700 - in line with /boot/grub2 directory:
install -d -m 700 ${RPM_BUILD_ROOT}/boot/boom/profiles
install -d -m 700 ${RPM_BUILD_ROOT}/boot/boom/hosts
install -d -m 700 ${RPM_BUILD_ROOT}/boot/loader/entries
install -d -m 700 ${RPM_BUILD_ROOT}/boot/boom/cache
install -m 644 examples/boom.conf ${RPM_BUILD_ROOT}/boot/boom

mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}/man8
mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}/man5
install -m 644 man/man8/boom.8 ${RPM_BUILD_ROOT}/%{_mandir}/man8
install -m 644 man/man5/boom.5 ${RPM_BUILD_ROOT}/%{_mandir}/man5

rm doc/Makefile
rm doc/conf.py

%check
pytest-3 --log-level=debug -v

%files
%license LICENSE
%doc README.md
%{_bindir}/boom
%doc %{_mandir}/man*/boom.*

%files -n python3-boom
%license LICENSE
%doc README.md
%{python3_sitelib}/boom/*
%if 0%{?rhel} && 0%{?rhel} < 11
%{python3_sitelib}/boom*.egg-info/
%else
%{python3_sitelib}/boom*.dist-info/
%endif
%doc doc

%files conf
%license LICENSE
%doc README.md
%dir /boot/boom
%config(noreplace) /boot/boom/boom.conf
%dir /boot/boom/profiles
%dir /boot/boom/hosts
%dir /boot/boom/cache
%dir /boot/loader/entries


%changelog
%autochangelog
