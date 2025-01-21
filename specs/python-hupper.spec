%global srcname hupper
%global sum Integrated process monitor for developing servers

Name:           python-%{srcname}
Version:        1.12.1
Release:        %autorelease
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%description
hupper is an integrated process monitor that will track changes
to any imported Python files in sys.modules as well as custom paths.
When files are changed the process is restarted.

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
hupper is an integrated process monitor that will track changes
to any imported Python files in sys.modules as well as custom paths.
When files are changed the process is restarted.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l hupper

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc CHANGES.rst CONTRIBUTING.rst docs/ LICENSE.txt PKG-INFO README.rst
%{_bindir}/hupper

%changelog
%autochangelog
