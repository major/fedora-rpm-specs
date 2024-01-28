%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname fontrpmspec
%global _description %{expand:
This contains tools to generate/convert a RPM spec file for fonts.
}

Name:           python-%{srcname}
Version:        0.12
Release:        5%{?dist}
Summary:        Font Packaging tool for Fedora
License:        GPL-3.0-or-later
URL:            https://github.com/fedora-i18n/font-rpm-spec-generator
Source0:        %{pypi_source %{srcname} %{version}}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%{__python3} -m unittest discover -s ./tests -p '*.py'


%files -n  python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/fontrpmspec-gen
%{_bindir}/fontrpmspec-conv


%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.12-2
- Rebuilt for Python 3.12

* Tue Mar 28 2023 Akira TAGOH <tagoh@redhat.com> - 0.12-1
- Update to 0.12.
- Revise the spec file.

* Mon Feb  6 2023 Akira TAGOH <tagoh@redhat.com> - 0.11-1
- Update to 0.11.

* Thu Jan 26 2023 Akira TAGOH <tagoh@redhat.com> - 0.10-1
- Update to 0.10.

* Wed Jan 25 2023 Akira TAGOH <tagoh@redhat.com> - 0.7-1
- Update to 0.7.

* Thu Dec 22 2022 Akira TAGOH <tagoh@redhat.com> - 0.2-1
- Initial package.
