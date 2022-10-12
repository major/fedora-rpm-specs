Name:           python-executing
Version:        1.1.1
Release:        1%{?dist}
Summary:        Python library for inspecting the current frame run footprint

License:        MIT
URL:            https://github.com/alexmojaki/executing
# The package uses setuptools_scm, GitHub tarball will not work
Source0:        %{pypi_source executing}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Get information about what a Python frame is currently doing, particularly the
AST node being executed}

%description %_description

%package -n python3-executing
Summary:        %{summary}

%description -n python3-executing %_description


%prep
%autosetup -p1 -n executing-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files executing


%check
%tox


%files -n python3-executing -f %{pyproject_files}
%doc README.md
%license LICENSE.txt


%changelog
* Sun Oct 09 2022 Lumír Balhar <lbalhar@redhat.com> - 1.1.1-1
- Update to 1.1.1
Resolves: rhbz#2133192

* Mon Sep 26 2022 Lumír Balhar <lbalhar@redhat.com> - 1.1.0-1
- Update to 1.1.0
Resolves: rhbz#2110285

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Roman Inflianskas <rominf@aiven.io> - 0.8.2-1
- Initial package
