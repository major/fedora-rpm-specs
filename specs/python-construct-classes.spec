Name:      python-construct-classes
Version:   0.1.2
Release:   9%{?dist}
Summary:   Parse your binary structs into dataclasses

License:   MIT
URL:       https://github.com/matejcik/construct-classes
Source0:   %{pypi_source construct-classes}

# Only include license and documentation for sdist #2
# https://github.com/matejcik/construct-classes/pull/2
Patch0:    https://patch-diff.githubusercontent.com/raw/matejcik/construct-classes/pull/2.patch#/only-include-license-documentation-for-sdist.patch

BuildArch: noarch

BuildRequires: python3-devel


%global _description %{expand:
Parse your binary data into dataclasses. Pack your dataclasses into binary data.

construct-classes rely on construct for parsing and packing. The programmer
needs to manually write the Construct expressions. There is also no type
verification, so it is the programmer's responsibility that the dataclass and
the Construct expression match.}

%description %_description

%package -n python3-construct-classes
Summary:       %{summary}

%description -n python3-construct-classes %_description


%prep
%autosetup -n construct-classes-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files construct_classes


%check
# Tests are left out from the sdist


%files -n python3-construct-classes -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.rst
%doc README.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.2-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.1.2-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 18 2022 Jonny Heggheim <hegjon@gmail.com> - 0.1.2-1
- Inital packaging
