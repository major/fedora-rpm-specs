%global srcname hatch-nodejs-version

Name:           python-%{srcname}
Version:        0.4.0
Release:        %autorelease
Summary:        Hatch plugin for versioning from a package.json file

License:        MIT
URL:            https://github.com/agoose77/hatch-nodejs-version
Source:         %{pypi_source hatch_nodejs_version}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This package provides two Hatch plugins:
- a version source plugin that reads/writes the package version from the
  version field of the Node.js package.json file.
- a metadata hook plugin that reads PEP 621 metadata from the Node.js
  package.json file.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n hatch_nodejs_version-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files hatch_nodejs_version

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
