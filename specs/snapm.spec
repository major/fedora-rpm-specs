%global summary A set of tools for managing snapshots

Name:		snapm
Version:	0.4.3
Release:	%autorelease
Summary:	%{summary}

License:	Apache-2.0
URL:		https://github.com/snapshotmanager/%{name}
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	boom-boot
BuildRequires:	lvm2
BuildRequires:	make
BuildRequires:	stratis-cli
BuildRequires:	stratisd
BuildRequires:	python3-devel
BuildRequires:	python3-sphinx

Requires: python3-snapm = %{version}-%{release}
Recommends: boom-boot

%package -n python3-snapm
Summary: %{summary}

%package -n python3-snapm-doc
Summary: %{summary}

%description
Snapshot manager (snapm) is a tool for managing sets of snapshots on Linux
systems.  The snapm tool allows snapshots of multiple volumes to be captured at
the same time, representing the system state at the time the set was created.

%description -n python3-snapm
Snapshot manager (snapm) is a tool for managing sets of snapshots on Linux
systems.  The snapm tool allows snapshots of multiple volumes to be captured at
the same time, representing the system state at the time the set was created.

This package provides the python3 snapm module.

%description -n python3-snapm-doc
Snapshot manager (snapm) is a tool for managing sets of snapshots on Linux
systems.  The snapm tool allows snapshots of multiple volumes to be captured at
the same time, representing the system state at the time the set was created.

This package provides the python3 snapm module documentation in HTML format.

%prep
%autosetup -p1 -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%{make_build} -C doc html
rm doc/_build/html/.buildinfo
mv doc/_build/html doc/html
rm -rf doc/html/_sources doc/_build
rm -f doc/*.rst doc/Makefile doc/conf.py

%install
%pyproject_install

mkdir -p %{buildroot}/%{_mandir}/man8
%{__install} -p -m 644 man/man8/snapm.8 %{buildroot}/%{_mandir}/man8

%check
%pytest --log-level=debug -v tests/

%files
# Main license for snapm (Apache-2.0)
%license LICENSE
%doc README.md
%{_bindir}/snapm
%doc %{_mandir}/man*/snapm.*

%files -n python3-snapm
# license for snapm (Apache-2.0)
%license LICENSE
%doc README.md
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.dist-info/

%files -n python3-snapm-doc
# license for snapm (Apache-2.0)
%license LICENSE
%doc README.md
%doc doc

%changelog
%autochangelog
