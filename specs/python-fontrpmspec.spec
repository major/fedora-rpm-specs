%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname fontrpmspec
%global _description %{expand:
This contains tools to generate/convert a RPM spec file for fonts.
}

Name:           python-%{srcname}
Version:        0.17
Release:        2%{?dist}
Summary:        Font Packaging tool for Fedora
License:        GPL-3.0-or-later
URL:            https://github.com/fedora-i18n/font-rpm-spec-generator
Source0:        %{pypi_source %{srcname} %{version}}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python3dist(fonttools)
BuildRequires:  python3dist(termcolor)
BuildRequires:  python3dist(python-rpm-spec)

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary: Python library for rpmspec tools for fonts

%description -n python%{python3_pkgversion}-%{srcname} %_description

This package contains a Python library for %{srcname}.

%package -n %{srcname}
Requires: python%{python3_pkgversion}-%{srcname} = %{version}-%{release}
Requires: fontconfig
Requires: fedpkg
Requires: tmt
Summary: %{summary}

%description -n %{srcname} %_description

This package contains the end-user executables for %{srcname}.

%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%files -n  python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%files -n %{srcname}
%license LICENSE
%doc README.md
%{_bindir}/fontrpmspec-conv
%{_bindir}/fontrpmspec-gen
%{_bindir}/fontrpmspec-gentmt


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 10 2024 Akira TAGOH <tagoh@redhat.com> - 0.17-1
- Update to 0.17

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 26 2024 Akira TAGOH <tagoh@redhat.com> - 0.16-1
- Update to 0.16

* Tue Jun 25 2024 Akira TAGOH <tagoh@redhat.com> - 0.15-1
- Update to 0.15
- Add fontrpmspec sub-package for executables.

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.12-6
- Rebuilt for Python 3.13

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
