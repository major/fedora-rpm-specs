Name:           cr2rpm
Version:        0.2.0
Release:        %autorelease
Summary:        Generate RPM spec files from Crystal shard manifests

License:        GPL-3.0-or-later
URL:            https://codeberg.org/fedora-crystal/cr2rpm
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-drop-shebang-from-main.patch

BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description
cr2rpm is a command-line tool designed for Fedora packagers to inspect Crystal
shards, generate standard-compliant Fedora RPM spec files from shard manifests
and lock files, query virtual provides and requires, and format topological
mock chain build sequences.


%prep
%autosetup -n %{name} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files cr2rpm


%check
%pytest


%files -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{_bindir}/cr2rpm


%changelog
%autochangelog
