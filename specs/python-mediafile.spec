%global shortname mediafile
Name:           python-mediafile
Version:        0.12.0
Release:        7%{dist}
Summary:        Elegant audio file tagging in Python

License:        MIT
URL:            https://github.com/beetbox/mediafile
Source0:        %{pypi_source mediafile}
Patch0:         0001-Set-new-ORIGINALDATE-tag-for-m4a-files-in-addition-t.patch
Patch1:         0002-Version-bump-changelog-for-71.patch
Patch2:         0003-remove-usage-of-six-__future__.patch
Patch3:         0004-Changelog-for-72.patch
Patch4:         0005-Bump-minimum-Python-versions.patch
# From PR 73 but without the binary change
Patch5:         49da9728a69ae8a63af8a4630fccc55c10e66392-nobinary.patch

BuildArch:     noarch
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
Requires:       python3-filetype >= 1.2.0
Requires:       python-mutagen

%description -n python3-%{shortname} %{_description}

Python 3 version.

%prep
%autosetup -n %{shortname}-%{version} -p1
rm test/rsrc/only-magic-bytes.jpg

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
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 02 2024 Michele Baldessari <michele@acksyn.org> - 0.12.0-6
- Apply patches from v0.12.0 to 6accdc4c4a7fe4d808b674a97fb5474e12621504
- Also apply PR 73 to avoid python 3.13 breakage (although it will regress on more obscure image formats)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.12.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

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
