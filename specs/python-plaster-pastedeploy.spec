%global srcname plaster-pastedeploy
%global sum A PasteDeploy binding to the plaster configuration loader

Name: python-%{srcname}
Version: 1.0.1
Release: %autorelease
BuildArch: noarch

License: MIT
Summary: %{sum}
URL:     https://github.com/Pylons/plaster_pastedeploy
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: python3-devel


%description
plaster_pastedeploy is a plaster plugin that provides a
plaster.Loader that can parse ini files according to the standard set
by PasteDeploy. It supports the wsgi plaster protocol, implementing
the plaster.protocols.IWSGIProtocol interface.


%package -n python3-%{srcname}
Summary: %{sum}


%description -n python3-%{srcname}
%{description}


%prep
%autosetup -n plaster_pastedeploy-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l plaster_pastedeploy

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc CHANGES.rst
%doc README.rst


%changelog
%autochangelog
