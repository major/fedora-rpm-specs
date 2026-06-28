%global srcname pyroute2

%global _description \
PyRoute2 provides several levels of API to work with Netlink\
protocols, such as Generic Netlink, RTNL, TaskStats, NFNetlink,\
IPQ.

Name: python-%{srcname}
Version: 0.9.6
Release: %autorelease
Summary: Pure Python netlink library
License: GPL-2.0-or-later OR Apache-2.0
URL: https://github.com/svinota/%{srcname}

BuildArch: noarch
Source0: %{pypi_source pyroute2}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary: %{summary}
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyroute2

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%{_bindir}/ss2
%{_bindir}/dhcp-server-detector
%{_bindir}/pyroute2-decoder
%{_bindir}/%{srcname}-dhcp-client
%{_bindir}/%{srcname}-test-platform
%doc README* CHANGELOG.rst
%license LICENSE.GPL-2.0-or-later LICENSE.Apache-2.0

%changelog
%autochangelog
