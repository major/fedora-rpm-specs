%global shortname mediafile
Name:           python-mediafile
Version:        0.12.0
Release:        2%{dist}
Summary:        Elegant audio file tagging in Python

License:        MIT
URL:            https://github.com/beetbox/mediafile
Source0:        %{pypi_source mediafile}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
MediaFile is a simple interface to the metadata tags for many audio file
formats. It wraps Mutagen, a high-quality library for low-level tag
manipulation, with a high-level, format-independent interface for a common set
of tags.}

%description %{_description}

%package -n python3-%{shortname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{shortname}}

Requires:       python3 >= 3.6
Requires:       python-mutagen

%description -n python3-%{shortname} %{_description}

Python 3 version.

%prep
%autosetup -n %{shortname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -r -t -e %{toxenv}-test

%build
%pyproject_wheel

%check
%tox -e %{toxenv}-test

%install
%pyproject_install
%pyproject_save_files '*%{shortname}*'

%files -n python3-%{shortname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 2 2024 Michele Baldessari <michele@acksyn.org> - 0.12.0-1
- New package

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.11.0-2
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Michele Baldessari <michele@acksyn.org> - 0.11.0-1
- New package (drop unneeded patches)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 Michele Baldessari <michele@acksyn.org> - 0.9.0-1
- New package
