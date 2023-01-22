Name:           python-pure-eval
Version:        0.2.2
Release:        4%{?dist}
Summary:        Safely evaluate AST nodes without side effects

License:        MIT
URL:            http://github.com/alexmojaki/pure_eval
Source0:        %{pypi_source pure_eval}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Python package that lets you safely evaluate certain AST nodes
without triggering arbitrary code that may have unwanted side effects.}


%description %_description

%package -n     python3-pure-eval
Summary:        %{summary}

%description -n python3-pure-eval %_description


%prep
%autosetup -p1 -n pure_eval-%{version}


%generate_buildrequires
%pyproject_buildrequires -r -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pure_eval


%check
%tox


%files -n python3-pure-eval -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.2-2
- Rebuilt for Python 3.11

* Sun Jan 23 2022 Lumír Balhar <lbalhar@redhat.com> - 0.2.2-1
- Update to 0.2.2
Resolves: rhbz#2043934

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Lumír Balhar <lbalhar@redhat.com> - 0.2.1-1
- Package generated with pyp2spec
